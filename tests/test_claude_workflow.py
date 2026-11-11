"""State integrity tests: no fake registration, duplicate launch, or continuing after failure."""
import importlib.util, json, pathlib, subprocess, tempfile, unittest
from unittest.mock import patch
SOURCE=pathlib.Path(__file__).resolve().parents[1]/'scripts/claude_workflow.py'
spec=importlib.util.spec_from_file_location('workflow',SOURCE)
w=importlib.util.module_from_spec(spec);spec.loader.exec_module(w)

class LaunchTests(unittest.TestCase):
    def test_duplicate_does_not_launch(self):
        with patch.object(w,'records',return_value=[{'name':'DMIC-complications','id':'one'}]),patch.object(w,'run') as execute:
            w.start('complications');execute.assert_not_called()

    def test_failed_launch_never_marks_registered(self):
        with tempfile.TemporaryDirectory() as temp:
            root=pathlib.Path(temp)
            (root/'workflow').mkdir();(root/'workflow/subagents.json').write_text('{}')
            with patch.object(w,'ROOT',root),patch.object(w,'LOCAL',root),patch.object(w,'records',return_value=[]),patch.object(w,'mcp_config',return_value=(root/'mcp.json',[])),patch.object(w,'prompt',return_value='review'),patch.object(w,'run',return_value=subprocess.CompletedProcess([],1,'','Workspace not trusted')),patch.object(w,'event') as event:
                with self.assertRaises(RuntimeError):w.start('complications')
                self.assertFalse(any(c.kwargs.get('status')=='registered_not_reviewed' for c in event.call_args_list))

    def test_success_without_registry_is_not_success(self):
        with tempfile.TemporaryDirectory() as temp:
            root=pathlib.Path(temp)
            (root/'workflow').mkdir();(root/'workflow/subagents.json').write_text('{}')
            with patch.object(w,'ROOT',root),patch.object(w,'LOCAL',root),patch.object(w,'records',return_value=[]),patch.object(w,'mcp_config',return_value=(root/'mcp.json',[])),patch.object(w,'prompt',return_value='review'),patch.object(w,'run',return_value=subprocess.CompletedProcess([],0,'backgrounded','')),patch.object(w,'event'):
                with self.assertRaisesRegex(RuntimeError,'not unique/verified'):w.start('complications')

    def test_verified_registration_preserves_model(self):
        with tempfile.TemporaryDirectory() as temp:
            root=pathlib.Path(temp)
            (root/'workflow').mkdir();(root/'workflow/subagents.json').write_text('{}')
            record={'name':'DMIC-complications','id':'one','sessionId':'sid','state':'working'}
            with patch.object(w,'ROOT',root),patch.object(w,'LOCAL',root),patch.object(w,'records',side_effect=[[],[record]]),patch.object(w,'mcp_config',return_value=(root/'mcp.json',[])),patch.object(w,'prompt',return_value='review'),patch.object(w,'run',return_value=subprocess.CompletedProcess([],0,'backgrounded','')) as execute,patch.object(w,'event') as event:
                w.start('complications')
                argv=execute.call_args.args[0]
                self.assertEqual(argv[argv.index('--model')+1],'claude-opus-5-5')
                self.assertNotIn('--dangerously-skip-permissions',argv)
                self.assertEqual(event.call_args.kwargs['status'],'registered_not_reviewed')

    def test_registry_schema_is_checked(self):
        with patch.object(w,'run',return_value=subprocess.CompletedProcess([],0,'{}','')):
            with self.assertRaises(RuntimeError):w.records()

if __name__=='__main__':unittest.main()
