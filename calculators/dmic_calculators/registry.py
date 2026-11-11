"""Implementation status of every requested tool. status:
implemented        - coefficients/formula grep-verified in a local full text/official document, tests executed
implemented_secondary - verified only in open SECONDARY reproductions (primary paywalled)
provisional        - implemented but needs allow_provisional=True (some constant/equation form not primary-verified)
spec_only          - NOT implemented; 'missing' says what is needed. No numbers are produced.
"""
from __future__ import annotations

REGISTRY = [
    # --- comorbidity burden
    dict(id="dcsi", tool="DCSI (Young 2008) / aDCSI (Chang 2012)", status="spec_only", entry="comorbidity.dcsi",
         missing="Table 1 rubric (0/1/2 per domain) and aDCSI ICD-9 map: PMC3810070 abstract-only; Chang 2012 OA=N; 11 OA DCSI-using papers inspected, none prints the rubric"),
    dict(id="cci", tool="Charlson (original 1987; Quan 2011)", status="implemented_secondary", entry="comorbidity.charlson",
         missing="primary papers; Quan renal weight conflict (1 vs 4); ICD mapping not coded"),
    dict(id="cci_age", tool="Age-adjusted Charlson", status="spec_only", entry="comorbidity.charlson_age_adjusted",
         missing="Charlson 1994 primary; two open sources give different age bands"),
    # --- organ / stratification
    dict(id="ckd_epi_cr", tool="CKD-EPI 2021 creatinine", status="implemented", entry="ckd.ckd_epi_2021_creatinine", missing=""),
    dict(id="ckd_epi_crcys", tool="CKD-EPI 2021 creatinine-cystatin C", status="implemented", entry="ckd.ckd_epi_2021_creatinine_cystatin", missing=""),
    dict(id="ckd_ga", tool="KDIGO 2024 CKD G/A and heat map", status="implemented", entry="staging.ckd_cga_risk", missing=""),
    dict(id="kfre_orig5", tool="KFRE 4-var Original 5-year", status="implemented", entry="ckd.kfre_4var", missing=""),
    dict(id="kfre_nonna5", tool="KFRE 4-var non-North-America 5-year", status="implemented", entry="ckd.kfre_4var", missing=""),
    dict(id="kfre_2y", tool="KFRE 4-var 2-year (Original, non-NA)", status="provisional", entry="ckd.kfre_4var",
         missing="2-year S0 not printed in any locally greppable text (eAppendix 2 p9 blocked 403)"),
    dict(id="kfre_na", tool="KFRE 4-var North-America regional (2/5-year)", status="spec_only", entry="ckd.kfre_4var",
         missing="S0 values not locally greppable"),
    dict(id="fib4", tool="FIB-4 (+ cut-offs 1.3/2.67; >65 y 2.0)", status="implemented_secondary", entry="liver.fib4",
         missing="Sterling 2006 primary; EASL 2024 and ADA 2026 cut-off tables not locally greppable"),
    dict(id="apri", tool="APRI (value only)", status="implemented_secondary", entry="liver.apri",
         missing="Wai 2003 primary; no cut-offs verified"),
    dict(id="iwgdf", tool="IWGDF 2023 risk categories 0-3", status="implemented", entry="foot.iwgdf_risk_category", missing=""),
    # --- event risk
    dict(id="prevent", tool="AHA PREVENT (base, +UACR, +HbA1c, full; 2026-10-14 HbA1c correction)", status="spec_only", entry=None,
         missing="coefficients only in Supplemental Table S12 A-J (NCBI proof-of-work / AHA 403); corrected HbA1c tables not obtained; do not implement HbA1c/full models until corrected tables in hand"),
    dict(id="score2d", tool="SCORE2-Diabetes", status="implemented", entry="cvd.score2_diabetes", missing=""),
    dict(id="recode", tool="RECODe (9 outcomes with lambda/mean printed)", status="implemented", entry="recode.recode", missing=""),
    dict(id="recode_other", tool="RECODe other 12 micro-vascular outcomes", status="spec_only", entry="recode.recode",
         missing="lambda and mean(linear predictor) not printed in open main text; appendix blocked"),
    dict(id="watchdm", tool="WATCH-DM (points; continuous)", status="spec_only", entry=None,
         missing="primary abstract-only; only secondary table (Iwakura 2024) with internal BMI-row conflict; continuous-model coefficients nowhere"),
    dict(id="timi", tool="TIMI TRS 2P in T2D (SAVOR-TIMI 53 application)", status="implemented", entry="cvd.timi_trs2p_t2d",
         missing="per-score composite rates only in an image"),
    dict(id="ukpds_re", tool="UKPDS Risk Engine CHD/stroke", status="provisional", entry="cvd.ukpds_risk_engine",
         missing="primary (Stevens 2001, Kothari 2002); d^t superscript lost in the only local print"),
    dict(id="ukpds_om2", tool="UKPDS Outcomes Model 2", status="spec_only", entry=None,
         missing="Hayes 2013 OA=N; Oxford DTU page 403; licence from University of Oxford (second-hand)"),
    dict(id="advance", tool="ADVANCE risk score", status="spec_only", entry=None,
         missing="Kengne 2011 OA=N; coefficients/points only as images in the open review"),
    dict(id="karter", tool="Karter hypoglycemia tool", status="spec_only", entry=None,
         missing="points table not in any local text (PMC5624849 abstract-only; 3 later papers lack the table)"),
    dict(id="chow2018", tool="Chow 2018 severe hypoglycemia score (ACCORD)", status="spec_only", entry=None,
         missing="points printed in PMC6091902 but not examined/validated by this session (candidate)"),
    dict(id="tw_esrd", tool="Taiwan ESRD score (Lin 2017 Sci Rep, PMID 28860599)", status="spec_only", entry=None,
         missing="Table 3 gives age points only as 'range -2 to 8' without the age->points rule; needs HbA1c/SBP variation; Table 4 cell typo '5381'"),
    dict(id="tw_ckd", tool="Taiwan CKD score (Lin 2022 Sci Rep, PMID 35314714)", status="spec_only", entry=None,
         missing="score-to-absolute-risk map in Supplementary S2 not obtained"),
    # --- scales
    dict(id="phq9", tool="PHQ-9", status="implemented", entry="scales.phq9", missing="missing-item rule not found"),
    dict(id="phq2", tool="PHQ-2", status="implemented", entry="scales.phq2", missing=""),
    dict(id="gad7", tool="GAD-7", status="implemented", entry="scales.gad7", missing=""),
    dict(id="who5", tool="WHO-5", status="implemented", entry="scales.who5", missing=""),
    dict(id="paid20", tool="PAID-20 (current 0-4)", status="implemented_secondary", entry="scales.paid20", missing="licence not found"),
    dict(id="paid5", tool="PAID-5", status="implemented_secondary", entry="scales.paid5", missing="cut-off from VUmc sheet; licence not found"),
    dict(id="dds2", tool="DDS-2", status="implemented", entry="scales.dds2", missing="DDS owner licence not found"),
    dict(id="dds17", tool="DDS-17 (total mean only)", status="implemented", entry="scales.dds17", missing="subscale scoring not implemented; licence"),
    dict(id="hfs2", tool="HFS-II (sums)", status="implemented_secondary", entry="scales.hfs2", missing="no cut-off exists"),
    dict(id="minicog", tool="Mini-Cog", status="implemented_secondary", entry="scales.minicog", missing="author's sheet via third-party reprint; research use needs permission"),
    dict(id="moca", tool="MoCA (total entry)", status="implemented_secondary", entry="scales.moca_total", missing="test content/training per MoCA terms"),
    dict(id="cfs", tool="Clinical Frailty Scale v2.0", status="implemented", entry="scales.clinical_frailty_scale", missing="licence/translation permission"),
    dict(id="frail", tool="FRAIL scale", status="implemented_secondary", entry="scales.frail_scale", missing="item wording differs by paper"),
]

STATUSES = {"implemented", "implemented_secondary", "provisional", "spec_only"}
