import math, pathlib, sys, unittest
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'calculators'))
from dmic_calculators import ckd

KEYS = {'tool', 'version', 'value', 'units', 'population_ok', 'reasons_unavailable', 'inputs_used', 'source', 'details'}


def ref_cr(age, female, scr):
    """Independent piecewise form transcribed from NIDDK Table 1 (not min/max code path)."""
    if female:
        base = 142 * (scr / 0.7) ** -0.241 if scr <= 0.7 else 142 * (scr / 0.7) ** -1.200
        return base * 0.9938 ** age * 1.012
    base = 142 * (scr / 0.9) ** -0.302 if scr <= 0.9 else 142 * (scr / 0.9) ** -1.200
    return base * 0.9938 ** age


def ref_crcys(age, female, scr, cys):
    """Piecewise forms of NIDDK Table 2."""
    k, a = (0.7, -0.219) if female else (0.9, -0.144)
    a_part = (scr / k) ** a if scr <= k else (scr / k) ** -0.544
    c_part = (cys / 0.8) ** -0.323 if cys <= 0.8 else (cys / 0.8) ** -0.778
    return 135 * a_part * c_part * 0.9961 ** age * (0.963 if female else 1)


class CkdEpi(unittest.TestCase):
    def test_structure(self):
        r = ckd.ckd_epi_2021_creatinine(60, 'female', 0.9)
        self.assertEqual(set(r), KEYS)

    def test_creatinine_matches_piecewise_reference(self):
        cases = [(60, 'female', 0.9), (60, 'female', 0.6), (45, 'male', 1.2), (45, 'male', 0.8),
                 (80, 'male', 2.5), (18, 'female', 0.7), (30, 'male', 0.9)]
        for age, sex, scr in cases:
            r = ckd.ckd_epi_2021_creatinine(age, sex, scr)
            self.assertAlmostEqual(r['value'], ref_cr(age, sex == 'female', scr), places=9)
            self.assertTrue(r['population_ok'])
            self.assertEqual(r['reasons_unavailable'], [])

    def test_kappa_boundary_closed_form(self):
        # At SCr == kappa the creatinine term is exactly 1.
        self.assertAlmostEqual(ckd.ckd_epi_2021_creatinine(50, 'male', 0.9)['value'], 142 * 0.9938 ** 50, places=9)
        self.assertAlmostEqual(ckd.ckd_epi_2021_creatinine(50, 'female', 0.7)['value'], 142 * 0.9938 ** 50 * 1.012, places=9)

    def test_umol_equals_mgdl(self):
        a = ckd.ckd_epi_2021_creatinine(55, 'male', scr_umol_l=88.4)['value']
        b = ckd.ckd_epi_2021_creatinine(55, 'male', scr_mg_dl=1.0)['value']
        self.assertAlmostEqual(a, b, places=9)

    def test_missing_and_invalid_return_none_with_reason(self):
        for kw, reason in [
            (dict(age_years=None, sex='male', scr_mg_dl=1.0), 'missing:age_years'),
            (dict(age_years=50, sex=None, scr_mg_dl=1.0), 'missing:sex'),
            (dict(age_years=50, sex='male'), 'missing:serum_creatinine'),
            (dict(age_years=50, sex='male', scr_mg_dl=0), 'non_positive:scr_mg_dl'),
            (dict(age_years=50, sex='male', scr_mg_dl=-1.0), 'non_positive:scr_mg_dl'),
            (dict(age_years=17, sex='male', scr_mg_dl=1.0), 'below_minimum:age_years<18'),
            (dict(age_years=50, sex='x', scr_mg_dl=1.0), 'invalid_value:sex'),
            (dict(age_years=50, sex='male', scr_mg_dl=1.0, scr_umol_l=88.4),
             'ambiguous_units:give_only_one_of_scr_mg_dl_or_scr_umol_l'),
            (dict(age_years=50, sex='male', scr_mg_dl=float('nan')), 'invalid_type:scr_mg_dl'),
            (dict(age_years=True, sex='male', scr_mg_dl=1.0), 'invalid_type:age_years'),
            (dict(age_years='50', sex='male', scr_mg_dl=1.0), 'invalid_type:age_years'),
        ]:
            r = ckd.ckd_epi_2021_creatinine(**kw)
            self.assertIsNone(r['value'], kw)
            self.assertIn(reason, r['reasons_unavailable'], kw)

    def test_cr_cys_matches_piecewise_reference(self):
        cases = [(60, 'female', 0.9, 1.2), (60, 'female', 0.6, 0.7), (45, 'male', 1.2, 1.5),
                 (45, 'male', 0.8, 0.6), (70, 'male', 0.9, 0.8), (70, 'female', 0.7, 0.8)]
        for age, sex, scr, cys in cases:
            r = ckd.ckd_epi_2021_creatinine_cystatin(age, sex, scr, cystatin_c_mg_l=cys)
            self.assertAlmostEqual(r['value'], ref_crcys(age, sex == 'female', scr, cys), places=9)

    def test_cr_cys_requires_cystatin(self):
        r = ckd.ckd_epi_2021_creatinine_cystatin(60, 'male', 1.0)
        self.assertIsNone(r['value'])
        self.assertIn('missing:cystatin_c_mg_l', r['reasons_unavailable'])
        r = ckd.ckd_epi_2021_creatinine_cystatin(60, 'male', 1.0, cystatin_c_mg_l=0)
        self.assertIn('non_positive:cystatin_c_mg_l', r['reasons_unavailable'])


def ref_kfre(age, male, egfr, uacr, s0):
    lp = (-0.2201 * (age / 10 - 7.036) + 0.2467 * (male - 0.5642)
          - 0.5567 * (egfr / 5 - 7.222) + 0.4510 * (math.log(uacr) - 5.137))
    return 1 - s0 ** math.exp(lp)


class Kfre(unittest.TestCase):
    def test_5yr_original_vector(self):
        r = ckd.kfre_4var(65, 'male', 30, 300, horizon_years=5)
        self.assertAlmostEqual(r['value'], ref_kfre(65, 1, 30, 300, 0.924), places=12)
        self.assertTrue(r['population_ok'])
        self.assertEqual(r['details']['s0_status'], 'verified')

    def test_5yr_non_north_america_vector(self):
        r = ckd.kfre_4var(65, 'female', 45, 100, horizon_years=5, calibration='non_north_america')
        self.assertAlmostEqual(r['value'], ref_kfre(65, 0, 45, 100, 0.9365), places=12)

    def test_lp_zero_returns_one_minus_s0(self):
        lp = ckd.kfre_linear_predictor(70.36, 0.5642, 36.11, math.exp(5.137))
        self.assertAlmostEqual(lp, 0.0, places=9)
        self.assertAlmostEqual(1 - 0.924 ** math.exp(lp), 0.076, places=9)

    def test_monotonic(self):
        lo = ckd.kfre_4var(60, 'male', 40, 30)['value']
        hi = ckd.kfre_4var(60, 'male', 40, 3000)['value']
        self.assertLess(lo, hi)
        self.assertLess(ckd.kfre_4var(60, 'male', 50, 300)['value'], ckd.kfre_4var(60, 'male', 20, 300)['value'])

    def test_mg_per_mmol_conversion(self):
        a = ckd.kfre_4var(60, 'male', 40, uacr_mg_mmol=10)['value']
        b = ckd.kfre_4var(60, 'male', 40, uacr_mg_g=88.4)['value']
        self.assertAlmostEqual(a, b, places=12)

    def test_two_units_ambiguous_and_missing_uacr(self):
        r = ckd.kfre_4var(60, 'male', 40, uacr_mg_g=100, uacr_mg_mmol=10)
        self.assertIsNone(r['value'])
        self.assertTrue(any(x.startswith('ambiguous_units') for x in r['reasons_unavailable']))
        r = ckd.kfre_4var(60, 'male', 40)
        self.assertIsNone(r['value'])
        self.assertIn('missing:uacr', r['reasons_unavailable'])

    def test_nonpositive_uacr_not_replaced(self):
        for u in (0, -5):
            r = ckd.kfre_4var(60, 'male', 40, uacr_mg_g=u)
            self.assertIsNone(r['value'])
            self.assertIn('non_positive:uacr_mg_g', r['reasons_unavailable'])

    def test_outside_population_egfr_ge_60(self):
        r = ckd.kfre_4var(60, 'male', 75, 300)
        self.assertIsNone(r['value'])
        self.assertFalse(r['population_ok'])

    def test_missing_each_input(self):
        base = dict(age_years=60, sex='male', egfr=40, uacr_mg_g=100)
        for k in base:
            kw = dict(base); kw[k] = None
            r = ckd.kfre_4var(**kw)
            self.assertIsNone(r['value'], k)
            self.assertTrue(r['reasons_unavailable'], k)

    def test_provisional_2yr_gated(self):
        r = ckd.kfre_4var(65, 'male', 30, 300, horizon_years=2)
        self.assertIsNone(r['value'])
        self.assertTrue(any(x.startswith('provisional_baseline_not_enabled') for x in r['reasons_unavailable']))
        r = ckd.kfre_4var(65, 'male', 30, 300, horizon_years=2, allow_provisional=True)
        self.assertAlmostEqual(r['value'], ref_kfre(65, 1, 30, 300, 0.975), places=12)
        self.assertEqual(r['details']['s0_status'], 'provisional')

    def test_north_america_is_spec_only(self):
        for h in (2, 5):
            r = ckd.kfre_4var(65, 'male', 30, 300, horizon_years=h, calibration='north_america', allow_provisional=True)
            self.assertIsNone(r['value'])
            self.assertTrue(any(x.startswith('spec_only') for x in r['reasons_unavailable']))

    def test_unsupported_version(self):
        r = ckd.kfre_4var(65, 'male', 30, 300, horizon_years=3)
        self.assertIsNone(r['value'])

    def test_non_na_2yr_consistency_with_32_9pct_reduction(self):
        # PMC4752167: regional factor lowers baseline 2-yr risk by 32.9% -> S0 ~0.9832 from 0.9750
        self.assertAlmostEqual(1 - (1 - 0.9750) * (1 - 0.329), 0.9832, places=4)
        # and 16.5% at 5 yr: 0.076 -> 0.0635
        self.assertAlmostEqual((1 - 0.9240) * (1 - 0.165), 1 - 0.9365, places=3)


if __name__ == '__main__':
    unittest.main()
