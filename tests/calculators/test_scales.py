import pathlib, sys, unittest
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'calculators'))
from dmic_calculators import scales as s


class Phq(unittest.TestCase):
    def test_official_worked_example_16(self):
        # phqscreeners instructions: 3 items scored 1, 2 items scored 2, 3 items scored 3 -> 16 (9th item scored 0)
        r = s.phq9([1, 1, 1, 2, 2, 3, 3, 3, 0])
        self.assertEqual(r['value'], 16)
        self.assertEqual(r['details']['severity'], 'moderately_severe')

    def test_cutpoints_and_range(self):
        for total, sev in ((0, 'minimal'), (4, 'minimal'), (5, 'mild'), (9, 'mild'), (10, 'moderate'),
                           (14, 'moderate'), (15, 'moderately_severe'), (19, 'moderately_severe'),
                           (20, 'severe'), (27, 'severe')):
            items, left = [], total
            for _ in range(9):
                x = min(3, left); items.append(x); left -= x
            r = s.phq9(items)
            self.assertEqual((r['value'], r['details']['severity']), (total, sev))
        self.assertEqual(s.phq9([3] * 9)['value'], 27)

    def test_item9_flag_independent_of_total(self):
        r = s.phq9([0, 0, 0, 0, 0, 0, 0, 0, 1])
        self.assertEqual(r['value'], 1)
        self.assertEqual(r['details']['severity'], 'minimal')
        self.assertTrue(r['details']['safety']['item9_positive'])
        self.assertFalse(s.phq9([1] * 8 + [0])['details']['safety']['item9_positive'])

    def test_item9_flag_survives_missing_other_items(self):
        r = s.phq9([None] * 8 + [2])
        self.assertIsNone(r['value'])
        self.assertTrue(r['details']['safety']['item9_positive'])

    def test_missing_not_zero(self):
        for items in (None, [1] * 8, [1] * 8 + [None], [1] * 8 + [4], [1] * 8 + [-1], [1] * 8 + [1.5], [1] * 8 + ['1'],
                      [1] * 8 + [True], [1] * 10):
            r = s.phq9(items)
            self.assertIsNone(r['value'], items)
            self.assertTrue(r['reasons_unavailable'])

    def test_phq2_gad7(self):
        self.assertEqual(s.phq2([1, 2])['details']['positive_screen_ge3'], True)
        self.assertEqual(s.phq2([1, 1])['details']['positive_screen_ge3'], False)
        self.assertIsNone(s.phq2([1])['value'])
        r = s.gad7([1, 1, 1, 1, 2, 2, 2])
        self.assertEqual((r['value'], r['details']['severity']), (10, 'moderate'))
        self.assertTrue(r['details']['further_evaluation_ge10'])
        self.assertEqual(s.gad7([3] * 7)['value'], 21)
        self.assertEqual(s.gad7([0] * 7)['details']['severity'], 'minimal')
        self.assertIsNone(s.gad7([1] * 6 + [None])['value'])


class Who5(unittest.TestCase):
    def test_direction_and_threshold(self):
        r = s.who5([3, 3, 3, 3, 3])
        self.assertEqual(r['value'], 60)
        self.assertEqual(r['details']['raw_score'], 15)
        self.assertFalse(r['details']['below_threshold'])
        r = s.who5([3, 3, 2, 2, 2])   # raw 12 -> 48 -> below threshold
        self.assertEqual((r['value'], r['details']['raw_score']), (48, 12))
        self.assertTrue(r['details']['below_threshold'])
        r = s.who5([3, 3, 3, 2, 2])   # raw 13 -> 52 -> not below
        self.assertEqual((r['value'], r['details']['below_threshold']), (52, False))
        self.assertEqual(s.who5([5] * 5)['value'], 100)
        self.assertEqual(s.who5([0] * 5)['value'], 0)

    def test_missing_and_range(self):
        self.assertIsNone(s.who5([3, 3, 3, 3, None])['value'])
        self.assertIsNone(s.who5([6, 3, 3, 3, 3])['value'])
        self.assertIsNone(s.who5([1, 2, 3, 4])['value'])
        for raw_pct in [s.who5([a, b, 1, 1, 1])['value'] for a in range(6) for b in range(6)]:
            self.assertEqual(raw_pct % 4, 0)


class Paid(unittest.TestCase):
    def test_scoring(self):
        r = s.paid20([2] * 16 + [0] * 4)   # sum 32 -> 40
        self.assertEqual(r['value'], 40.0)
        self.assertTrue(r['details']['severe_distress_ge40'])
        r = s.paid20([2] * 15 + [0] * 5)   # sum 30 -> 37.5
        self.assertEqual(r['value'], 37.5)
        self.assertFalse(r['details']['severe_distress_ge40'])
        self.assertEqual(s.paid20([4] * 20)['value'], 100.0)
        self.assertEqual(s.paid20([3, 4] + [0] * 18)['details']['items_scored_3_or_4'], 2)

    def test_not_for_paid5_and_missing(self):
        self.assertIsNone(s.paid20([2] * 5)['value'])
        self.assertIsNone(s.paid20([2] * 19 + [None])['value'])
        self.assertIsNone(s.paid20([5] + [0] * 19)['value'])


class Dds(unittest.TestCase):
    def test_dds17_categories_use_unrounded_mean(self):
        self.assertEqual(s.dds17([1] * 17)['details']['category'], 'little_or_none')
        r = s.dds17([2] * 17)
        self.assertEqual((r['value'], r['details']['category']), (2.0, 'moderate'))
        items = [3] * 16 + [3]
        self.assertEqual(s.dds17(items)['details']['category'], 'high')
        items = [3] * 15 + [2, 2]    # mean 49/17 = 2.882 -> moderate
        self.assertEqual(s.dds17(items)['details']['category'], 'moderate')
        items = [3] * 16 + [2]       # 50/17 = 2.941 -> still moderate (not rounded to 3)
        r = s.dds17(items)
        self.assertAlmostEqual(r['value'], 50 / 17.0)
        self.assertEqual(r['details']['category'], 'moderate')
        self.assertEqual(s.dds17([6] * 17)['value'], 6.0)

    def test_dds17_range_starts_at_1(self):
        self.assertIsNone(s.dds17([0] + [2] * 16)['value'])
        self.assertIsNone(s.dds17([7] + [2] * 16)['value'])
        self.assertIsNone(s.dds17([2] * 16)['value'])

    def test_dds2(self):
        self.assertTrue(s.dds2([3, 3])['details']['screen_positive_ge3'])
        self.assertFalse(s.dds2([2, 3])['details']['screen_positive_ge3'])
        self.assertEqual(s.dds2([2, 3])['value'], 2.5)
        self.assertIsNone(s.dds2([3, None])['value'])


if __name__ == '__main__':
    unittest.main()


class MoreScales(unittest.TestCase):
    def test_paid5(self):
        r = s.paid5([2, 2, 2, 1, 1])
        self.assertEqual((r['value'], r['details']['possible_distress_ge8']), (8, True))
        self.assertFalse(s.paid5([2, 2, 1, 1, 1])['details']['possible_distress_ge8'])
        self.assertEqual(s.paid5([4] * 5)['value'], 20)
        self.assertIsNone(s.paid5([4] * 4 + [None])['value'])

    def test_hfs2_sums_and_ranges(self):
        r = s.hfs2([4] * 15, [4] * 18)
        self.assertEqual((r['value'], r['details']['behavior_subscale'], r['details']['worry_subscale']), (132, 60, 72))
        self.assertEqual(s.hfs2([0] * 15, [0] * 18)['value'], 0)
        self.assertIsNone(s.hfs2([1] * 14, [1] * 18)['value'])
        self.assertIsNone(s.hfs2([1] * 15, None)['value'])
        self.assertIsNone(s.hfs2([5] + [1] * 14, [1] * 18)['value'])

    def test_minicog(self):
        self.assertEqual(s.minicog(3, True)['value'], 5)
        self.assertEqual(s.minicog(0, False)['value'], 0)
        r = s.minicog(1, True)   # 3
        self.assertEqual((r['value'], r['details']['positive_screen_lt3'], r['details']['higher_sensitivity_lt4']), (3, False, True))
        self.assertTrue(s.minicog(0, True)['details']['positive_screen_lt3'])   # 2
        self.assertIsNone(s.minicog(None, True)['value'])
        self.assertIsNone(s.minicog(2, None)['value'])
        self.assertIsNone(s.minicog(4, True)['value'])
        self.assertIsNone(s.minicog(2, 1)['value'])

    def test_moca_education_adjustment(self):
        self.assertEqual(s.moca_total(24, 12)['value'], 25)
        self.assertEqual(s.moca_total(24, 13)['value'], 24)
        self.assertEqual(s.moca_total(30, 8)['value'], 30)          # no point added at 30
        r = s.moca_total(25, 12)
        self.assertEqual((r['value'], r['details']['abnormal_lt26']), (26, False))
        self.assertTrue(s.moca_total(24, 16)['details']['abnormal_lt26'])
        self.assertIsNone(s.moca_total(None, 12)['value'])
        self.assertIsNone(s.moca_total(24, None)['value'])           # education unknown -> not assumed
        self.assertIsNone(s.moca_total(31, 12)['value'])
        self.assertIsNone(s.moca_total(24.5, 12)['value'])

    def test_cfs(self):
        r = s.clinical_frailty_scale(5, 80)
        self.assertEqual((r['value'], r['details']['label']), (5, 'Living with Mild Frailty'))
        self.assertTrue(r['population_ok'])
        self.assertFalse(s.clinical_frailty_scale(5, 50)['population_ok'])
        self.assertIsNone(s.clinical_frailty_scale(5)['population_ok'])
        for bad in (0, 10, 4.5, None, '5'):
            self.assertIsNone(s.clinical_frailty_scale(bad, 80)['value'], bad)

    def test_frail(self):
        T, F = True, False
        self.assertEqual(s.frail_scale(F, F, F, F, F)['details']['category'], 'robust')
        self.assertEqual(s.frail_scale(T, F, F, F, F)['details']['category'], 'pre_frail')
        self.assertEqual(s.frail_scale(T, T, F, F, F)['details']['category'], 'pre_frail')
        self.assertEqual(s.frail_scale(T, T, T, F, F)['details']['category'], 'frail')
        self.assertEqual(s.frail_scale(T, T, T, T, T)['value'], 5)
        self.assertIsNone(s.frail_scale(T, T, T, T, None)['value'])    # unknown not treated as 'no'
        self.assertIsNone(s.frail_scale(T, T, T, T, 1)['value'])
