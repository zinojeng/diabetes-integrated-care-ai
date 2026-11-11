#!/usr/bin/env python3
"""Readiness checks; never changes trust, permissions, login or global settings."""
import argparse, json, os, pathlib, re, shutil, socket, subprocess, tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]

def command(argv, timeout=15):
    return subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=timeout)

def write_probe(directory):
    """A real temporary-file check; os.access cannot detect an outer sandbox."""
    directory = pathlib.Path(directory)
    try:
        directory.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryFile(dir=directory) as stream:
            stream.write(b'dmic write check')
        return 'PASS', 'temporary write succeeded'
    except OSError as error:
        return 'FAIL', f'{type(error).__name__}, errno={error.errno}; no chmod or trust change attempted'

def inspect(probe=False, network=True):
    checks=[]
    def add(name, status, detail, required=True):
        checks.append(dict(name=name,status=status,detail=detail,required=required))
    executable=shutil.which('claude')
    add('claude_cli','PASS' if executable else 'FAIL',executable or 'claude not found')
    if executable:
        try:
            result=command([executable,'--version'])
            match=re.search(r'(\d+)\.(\d+)\.(\d+)',result.stdout)
            valid=bool(match and tuple(map(int,match.groups())) >= (2,1,248))
            add('version','PASS' if valid else 'FAIL',result.stdout.strip()[:100])
            auth=command([executable,'auth','status'])
            data=json.loads(auth.stdout)
            safe={k:data.get(k) for k in ('loggedIn','authMethod','apiProvider')}
            add('authentication','PASS' if data.get('loggedIn') else 'FAIL',safe)
        except (OSError,ValueError,subprocess.TimeoutExpired) as error:
            add('claude_checks','FAIL',type(error).__name__)
    config=pathlib.Path(os.environ.get('CLAUDE_CONFIG_DIR',str(pathlib.Path.home()/'.claude'))).expanduser()
    for name,path in [('project',ROOT/'.local'),('claude_config',config),('claude_sessions',config/'session-env'),('claude_transcripts',config/'projects')]:
        state,detail=write_probe(path) if probe else ('NOT_PROBED','use --probe-writes in the ordinary host Terminal')
        add(name+'_write',state,{'path':str(path),'result':detail})
    if network:
        for host in ('api.anthropic.com','eutils.ncbi.nlm.nih.gov'):
            try:
                result=command(['curl','--head','--silent','--output','/dev/null','--write-out','%{http_code}','--connect-timeout','4','--max-time','8','https://'+host],timeout=10)
                reachable=result.returncode==0 and result.stdout.strip()!='000'
                add('https_'+host,'PASS' if reachable else 'FAIL',{'curl_exit':result.returncode,'http_status':result.stdout.strip()[:3]},required=host=='api.anthropic.com')
            except (OSError,subprocess.TimeoutExpired) as error:
                add('https_'+host,'FAIL',type(error).__name__,required=host=='api.anthropic.com')
    else:
        add('network','NOT_PROBED','skipped by --offline')
    mcp_names=set()
    sources=[pathlib.Path.home()/'.claude.json',ROOT/'.mcp.json']
    for path in sources:
        try:
            data=json.loads(path.read_text())
            mcp_names.update(data.get('mcpServers',{}))
            mcp_names.update(data.get('projects',{}).get(str(ROOT),{}).get('mcpServers',{}))
        except (OSError,ValueError):
            pass
    selected=sorted(n for n in mcp_names if n in ('research_hub','paper-search','google-scholar','scihub','llamaparse'))
    add('research_mcp','PASS' if selected else 'WARN',selected or 'none configured on this host',required=False)
    add('llamaparse_key','PRESENT_UNVERIFIED' if os.environ.get('LLAMA_CLOUD_API_KEY') or (ROOT/'.local/llamaparse.key').is_file() else 'MISSING','key contents never printed',required=False)
    ready=all(c['status']=='PASS' for c in checks if c['required'])
    return {'host':socket.gethostname(),'project':str(ROOT),'requested_model':'claude-opus-5-5','ready_for_launch_attempt':ready,'model_reply_verified':False,'checks':checks}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--probe-writes',action='store_true')
    parser.add_argument('--offline',action='store_true')
    args=parser.parse_args()
    result=inspect(args.probe_writes,not args.offline)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0 if result['ready_for_launch_attempt'] else 2

if __name__=='__main__':
    raise SystemExit(main())
