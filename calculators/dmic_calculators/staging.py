"""KDIGO 2024 CKD G/A categories and prognosis heat map (stratification, not a risk probability).

Source: KDIGO 2024 CKD guideline (Kidney Int 2024;105 Suppl 4S) 'CKD nomenclature' page S126
(literature/fulltext/calculators/official/KDIGO-2024-CKD-Guideline.txt L447-L487, L518-L522);
heat-map colours read from the page image kdigo_p11-011.png (colours are not in the text layer).
"""
from __future__ import annotations

from typing import Any, Dict, Optional

from .result import need_number, result

KDIGO_SRC = "KDIGO 2024 CKD Guideline, CKD nomenclature (Kidney Int 2024;105(4S)) p.S126"

# rows G1..G5 ; columns A1..A3
HEATMAP = {
    "G1": ("green", "green_low", "yellow"), "G2": ("green", "yellow", "orange"),
    "G3a": ("yellow", "orange", "red"), "G3b": ("orange", "red", "red"),
    "G4": ("red", "red", "red"), "G5": ("red", "red", "red"),
}
# G1 row: A1 green, A2 yellow, A3 orange (image); normalise names below
HEATMAP["G1"] = ("green", "yellow", "orange")
RISK_LABEL = {"green": "low risk (no CKD if no other kidney-damage markers)",
              "yellow": "moderately increased risk", "orange": "high risk", "red": "very high risk"}


def g_category(egfr: float) -> str:
    if egfr >= 90:
        return "G1"
    if egfr >= 60:
        return "G2"
    if egfr >= 45:
        return "G3a"
    if egfr >= 30:
        return "G3b"
    if egfr >= 15:
        return "G4"
    return "G5"


def ckd_g_category(egfr: Any = None) -> Dict[str, Any]:
    r: list = []
    g = need_number("egfr", egfr, r, positive=True)
    val = g_category(g) if not r else None
    return result("CKD G category", "KDIGO 2024", val, "G1-G5 (mL/min/1.73 m2)", None if r else True, r,
                  {"egfr": egfr}, KDIGO_SRC, "stratification",
                  caveats=["Category requires >=3 months persistence; a single eGFR does not diagnose CKD"])


def ckd_a_category(uacr_mg_g: Any = None, uacr_mg_mmol: Any = None) -> Dict[str, Any]:
    """A1 <30 mg/g (<3 mg/mmol); A2 30-300 mg/g (3-30 mg/mmol); A3 >300 mg/g (>30 mg/mmol)."""
    r: list = []
    cut_lo, cut_hi = None, None
    if uacr_mg_g is not None and uacr_mg_mmol is not None:
        r.append("ambiguous_units:give_only_one_of_uacr_mg_g_or_uacr_mg_mmol")
        u = None
    elif uacr_mg_g is not None:
        u = need_number("uacr_mg_g", uacr_mg_g, r, minimum=0)
        cut_lo, cut_hi = 30.0, 300.0
    elif uacr_mg_mmol is not None:
        u = need_number("uacr_mg_mmol", uacr_mg_mmol, r, minimum=0)
        cut_lo, cut_hi = 3.0, 30.0
    else:
        r.append("missing:uacr")
        u = None
    val, boundary = None, False
    if not r:
        val = "A1" if u < cut_lo else ("A2" if u <= cut_hi else "A3")
        boundary = (u == cut_hi)
    warnings = []
    if boundary:
        warnings.append("value_equals_A2/A3_boundary: KDIGO 2024 tables print 30-300 (A2) in the nomenclature but "
                        "30-299/>=300 elsewhere; reported as A2, confirm local convention")
    return result("CKD A category", "KDIGO 2024", val, "A1-A3 (albuminuria, ACR)", None if r else True, r,
                  {"uacr_mg_g": uacr_mg_g, "uacr_mg_mmol": uacr_mg_mmol}, KDIGO_SRC, "stratification",
                  warnings=warnings,
                  caveats=["Needs persistence (>=3 months) and exclusion of transient causes; urine dipstick is not ACR"])


def ckd_cga_risk(egfr: Any = None, uacr_mg_g: Any = None, uacr_mg_mmol: Any = None) -> Dict[str, Any]:
    """KDIGO prognosis heat-map colour for the (G, A) cell. Not a probability of any event."""
    gr = ckd_g_category(egfr)
    ar = ckd_a_category(uacr_mg_g, uacr_mg_mmol)
    r = gr["reasons_unavailable"] + ar["reasons_unavailable"]
    val = colour = None
    if not r:
        colour = HEATMAP[gr["value"]][int(ar["value"][1]) - 1]
        val = "%s/%s" % (gr["value"], ar["value"])
    return result("KDIGO CGA risk category", "KDIGO 2024 heat map", val,
                  "G/A cell; colour in details", None if r else True, r,
                  {"egfr": egfr, "uacr_mg_g": uacr_mg_g, "uacr_mg_mmol": uacr_mg_mmol}, KDIGO_SRC, "stratification",
                  g=gr["value"], a=ar["value"], risk_colour=colour,
                  risk_label=RISK_LABEL.get(colour) if colour else None,
                  warnings=ar["details"].get("warnings", []),
                  caveats=["Colour is a prognosis tier, not a percentage; cause (C) of CKD is not assessed here"])
