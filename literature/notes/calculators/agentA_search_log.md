# agentA_search_log.md (calculators, agent A, date 2026-11-11)

Method: Europe PMC REST (`/europepmc/webservices/rest/search`, resultType=lite, honest UA `dmic-research-fulltext-tool/1.0`, pageSize<=15) via a scratchpad helper; full text only by `python3 scripts/fulltext_tools.py pmc PMCxxxx --role calculators` with EXACT PMCIDs (title on line 1 checked every time); table-only extraction from the saved JATS XML (literature/fulltext/calculators/<PMCID>.xml -> literature/parsed/calculators/<PMCID>_tables.md) because the stock converter drops table-wraps nested outside body `<sec>`. No Sci-Hub, no paywall scrapers, no PoW/CAPTCHA/Cloudflare bypass.

## A. Pre-existing local files examined (not fetched by me)
| File | Line-1 title check | Result |
|---|---|---|
| PMC5769867.md | RECODe (OK) | converter dropped Tables 1-5; recovered from XML -> PMC5769867_tables.md (coefficients FOUND) |
| PMC5829964.md | TIMI Risk Score ... (OK) | TRS 2P in T2D; included |
| PMC3810070.md (Young 2008) | OK | abstract only |
| PMC5624849.md (Karter 2017) | OK | abstract only; DOI in file = 10.1001/jamainternmed.2017.3844 |
| PMC7364669.md (Segar 2019) | OK | abstract only |
| earlier wrong elink results (PMC13671262, PMC13746622, PMC13741072, PMC13746842) | mismatch | already removed before my run (receipts remain in literature/receipts/calculators.jsonl) - NOT re-fetched by me |

## B. Queries (Europe PMC unless stated). hits = hitCount
| # | Query (abridged) | Hits | Outcome |
|---|---|---|---|
| 1 | TITLE:"Diabetes Complications Severity Index" AND OPEN_ACCESS:y | 3 | fetched PMC10069524, PMC10959489, PMC7418200 - none prints rubric; only 10069524 kept (structure sentence + Deyo CCI weights text) |
| 2 | TITLE:"Diabetes Complications Severity Index" AND (ICD-10 OR update OR translation) | 7 | Glasheen 2017 (28416120), Wicke 2019 (30763043), Young 2008 (18197741): OA=N; excluded (no full text) |
| 3 | TITLE:"adapted DCSI" OR aDCSI | 7 | Chang 2012 (23198714) OA=N; others use aDCSI only |
| 4-7 | DCSI + "vitreous hemorrhage"/"retinal detachment"/"ketoacidosis"/ICD codes 362.0, 250.4, E11.3 + OA | 3,73,11,2,1,8 | fetched PMC10698929, PMC12803608, PMC6473045, PMC9250218, PMC12398047, PMC9623510, PMC11432947, PMC11006598: none prints DCSI rubric -> DELETED (md, tables, xml) |
| 8 | Tavily web search "DCSI Young 2008 Table 1 scoring..." | 5 | only a Scribd copy of Glasheen (not an authorised open source; not used) |
| 9 | curl europepmc fullTextXML PMC3810070 | HTTP 500 | not available |
| 10 | curl europepmc ptpmcrender PDF PMC3810070 | HTTP 403 Cloudflare "Just a moment" | STOPPED, not bypassed |
| 11 | curl ajmc.com view URLs | HTTP 404 | n/a |
| 12 | TITLE:Charlson AND (updating/updated weights/ICD-10/coding algorithms) AND OA | 4 | fetched PMC8742382, PMC6554904, PMC3125388, PMC2267188: no weight table -> PMC8742382, 6554904, 2267188 DELETED; PMC3125388 kept (Danish ICD-10 list; different mapping, low priority) |
| 13 | "Charlson" "updated weights" "Quan" "metastatic solid tumor" Table OA | 8 | PMC13436062 (kept: Quan weights), PMC13084228 (kept: original/Quan/Choi weights, renal=4 conflict), PMC13665550 (kept: Table A2 weights+Quan ICD-10+hierarchy) |
| 14 | "Charlson" Quan weights renal disease hemiplegia AIDS Table OA 2012-2026 | 76 | fetched PMC13721275 (kept: original weights), PMC13586706 (kept: Quan ICD-10 mapping), PMC13590208/PMC13210387/PMC12675838/PMC12112135/PMC12174718 (no weights; DELETED) |
| 15 | TITLE:Charlson AND (Quan/updated/revised/modified) AND OA | 9 | not fetched |
| 16 | "age-adjusted Charlson" one point per decade OA | 140 | fetched PMC13701863 (kept), PMC13094585 (kept), PMC13090039 (DELETED, no definition) |
| 17 | Charlson ICD-9-CM 250.4 250.7 250.0 OA | 1 | PMC7756119 (kept; ICD-9-CM list in table footnote) |
| 18 | Charlson hierarchy/double count diabetes OA | 96 | fetched PMC9517356 (kept; Quan ICD-10 groups + comparison), no normative hierarchy statement found |
| 19 | "WATCH-DM" AND OA | 14 (one attempt HTTP 503, retried) | fetched PMC9238735 (Segar 2022 JAHA, kept), PMC13009881 (Kuo 2026, kept), PMC10798943 (Iwakura 2024, kept: original-style point table) |
| 20 | Karter hypoglycemia risk stratification tool validation OA | 9 / 7 | fetched PMC6429629 (ICD-10 revalidation), PMC10066459 (CGM validation), PMC12917679 (RCT) - none prints points table; all kept for definitions |
| 21 | TITLE:"UKPDS Outcomes Model 2" | 3 | Hayes 2013 (23793713) OA=N; Leal 2021 (34297424) OA=N; Laxy 2019 OA=N |
| 22 | TITLE UKPDS risk engine / model OA | 9, 2, 6, 13 | fetched PMC3716447 (Yang 2013: equations+parameters KEPT), PMC3017299 (van Dieren 2011, validation only, kept), PMC3661828 (Leal 2013 OM1 temporal validation, tables not equations, kept), PMC12803570 (Coleman 2026 OM2 validation, kept), PMC11344020 (Gao 2024 time-path equations, kept) |
| 23 | Tavily "UKPDS OM2 licence Oxford DTU" ; curl dtu.ox.ac.uk/outcomesmodel | 5 / HTTP 403 | official licence text NOT obtained; Mt Hood page excerpt saved (second-hand) |
| 24 | AUTH:Kengne ADVANCE; "Contemporary model for CV risk prediction in T2D" ; "ADVANCE-ON" | 4 / 1 / many | Kengne 2011 (21450612) OA=N; Kengne 2013 review PMC3902381 fetched (coefficient table is an image); no ADVANCE-ON model paper found |
| 25 | curl europepmc / ncbi image URLs for PMC3902381 g001 | 403 / 404 | not bypassed |
| 26 | Taiwan T2D prediction queries (title + AFF:"Taiwan" + OA), hypoglycaemia Taiwan | 10, 4, 1, 2 | fetched PMC5579050 (ESRD score, KEPT), PMC8938464 (CKD model, KEPT), PMC11238483 (EHR adaptation, performance only, kept), PMC8537078 (mortality, kept); no Taiwan hypoglycaemia model found |
| 27 | Chow 2018 severe hypoglycaemia (from query 20 list) | - | PMC6091902 fetched, point table KEPT |
| 28 | PMC13741277 (2026 review, macrovascular models in T2DM) | - | fetched; Table 1 gives ADVANCE final variable list (secondary) |
| 29 | efetch db=pmc PMC5769867 (XML) | 200 | tables T1-T5 present in XML |

## C. Files written
- literature/fulltext/calculators/<PMCID>.xml for every kept paper (+ mthood_ukpds_excerpt_20261111.txt)
- literature/parsed/calculators/<PMCID>.md (stock converter) and <PMCID>_tables.md (my table extractor) - these are git-ignored copyright material
- literature/receipts/calculators.jsonl: appended by the stock tool for each `pmc` call (including those later deleted as irrelevant)
- literature/notes/calculators/agentA_tables.md, agentA_search_log.md

## D. Caveats
- _tables.md files for PMC10361012, PMC10910659, PMC11813909 were also generated by me (papers fetched earlier by others); they are additive.
- Concurrent sessions are adding other PMC*.md files in the same directory (e.g. PMC10735173, PMC1188185, PMC13261269 ...); I did not touch them.
