"""IWGDF 2023 risk stratification (categories 0-3). Source: IWGDF 2023 prevention guideline, Table 1
(literature/fulltext/calculators/official/IWGDF-2023-02-Prevention-Guideline.txt L542-L556).
Unknown (None) inputs are never treated as absent: the category is reported only if it is the same under
every completion of the unknown inputs; otherwise value=None with at_least/at_most bounds.
"""
from __future__ import annotations

import itertools
from typing import Any, Dict

from .result import result

IWGDF_SRC = "IWGDF 2023 Guidelines on the prevention of foot ulcers in persons with diabetes, Table 1"
FREQ = {0: "once a year", 1: "once every 6-12 months", 2: "once every 3-6 months", 3: "once every 1-3 months"}
RISK = {0: "very low", 1: "low", 2: "moderate", 3: "high"}
FIELDS = ("loss_of_protective_sensation", "peripheral_artery_disease", "foot_deformity",
          "history_foot_ulcer", "lower_extremity_amputation", "end_stage_renal_disease")


def _category(lops, pad, deform, ulcer, amput, esrd) -> int:
    if not (lops or pad):
        return 0
    if ulcer or amput or esrd:
        return 3
    if (lops and pad) or (lops and deform) or (pad and deform):
        return 2
    return 1


def iwgdf_risk_category(loss_of_protective_sensation: Any = None, peripheral_artery_disease: Any = None,
                        foot_deformity: Any = None, history_foot_ulcer: Any = None,
                        lower_extremity_amputation: Any = None, end_stage_renal_disease: Any = None
                        ) -> Dict[str, Any]:
    vals = dict(zip(FIELDS, (loss_of_protective_sensation, peripheral_artery_disease, foot_deformity,
                             history_foot_ulcer, lower_extremity_amputation, end_stage_renal_disease)))
    r: list = []
    for k, v in vals.items():
        if v is not None and not isinstance(v, bool):
            r.append("invalid_type:%s(need True/False/None)" % k)
    unknown = [k for k, v in vals.items() if v is None]
    cats, val = set(), None
    if not r:
        for combo in itertools.product((False, True), repeat=len(unknown)):
            d = dict(vals); d.update(zip(unknown, combo))
            cats.add(_category(*(d[k] for k in FIELDS)))
        if len(cats) == 1:
            val = next(iter(cats))
        else:
            r.append("undetermined:unknown_inputs=%s (not assumed absent); possible categories %s"
                     % (",".join(unknown), sorted(cats)))
    return result("IWGDF risk category", "IWGDF 2023", val, "category 0-3 (ulcer risk)",
                  None if (r and not cats) else True, r, vals, IWGDF_SRC, "stratification",
                  label=RISK.get(val), screening_frequency=FREQ.get(val),
                  at_least=min(cats) if cats and len(cats) > 1 else None,
                  at_most=max(cats) if cats and len(cats) > 1 else None,
                  caveats=["Stratification of ulcer risk and follow-up interval (expert opinion), not a percentage of future amputation",
                           "An examination not done is 'unknown', not 'absent'"])
