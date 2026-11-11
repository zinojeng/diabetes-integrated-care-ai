"""CKD-EPI 2021 eGFR (creatinine; creatinine-cystatin C) and KFRE 4-variable.

Sources (local copies are git-ignored; see sessions/calculators/evidence_table.csv):
- CKD-EPI 2021 constants: NIDDK adult equations page (official), saved at
  literature/fulltext/calculators/official/niddk_gfr_adults.txt (lines ~119-215).
  Original paper: Inker NEJM 2021 (PMID 34554658) – main text has no constants.
- KFRE: Tangri JAMA 2016 (PMID 26757465). Coefficients/centering confirmed locally in
  PMC7203563 (5-yr equation with S0=0.924) and PMC11813909 (Table 4, non-USA original base
  hazard 0.0635). The primary JAMA eAppendix 2 p9 is behind a 403 bot wall for this
  session, so 2-year S0 values and North-America values are NOT locally verifiable.
"""
from __future__ import annotations

import math
from typing import Any, Dict, Optional

from .result import need_number, need_sex, result

NIDDK_SRC = "NIDDK adult GFR equations (official page) / Inker NEJM 2021 PMID 34554658"
UMOL_PER_MGDL_CREATININE = 88.4  # NIDDK page: 'serum creatinine umol/L to mg/dL, divide by 88.4'


def _scr_mgdl(scr_mg_dl: Any, scr_umol_l: Any, reasons) -> Optional[float]:
    if scr_mg_dl is not None and scr_umol_l is not None:
        reasons.append("ambiguous_units:give_only_one_of_scr_mg_dl_or_scr_umol_l")
        return None
    if scr_mg_dl is None and scr_umol_l is None:
        reasons.append("missing:serum_creatinine")
        return None
    if scr_mg_dl is not None:
        return need_number("scr_mg_dl", scr_mg_dl, reasons, positive=True)
    v = need_number("scr_umol_l", scr_umol_l, reasons, positive=True)
    return None if v is None else v / UMOL_PER_MGDL_CREATININE


def ckd_epi_2021_creatinine(age_years: Any = None, sex: Any = None, scr_mg_dl: Any = None,
                            scr_umol_l: Any = None) -> Dict[str, Any]:
    """Race-free CKD-EPI 2021 eGFRcr (mL/min/1.73 m2). Adults only (age >= 18)."""
    r: list = []
    age = need_number("age_years", age_years, r, minimum=18)
    s = need_sex(sex, r)
    scr = _scr_mgdl(scr_mg_dl, scr_umol_l, r)
    val = None
    if not r:
        kappa, alpha = (0.7, -0.241) if s == "female" else (0.9, -0.302)
        x = scr / kappa
        val = (142.0 * min(x, 1.0) ** alpha * max(x, 1.0) ** -1.200
               * 0.9938 ** age * (1.012 if s == "female" else 1.0))
    return result(
        "CKD-EPI 2021 creatinine", "2021 race-free (Inker 2021)", val, "mL/min/1.73 m2",
        None if r else True, r,
        {"age_years": age_years, "sex": sex, "scr_mg_dl": scr_mg_dl, "scr_umol_l": scr_umol_l},
        NIDDK_SRC, "organ_function",
        caveats=["Single eGFR is not a CKD diagnosis (needs chronicity/albuminuria/other damage evidence)",
                 "Not valid in AKI, extremes of muscle mass, amputation; consider cystatin C/measured GFR",
                 "Not a probability of kidney failure"],
    )


def ckd_epi_2021_creatinine_cystatin(age_years: Any = None, sex: Any = None, scr_mg_dl: Any = None,
                                     scr_umol_l: Any = None, cystatin_c_mg_l: Any = None) -> Dict[str, Any]:
    """CKD-EPI 2021 eGFRcr-cys (mL/min/1.73 m2). Cystatin C in mg/L; adults only."""
    r: list = []
    age = need_number("age_years", age_years, r, minimum=18)
    s = need_sex(sex, r)
    scr = _scr_mgdl(scr_mg_dl, scr_umol_l, r)
    cys = need_number("cystatin_c_mg_l", cystatin_c_mg_l, r, positive=True)
    val = None
    if not r:
        kappa, alpha = (0.7, -0.219) if s == "female" else (0.9, -0.144)
        x = scr / kappa
        c = cys / 0.8
        val = (135.0 * min(x, 1.0) ** alpha * max(x, 1.0) ** -0.544
               * min(c, 1.0) ** -0.323 * max(c, 1.0) ** -0.778
               * 0.9961 ** age * (0.963 if s == "female" else 1.0))
    return result(
        "CKD-EPI 2021 creatinine-cystatin C", "2021 race-free (Inker 2021)", val, "mL/min/1.73 m2",
        None if r else True, r,
        {"age_years": age_years, "sex": sex, "scr_mg_dl": scr_mg_dl, "scr_umol_l": scr_umol_l,
         "cystatin_c_mg_l": cystatin_c_mg_l},
        NIDDK_SRC, "organ_function",
        caveats=["Cystatin C is affected by obesity, inflammation, thyroid disease, steroids"],
    )


# ---------------------------------------------------------------- KFRE 4-variable
# (age/10 - 7.036), (male - 0.5642), (eGFR/5 - 7.222), (ln UACR mg/g - 5.137); local grep: PMC7203563 Table 4
KFRE_COEF = {"age10": -0.2201, "male": 0.2467, "egfr5": -0.5567, "lnuacr": 0.4510}
KFRE_CENTER = {"age10": 7.036, "male": 0.5642, "egfr5": 7.222, "lnuacr": 5.137}

# S0 by (calibration, horizon_years): (value, status, evidence)
KFRE_S0 = {
    ("original", 5): (0.9240, "verified", "PMC7203563 Table 4 equation '1 - 0.924^exp(...)'"),
    ("non_north_america", 5): (0.9365, "verified",
                               "PMC11813909 Table 4: non-USA original KFRE base hazard 0.0635 (S0=1-0.0635)"),
    ("original", 2): (0.9750, "provisional",
                      "not printed in any locally greppable text; stated in repo note "
                      "research/VERIFICATION_CALCULATORS_20261111.md citing eAppendix 2 p9"),
    ("non_north_america", 2): (0.9832, "provisional",
                               "not printed locally; consistent with PMC4752167 statement that the non-NA "
                               "factor lowers baseline 2-yr risk by 32.9% (0.0250*0.671 -> S0 0.9832)"),
}
KFRE_SPEC_ONLY = {
    ("north_america", 2): "North-America regional S0 not locally greppable (repo note lists 0.9751)",
    ("north_america", 5): "North-America regional S0 not locally greppable (repo note lists 0.8996)",
}
KFRE_SRC = "Tangri JAMA 2016 PMID 26757465 (eAppendix 2 p9: blocked 403 for this session)"


def kfre_linear_predictor(age_years: float, male: int, egfr: float, uacr_mg_g: float) -> float:
    return (KFRE_COEF["age10"] * (age_years / 10.0 - KFRE_CENTER["age10"])
            + KFRE_COEF["male"] * (male - KFRE_CENTER["male"])
            + KFRE_COEF["egfr5"] * (egfr / 5.0 - KFRE_CENTER["egfr5"])
            + KFRE_COEF["lnuacr"] * (math.log(uacr_mg_g) - KFRE_CENTER["lnuacr"]))


def kfre_4var(age_years: Any = None, sex: Any = None, egfr: Any = None, uacr_mg_g: Any = None,
              uacr_mg_mmol: Any = None, horizon_years: int = 5, calibration: str = "original",
              allow_provisional: bool = False) -> Dict[str, Any]:
    """4-variable KFRE risk (0-1) of kidney failure (dialysis/transplant) at 2 or 5 years.

    Population: adults with CKD G3-G5 (eGFR < 60) not on KRT. NOT for G1-G2, AKI, or KRT.
    UACR must be mg/g (mg/mmol is converted by x8.84). calibration:
    'original' | 'non_north_america' | 'north_america' (spec_only).
    2-year S0 values are 'provisional' and only used with allow_provisional=True.
    """
    r: list = []
    age = need_number("age_years", age_years, r, minimum=18)
    s = need_sex(sex, r)
    g = need_number("egfr", egfr, r, positive=True)
    if uacr_mg_g is not None and uacr_mg_mmol is not None:
        r.append("ambiguous_units:give_only_one_of_uacr_mg_g_or_uacr_mg_mmol")
        u = None
    elif uacr_mg_g is None and uacr_mg_mmol is None:
        r.append("missing:uacr")
        u = None
    elif uacr_mg_g is not None:
        u = need_number("uacr_mg_g", uacr_mg_g, r, positive=True)
    else:
        v = need_number("uacr_mg_mmol", uacr_mg_mmol, r, positive=True)
        u = None if v is None else v * 8.84
    key = (calibration, horizon_years)
    s0 = None
    status = None
    if key in KFRE_SPEC_ONLY:
        r.append("spec_only:" + KFRE_SPEC_ONLY[key])
    elif key not in KFRE_S0:
        r.append("unsupported_version:calibration=%s,horizon=%s" % (calibration, horizon_years))
    else:
        s0, status, _ev = KFRE_S0[key]
        if status == "provisional" and not allow_provisional:
            r.append("provisional_baseline_not_enabled:set allow_provisional=True to use S0 not locally verified")
            s0 = None
    pop_ok: Optional[bool] = None
    if g is not None:
        pop_ok = g < 60
        if not pop_ok:
            r.append("outside_population:eGFR>=60 (KFRE is for CKD G3-G5)")
    val = None
    if not r and s0 is not None:
        lp = kfre_linear_predictor(age, 1 if s == "male" else 0, g, u)
        val = 1.0 - s0 ** math.exp(lp)
    return result(
        "KFRE 4-variable", "%s S0, %d-year (%s)" % (calibration, horizon_years, status), val,
        "probability (0-1) of dialysis/transplant within %d years" % horizon_years,
        pop_ok, r,
        {"age_years": age_years, "sex": sex, "egfr": egfr, "uacr_mg_g": uacr_mg_g,
         "uacr_mg_mmol": uacr_mg_mmol, "horizon_years": horizon_years, "calibration": calibration},
        KFRE_SRC, "risk_estimate",
        s0_status=status,
        caveats=["Not locally validated for Taiwan; competing death and modern organ-protective drugs not modelled",
                 "Risk estimate, not a diagnosis; use with eGFR, clinical course and patient preference"],
    )
