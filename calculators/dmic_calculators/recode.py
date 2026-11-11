"""RECODe (Basu et al., Lancet Diabetes Endocrinol 2017; PMID 28803840) — one equation per outcome, no total score.

Coefficients: Tables 2-4 of the open PMC full text (PMC5769867; table bodies extracted from the JATS XML to
literature/parsed/calculators/PMC5769867_tables.md). Risk = 1 - lambda^exp(sum(beta*x) - mean_lp) (table footnotes).
lambda and mean_lp are printed ONLY for the outcomes implemented below; the other microvascular outcomes are
spec_only (missing lambda/mean in the main text; appendix behind a bot wall).
Derivation: ACCORD, age 40-79 y, T2D, HbA1c >= 7.5%, history of or risk factors for CVD. Horizon: 10 years.
"""
from __future__ import annotations

import math
from typing import Any, Dict, Optional

from .result import need_number, result

RECODE_SRC = "Basu 2017 Lancet Diabetes Endocrinol PMID 28803840, PMC5769867 Tables 2-4 + footnotes"

COVARIATES = ("age_years", "female", "black", "hispanic", "current_smoker", "sbp_mmhg", "cvd_history",
              "bp_lowering_drugs", "oral_diabetes_drugs", "statins", "anticoagulants", "hba1c_percent",
              "total_chol_mg_dl", "hdl_mg_dl", "creatinine_mg_dl", "uacr_mg_g")
BINARY = {"female", "black", "hispanic", "current_smoker", "cvd_history", "bp_lowering_drugs",
          "oral_diabetes_drugs", "statins", "anticoagulants"}

# outcome -> (lambda, mean_lp, {covariate: beta}, table)
MODELS: Dict[str, Any] = {
    "renal_failure_esrd": (0.973, 0.23, dict(age_years=-0.01938, female=-0.01129, black=0.08812,
        hispanic=0.23380, current_smoker=0.14830, sbp_mmhg=0.00303, cvd_history=-0.02164,
        bp_lowering_drugs=-0.07952, oral_diabetes_drugs=-0.12560, anticoagulants=0.03199, hba1c_percent=0.13690,
        total_chol_mg_dl=-0.00111, hdl_mg_dl=0.00629, creatinine_mg_dl=0.86090, uacr_mg_g=0.00036), "Table 2"),
    "severe_vision_loss": (0.921, 4.56, dict(age_years=0.02285, female=0.22640, black=-0.16770, sbp_mmhg=0.00824,
        cvd_history=0.1127, bp_lowering_drugs=0.06393, oral_diabetes_drugs=-0.23490, hba1c_percent=0.1449,
        total_chol_mg_dl=-0.00017, hdl_mg_dl=0.00545, creatinine_mg_dl=0.69470, uacr_mg_g=0.00020), "Table 2"),
    "pressure_sensation_loss": (0.870, 4.75, dict(age_years=0.03022, female=-0.18680, black=-0.09448,
        sbp_mmhg=0.00456, cvd_history=0.26672, bp_lowering_drugs=0.18192, oral_diabetes_drugs=-0.25747,
        hba1c_percent=0.18866, total_chol_mg_dl=0.00219, hdl_mg_dl=-0.00539, creatinine_mg_dl=0.60442), "Table 3"),
    "ascvd": (0.85, 3.65, dict(age_years=0.03412, female=-0.16720, black=-0.11870, current_smoker=0.15100,
        sbp_mmhg=0.00007, cvd_history=0.77840, bp_lowering_drugs=0.05579, statins=-0.03361, anticoagulants=0.25240,
        hba1c_percent=0.17160, total_chol_mg_dl=0.00193, hdl_mg_dl=-0.00837, creatinine_mg_dl=0.43550,
        uacr_mg_g=0.00033), "Table 4"),
    "myocardial_infarction": (0.93, 2.92, dict(age_years=0.04363, female=-0.20660, black=-0.11630,
        current_smoker=0.23580, sbp_mmhg=-0.00514, cvd_history=0.96180, bp_lowering_drugs=-0.12480, statins=0.04699,
        anticoagulants=0.54400, hba1c_percent=0.21350, total_chol_mg_dl=0.00019, hdl_mg_dl=-0.01358,
        creatinine_mg_dl=0.08027, uacr_mg_g=0.00042), "Table 4"),
    "stroke": (0.98, 6.96, dict(age_years=0.02896, female=-0.00326, black=0.27160, current_smoker=0.16650,
        sbp_mmhg=0.01659, cvd_history=0.41380, bp_lowering_drugs=0.15980, statins=-0.18870, anticoagulants=-0.13870,
        hba1c_percent=0.33650, total_chol_mg_dl=0.00171, hdl_mg_dl=-0.00639, creatinine_mg_dl=0.59550,
        uacr_mg_g=0.00030), "Table 4"),
    "heart_failure": (0.96, 5.15, dict(age_years=0.05268, female=0.25290, black=-0.04969, current_smoker=0.29050,
        sbp_mmhg=0.00121, cvd_history=1.00700, bp_lowering_drugs=0.63890, statins=-0.11750, anticoagulants=0.73650,
        hba1c_percent=0.20920, total_chol_mg_dl=-0.00136, hdl_mg_dl=-0.01758, creatinine_mg_dl=0.82140,
        uacr_mg_g=0.00041), "Table 4"),
    "cardiovascular_mortality": (0.97, 3.97, dict(age_years=0.05501, female=-0.30560, black=0.07957,
        current_smoker=-0.05764, sbp_mmhg=-0.00394, cvd_history=1.01600, bp_lowering_drugs=-0.15770,
        statins=-0.20450, anticoagulants=0.69460, hba1c_percent=0.24540, total_chol_mg_dl=-0.00127,
        hdl_mg_dl=-0.01081, creatinine_mg_dl=0.45440, uacr_mg_g=0.00047), "Table 4"),
    "all_cause_mortality": (0.93, 4.66, dict(age_years=0.06703, female=-0.15290, black=-0.02393,
        current_smoker=0.5399, sbp_mmhg=-0.00299, cvd_history=0.58880, bp_lowering_drugs=0.08776,
        statins=-0.26810, anticoagulants=0.40360, hba1c_percent=0.16590, total_chol_mg_dl=-0.00095,
        hdl_mg_dl=-0.00438, creatinine_mg_dl=0.35970, uacr_mg_g=0.00039), "Table 4"),
}
SPEC_ONLY_OUTCOMES = ("microalbuminuria", "macroalbuminuria", "doubling_creatinine_or_egfr_drop",
                      "composite_nephropathy_a", "composite_nephropathy_b", "photocoagulation_or_vitrectomy",
                      "cataract_extraction", "three_line_visual_acuity_loss", "composite_retinopathy",
                      "mnsi_gt2", "vibratory_sensation_loss", "ankle_jerk_loss")


def recode(outcome: str, allow_omit_missing_terms: bool = False, **covariates: Any) -> Dict[str, Any]:
    """10-year risk (%) for ONE RECODe outcome. Missing required covariate -> None unless the caller explicitly
    opts in to the paper's 'omit the term' option (then omitted terms are listed and flagged as unvalidated).

    Units: age y; binary variables True/False; SBP mmHg; HbA1c %; cholesterol mg/dL; creatinine mg/dL; UACR mg/g.
    ethnicity: 'black' / 'hispanic' flags; white/other = both False.
    """
    unknown = set(covariates) - set(COVARIATES)
    r: list = []
    if unknown:
        r.append("unknown_covariate:%s" % ",".join(sorted(unknown)))
    if outcome in SPEC_ONLY_OUTCOMES:
        r.append("spec_only:lambda and mean(linear predictor) not printed in the open main text for this outcome")
    elif outcome not in MODELS:
        r.append("unsupported_outcome:%s" % outcome)
    if r:
        return result("RECODe", "outcome=%s" % outcome, None, None, None, r, covariates, RECODE_SRC, "risk_estimate")
    lam, mean_lp, betas, table = MODELS[outcome]
    omitted = []
    s = 0.0
    used = {}
    for name, beta in betas.items():
        x = covariates.get(name)
        if x is None:
            if allow_omit_missing_terms:
                omitted.append(name)
            else:
                r.append("missing:%s" % name)
            continue
        if name in BINARY:
            if not isinstance(x, bool):
                r.append("invalid_type:%s(need True/False)" % name)
                continue
            xv = 1.0 if x else 0.0
        else:
            v = need_number(name, x, r, positive=True)
            if v is None:
                continue
            xv = v
        used[name] = x
        s += beta * xv
    age = covariates.get("age_years")
    pop: Optional[bool] = None
    if isinstance(age, (int, float)) and not isinstance(age, bool):
        pop = 40 <= age <= 79
        if not pop:
            r.append("outside_population:age not in 40-79 (ACCORD)")
    elif not r:
        pop = True
    if omitted and len(omitted) == len(betas):
        r.append("no_covariates_supplied")
    val = None
    if not r:
        val = 100.0 * (1.0 - lam ** math.exp(s - mean_lp))
    return result("RECODe", "outcome=%s (%s)" % (outcome, table), val, "percent 10-year risk of " + outcome.replace("_", " "),
                  pop, r, covariates, RECODE_SRC, "risk_estimate", omitted_terms=omitted,
                  lambda_=lam, mean_linear_predictor=mean_lp,
                  warnings=(["terms omitted at caller's request (paper footnote allows omission; not validated): %s"
                             % ",".join(omitted)] if omitted else []),
                  caveats=["Derived in ACCORD (HbA1c >=7.5% at entry, high CV risk); not calibrated for Taiwan",
                           "Coefficients are the 5-decimal table values; the paper's worked examples use more digits",
                           "One equation per outcome; outcomes must not be summed or averaged into an overall risk",
                           "Binary-variable coding (1=yes) follows the footnote worked examples"])
