"""FIB-4 and APRI (screening indices for advanced fibrosis; not a diagnosis of MASH/cirrhosis).

Formula source for FIB-4: open review PMC13706892 L69 ('age x AST / [platelets x sqrt(ALT)]'; Sterling 2006
PMID 16729309 itself is paywalled and not locally available). Cut-offs 1.3 / 2.67 and the AASLD age>65 value 2.0:
PMC13706892 L75 (secondary source quoting AASLD); McPherson 2017 (PMC5418560) for age >=65 behaviour.
APRI formula: PMC13659483 Table 1 '(AST/LSN) x 100 / platelets'. No APRI cut-offs are implemented
(no locally verified source). EASL-EASD-EASO 2024 and ADA 2026 cut-offs: spec_only (not locally greppable).
"""
from __future__ import annotations

import math
from typing import Any, Dict

from .result import need_number, result

FIB4_SRC = ("Sterling 2006 PMID 16729309 (formula via PMC13706892 L69); cut-offs PMC13706892 L75 quoting AASLD; "
            "McPherson 2017 PMC5418560")
APRI_SRC = "APRI formula as printed in PMC13659483 Table 1 (Wai 2003 PMID 12883497 not locally available)"


def fib4(age_years: Any = None, ast_u_l: Any = None, alt_u_l: Any = None, platelets_10e9_l: Any = None,
         acute_illness: Any = None) -> Dict[str, Any]:
    """FIB-4 = age x AST / (platelets[10^9/L] x sqrt(ALT)). Platelets 10^3/uL == 10^9/L; raw cells/uL must be /1000."""
    r: list = []
    age = need_number("age_years", age_years, r, positive=True)
    ast = need_number("ast_u_l", ast_u_l, r, positive=True)
    alt = need_number("alt_u_l", alt_u_l, r, positive=True)
    plt = need_number("platelets_10e9_l", platelets_10e9_l, r, positive=True)
    if plt is not None and plt > 2000:
        r.append("suspect_units:platelets_10e9_l>2000 (raw cells/uL? divide by 1000)")
    pop = None
    if age is not None and age < 18:
        r.append("outside_population:age<18")
    if acute_illness is True:
        r.append("outside_population:acute_illness (aminotransferases unreliable)")
    if acute_illness is not None and not isinstance(acute_illness, bool):
        r.append("invalid_type:acute_illness")
    if not r:
        pop = True
    elif any(x.startswith("outside_population") for x in r):
        pop = False
    val = None
    if not r:
        val = age * ast / (plt * math.sqrt(alt))
    cat, warn = None, []
    if val is not None:
        if age < 35:
            warn.append("age<35: reduced accuracy (low specificity/sensitivity reports)")
        if age == 65:
            warn.append("age==65: AASLD wording '>65', McPherson '>=65'; standard 1.3 lower cut-off applied")
        lower = 2.0 if age > 65 else 1.3
        cat = "low" if val < lower else ("high" if val > 2.67 else "indeterminate")
    return result("FIB-4", "Sterling 2006 formula; cut-offs <1.3 (>65y: <2.0) / 2.67", val, "index (unitless)",
                  pop, r,
                  {"age_years": age_years, "ast_u_l": ast_u_l, "alt_u_l": alt_u_l,
                   "platelets_10e9_l": platelets_10e9_l, "acute_illness": acute_illness},
                  FIB4_SRC, "screening_index", category=cat, warnings=warn,
                  caveats=["Triage index for advanced fibrosis; not MASH pathology or a cirrhosis probability",
                           "Low value does not exclude advanced fibrosis in T2D with multiple cardiometabolic risk factors "
                           "(ADA 2026; not locally verified)",
                           "Original derivation: HIV/HCV coinfection"])


def apri(ast_u_l: Any = None, ast_uln_u_l: Any = None, platelets_10e9_l: Any = None) -> Dict[str, Any]:
    """APRI = (AST / AST-ULN) x 100 / platelets[10^9/L]. ULN is lab-specific and must be supplied."""
    r: list = []
    ast = need_number("ast_u_l", ast_u_l, r, positive=True)
    uln = need_number("ast_uln_u_l", ast_uln_u_l, r, positive=True)
    plt = need_number("platelets_10e9_l", platelets_10e9_l, r, positive=True)
    val = (ast / uln) * 100.0 / plt if not r else None
    return result("APRI", "Wai 2003 formula (as printed in PMC13659483)", val, "index (unitless)",
                  None if r else True, r,
                  {"ast_u_l": ast_u_l, "ast_uln_u_l": ast_uln_u_l, "platelets_10e9_l": platelets_10e9_l},
                  APRI_SRC, "screening_index",
                  caveats=["No cut-off interpretation implemented (no locally verified source)",
                           "Depends on laboratory-specific AST upper limit of normal"])
