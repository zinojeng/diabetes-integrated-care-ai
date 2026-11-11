import pathlib, sys, unittest
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'calculators'))
from dmic_calculators import cvd

# Official SCORE2-Diabetes Excel (appendix_2.xlsx, sheet 'calculator'/'values'): same inputs, both sexes.
OFFICIAL = dict(age_years=53, diabetes_age_at_diagnosis=30, current_smoker=True, sbp_mmhg=110,
                total_chol_mmol_l=4.5, hdl_mmol_l=1.4, hba1c_mmol_mol=55, egfr=95,
                prior_cvd=False, severe_target_organ_damage=False, egfr_equation='CKD-EPI-2009')
EXCEL = {  # (sex, region) -> calibrated 10-yr risk %, Excel cells D14:D17 (men), H14:H17 (women)
    ('male', 'low'): 9.9553916389537811, ('male', 'moderate'): 13.116444885691047,
    ('male', 'high'): 15.388566936926818, ('male', 'very_high'): 24.147741949388656,
    ('female', 'low'): 8.0800210342973351, ('female', 'moderate'): 10.302441868725165,
    ('female', 'high'): 16.007637019557475, ('female', 'very_high'): 27.869447538407009,
}
EXCEL_LP = {'male': 0.95724968797531651, 'female': 1.314179117224475}


class Score2Diabetes(unittest.TestCase):
    def test_official_excel_vectors(self):
        for (sex, region), expect in EXCEL.items():
            r = cvd.score2_diabetes(sex=sex, risk_region=region, **OFFICIAL)
            self.assertAlmostEqual(r['value'], expect, places=9, msg=(sex, region))
            self.assertTrue(r['population_ok'])
            self.assertAlmostEqual(r['details']['linear_predictor'], EXCEL_LP[sex], places=9)
            self.assertEqual(r['reasons_unavailable'], [])

    def test_missing_each_required_input(self):
        full = dict(sex='male', risk_region='moderate', **OFFICIAL)
        for k in ['sex', 'age_years', 'diabetes_age_at_diagnosis', 'current_smoker', 'sbp_mmhg',
                  'total_chol_mmol_l', 'hdl_mmol_l', 'hba1c_mmol_mol', 'egfr', 'risk_region', 'prior_cvd']:
            kw = dict(full); kw[k] = None
            r = cvd.score2_diabetes(**kw)
            self.assertIsNone(r['value'], k)
            self.assertTrue(r['reasons_unavailable'], k)

    def test_no_default_region(self):
        r = cvd.score2_diabetes(sex='male', **OFFICIAL)
        self.assertIsNone(r['value'])
        self.assertTrue(any(x.startswith('missing:risk_region') for x in r['reasons_unavailable']))
        r = cvd.score2_diabetes(sex='male', risk_region='taiwan', **OFFICIAL)
        self.assertIn('invalid_value:risk_region', r['reasons_unavailable'])

    def test_population_exclusions(self):
        base = dict(sex='male', risk_region='moderate', **OFFICIAL)
        for override in (dict(age_years=39), dict(age_years=70), dict(prior_cvd=True),
                         dict(severe_target_organ_damage=True)):
            kw = dict(base); kw.update(override)
            r = cvd.score2_diabetes(**kw)
            self.assertIsNone(r['value'], override)
            self.assertFalse(r['population_ok'], override)

    def test_age_boundaries_inclusive(self):
        for a in (40, 69):
            kw = dict(sex='female', risk_region='low', **OFFICIAL); kw['age_years'] = a
            self.assertIsNotNone(cvd.score2_diabetes(**kw)['value'], a)

    def test_diagnosis_age_after_current_age_rejected(self):
        kw = dict(sex='male', risk_region='low', **OFFICIAL); kw['diabetes_age_at_diagnosis'] = 60
        r = cvd.score2_diabetes(**kw)
        self.assertIsNone(r['value'])
        self.assertIn('inconsistent:diabetes_age_at_diagnosis>age_years', r['reasons_unavailable'])

    def test_non_bool_smoker_and_nonpositive_values_rejected(self):
        kw = dict(sex='male', risk_region='low', **OFFICIAL)
        kw['current_smoker'] = 'yes'
        self.assertIsNone(cvd.score2_diabetes(**kw)['value'])
        kw = dict(sex='male', risk_region='low', **OFFICIAL); kw['egfr'] = 0
        self.assertIn('non_positive:egfr', cvd.score2_diabetes(**kw)['reasons_unavailable'])
        kw = dict(sex='male', risk_region='low', **OFFICIAL); kw['hba1c_mmol_mol'] = -1
        self.assertIsNone(cvd.score2_diabetes(**kw)['value'])

    def test_egfr_equation_warning_and_unknown_tod_not_assumed_absent(self):
        kw = dict(sex='male', risk_region='low', **OFFICIAL)
        kw['egfr_equation'] = 'CKD-EPI-2021'; kw['severe_target_organ_damage'] = None
        r = cvd.score2_diabetes(**kw)
        self.assertIsNotNone(r['value'])
        self.assertEqual(len(r['details']['warnings']), 2)

    def test_higher_region_higher_risk(self):
        vals = [cvd.score2_diabetes(sex='male', risk_region=g, **OFFICIAL)['value']
                for g in ('low', 'moderate', 'high', 'very_high')]
        self.assertEqual(vals, sorted(vals))


if __name__ == '__main__':
    unittest.main()


class TimiTrs2p(unittest.TestCase):
    BASE = dict(age_years=60, hypertension=False, current_smoker=False, peripheral_artery_disease=False,
                prior_stroke=False, prior_mi=False, prior_cabg=False, heart_failure=False, egfr=90,
                type2_diabetes=True)

    def mk(self, **o):
        d = dict(self.BASE); d.update(o)
        return cvd.timi_trs2p_t2d(**d)

    def test_minimum_score_is_one_in_t2d(self):
        r = self.mk()
        self.assertEqual(r['value'], 1)                       # 'lowest possible score was 1' (paper)
        self.assertEqual(r['details']['score_bin'], '<=2')

    def test_each_criterion_adds_one(self):
        for k, v in (('hypertension', True), ('current_smoker', True), ('peripheral_artery_disease', True),
                     ('prior_stroke', True), ('prior_mi', True), ('prior_cabg', True), ('heart_failure', True),
                     ('age_years', 75), ('egfr', 59)):
            self.assertEqual(self.mk(**{k: v})['value'], 2, k)
        self.assertEqual(self.mk(egfr=60)['value'], 1)

    def test_all_ten(self):
        r = self.mk(age_years=80, hypertension=True, current_smoker=True, peripheral_artery_disease=True,
                    prior_stroke=True, prior_mi=True, prior_cabg=True, heart_failure=True, egfr=30)
        self.assertEqual(r['value'], 10)
        self.assertEqual(r['details']['score_bin'], '>=5')
        self.assertEqual(r['details']['group_reference_rates_2yr_pct']['cv_death'], 6.8)

    def test_bins_match_table3(self):
        self.assertEqual(self.mk(hypertension=True, current_smoker=True)['details']['score_bin'], '3')
        self.assertEqual(self.mk(hypertension=True, current_smoker=True, prior_mi=True)['details']['score_bin'], '4')
        self.assertEqual(sum(v['n'] for v in cvd.TIMI_BIN_RATES.values()), 4034 + 5516 + 4221 + 2717)

    def test_missing_any_input_no_default_negative(self):
        for k in self.BASE:
            r = self.mk(**{k: None})
            self.assertIsNone(r['value'], k)
            self.assertTrue(r['reasons_unavailable'], k)

    def test_not_t2d_excluded_and_age_75_warning(self):
        r = self.mk(type2_diabetes=False)
        self.assertIsNone(r['value']); self.assertFalse(r['population_ok'])
        self.assertTrue(any('age==75' in w for w in self.mk(age_years=75)['details']['warnings']))


class UkpdsRiskEngine(unittest.TestCase):
    import math as _m
    BASE = dict(sex='male', age_at_diagnosis=55, diabetes_duration_years=0, current_smoker=False, hba1c_percent=6.72,
                sbp_mmhg=135.7, total_chol_hdl_ratio=cvd.math.exp(1.59), afro_caribbean=False, atrial_fibrillation=False,
                prior_chd_or_stroke=False, horizon_years=10, allow_provisional=True)

    def test_reference_individual_equals_q0_closed_form(self):
        # all covariates at reference -> q = q0; T=0 -> R = 1-exp(-q0 (1-d^t)/(1-d))
        r = cvd.ukpds_risk_engine('chd', **self.BASE)
        d, q0 = 1.078, 0.0112
        expect = 100 * (1 - cvd.math.exp(-q0 * (1 - d ** 10) / (1 - d)))
        self.assertAlmostEqual(r['value'], expect, places=9)
        kw = dict(self.BASE, total_chol_hdl_ratio=5.11)
        r = cvd.ukpds_risk_engine('stroke', **kw)
        d, q0 = 1.145, 0.00186
        self.assertAlmostEqual(r['value'], 100 * (1 - cvd.math.exp(-q0 * (1 - d ** 10) / (1 - d))), places=9)

    def test_zero_horizon_gives_zero_not_nonzero(self):
        # the d*t misreading would give non-zero; horizon must be positive so check tiny horizon is near 0
        r = cvd.ukpds_risk_engine('chd', **dict(self.BASE, horizon_years=1e-9))
        self.assertLess(r['value'], 1e-6)

    def test_provisional_gate(self):
        r = cvd.ukpds_risk_engine('chd', **dict(self.BASE, allow_provisional=False))
        self.assertIsNone(r['value'])
        self.assertTrue(any(x.startswith('provisional_equation_not_enabled') for x in r['reasons_unavailable']))

    def test_hazard_directions(self):
        base = cvd.ukpds_risk_engine('chd', **self.BASE)['value']
        self.assertGreater(cvd.ukpds_risk_engine('chd', **dict(self.BASE, current_smoker=True))['value'], base)
        self.assertGreater(cvd.ukpds_risk_engine('chd', **dict(self.BASE, hba1c_percent=9))['value'], base)
        self.assertLess(cvd.ukpds_risk_engine('chd', **dict(self.BASE, sex='female'))['value'], base)
        self.assertGreater(cvd.ukpds_risk_engine('stroke', **dict(self.BASE, total_chol_hdl_ratio=5.11, atrial_fibrillation=True))['value'],
                           cvd.ukpds_risk_engine('stroke', **dict(self.BASE, total_chol_hdl_ratio=5.11))['value'])

    def test_missing_inputs_and_population(self):
        for k in ('sex', 'age_at_diagnosis', 'diabetes_duration_years', 'current_smoker', 'sbp_mmhg',
                  'total_chol_hdl_ratio', 'horizon_years', 'prior_chd_or_stroke', 'hba1c_percent', 'afro_caribbean'):
            kw = dict(self.BASE); kw[k] = None
            self.assertIsNone(cvd.ukpds_risk_engine('chd', **kw)['value'], k)
        r = cvd.ukpds_risk_engine('chd', **dict(self.BASE, prior_chd_or_stroke=True))
        self.assertIsNone(r['value']); self.assertFalse(r['population_ok'])
        self.assertIsNone(cvd.ukpds_risk_engine('mi', **self.BASE)['value'])
        self.assertIsNone(cvd.ukpds_risk_engine('stroke', **dict(self.BASE, atrial_fibrillation=None))['value'])
