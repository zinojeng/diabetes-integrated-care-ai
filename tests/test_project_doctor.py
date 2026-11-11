import importlib.util, json, pathlib, subprocess, tempfile, unittest
from unittest.mock import patch
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/'scripts'/f'{name}.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
d=load('project_doctor');w=load('claude_workflow')
class DoctorTests(unittest.TestCase):
    def test_actual_write_probe(self):
        with tempfile.TemporaryDirectory() as folder:
            target=pathlib.Path(folder)/'session-env'
            self.assertEqual(d.write_probe(target)[0],'PASS')
            self.assertEqual(list(target.iterdir()),[])
    def test_denial_is_failure_and_not_repaired(self):
        with patch.object(pathlib.Path,'mkdir',side_effect=PermissionError(1,'denied')):
            status,detail=d.write_probe('/not-written')
        self.assertEqual(status,'FAIL');self.assertIn('errno=1',detail)
    def test_no_login_blocks_launch(self):
        replies=[subprocess.CompletedProcess([],0,'2.1.321',''),subprocess.CompletedProcess([],1,'{"loggedIn":false}','')]
        with patch.object(d.shutil,'which',return_value='/mock/claude'),patch.object(d,'command',side_effect=replies),patch.object(d,'write_probe',return_value=('PASS','ok')):
            report=d.inspect(probe=True,network=False)
        self.assertFalse(report['ready_for_launch_attempt'])
        self.assertFalse(report['model_reply_verified'])
    def test_skipped_write_probe_is_not_pass(self):
        with patch.object(d.shutil,'which',return_value=None):report=d.inspect(False,False)
        self.assertFalse(report['ready_for_launch_attempt'])
        self.assertEqual(next(c for c in report['checks'] if c['name']=='claude_sessions_write')['status'],'NOT_PROBED')
    def test_key_forwarded_and_generated_config_private(self):
        with tempfile.TemporaryDirectory() as folder:
            root=pathlib.Path(folder);local=root/'.local';local.mkdir()
            (root/'.claude.json').write_text(json.dumps({'mcpServers':{'llamaparse':{'command':'python3','env':{'LLAMA_CLOUD_API_KEY':'old_value'}}}}))
            (local/'llamaparse.key').write_text('new_test_value\n')
            with patch.object(w,'ROOT',root),patch.object(w,'LOCAL',local),patch.object(pathlib.Path,'home',return_value=root):
                path,names=w.mcp_config()
            data=json.loads(path.read_text())
            self.assertEqual(data['mcpServers']['llamaparse']['env']['LLAMA_CLOUD_API_KEY'],'new_test_value')
            self.assertEqual(path.stat().st_mode & 0o777,0o600)
            self.assertEqual(names,['llamaparse'])
    def test_no_new_key_preserves_existing_configured_key(self):
        with tempfile.TemporaryDirectory() as folder:
            root=pathlib.Path(folder);local=root/'.local'
            (root/'.claude.json').write_text(json.dumps({'mcpServers':{'llamaparse':{'command':'python3','env':{'LLAMA_CLOUD_API_KEY':'existing_test_value'}}}}))
            with patch.object(w,'ROOT',root),patch.object(w,'LOCAL',local),patch.object(pathlib.Path,'home',return_value=root),patch.dict(w.os.environ,{},clear=True):path,_=w.mcp_config()
            self.assertEqual(json.loads(path.read_text())['mcpServers']['llamaparse']['env']['LLAMA_CLOUD_API_KEY'],'existing_test_value')
    def test_bootstrap_rejects_ancestor_repository(self):
        with tempfile.TemporaryDirectory() as folder:
            parent=pathlib.Path(folder).resolve()
            subprocess.run(['git','init','-q',str(parent)],check=True)
            target=parent/'medical'/'integrated_care'
            result=subprocess.run(['bash',str(ROOT/'scripts/bootstrap_macmini.sh'),str(target)],capture_output=True,text=True)
            self.assertEqual(result.returncode,2)
            self.assertIn('另一個 Git repository',result.stdout)
            self.assertFalse(target.exists())
    def test_mcp_symlink_not_followed(self):
        with tempfile.TemporaryDirectory() as folder:
            root=pathlib.Path(folder);local=root/'.local';local.mkdir()
            target=root/'untouched';target.write_text('keep')
            (local/'mcp.research.json').symlink_to(target)
            with patch.object(w,'ROOT',root),patch.object(w,'LOCAL',local),patch.object(pathlib.Path,'home',return_value=root):
                with self.assertRaises(RuntimeError):w.mcp_config()
            self.assertEqual(target.read_text(),'keep')
if __name__=='__main__':unittest.main()
