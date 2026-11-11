import math, pathlib, sys, unittest
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'calculators'))
from dmic_calculators import staging, liver, foot


class Staging(unittest.TestCase):
    def test_g_boundaries(self):
        cases = {95: 'G1', 90: 'G1', 89.9: 'G2', 60: 'G2', 59.9: 'G3a', 45: 'G3a', 44.9: 'G3b', 30: 'G3b',
                 29.9: 'G4', 15: 'G4', 14.9: 'G5'}
        for e, g in cases.items():
            self.assertEqual(staging.ckd_g_category(e)['value'], g, e)

    def test_a_boundaries_mg_g(self):
        for u, a in ((0, 'A1'), (29.9, 'A1'), (30, 'A2'), (300, 'A2'), (300.1, 'A3')):
            self.assertEqual(staging.ckd_a_category(uacr_mg_g=u)['value'], a, u)
        self.assertTrue(staging.ckd_a_category(uacr_mg_g=300)['details']['warnings'])

    def test_a_boundaries_mg_mmol(self):
        for u, a in ((2.9, 'A1'), (3, 'A2'), (30, 'A2'), (30.1, 'A3')):
            self.assertEqual(staging.ckd_a_category(uacr_mg_mmol=u)['value'], a, u)

    def test_a_missing_ambiguous_negative(self):
        self.assertIn('missing:uacr', staging.ckd_a_category()['reasons_unavailable'])
        self.assertIsNone(staging.ckd_a_category(uacr_mg_g=10, uacr_mg_mmol=1)['value'])
        self.assertIsNone(staging.ckd_a_category(uacr_mg_g=-1)['value'])

    def test_heatmap_all_cells_against_figure(self):
        expect = {'G1': 'gyo', 'G2': 'gyo', 'G3a': 'yor', 'G3b': 'orr', 'G4': 'rrr', 'G5': 'rrr'}
        name = {'g': 'green', 'y': 'yellow', 'o': 'orange', 'r': 'red'}
        egfr = {'G1': 95, 'G2': 75, 'G3a': 50, 'G3b': 35, 'G4': 20, 'G5': 10}
        acr = {'A1': 10, 'A2': 100, 'A3': 1000}
        for g, row in expect.items():
            for i, a in enumerate(('A1', 'A2', 'A3')):
                r = staging.ckd_cga_risk(egfr[g], uacr_mg_g=acr[a])
                self.assertEqual(r['value'], '%s/%s' % (g, a))
                self.assertEqual(r['details']['risk_colour'], name[row[i]], (g, a))

    def test_cga_missing_partial(self):
        r = staging.ckd_cga_risk(50)
        self.assertIsNone(r['value'])
        self.assertIn('missing:uacr', r['reasons_unavailable'])


class Fib4(unittest.TestCase):
    def test_formula_vector(self):
        r = liver.fib4(50, 40, 25, 200)
        self.assertAlmostEqual(r['value'], 2.0, places=12)  # 50*40/(200*sqrt(25))
        self.assertEqual(r['details']['category'], 'indeterminate')
        self.assertTrue(r['population_ok'])

    def test_categories(self):
        self.assertEqual(liver.fib4(40, 25, 25, 200)['details']['category'], 'low')           # 1.0
        self.assertEqual(liver.fib4(52, 25, 25, 200)['details']['category'], 'indeterminate')  # 1.3 boundary
        self.assertEqual(liver.fib4(60, 50, 25, 100)['details']['category'], 'high')          # 6.0

    def test_age_over_65_uses_2_0_lower_cutoff(self):
        old = liver.fib4(70, 30, 25, 280)     # 1.5
        young = liver.fib4(50, 30, 25, 200)   # 1.5
        self.assertAlmostEqual(old['value'], 1.5, places=12)
        self.assertAlmostEqual(young['value'], 1.5, places=12)
        self.assertEqual(old['details']['category'], 'low')
        self.assertEqual(young['details']['category'], 'indeterminate')

    def test_age_65_flagged_and_under_35_warned(self):
        self.assertTrue(liver.fib4(65, 30, 25, 200)['details']['warnings'])
        self.assertTrue(liver.fib4(30, 30, 25, 200)['details']['warnings'])

    def test_missing_and_nonpositive(self):
        base = dict(age_years=50, ast_u_l=40, alt_u_l=25, platelets_10e9_l=200)
        for k in base:
            kw = dict(base); kw[k] = None
            r = liver.fib4(**kw)
            self.assertIsNone(r['value'], k)
            self.assertIn('missing:%s' % k, r['reasons_unavailable'])
        for k in ('ast_u_l', 'alt_u_l', 'platelets_10e9_l'):
            kw = dict(base); kw[k] = 0
            self.assertIsNone(liver.fib4(**kw)['value'], k)

    def test_raw_platelet_count_flagged_not_converted(self):
        r = liver.fib4(50, 40, 25, 250000)
        self.assertIsNone(r['value'])
        self.assertTrue(any(x.startswith('suspect_units') for x in r['reasons_unavailable']))

    def test_acute_illness_and_minor_excluded(self):
        r = liver.fib4(50, 40, 25, 200, acute_illness=True)
        self.assertIsNone(r['value']); self.assertFalse(r['population_ok'])
        self.assertFalse(liver.fib4(16, 40, 25, 200)['population_ok'])

    def test_apri(self):
        self.assertAlmostEqual(liver.apri(80, 40, 100)['value'], 2.0, places=12)
        r = liver.apri(80, None, 100)
        self.assertIsNone(r['value']); self.assertIn('missing:ast_uln_u_l', r['reasons_unavailable'])


class Iwgdf(unittest.TestCase):
    def cat(self, **kw):
        return foot.iwgdf_risk_category(**kw)

    def test_table1_rows(self):
        F, T = False, True
        base = dict(loss_of_protective_sensation=F, peripheral_artery_disease=F, foot_deformity=F,
                    history_foot_ulcer=F, lower_extremity_amputation=F, end_stage_renal_disease=F)
        def mk(**over):
            d = dict(base); d.update(over); return self.cat(**d)
        self.assertEqual(mk()['value'], 0)
        self.assertEqual(mk(foot_deformity=T)['value'], 0)                                 # deformity alone
        self.assertEqual(mk(loss_of_protective_sensation=T)['value'], 1)
        self.assertEqual(mk(peripheral_artery_disease=T)['value'], 1)
        self.assertEqual(mk(loss_of_protective_sensation=T, peripheral_artery_disease=T)['value'], 2)
        self.assertEqual(mk(loss_of_protective_sensation=T, foot_deformity=T)['value'], 2)
        self.assertEqual(mk(peripheral_artery_disease=T, foot_deformity=T)['value'], 2)
        for h in ('history_foot_ulcer', 'lower_extremity_amputation', 'end_stage_renal_disease'):
            self.assertEqual(mk(loss_of_protective_sensation=T, **{h: T})['value'], 3, h)
            self.assertEqual(mk(peripheral_artery_disease=T, **{h: T})['value'], 3, h)
            self.assertEqual(mk(**{h: T})['value'], 0, h)   # history alone, no LOPS/PAD
        r = mk(loss_of_protective_sensation=T, history_foot_ulcer=T)
        self.assertEqual(r['details']['screening_frequency'], 'once every 1-3 months')

    def test_all_unknown_is_not_zero(self):
        r = self.cat()
        self.assertIsNone(r['value'])
        self.assertEqual((r['details']['at_least'], r['details']['at_most']), (0, 3))

    def test_unknown_exam_not_assumed_negative(self):
        r = self.cat(loss_of_protective_sensation=True)  # PAD, deformity, history unknown
        self.assertIsNone(r['value'])
        self.assertEqual(r['details']['at_least'], 1)

    def test_unknown_irrelevant_fields_still_determinate(self):
        r = self.cat(loss_of_protective_sensation=False, peripheral_artery_disease=False)
        self.assertEqual(r['value'], 0)   # remaining unknowns cannot change category 0
        r = self.cat(loss_of_protective_sensation=True, peripheral_artery_disease=True, end_stage_renal_disease=True)
        self.assertEqual(r['value'], 3)

    def test_non_bool_rejected(self):
        r = self.cat(loss_of_protective_sensation='yes')
        self.assertIsNone(r['value'])


if __name__ == '__main__':
    unittest.main()
