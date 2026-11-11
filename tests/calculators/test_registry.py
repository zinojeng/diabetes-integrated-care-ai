import importlib, pathlib, sys, unittest
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'calculators'))
import dmic_calculators as pkg
from dmic_calculators.registry import REGISTRY, STATUSES


class Registry(unittest.TestCase):
    def test_entries_resolve_and_statuses_valid(self):
        ids = set()
        for e in REGISTRY:
            self.assertIn(e['status'], STATUSES, e['id'])
            self.assertNotIn(e['id'], ids); ids.add(e['id'])
            if e['entry']:
                mod, fn = e['entry'].split('.')
                self.assertTrue(callable(getattr(getattr(pkg, mod), fn)), e['entry'])
            if e['status'] == 'spec_only' or e['status'] == 'provisional':
                self.assertTrue(e['missing'], e['id'])

    def test_spec_only_without_entry_have_no_function(self):
        for e in REGISTRY:
            if e['status'] == 'spec_only' and e['entry'] is None:
                for mod in ('cvd', 'recode', 'comorbidity', 'ckd'):
                    for bad in ('prevent', 'watch_dm', 'watchdm', 'karter', 'advance', 'ukpds_om2'):
                        self.assertFalse(hasattr(getattr(pkg, mod), bad), (e['id'], mod, bad))

    def test_all_results_have_unified_keys(self):
        keys = {'tool', 'version', 'value', 'units', 'population_ok', 'reasons_unavailable', 'inputs_used', 'source', 'details'}
        samples = [pkg.ckd.ckd_epi_2021_creatinine(), pkg.ckd.kfre_4var(), pkg.cvd.score2_diabetes(),
                   pkg.cvd.timi_trs2p_t2d(), pkg.cvd.ukpds_risk_engine(), pkg.recode.recode('ascvd'),
                   pkg.liver.fib4(), pkg.liver.apri(), pkg.foot.iwgdf_risk_category(), pkg.staging.ckd_cga_risk(),
                   pkg.scales.phq9(), pkg.scales.who5(), pkg.scales.paid20(), pkg.scales.dds17(), pkg.scales.frail_scale(),
                   pkg.comorbidity.charlson('quan_2011', {}), pkg.comorbidity.dcsi()]
        for s in samples:
            self.assertEqual(set(s), keys, s['tool'])
            self.assertIn('kind', s['details'], s['tool'])
            self.assertIsNone(s['value'], s['tool'])     # no inputs -> never a number
            self.assertTrue(s['reasons_unavailable'], s['tool'])

    def test_no_value_with_reasons_ever(self):
        r = pkg.result.result('x', 'v', 5, 'u', True, ['why'], {}, 's', 'risk_estimate')
        self.assertIsNone(r['value'])


if __name__ == '__main__':
    unittest.main()
