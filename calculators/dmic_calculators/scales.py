"""Scoring of patient-reported scales (symptom/distress/well-being) — NOT risk of organ events.

Rules shared by every scale here:
- All items must be present and within the printed response range; any missing/out-of-range item -> value None
  (no imputation of zero, no inference from the chart). Individual-item answers must be supplied by a person.
- Scoring only: this module does not contain questionnaire wording; use an officially licensed/translated form.
- Cut-offs mark 'further assessment' tiers, not diagnoses. Any non-zero PHQ-9 item 9 raises a separate safety flag
  that is never overridden by the total score.

Sources (local copies git-ignored): PHQ/GAD instructions (phqscreeners.com PDF) literature/fulltext/calculators/
official/phq_instructions.txt L76-L83, L112-L131, L214-L240; PAID: NDSS page ndss_paid.txt L74-L79; WHO-5: WHO document
who5_english_original.txt 'The Scoring'; DDS: Fisher 2012 (PMC3263871 L98) and Fisher 2008 DDS2 (annfammed_dds2.txt L131-132).
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence

from .result import is_number, need_number, result


def _items(name: str, items: Any, n: int, lo: int, hi: int, reasons: List[str]) -> Optional[List[int]]:
    if items is None:
        reasons.append("missing:%s" % name)
        return None
    if not isinstance(items, (list, tuple)) or len(items) != n:
        reasons.append("invalid_length:%s(need exactly %d items)" % (name, n))
        return None
    out: List[int] = []
    for i, v in enumerate(items, 1):
        if v is None:
            reasons.append("missing_item:%s[%d]" % (name, i))
        elif (not is_number(v)) or int(v) != v or not (lo <= v <= hi):
            reasons.append("invalid_item:%s[%d]=%r(need integer %d-%d)" % (name, i, v, lo, hi))
        else:
            out.append(int(v))
    return out if len(out) == n else None


def phq9(items: Sequence[Optional[int]] = None) -> Dict[str, Any]:
    """PHQ-9 (Kroenke 2001): 9 items 0-3, total 0-27; 5/10/15/20 = mild/moderate/moderately severe/severe."""
    r: List[str] = []
    it = _items("phq9_items", items, 9, 0, 3, r)
    val = cat = flag = None
    if it is not None:
        val = sum(it)
        cat = ("minimal" if val < 5 else "mild" if val < 10 else "moderate" if val < 15
               else "moderately_severe" if val < 20 else "severe")
        flag = it[8] > 0
    # item 9 is informative even when the rest is incomplete
    item9 = None
    if isinstance(items, (list, tuple)) and len(items) == 9 and isinstance(items[8], int) and not isinstance(items[8], bool):
        item9 = items[8]
    safety = {"item9_positive": (item9 > 0) if item9 is not None else None,
              "action": "any item-9 response >0 requires same-day clinician assessment (not total-score dependent)"}
    return result("PHQ-9", "Kroenke 2001; instructions phqscreeners.com", val, "points (0-27)",
                  None if r else True, r, {"items": list(items) if items is not None else None},
                  "PHQ/GAD instructions (phq_instructions.txt L214-L218); Kroenke 2001 PMID 11556941",
                  "symptom_score", severity=cat, further_assessment_ge10=(val >= 10) if val is not None else None,
                  safety=safety,
                  caveats=["Screening/severity tool; does not establish a diagnosis of major depression",
                           "Not a predictor of organ events; Traditional-Chinese validated form must be used clinically"])


def phq2(items: Sequence[Optional[int]] = None) -> Dict[str, Any]:
    """PHQ-2: first two PHQ-9 items, 0-6; >=3 prompts full PHQ-9 and interview."""
    r: List[str] = []
    it = _items("phq2_items", items, 2, 0, 3, r)
    val = sum(it) if it is not None else None
    return result("PHQ-2", "Kroenke 2003; instructions phqscreeners.com", val, "points (0-6)",
                  None if r else True, r, {"items": list(items) if items is not None else None},
                  "PHQ/GAD instructions (phq_instructions.txt L83-L85, L127)", "symptom_score",
                  positive_screen_ge3=(val >= 3) if val is not None else None,
                  caveats=["Positive screen prompts PHQ-9 and clinical interview; not a diagnosis"])


def gad7(items: Sequence[Optional[int]] = None) -> Dict[str, Any]:
    """GAD-7 (Spitzer 2006): 7 items 0-3, total 0-21; 5/10/15 = mild/moderate/severe; >=10 further evaluation."""
    r: List[str] = []
    it = _items("gad7_items", items, 7, 0, 3, r)
    val = sum(it) if it is not None else None
    cat = None if val is None else ("minimal" if val < 5 else "mild" if val < 10 else "moderate" if val < 15 else "severe")
    return result("GAD-7", "Spitzer 2006; instructions phqscreeners.com", val, "points (0-21)",
                  None if r else True, r, {"items": list(items) if items is not None else None},
                  "PHQ/GAD instructions (phq_instructions.txt L235-L240); Spitzer 2006 PMID 16717171",
                  "symptom_score", severity=cat, further_evaluation_ge10=(val >= 10) if val is not None else None,
                  caveats=["Symptom screening; not a risk model for CVD or other outcomes"])


def who5(items: Sequence[Optional[int]] = None) -> Dict[str, Any]:
    """WHO-5: 5 items 0-5, raw 0-25 (higher = better), percentage = raw x 4; raw <13 (<50%) = poor well-being."""
    r: List[str] = []
    it = _items("who5_items", items, 5, 0, 5, r)
    raw = sum(it) if it is not None else None
    pct = raw * 4 if raw is not None else None
    return result("WHO-5", "WHO 2024 (WHO-UCN-MSD-MHE-2024.01)", pct, "percentage 0-100 (raw x4); HIGHER = BETTER",
                  None if r else True, r, {"items": list(items) if items is not None else None},
                  "WHO-5 document 'The Scoring' (who5_english_original.txt); Topp 2015 PMID 25831962",
                  "symptom_score", raw_score=raw, below_threshold=(raw < 13) if raw is not None else None,
                  caveats=["Direction is opposite to PHQ/GAD/PAID: low score = poor well-being",
                           "<50% / raw<13 suggests further assessment (e.g. depression screening), not a diagnosis",
                           "Licence CC BY-NC-SA 3.0 IGO for the WHO 2024 document: check commercial use"])


def paid20(items: Sequence[Optional[int]] = None) -> Dict[str, Any]:
    """PAID-20 current 0-4 form: sum 0-80 x 1.25 -> 0-100; >=40 = severe diabetes distress (NDSS).

    The 1995 original used a different response format; PAID-5 must not use this function.
    """
    r: List[str] = []
    it = _items("paid20_items", items, 20, 0, 4, r)
    val = sum(it) * 1.25 if it is not None else None
    hi = sum(1 for x in it if x >= 3) if it is not None else None
    return result("PAID-20", "current 0-4 form (NDSS description); original Polonsky 1995 PMID 7555499", val,
                  "points 0-100 (sum x1.25); HIGHER = WORSE", None if r else True, r,
                  {"items": list(items) if items is not None else None},
                  "NDSS PAID page (ndss_paid.txt L74-L79)", "symptom_score",
                  severe_distress_ge40=(val >= 40) if val is not None else None, items_scored_3_or_4=hi,
                  caveats=["Item-level problem areas (3-4) should be reviewed, not only the total",
                           "PAID-5 uses a different scale; do not use this formula for it"])


def dds2(items: Sequence[Optional[int]] = None) -> Dict[str, Any]:
    """DDS2 (Fisher 2008): 2 items 1-6; mean >=3 = moderate-or-higher distress (screen positive)."""
    r: List[str] = []
    it = _items("dds2_items", items, 2, 1, 6, r)
    mean = sum(it) / 2.0 if it is not None else None
    return result("DDS-2", "Fisher 2008 Ann Fam Med", mean, "mean item score 1-6; HIGHER = WORSE",
                  None if r else True, r, {"items": list(items) if items is not None else None},
                  "annfammed_dds2.txt L131 ('average item score >=3')", "symptom_score",
                  screen_positive_ge3=(mean >= 3.0) if mean is not None else None,
                  caveats=["Screen only; do not interchange with DDS-17 or T2-DDAS"])


def dds17(items: Sequence[Optional[int]] = None) -> Dict[str, Any]:
    """DDS17: 17 items 1-6, MEAN item score; <2 little/none, 2<=x<3 moderate, >=3 high (Fisher 2012).

    Subscale scoring is not implemented (item-to-subscale mapping not locally verified here).
    """
    r: List[str] = []
    it = _items("dds17_items", items, 17, 1, 6, r)
    mean = sum(it) / 17.0 if it is not None else None
    cat = None if mean is None else ("little_or_none" if mean < 2.0 else "moderate" if mean < 3.0 else "high")
    return result("DDS-17", "Polonsky 2005; cut points Fisher 2012", mean, "mean item score 1-6; HIGHER = WORSE",
                  None if r else True, r, {"items": list(items) if items is not None else None},
                  "Fisher 2012 PMC3263871 L98 (<2.0 / 2.0-2.9 / >=3.0); Polonsky 2005 PMID 15735199", "symptom_score",
                  category=cat,
                  caveats=["Category computed from the unrounded mean (2.94 is 'moderate', not rounded to 3)",
                           "Legacy 17-item DDS is not interchangeable with DDS-2 or the newer 28-29 item T2-DDAS"])


# ---------------------------------------------------------------- further scales (scoring only)
def paid5(items: Sequence[Optional[int]] = None) -> Dict[str, Any]:
    """PAID-5 (McGuire 2010): five PAID items (3, 6, 12, 16, 19 of PAID-20), each 0-4, total 0-20; >=8 -> assess further."""
    r: List[str] = []
    it = _items("paid5_items", items, 5, 0, 4, r)
    val = sum(it) if it is not None else None
    return result("PAID-5", "McGuire 2010 Diabetologia", val, "points (0-20); HIGHER = WORSE", None if r else True, r,
                  {"items": list(items) if items is not None else None},
                  "vumc_paid1_5.txt L77-L78 (>=8); PMC11983946 L47 (0-4 items); McGuire 2010 abstract (items 3,6,12,16,19)",
                  "symptom_score", possible_distress_ge8=(val >= 8) if val is not None else None,
                  caveats=["Do not apply the PAID-20 x1.25 formula", "Cut-off from a secondary (VUmc) sheet; licence not located"])


def hfs2(behavior_items: Sequence[Optional[int]] = None, worry_items: Sequence[Optional[int]] = None
         ) -> Dict[str, Any]:
    """HFS-II: 15 Behavior (0-4 each, 0-60) + 18 Worry (0-4 each, 0-72); total 0-132; higher = more fear.

    Source: Singapore validation PMC5530240 L62 (sums and ranges). No clinical cut-off exists in the sources.
    """
    r: List[str] = []
    b = _items("hfs2_behavior_items", behavior_items, 15, 0, 4, r)
    w = _items("hfs2_worry_items", worry_items, 18, 0, 4, r)
    bs = sum(b) if b is not None else None
    ws = sum(w) if w is not None else None
    tot = bs + ws if (bs is not None and ws is not None) else None
    return result("HFS-II", "Gonder-Frederick 2011; sums per Singapore validation 2017", tot,
                  "points (0-132); HIGHER = MORE FEAR", None if r else True, r,
                  {"behavior_items": list(behavior_items) if behavior_items is not None else None,
                   "worry_items": list(worry_items) if worry_items is not None else None},
                  "PMC5530240 L62; PMC3064031 (development)", "symptom_score",
                  behavior_subscale=bs, worry_subscale=ws,
                  caveats=["No validated clinical cut-off in local sources (do not invent one)",
                           "Subscales should be analysed separately; two-factor structure not confirmed in Singapore sample"])


def minicog(word_recall_0_3: Any = None, clock_draw_normal: Any = None) -> Dict[str, Any]:
    """Mini-Cog total 0-5 = recall (0-3) + clock (2 if normal else 0); <3 positive; <4 higher-sensitivity option."""
    r: List[str] = []
    rec = _items("recall", [word_recall_0_3], 1, 0, 3, r)
    if clock_draw_normal is None:
        r.append("missing:clock_draw_normal")
    elif not isinstance(clock_draw_normal, bool):
        r.append("invalid_type:clock_draw_normal(need True/False)")
    val = None
    if not r:
        val = rec[0] + (2 if clock_draw_normal else 0)
    return result("Mini-Cog", "Borson sheet v.01.19.16 (reprint)", val, "points (0-5); HIGHER = BETTER", None if r else True, r,
                  {"word_recall_0_3": word_recall_0_3, "clock_draw_normal": clock_draw_normal},
                  "minicog_sfhp_standardized.txt L41-L56", "screening_index",
                  positive_screen_lt3=(val < 3) if val is not None else None,
                  higher_sensitivity_lt4=(val < 4) if val is not None else None,
                  caveats=["Cognitive screen, not a dementia diagnosis",
                           "Licence: clinical/educational reprint; research/commercial use needs the author's permission"])


def moca_total(total_0_30: Any = None, education_years: Any = None) -> Dict[str, Any]:
    """MoCA: accepts the 0-30 total scored by an authorised rater; +1 if education <=12 y and total <30; <26 abnormal.

    No test content is embedded. Certification/licence conditions: mocacognition.com (see report).
    """
    r: List[str] = []
    t = need_number("moca_total", total_0_30, r, minimum=0, maximum=30)
    if t is not None and int(t) != t:
        r.append("invalid_value:moca_total must be an integer")
    ed = need_number("education_years", education_years, r, minimum=0)
    val = None
    if not r:
        val = int(t) + (1 if (ed <= 12 and t < 30) else 0)
    return result("MoCA (total entry)", "MoCA 8.x total; cut-off per 2005 study / site FAQ", val, "points (0-30); HIGHER = BETTER",
                  None if r else True, r, {"moca_total": total_0_30, "education_years": education_years},
                  "moca_faq.txt L150-L162; Nasreddine 2005 PMID 15817019 (abstract)", "screening_index",
                  raw_total=int(t) if t is not None and int(t) == t else None,
                  abnormal_lt26=(val < 26) if val is not None else None,
                  caveats=["Validated for ages 55-85 on the site; cut-off depends on language/education/version",
                           "Total from a trained/permitted rater only; not a diagnosis of MCI/dementia"])


CFS_LABELS = {1: "Very Fit", 2: "Fit", 3: "Managing Well", 4: "Living with Very Mild Frailty",
              5: "Living with Mild Frailty", 6: "Living with Moderate Frailty", 7: "Living with Severe Frailty",
              8: "Living with Very Severe Frailty", 9: "Terminally Ill"}


def clinical_frailty_scale(level: Any = None, age_years: Any = None) -> Dict[str, Any]:
    """CFS v2.0 (Rockwood): clinician-assigned 1-9; this function only validates/labels the rating (no formula)."""
    r: List[str] = []
    lv = need_number("cfs_level", level, r, minimum=1, maximum=9)
    if lv is not None and int(lv) != lv:
        r.append("invalid_value:cfs_level must be an integer 1-9")
    age = None
    warn = []
    if age_years is not None:
        age = need_number("age_years", age_years, r, positive=True)
        if age is not None and age < 65:
            warn.append("age<65: CFS not validated in people under 65")
    else:
        warn.append("age_unknown: CFS validated in people aged >=65")
    val = int(lv) if not r else None
    return result("Clinical Frailty Scale", "v2.0 (Rockwood & Theou 2020)", val, "level 1-9; HIGHER = MORE FRAIL",
                  None if r else (None if age is None else age >= 65), r, {"level": level, "age_years": age_years},
                  "cfs_cgj2020.txt L209-L318; cfs_guidance_for_use.txt L6", "screening_index",
                  label=CFS_LABELS.get(val), warnings=warn,
                  caveats=["Clinical judgement of baseline status ~2 weeks before illness, not a questionnaire",
                           "No developer-defined numeric cut-off; licence: free non-commercial, translations need permission"])


def frail_scale(fatigue: Any = None, resistance: Any = None, ambulation: Any = None, illnesses: Any = None,
                weight_loss: Any = None) -> Dict[str, Any]:
    """FRAIL (Morley 2012/2013): 5 yes/no components, 0-5; 3-5 frail, 1-2 pre-frail, 0 robust."""
    r: List[str] = []
    vals = {}
    for k, v in (("fatigue", fatigue), ("resistance", resistance), ("ambulation", ambulation),
                 ("illnesses", illnesses), ("weight_loss", weight_loss)):
        if v is None:
            r.append("missing:%s" % k)
        elif not isinstance(v, bool):
            r.append("invalid_type:%s(need True/False)" % k)
        else:
            vals[k] = v
    val = sum(vals.values()) if not r else None
    cat = None if val is None else ("robust" if val == 0 else "pre_frail" if val <= 2 else "frail")
    return result("FRAIL scale", "Morley 2012 JNHA / 2013 JAMDA consensus", val, "points (0-5); HIGHER = WORSE",
                  None if r else True, r, {k: v for k, v in (("fatigue", fatigue), ("resistance", resistance),
                  ("ambulation", ambulation), ("illnesses", illnesses), ("weight_loss", weight_loss))},
                  "pmc4084863_morley2013.txt L225-L232; PMC4515112 L37", "screening_index", category=cat,
                  caveats=["Item wording differs between publications (6 vs 12 months weight loss, illness counts); fix one version",
                           "Validation cohorts: African Americans 49-65 y (2012); consensus screens >=70 y or >=5% weight loss"])
