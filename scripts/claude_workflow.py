#!/usr/bin/env python3
"""Codex-directed independent Claude sessions. Never changes workspace trust."""
import argparse, contextlib, datetime, fcntl, json, os, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
MODEL = 'claude-opus-5-5'
ROLES = ('complications', 'psychosocial', 'calculators', 'methods_ai')
LOCAL = ROOT / '.local'

def run(args, timeout=30):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, timeout=timeout)

def records():
    p = run(['claude', 'agents', '--json', '--all', '--cwd', str(ROOT)])
    if p.returncode:
        raise RuntimeError(p.stderr.strip() or 'Cannot query Claude agent registry.')
    items = json.loads(p.stdout)
    if not isinstance(items, list):
        raise RuntimeError('Unexpected registry schema; do not launch duplicate sessions.')
    return [x for x in items if x.get('kind', 'background') == 'background'
            and pathlib.Path(x.get('cwd', '')).resolve() == ROOT.resolve()]

def event(**data):
    LOCAL.mkdir(exist_ok=True)
    with (LOCAL/'dispatch.jsonl').open('a') as f:
        f.write(json.dumps({'time': datetime.datetime.now(datetime.timezone.utc).isoformat(), **data}, ensure_ascii=False)+'\n')

@contextlib.contextmanager
def lock():
    LOCAL.mkdir(exist_ok=True)
    with (LOCAL/'launcher.lock').open('a') as f:
        try: fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError: raise RuntimeError('Another project launcher is running.')
        try: yield
        finally: fcntl.flock(f, fcntl.LOCK_UN)

def mcp_config():
    source = pathlib.Path.home()/'.claude.json'
    global_config = json.loads(source.read_text()) if source.exists() else {}
    selected = {}
    for name in ('research_hub', 'paper-search', 'google-scholar', 'scihub', 'llamaparse'):
        item = global_config.get('mcpServers', {}).get(name)
        if item: selected[name] = json.loads(json.dumps(item))
    if 'research_hub' in selected:
        item = selected['research_hub']
        argv = item.setdefault('args', [])
        if '--download-dir' not in argv:
            argv.extend(['--download-dir', str(ROOT/'literature/fulltext')])
    if 'paper-search' in selected:
        cached = pathlib.Path.home()/'paper-search-mcp/.venv/bin/python'
        if cached.exists():
            selected['paper-search']['command'] = str(cached)
            selected['paper-search']['args'] = ['-m','paper_search_mcp.server']
    # All secrets remain local. Never print the generated configuration.
    if 'llamaparse' in selected:
        env = selected['llamaparse'].setdefault('env', {})
        env.pop('LLAMA_CLOUD_API_KEY', None)
        key = LOCAL/'llamaparse.key'
        if key.exists(): env['LLAMA_CLOUD_API_KEY_FILE'] = str(key)
    path = LOCAL/'mcp.research.json'
    LOCAL.mkdir(exist_ok=True)
    path.write_text(json.dumps({'mcpServers': selected}, ensure_ascii=False, indent=2)+'\n')
    path.chmod(0o600)
    return path, sorted(selected)

def settings():
    return json.dumps({'env': {'CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS': '0',
                               'CLAUDE_CODE_SUBAGENT_MODEL': MODEL,
                               'CLAUDE_CODE_SUBAGENT_MODEL_FORCE': '1'},
                       'worktree': {'bgIsolation': 'none'}})

def prompt(role):
    peers = ', '.join('DMIC-'+r for r in ROLES if r != role)
    text = (ROOT/'workflow/prompts'/f'{role}.md').read_text()
    return text + f'''
Read CLAUDE.md and workflow/codex_lead.md first. Project root: {ROOT}
Your exact name: DMIC-{role}. Requested model: {MODEL}; no model substitution.
Write only sessions/{role}/ and literature/notes/{role}/. Do not edit the synthesis.
Record requested model and runtime-verified model separately (unknown if unavailable).
Use English search terms and primary sources; report in zh-TW, medical/drug names English.
Do not claim a PubMed search, full-text download, PDF parse, or peer reply occurred without receipts.
Report evidence table, sources, conflicts, unresolved claims and a checkpoint.

Cross-session talking: use ListAgents to find exact project peers {peers}.
Complete your independent appraisal first, then send at most one evidence question to
each reachable peer with SendMessage. Maximum two substantive rounds, no polling loops.
Use the exact reachable identity returned by ListAgents; never assume a launch alias is routable.
Message fields: message_id, in_reply_to, sender, recipient, claim_id, source_url,
source_locator, question_or_answer, status. Receiver replies ACK with original message_id.
Save actual sent/received content in sessions/{role}/exchange_log.jsonl.
Tool success without ACK is only sent_unacknowledged, never verified_agreement.
If peers are absent, save unsent questions in pending_questions.md and stop that exchange.
For questions from Codex answer ACCEPT/REVISE/UNRESOLVED with evidence and exact edits.
You may use one custom subagent at a time from workflow/subagents.json, always {MODEL}.
These are independent contexts with assigned output folders, not an OS security boundary.
No agent team, no work outside this project, no git push/merge, no patient data.
Use existing research MCPs when available. Prefer PMC/publisher open access, record provenance;
never commit third-party full-text PDFs or private credentials. Mark unavailable PDFs blocked.
Final output sessions/{role}/review.md; update checkpoint.md at recoverable milestones.
Only Codex can mark the integrated manuscript reviewed. Registration alone is not completion.
'''

def start(role):
    name = 'DMIC-'+role
    existing = [x for x in records() if x.get('name') == name]
    if existing:
        print(name+' already exists; attach original session. '+json.dumps(
            {k: existing[-1].get(k) for k in ('id','sessionId','state')}, ensure_ascii=False))
        return
    config, names = mcp_config()
    (ROOT/'sessions'/role).mkdir(parents=True, exist_ok=True)
    (ROOT/'literature/notes'/role).mkdir(parents=True, exist_ok=True)
    dispatch = prompt(role)
    (LOCAL/f'codex_to_{role}.md').write_text(dispatch)
    args = ['claude', '--bg', '--name', name, '--model', MODEL, '--effort', 'max',
            '--permission-mode', 'acceptEdits', '--strict-mcp-config', '--mcp-config', str(config),
            '--settings', settings(), '--agents', json.dumps(json.loads((ROOT/'workflow/subagents.json').read_text())), dispatch]
    try: p = run(args)
    except subprocess.TimeoutExpired:
        event(role=role, status='launch_timeout_unverified', requested_model=MODEL)
        raise RuntimeError('Launch timed out. Query status before retry; do not duplicate.')
    event(role=role, returncode=p.returncode, requested_model=MODEL, mcp_names=names)
    print(p.stdout.strip())
    if p.returncode:
        print(p.stderr.strip(), file=sys.stderr)
        raise RuntimeError('Launch failed. If Workspace not trusted, run interactive claude in this folder and accept its native prompt. Trust is never edited by this launcher.')
    matches = [x for x in records() if x.get('name') == name]
    if len(matches) != 1:
        raise RuntimeError('Session registration not unique/verified. Inspect registry before retry.')
    x = matches[0]
    event(role=role, status='registered_not_reviewed', id=x.get('id'), sessionId=x.get('sessionId'))
    print(json.dumps({k:x.get(k) for k in ('id','sessionId','name','state')},ensure_ascii=False))

def status():
    items = records()
    print('Project:', ROOT, '\nRequested model:', MODEL)
    for role in ROLES:
        matched = [x for x in items if x.get('name') == 'DMIC-'+role]
        print(role+': '+ ('not registered' if not matched else json.dumps([
            {k:x.get(k) for k in ('id','sessionId','state','status','waitingFor')} for x in matched],ensure_ascii=False)))
        print('  review.md:', (ROOT/'sessions'/role/'review.md').exists())
    print('View: claude agents --cwd "$PWD"; full transcript: claude attach <id>')

def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='command', required=True)
    s = sp.add_parser('start'); s.add_argument('role', nargs='?', default='all', choices=(*ROLES,'all'))
    sp.add_parser('status'); sp.add_parser('doctor')
    f = sp.add_parser('feedback'); f.add_argument('role', choices=ROLES); f.add_argument('message_file')
    a = ap.parse_args()
    if a.command == 'status': status(); return
    if a.command == 'doctor':
        p=run(['claude','--version']);print(p.stdout.strip())
        p=run(['claude','auth','status'])
        try:
            auth=json.loads(p.stdout)
            print(json.dumps({k:auth.get(k) for k in ('loggedIn','authMethod','subscriptionType')}))
        except json.JSONDecodeError: print('Authentication status unknown.')
        _, names=mcp_config();print('Configured MCP names:', ', '.join(names));status();return
    if a.command == 'feedback':
        path = pathlib.Path(a.message_file)
        if not path.exists(): raise RuntimeError('Feedback file missing.')
        matches=[x for x in records() if x.get('name')=='DMIC-'+a.role]
        if len(matches)!=1: raise RuntimeError('Need one registered session before feedback.')
        # Deliberately do not resume a live session into a duplicate ID.
        print('Attach original session: claude attach '+str(matches[0].get('id')))
        print('Deliver this Codex feedback verbatim in that conversation:\n'+path.read_text())
        return
    with lock():
        for role in ROLES if a.role=='all' else (a.role,): start(role)

if __name__ == '__main__':
    try: main()
    except (RuntimeError, OSError, ValueError, subprocess.TimeoutExpired) as e:
        print('BLOCKED: '+str(e), file=sys.stderr);sys.exit(1)
