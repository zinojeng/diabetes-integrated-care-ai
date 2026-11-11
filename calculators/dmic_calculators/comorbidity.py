"""Charlson Comorbidity Index (disease-burden score, NOT a current mortality percentage) and DCSI (spec_only).

Weights are locally greppable only in OPEN SECONDARY reproductions (primary papers are paywalled):
- Original Charlson 1987 weights: PMC13721275 Table 1 (literature/parsed/calculators/PMC13721275_tables.md L3-L22).
- Quan 2011 updated weights: PMC13665550 Table A2 (L68-L90) and PMC13436062 Table 2 (L48-L64) agree;
  PMC13084228 Table 1 prints renal disease = 4 for Quan 2011 (conflict; the two agreeing sources use 1).
Inputs are clinician/algorithm-assigned flags for the HIGHEST severity within the three hierarchical groups, so
diabetes (uncomplicated vs complicated), liver (mild vs moderate/severe) and cancer (any vs metastatic) are never
double counted. An unspecified category is UNKNOWN, not absent: no total is returned (a lower bound is reported).
ICD code mapping is NOT implemented (Quan 2005 code lists exist in PMC13586706 for a future step).
Age-adjusted CCI is spec_only: the two open sources that describe it disagree on age bands and the primary
(Charlson 1994) is unavailable.
"""
from __future__ import annotations

from typing import Any, Dict, Optional

from .result import result

CCI_SRC = ("Charlson 1987 (PMID 3558716) weights via PMC13721275 Table 1; Quan 2011 (PMID 21330339) weights via "
           "PMC13665550 Table A2 / PMC13436062 Table 2 (secondary reproductions)")

BOOL_CATS = ("myocardial_infarction", "congestive_heart_failure", "peripheral_vascular_disease",
             "cerebrovascular_disease", "dementia", "chronic_pulmonary_disease", "rheumatologic_disease",
             "peptic_ulcer_disease", "hemiplegia_paraplegia", "renal_disease", "aids_hiv")
ORIGINAL = {"myocardial_infarction": 1, "congestive_heart_failure": 1, "peripheral_vascular_disease": 1,
            "cerebrovascular_disease": 1, "dementia": 1, "chronic_pulmonary_disease": 1,
            "rheumatologic_disease": 1, "peptic_ulcer_disease": 1, "hemiplegia_paraplegia": 2,
            "renal_disease": 2, "aids_hiv": 6}
QUAN2011 = {"myocardial_infarction": 0, "congestive_heart_failure": 2, "peripheral_vascular_disease": 0,
            "cerebrovascular_disease": 0, "dementia": 2, "chronic_pulmonary_disease": 1,
            "rheumatologic_disease": 1, "peptic_ulcer_disease": 0, "hemiplegia_paraplegia": 2,
            "renal_disease": 1, "aids_hiv": 4}
# hierarchical groups: level -> weight
GROUPS = {
    "diabetes": {"original": {"none": 0, "uncomplicated": 1, "complicated": 2},
                 "quan2011": {"none": 0, "uncomplicated": 0, "complicated": 1}},
    "liver": {"original": {"none": 0, "mild": 1, "moderate_severe": 3},
              "quan2011": {"none": 0, "mild": 2, "moderate_severe": 4}},
    "cancer": {"original": {"none": 0, "malignancy": 2, "metastatic": 6},
               "quan2011": {"none": 0, "malignancy": 2, "metastatic": 6}},
}
VERSIONS = {"original_1987": ("original", ORIGINAL), "quan_2011": ("quan2011", QUAN2011)}


def charlson(version: str = None, conditions: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """CCI = sum of version-specific weights. ``conditions``: 11 booleans (BOOL_CATS) plus diabetes
    ('none'|'uncomplicated'|'complicated'), liver ('none'|'mild'|'moderate_severe'),
    cancer ('none'|'malignancy'|'metastatic'). Version is mandatory (no default)."""
    r: list = []
    if version not in VERSIONS:
        r.append("unsupported_or_missing_version:%r(use original_1987 or quan_2011)" % (version,))
        return result("Charlson Comorbidity Index", str(version), None, None, None, r, conditions or {}, CCI_SRC,
                      "disease_burden")
    gkey, weights = VERSIONS[version]
    cond = dict(conditions or {})
    total, unknown, contrib = 0, [], {}
    for k in BOOL_CATS:
        v = cond.get(k)
        if v is None:
            unknown.append(k)
        elif not isinstance(v, bool):
            r.append("invalid_type:%s(need True/False)" % k)
        else:
            if v:
                contrib[k] = weights[k]
                total += weights[k]
    for g, lv in GROUPS.items():
        v = cond.get(g)
        if v is None:
            unknown.append(g)
        elif not isinstance(v, str) or v not in lv[gkey]:
            r.append("invalid_value:%s=%r(allowed %s)" % (g, v, "/".join(lv[gkey])))
        else:
            w = lv[gkey][v]
            if w:
                contrib[g + ":" + v] = w
            total += w
    extra = set(cond) - set(BOOL_CATS) - set(GROUPS)
    if extra:
        r.append("unknown_condition:%s" % ",".join(sorted(extra)))
    if unknown:
        r.append("unspecified_categories(unknown, not absent):%s" % ",".join(unknown))
    n_cat = len(BOOL_CATS) + len(GROUPS)
    return result("Charlson Comorbidity Index", version, total if not r else None, "points (unweighted by age)",
                  None if r else True, r, cond, CCI_SRC, "disease_burden",
                  lower_bound=total if (unknown and not any(x.startswith(("invalid", "unknown_condition")) for x in r)) else None,
                  data_completeness={"specified": n_cat - len(unknown), "of": n_cat, "unknown": unknown},
                  contributions=contrib,
                  warnings=(["Quan 2011 renal disease weight conflicts across open sources (1 in two, 4 in one); 1 used"]
                            if version == "quan_2011" else []),
                  caveats=["Comorbidity burden, not a current-day mortality probability; do not read historical survival as local risk",
                           "Age-adjusted CCI is not implemented (spec_only)",
                           "Absence in claims/records is not evidence of absence; supply None for unknown"])


def charlson_age_adjusted(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    return result("Age-adjusted Charlson", "spec_only", None, None, None,
                  ["spec_only:age bands differ between open sources (PMC13701863 vs PMC13094585) and Charlson 1994 is unavailable"],
                  {}, CCI_SRC, "disease_burden")


def dcsi(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    return result("DCSI / aDCSI", "spec_only", None, None, None,
                  ["spec_only:Young 2008 Table 1 rubric and Chang 2012 ICD mapping are not in any locally available full text "
                   "(PMC3810070 abstract only; only 'seven categories, each 0-2 except neuropathy 0-1, total 0-13' is printed in PMC10069524 L49)"],
                  {}, "Young 2008 PMID 18197741; Chang 2012 PMID 23198714 (no local full text)", "disease_burden")
