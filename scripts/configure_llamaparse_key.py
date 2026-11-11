#!/usr/bin/env python3
"""Accept a local key without putting it in shell history, source or stdout."""
import getpass, os, pathlib, tempfile
root=pathlib.Path(__file__).resolve().parents[1]
key=getpass.getpass('LlamaParse API key（輸入不顯示）: ').strip()
if not key.startswith('llx-') or len(key)<16:
    raise SystemExit('格式不符；未儲存。')
folder=root/'.local'
folder.mkdir(mode=0o700,exist_ok=True)
fd,name=tempfile.mkstemp(prefix='.llamaparse-',dir=folder,text=True)
try:
    os.fchmod(fd,0o600)
    with os.fdopen(fd,'w') as stream:stream.write(key+'\n')
    os.replace(name,folder/'llamaparse.key')
finally:
    if os.path.exists(name):os.unlink(name)
print('已儲存本機 key；尚未驗證 API 或完成 PDF 解析。')
