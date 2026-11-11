import pathlib, sys, unittest
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'calculators'))
from dmic_calculators import recode as rc

# Paper's worked example (Lancet Diabetes Endocrinol 2017, footnotes of Tables 2-4):
# 60-y white man, SBP 140, no CVD, no drugs, no smoking, HbA1c 8%, TC 190, HDL 50, Cr 1.1, UACR 10.
EX = dict(age_years=60, female=False, black=False, hispanic=False, current_smoker=False, sbp_mmhg=140,
          cvd_history=False, bp_lowering_drugs=False, oral_diabetes_drugs=False, statins=False,
          anticoagulants=False, hba1c_percent=8, total_chol_mg_dl=190, hdl_mg_dl=50, creatinine_mg_dl=1.1,
          uacr_mg_g=10)


class Recode(unittest.TestCase):
    def test_paper_example_esrd_8_5_percent(self):
        r = rc.recode('renal_failure_esrd', **EX)
        self.assertAlmostEqual(r['value'], 8.5, delta=0.3)   # paper: 0.085 (coefficients printed with more digits)
        self.assertTrue(r['population_ok'])

    def test_paper_example_all_cause_mortality_9_percent(self):
        r = rc.recode('all_cause_mortality', **EX)
        self.assertAlmostEqual(r['value'], 9.0, delta=0.5)   # paper: 0.09

    def test_paper_example_pressure_sensation_13_percent(self):
        kw = {k: v for k, v in EX.items() if k != 'uacr_mg_g'}   # UACR has no term in this model
        r = rc.recode('pressure_sensation_loss', **kw)
        self.assertAlmostEqual(r['value'], 13.0, delta=0.6)       # paper: 0.13

    def test_exact_footnote_arithmetic_esrd(self):
        # footnote's own more-precise coefficients -> 1-0.973^exp(...) = 0.085
        import math
        lp = -0.01938*60 + 0.003027*140 + 0.1369*8 - 0.001112*190 + 0.006289*50 + 0.8609*1.1 + 0.000362*10 - 0.23
        self.assertAlmostEqual(1 - 0.973 ** math.exp(lp), 0.085, places=3)

    def test_missing_covariate_returns_none_by_default(self):
        kw = dict(EX); kw['uacr_mg_g'] = None
        r = rc.recode('all_cause_mortality', **kw)
        self.assertIsNone(r['value'])
        self.assertIn('missing:uacr_mg_g', r['reasons_unavailable'])

    def test_omit_option_is_explicit_and_flagged(self):
        kw = dict(EX); kw['uacr_mg_g'] = None
        r = rc.recode('all_cause_mortality', allow_omit_missing_terms=True, **kw)
        self.assertIsNotNone(r['value'])
        self.assertEqual(r['details']['omitted_terms'], ['uacr_mg_g'])
        self.assertTrue(r['details']['warnings'])

    def test_binary_requires_bool_and_numbers_positive(self):
        kw = dict(EX); kw['female'] = 0
        self.assertIsNone(rc.recode('all_cause_mortality', **kw)['value'])
        kw = dict(EX); kw['creatinine_mg_dl'] = 0
        self.assertIsNone(rc.recode('all_cause_mortality', **kw)['value'])

    def test_spec_only_and_unknown_outcome(self):
        for o in ('microalbuminuria', 'cataract_extraction'):
            r = rc.recode(o, **EX)
            self.assertIsNone(r['value'])
            self.assertTrue(r['reasons_unavailable'][0].startswith('spec_only'))
        self.assertIsNone(rc.recode('total_risk', **EX)['value'])

    def test_unknown_covariate_name_rejected(self):
        kw = dict(EX); kw['bmi'] = 30
        self.assertIsNone(rc.recode('ascvd', **kw)['value'])

    def test_age_outside_accord_range(self):
        kw = dict(EX); kw['age_years'] = 85
        r = rc.recode('ascvd', **kw)
        self.assertIsNone(r['value']); self.assertFalse(r['population_ok'])

    def test_all_models_run_and_in_unit_interval(self):
        for o in rc.MODELS:
            r = rc.recode(o, **EX)
            self.assertIsNotNone(r['value'], (o, r['reasons_unavailable']))
            self.assertTrue(0 < r['value'] < 100, o)

    def test_monotonic_age(self):
        a = rc.recode('all_cause_mortality', **dict(EX, age_years=50))['value']
        b = rc.recode('all_cause_mortality', **dict(EX, age_years=70))['value']
        self.assertLess(a, b)


if __name__ == '__main__':
    unittest.main()
