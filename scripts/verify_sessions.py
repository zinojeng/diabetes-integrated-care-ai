#!/usr/bin/env python3
"""Read actual assistant receipts; model configuration alone never counts as a reply."""
import json, pathlib, re, subprocess
ROOT=pathlib.Path(__file__).resolve().parents[1]

def main():
    p=subprocess.run(['claude','agents','--json','--all','--cwd',str(ROOT)],capture_output=True,text=True,check=True,timeout=20)
    records=json.loads(p.stdout)
    result=[]
    for record in records:
        if not str(record.get('name','')).startswith('DMIC-'):continue
        sid=record.get('sessionId')
        receipt={'id':record.get('id'),'session_id':sid,'name':record.get('name'),
                 'requested_model':'claude-opus-5-5','actual_model':None,'first_reply':None}
        if sid and re.fullmatch(r'[0-9a-fA-F-]{36}',sid):
            for transcript in (pathlib.Path.home()/'.claude/projects').glob('*/'+sid+'.jsonl'):
                for line in transcript.read_text(errors='replace').splitlines():
                    try:item=json.loads(line)
                    except json.JSONDecodeError:continue
                    if item.get('type')!='assistant':continue
                    msg=item.get('message',{})
                    model=msg.get('model')
                    if model and model!='<synthetic>':receipt['actual_model']=model
                    content=msg.get('content',[])
                    text='\n'.join(x.get('text','') for x in content if isinstance(x,dict) and x.get('type')=='text') if isinstance(content,list) else str(content)
                    if text and receipt['actual_model']:
                        receipt['first_reply']=re.sub(r'(?i)(llx-|sk-|ghp_|github_pat_)[A-Za-z0-9_-]+','[REDACTED]',text[:1600]);break
                if receipt['first_reply']:break
        receipt['status']='verified_first_reply' if receipt['actual_model']=='claude-opus-5-5' and receipt['first_reply'] else 'pending_or_model_mismatch'
        result.append(receipt)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if not result:raise SystemExit(2)

if __name__=='__main__':main()
