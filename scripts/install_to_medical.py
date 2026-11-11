#!/usr/bin/env python3
"""Run from ordinary Mac Terminal to copy this project without overwriting originals silently."""
import argparse, datetime, hashlib, pathlib, shutil
ROOT = pathlib.Path(__file__).resolve().parents[1]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--destination', default='/Users/ander/documents/medical/diabetes/integrated_care')
    ap.add_argument('--copy-local-key', action='store_true')
    args=ap.parse_args()
    dest=pathlib.Path(args.destination).expanduser().resolve()
    if dest == ROOT: raise SystemExit('Destination already is this project.')
    stamp=datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
    count=0
    for src in sorted(ROOT.rglob('*')):
        rel=src.relative_to(ROOT)
        if not src.is_file() or any(p in {'.git','.local','.venv','__pycache__','sessions','fulltext','parsed'} for p in rel.parts):continue
        if src.suffix in {'.key','.pem','.pdf'} or src.name.startswith('.env'):continue
        target=dest/rel
        if target.exists():
            if hashlib.sha256(src.read_bytes()).digest()==hashlib.sha256(target.read_bytes()).digest():continue
            backup=dest/'.local/install-backup'/stamp/rel
            backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(target,backup)
        target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,target);count+=1
    # Preserve the user's expected top-level filename as a reading copy.
    report=dest/'research/DM_AI_Integrated_Literature_Review_20261111.md'
    top=dest/report.name
    if top.exists() and top.read_bytes()!=report.read_bytes():
        backup=dest/'.local/install-backup'/stamp/top.name
        backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(top,backup)
    shutil.copy2(report,top)
    key=ROOT/'.local/llamaparse.key'
    if args.copy_local_key and key.exists():
        target=dest/'.local/llamaparse.key';target.parent.mkdir(exist_ok=True)
        if target.exists() and target.read_bytes()!=key.read_bytes():
            raise SystemExit('Existing different parsing key preserved; reconcile manually.')
        target.write_bytes(key.read_bytes());target.chmod(0o600)
    print('Installed files:',count,'\nProject:',dest)
    print('Run: cd "'+str(dest)+'"; claude --model claude-opus-5-5')
    print('After native trust and a successful reply: /exit, then python3 scripts/claude_workflow.py start all')

if __name__=='__main__':main()
