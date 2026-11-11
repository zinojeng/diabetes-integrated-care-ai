import pathlib, sys, unittest
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'calculators'))
from dmic_calculators import comorbidity as cm

NONE = dict(myocardial_infarction=False, congestive_heart_failure=False, peripheral_vascular_disease=False,
            cerebrovascular_disease=False, dementia=False, chronic_pulmonary_disease=False,
            rheumatologic_disease=False, peptic_ulcer_disease=False, hemiplegia_paraplegia=False,
            renal_disease=False, aids_hiv=False, diabetes='none', liver='none', cancer='none')


def c(**o):
    d = dict(NONE); d.update(o); return d


class Charlson(unittest.TestCase):
    def test_zero(self):
        for v in ('original_1987', 'quan_2011'):
            self.assertEqual(cm.charlson(v, NONE)['value'], 0)

    def test_original_weights(self):
        cases = {'myocardial_infarction': 1, 'congestive_heart_failure': 1, 'dementia': 1, 'peptic_ulcer_disease': 1,
                 'hemiplegia_paraplegia': 2, 'renal_disease': 2, 'aids_hiv': 6}
        for k, w in cases.items():
            self.assertEqual(cm.charlson('original_1987', c(**{k: True}))['value'], w, k)
        self.assertEqual(cm.charlson('original_1987', c(diabetes='uncomplicated'))['value'], 1)
        self.assertEqual(cm.charlson('original_1987', c(diabetes='complicated'))['value'], 2)
        self.assertEqual(cm.charlson('original_1987', c(liver='mild'))['value'], 1)
        self.assertEqual(cm.charlson('original_1987', c(liver='moderate_severe'))['value'], 3)
        self.assertEqual(cm.charlson('original_1987', c(cancer='malignancy'))['value'], 2)
        self.assertEqual(cm.charlson('original_1987', c(cancer='metastatic'))['value'], 6)

    def test_quan_weights(self):
        cases = {'myocardial_infarction': 0, 'congestive_heart_failure': 2, 'peripheral_vascular_disease': 0,
                 'cerebrovascular_disease': 0, 'dementia': 2, 'chronic_pulmonary_disease': 1,
                 'rheumatologic_disease': 1, 'peptic_ulcer_disease': 0, 'hemiplegia_paraplegia': 2,
                 'renal_disease': 1, 'aids_hiv': 4}
        for k, w in cases.items():
            self.assertEqual(cm.charlson('quan_2011', c(**{k: True}))['value'], w, k)
        self.assertEqual(cm.charlson('quan_2011', c(diabetes='uncomplicated'))['value'], 0)
        self.assertEqual(cm.charlson('quan_2011', c(diabetes='complicated'))['value'], 1)
        self.assertEqual(cm.charlson('quan_2011', c(liver='mild'))['value'], 2)
        self.assertEqual(cm.charlson('quan_2011', c(liver='moderate_severe'))['value'], 4)

    def test_diabetes_not_double_counted(self):
        # one hierarchical level per group: both uncomplicated+complicated cannot be expressed
        r = cm.charlson('original_1987', c(diabetes=['uncomplicated', 'complicated']))
        self.assertIsNone(r['value'])
        self.assertEqual(cm.charlson('original_1987', c(diabetes='complicated', liver='mild', cancer='metastatic'))['value'], 2 + 1 + 6)

    def test_combined_example(self):
        r = cm.charlson('quan_2011', c(congestive_heart_failure=True, renal_disease=True, diabetes='complicated'))
        self.assertEqual(r['value'], 2 + 1 + 1)
        self.assertEqual(r['details']['data_completeness']['specified'], 14)

    def test_unknown_is_not_absent(self):
        d = dict(NONE); del d['dementia']; d['renal_disease'] = None
        r = cm.charlson('quan_2011', d)
        self.assertIsNone(r['value'])
        self.assertEqual(r['reasons_unavailable'], ['unspecified_categories(unknown, not absent):dementia,renal_disease'])
        self.assertEqual(r['details']['lower_bound'], 0)
        self.assertEqual(r['details']['data_completeness']['specified'], 12)
        d2 = c(congestive_heart_failure=True); d2['dementia'] = None
        self.assertEqual(cm.charlson('quan_2011', d2)['details']['lower_bound'], 2)

    def test_version_mandatory_and_invalid_inputs(self):
        self.assertIsNone(cm.charlson(None, NONE)['value'])
        self.assertIsNone(cm.charlson('charlson_age', NONE)['value'])
        self.assertIsNone(cm.charlson('quan_2011', c(dementia='yes'))['value'])
        self.assertIsNone(cm.charlson('quan_2011', c(diabetes='severe'))['value'])
        self.assertIsNone(cm.charlson('quan_2011', dict(NONE, extra=True))['value'])
        self.assertIsNone(cm.charlson('quan_2011', None)['value'])

    def test_spec_only_stubs(self):
        for r in (cm.dcsi(), cm.charlson_age_adjusted()):
            self.assertIsNone(r['value'])
            self.assertTrue(r['reasons_unavailable'][0].startswith('spec_only'))


if __name__ == '__main__':
    unittest.main()
