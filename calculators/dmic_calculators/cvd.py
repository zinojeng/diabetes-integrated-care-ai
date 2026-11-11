"""Cardiovascular event-risk models with locally verified coefficients.

SCORE2-Diabetes (Pennells et al., Eur Heart J 2023; PMID 37247330). Coefficients, centering,
baseline survival and region scaling: OA Supplementary Methods table 1
(literature/fulltext/calculators/supp/s2d/supplementary_material.txt L94-L139); the official
Excel calculator (appendix_2.xlsx) is the source of the test vectors.
"""
from __future__ import annotations

import math
from typing import Any, Dict, Optional

from .result import need_number, need_sex, result

S2D_SRC = ("SCORE2-Diabetes, Eur Heart J 2023 PMID 37247330, OA Supplementary Methods table 1 "
           "+ official Excel calculator (appendix_2.xlsx)")

# log SHR (men, women)
S2D = {
    "age": (0.5368, 0.6624), "smoking": (0.4774, 0.6139), "sbp": (0.1322, 0.1421),
    "diabetes": (0.6457, 0.8096), "tchol": (0.1102, 0.1127), "hdl": (-0.1087, -0.1568),
    "age_x_smoking": (-0.0672, -0.1122), "age_x_sbp": (-0.0268, -0.0167),
    "age_x_diabetes": (-0.0983, -0.1272), "age_x_tchol": (-0.0181, -0.0200),
    "age_x_hdl": (0.0095, 0.0186), "agediab": (-0.0998, -0.118), "hba1c": (0.0955, 0.1173),
    "lnegfr": (-0.0591, -0.0640), "lnegfr2": (0.0058, 0.0062),
    "age_x_hba1c": (-0.0134, -0.0196), "age_x_lnegfr": (0.0115, 0.0169),
}
S2D_BASE_SURV = (0.9605, 0.9776)
# region -> ((scale1, scale2) men, (scale1, scale2) women)
S2D_SCALE = {
    "low": ((-0.5699, 0.7476), (-0.7380, 0.7019)),
    "moderate": ((-0.1565, 0.8009), (-0.3143, 0.7701)),
    "high": ((0.3207, 0.9360), (0.5710, 0.9369)),
    "very_high": ((0.5836, 0.8294), (0.9412, 0.8329)),
}


def _bool(name: str, x: Any, reasons, required: bool = True) -> Optional[bool]:
    if x is None:
        if required:
            reasons.append("missing:%s" % name)
        return None
    if not isinstance(x, bool):
        reasons.append("invalid_type:%s(need True/False)" % name)
        return None
    return x


def score2_diabetes(sex: Any = None, age_years: Any = None, diabetes_age_at_diagnosis: Any = None,
                    current_smoker: Any = None, sbp_mmhg: Any = None, total_chol_mmol_l: Any = None,
                    hdl_mmol_l: Any = None, hba1c_mmol_mol: Any = None, egfr: Any = None,
                    risk_region: Any = None, prior_cvd: Any = None,
                    severe_target_organ_damage: Any = None, egfr_equation: Optional[str] = None
                    ) -> Dict[str, Any]:
    """10-year risk (%) of fatal/non-fatal MI, stroke or CVD death in type 2 diabetes.

    risk_region must be given explicitly ('low','moderate','high','very_high'); Taiwan has no
    assigned European region, so no default exists. Units: HbA1c mmol/mol, cholesterol mmol/L.
    eGFR in the original model is CKD-EPI 2009 (a different equation is flagged in details).
    """
    r: list = []
    s = need_sex(sex, r)
    age = need_number("age_years", age_years, r, positive=True)
    dx = need_number("diabetes_age_at_diagnosis", diabetes_age_at_diagnosis, r, positive=True)
    smoker = _bool("current_smoker", current_smoker, r)
    sbp = need_number("sbp_mmhg", sbp_mmhg, r, positive=True)
    tc = need_number("total_chol_mmol_l", total_chol_mmol_l, r, positive=True)
    hdl = need_number("hdl_mmol_l", hdl_mmol_l, r, positive=True)
    a1c = need_number("hba1c_mmol_mol", hba1c_mmol_mol, r, positive=True)
    gfr = need_number("egfr", egfr, r, positive=True)
    pcvd = _bool("prior_cvd", prior_cvd, r)
    std = _bool("severe_target_organ_damage", severe_target_organ_damage, r, required=False)
    if risk_region is None:
        r.append("missing:risk_region(no default; Taiwan is not assigned to a European region)")
    elif risk_region not in S2D_SCALE:
        r.append("invalid_value:risk_region")
    if age is not None and dx is not None and dx > age:
        r.append("inconsistent:diabetes_age_at_diagnosis>age_years")
    pop: Optional[bool] = None
    reasons_pop = []
    if age is not None:
        if not (40 <= age <= 69):
            reasons_pop.append("outside_population:age not in 40-69 (SCORE2-Diabetes chart range)")
    if pcvd is True:
        reasons_pop.append("outside_population:established CVD (secondary prevention)")
    if std is True:
        reasons_pop.append("outside_population:severe target-organ damage (ESC 2023 excludes from primary-prevention scoring)")
    if reasons_pop:
        pop = False
        r.extend(reasons_pop)
    elif not r:
        pop = True
    val = None
    lp = None
    if not r:
        i = 0 if s == "male" else 1
        c = S2D
        cage = (age - 60.0) / 5.0
        csbp = (sbp - 120.0) / 20.0
        ctc = tc - 6.0
        chdl = (hdl - 1.3) / 0.5
        cdx = (dx - 50.0) / 5.0
        ca1c = (a1c - 31.0) / 9.34
        cegfr = (math.log(gfr) - 4.5) / 0.15
        sm = 1.0 if smoker else 0.0
        lp = (c["age"][i] * cage + c["smoking"][i] * sm + c["sbp"][i] * csbp + c["diabetes"][i]
              + c["tchol"][i] * ctc + c["hdl"][i] * chdl
              + c["age_x_smoking"][i] * cage * sm + c["age_x_sbp"][i] * cage * csbp
              + c["age_x_diabetes"][i] * cage + c["age_x_tchol"][i] * cage * ctc
              + c["age_x_hdl"][i] * cage * chdl
              + c["agediab"][i] * cdx + c["hba1c"][i] * ca1c + c["lnegfr"][i] * cegfr
              + c["lnegfr2"][i] * cegfr * cegfr + c["age_x_hba1c"][i] * ca1c * cage
              + c["age_x_lnegfr"][i] * cegfr * cage)
        uncal = 1.0 - S2D_BASE_SURV[i] ** math.exp(lp)
        s1, s2 = S2D_SCALE[risk_region][i]
        val = 100.0 * (1.0 - math.exp(-math.exp(s1 + s2 * math.log(-math.log(1.0 - uncal)))))
    warn = []
    if egfr_equation is None:
        warn.append("egfr_equation_unspecified: model was built with CKD-EPI 2009 eGFR")
    elif egfr_equation != "CKD-EPI-2009":
        warn.append("egfr_equation=%s differs from CKD-EPI 2009 used in development (not recalibrated)" % egfr_equation)
    if severe_target_organ_damage is None:
        warn.append("severe_target_organ_damage_unknown: not assumed absent")
    return result(
        "SCORE2-Diabetes", "ESC 2023, region=%s" % (risk_region,), val,
        "percent 10-year risk of fatal/non-fatal MI, stroke, or CVD death", pop, r,
        {"sex": sex, "age_years": age_years, "diabetes_age_at_diagnosis": diabetes_age_at_diagnosis,
         "current_smoker": current_smoker, "sbp_mmhg": sbp_mmhg, "total_chol_mmol_l": total_chol_mmol_l,
         "hdl_mmol_l": hdl_mmol_l, "hba1c_mmol_mol": hba1c_mmol_mol, "egfr": egfr,
         "risk_region": risk_region, "prior_cvd": prior_cvd,
         "severe_target_organ_damage": severe_target_organ_damage},
        S2D_SRC, "risk_estimate", linear_predictor=lp, warnings=warn,
        caveats=["European regional recalibration; not validated/calibrated for Taiwan",
                 "Footnotes in the supplement quote median baseline survival 0.9625/0.9795 vs 0.9605/0.9776 in the "
                 "calculation table; the calculation table (and official Excel) values are used"],
    )


# ------------------------------------------------------------------ TIMI TRS 2°P in T2D
TIMI_SRC = ("Bergmark 2018 Diabetes Care PMID 29196298 (PMC5829964): Methods 'TRS 2°P' / 'Statistical Analysis', "
            "Table 2, Table 3")
# Table 3, full trial population: 2-year Kaplan-Meier event rates (%) by score bin in SAVOR-TIMI 53 (group rates).
TIMI_BIN_RATES = {
    "<=2": {"n": 4034, "cv_death": 1.0, "mi": 1.5, "ischemic_stroke": 1.0},
    "3": {"n": 5516, "cv_death": 2.1, "mi": 2.7, "ischemic_stroke": 1.4},
    "4": {"n": 4221, "cv_death": 4.1, "mi": 3.5, "ischemic_stroke": 2.4},
    ">=5": {"n": 2717, "cv_death": 6.8, "mi": 7.1, "ischemic_stroke": 3.0},
}


def timi_trs2p_t2d(age_years: Any = None, hypertension: Any = None, current_smoker: Any = None,
                   peripheral_artery_disease: Any = None, prior_stroke: Any = None, prior_mi: Any = None,
                   prior_cabg: Any = None, heart_failure: Any = None, egfr: Any = None,
                   type2_diabetes: Any = None) -> Dict[str, Any]:
    """TRS 2°P applied to type 2 diabetes (10 criteria, 1 point each; diabetes itself scores 1).

    Output is an integer risk-factor COUNT (1-10 in T2D). It is a rank/stratification score; the published
    2-year event rates are group rates for the SAVOR-TIMI 53 population, not an individual probability.
    """
    r: list = []
    age = need_number("age_years", age_years, r, positive=True)
    gfr = need_number("egfr", egfr, r, positive=True)
    flags = {}
    for name, v in (("hypertension", hypertension), ("current_smoker", current_smoker),
                    ("peripheral_artery_disease", peripheral_artery_disease), ("prior_stroke", prior_stroke),
                    ("prior_mi", prior_mi), ("prior_cabg", prior_cabg), ("heart_failure", heart_failure),
                    ("type2_diabetes", type2_diabetes)):
        flags[name] = _bool(name, v, r)
    pop: Optional[bool] = None
    if flags.get("type2_diabetes") is False:
        r.append("outside_population:type 2 diabetes required (cohort: SAVOR-TIMI 53)")
        pop = False
    elif not r:
        pop = True
    val = bin_ = rates = None
    warn = []
    if not r:
        pts = (int(age >= 75) + 1 + sum(int(bool(flags[k])) for k in (
            "hypertension", "current_smoker", "peripheral_artery_disease", "prior_stroke", "prior_mi",
            "prior_cabg", "heart_failure")) + int(gfr < 60))
        val = pts
        bin_ = "<=2" if pts <= 2 else str(pts) if pts in (3, 4) else ">=5"
        rates = TIMI_BIN_RATES[bin_]
        if age == 75:
            warn.append("age==75: Methods text says '>=75', Table 2 says '>75'; '>=75' applied")
        warn.append("eGFR<60 was defined with MDRD in the source; other equations are not equivalent")
    return result(
        "TIMI Risk Score for Secondary Prevention (TRS 2°P) in T2D", "SAVOR-TIMI 53 application (Bergmark 2018)",
        val, "points (count of 10 criteria; 1-10 in T2D)", pop, r,
        {"age_years": age_years, "egfr": egfr, **{k: v for k, v in flags.items()}}, TIMI_SRC, "risk_estimate",
        score_bin=bin_, group_reference_rates_2yr_pct=rates, warnings=warn,
        caveats=["Group Kaplan-Meier rates from SAVOR-TIMI 53 (n=16,488), not an individual probability",
                 "Composite per-bin rates are only in a figure (extremes 0.9%/19.8% in the abstract); component rates in Table 3",
                 "Prior MI was added as a tenth item by the authors; the original TRS 2°P derivation cohort had prior MI",
                 "No Taiwan validation; SAVOR excluded dialysis, creatinine >6.0 mg/dL and transplant"],
    )


# ------------------------------------------------------------------ UKPDS Risk Engine (CHD / stroke), PROVISIONAL
UKPDS_RE_SRC = ("UKPDS risk engine equations as reproduced in Yang 2013 (PMC3716447) Appendices 2-5; originals "
                "Stevens 2001 / Kothari 2002 not locally available")
UKPDS_CHD = dict(q0=0.0112, age=1.059, female=0.525, afro=0.390, smoking=1.350, hba1c=1.183, sbp10=1.088, lr=3.845, d=1.078)
UKPDS_STROKE = dict(q0=0.00186, age=1.092, female=0.7, af=8.554, smoking=1.547, sbp10=1.122, lr=1.138, d=1.145)


def ukpds_risk_engine(outcome: str = None, sex: Any = None, age_at_diagnosis: Any = None,
                      diabetes_duration_years: Any = None, current_smoker: Any = None, hba1c_percent: Any = None,
                      sbp_mmhg: Any = None, total_chol_hdl_ratio: Any = None, afro_caribbean: Any = None,
                      atrial_fibrillation: Any = None, prior_chd_or_stroke: Any = None, horizon_years: Any = None,
                      allow_provisional: bool = False) -> Dict[str, Any]:
    """UKPDS risk engine, CHD or stroke ('chd' | 'stroke'), for T2D without prior CHD/stroke.

    R(t) = 1 - exp(-q d^T (1 - d^t)/(1 - d)), T = years since diagnosis, t = horizon. CHD: q = q0 b1^(AGE-55)
    b2^SEX b3^AC b4^SMOK b5^(H-6.72) b6^((SBP-135.7)/10) b7^(ln(LR)-1.59); stroke: AF instead of AC/H and
    b7^(LR-5.11). AGE = age AT DIAGNOSIS. PROVISIONAL: the source prints '(1 - dt)' with the superscript of d^t lost;
    d^t is the only reading with R(0)=0, but it is not confirmed from a primary text, so allow_provisional=True is required.
    """
    r: list = []
    if outcome not in ("chd", "stroke"):
        r.append("unsupported_outcome:%r(use 'chd' or 'stroke')" % (outcome,))
    s = need_sex(sex, r)
    age = need_number("age_at_diagnosis", age_at_diagnosis, r, positive=True)
    T = need_number("diabetes_duration_years", diabetes_duration_years, r, minimum=0)
    sm = _bool("current_smoker", current_smoker, r)
    sbp = need_number("sbp_mmhg", sbp_mmhg, r, positive=True)
    lr = need_number("total_chol_hdl_ratio", total_chol_hdl_ratio, r, positive=True)
    t = need_number("horizon_years", horizon_years, r, positive=True)
    prior = _bool("prior_chd_or_stroke", prior_chd_or_stroke, r)
    a1c = ac = af = None
    if outcome == "chd":
        a1c = need_number("hba1c_percent", hba1c_percent, r, positive=True)
        ac = _bool("afro_caribbean", afro_caribbean, r)
    elif outcome == "stroke":
        af = _bool("atrial_fibrillation", atrial_fibrillation, r)
    pop: Optional[bool] = None
    if prior is True:
        pop = False
        r.append("outside_population:prior CHD/stroke (primary-prevention equation)")
    elif not r:
        pop = True
    if not r and not allow_provisional:
        r.append("provisional_equation_not_enabled:d^t reading unconfirmed from a primary source; set allow_provisional=True")
    val = None
    if not r:
        fem = 1.0 if s == "female" else 0.0
        if outcome == "chd":
            p = UKPDS_CHD
            q = (p["q0"] * p["age"] ** (age - 55) * p["female"] ** fem * p["afro"] ** (1.0 if ac else 0.0)
                 * p["smoking"] ** (1.0 if sm else 0.0) * p["hba1c"] ** (a1c - 6.72)
                 * p["sbp10"] ** ((sbp - 135.7) / 10.0) * p["lr"] ** (math.log(lr) - 1.59))
        else:
            p = UKPDS_STROKE
            q = (p["q0"] * p["age"] ** (age - 55) * p["female"] ** fem * p["af"] ** (1.0 if af else 0.0)
                 * p["smoking"] ** (1.0 if sm else 0.0) * p["sbp10"] ** ((sbp - 135.7) / 10.0)
                 * p["lr"] ** (lr - 5.11))
        d = p["d"]
        val = 100.0 * (1.0 - math.exp(-q * d ** T * (1.0 - d ** t) / (1.0 - d)))
    return result(
        "UKPDS Risk Engine", "%s, provisional" % outcome, val, "percent risk of %s within horizon" % outcome, pop, r,
        {"outcome": outcome, "sex": sex, "age_at_diagnosis": age_at_diagnosis,
         "diabetes_duration_years": diabetes_duration_years, "current_smoker": current_smoker,
         "hba1c_percent": hba1c_percent, "sbp_mmhg": sbp_mmhg, "total_chol_hdl_ratio": total_chol_hdl_ratio,
         "afro_caribbean": afro_caribbean, "atrial_fibrillation": atrial_fibrillation,
         "prior_chd_or_stroke": prior_chd_or_stroke, "horizon_years": horizon_years},
        UKPDS_RE_SRC, "risk_estimate",
        warnings=["Ethnicity coding only defines Afro-Caribbean vs Caucasian/Asian Indian; East Asian not defined",
                  "Original inputs are mean values of years 1-2 after diagnosis"],
        caveats=["Not the UKPDS Outcomes Model 2 (spec_only: Oxford licence and equations not locally available)",
                 "Development cohort 1977-1991 UK; no Taiwan calibration; Oxford licence terms for the engine not verified"])
