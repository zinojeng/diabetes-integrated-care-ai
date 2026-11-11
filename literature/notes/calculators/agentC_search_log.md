# agentC_search_log.md  (date of all entries: 2026-11-11; times local)
Format: query/URL | source/tool | outcome

1. EBI supplementaryFiles PMC10361012 (curl -m 600, UA dmic-research-fulltext-tool/1.0, background, up to 4 tries, to .part then mv after unzip -t) | Europe PMC REST | OK on first background run: HTTP 200, 2,164,540 bytes; old HTTP-500 HTML stub (10,135 bytes) deleted first. Extracted to supp/s2d/.
2. https://professional.heart.org/-/media/PHD-Files/Guidelines-and-Statements/PREVENT/PREVENT-Update-FAQ-101426.pdf | curl + WebFetch | HTTP 403 (HTML 4,558 bytes; saved file removed). BLOCKED.
3. https://professional.heart.org/en/guidelines-and-statements/about-prevent-calculator, .../prevent, PREVENT-FAQs-FINAL.pdf | curl, WebFetch | HTTP 403. BLOCKED.
4. WebSearch "AHA PREVENT equations HbA1c correction update 2026 FAQ" | web search | returned the AHA FAQ URL and a search-generated summary (HbA1c add-on and full equations only; ~0.1% reclassification). Summary is secondary/unverified; no coefficients; exact wording and effective date not obtained.
5. EBI supplementaryFiles PMC10910659 (PREVENT) | Europe PMC REST | HTTP 200, XML error "not open access one". NOT_FOUND via EBI.
6. search_europepmc "PREVENT equations coefficients HbA1c ... supplemental table" (8) | paper-search | no paper printing coefficients; found Krishnan 2026 PMC13261269 (OA).
7. scripts/fulltext_tools.py pmc PMC13261269 | NCBI E-utilities | OK, title matches (Systematic examination of the PREVENT equations). Gives age ranges 30-79 (10 y) and 30-59 (30 y), L36.
8. search_europepmc "PREVENT equations erratum correction HbA1c coefficient" | paper-search | irrelevant abstracts. NOT_FOUND.
9. EBI supplementaryFiles PMC8822996 (Inker NEJM 2021) | Europe PMC REST | "not open access one".
10. search_europepmc "CKD-EPI 2021 race-free ... 142 0.9938 ..." | paper-search | empty.
11. https://www.niddk.nih.gov/research-funding/.../glomerular-filtration-rate-equations/adults | curl | HTTP 200, 49,619 bytes -> official/agentC_niddk_gfr_adults.html/.txt. FULLTEXT_VERIFIED for both CKD-EPI 2021 equations. (First guess URL .../clinical-tools-patient-management/... returned 404.) Also found pre-existing official/niddk_gfr_adults.html/.txt not authored by agent C.
12. https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf | curl UA honest | HTTP 200, 5,966,902 bytes. pdftotext OK; heat map page rendered to PNG (pdftoppm p.11) and read visually.
13. pmc PMC10735173 (AASLD 2023), PMC13706892, PMC13467911, PMC5418560 (McPherson 2017), PMC13659483 | fulltext_tools | all OK, line-1 titles match.
14. search_europepmc "AASLD practice guidance ... FIB-4 2023" | paper-search | review articles; used PMC13706892/PMC13467911 as secondary sources.
15. search_europepmc McPherson age FIB-4 | paper-search | found PMID 27725647 -> PMC5418560 (OA).
16. search_europepmc APRI formula WHO | paper-search | irrelevant. Wai 2003 NOT_FOUND open.
17. https://iris.who.int/bitstream/handle/10665/154590/9789241549059_eng.pdf | curl | HTTP 200 but 755-byte DSpace JS shell, not a PDF; deleted. NOT obtained.
18. https://diabetesjournals.org/care/article/49/Supplement_1/S58/... (ADA SOC 2026 s4, resolved via doi.org) | curl | HTTP 403 Cloudflare "Just a moment". BLOCKED; not bypassed.
19. https://iwgdfguidelines.org/wp-content/uploads/2023/07/IWGDF-2023-02-Prevention-Guideline.pdf | curl | HTTP 200, 752,028 bytes, 36 pages. FULLTEXT_VERIFIED. (second guess URL -1.pdf 404 had overwritten the file; re-downloaded.)
20. search_europepmc IWGDF prevention 2023 | paper-search | no PMC article; official PDF used instead.
21. search_pubmed "Taiwan type 2 diabetes risk prediction model cardiovascular ... coefficients" | paper-search | empty (too long query). Then "Taiwan diabetes risk score cardiovascular" | noisy; found PMID 41038763.
22. search_europepmc x3 (Taiwanese T2D ESKD risk score; hypoglycemia prediction; Taiwan Diabetes Study CV risk engine) | paper-search | mostly noise; found PMID 35314714 (PMC8938464).
23. search_pubmed "Taiwan type 2 diabetes hypoglycemia risk prediction model" | found PMID 32446799, 29458073. "Taiwan diabetes all-cause mortality prediction risk score ..." -> tool error (output too large, 115,928 chars); read saved JSON via python: PMIDs 34682901, 33118688.
24. EBI search EXT_ID lookups for 33118688, 34682901, 32446799, 29458073, 41038763, 35314714 | Europe PMC REST | only 34682901 (PMC8537078) and 35314714 (PMC8938464) are OA.
25. pmc PMC8938464, PMC8537078 + EBI fullTextXML (saved in fulltext/calculators/taiwan/) | OK; tables extracted from XML since fulltext_tools md drops tables.
Tool failures worth noting: paper-search search_pubmed output overflow (item 23); search_europepmc returns many irrelevant congress abstracts; fulltext_tools md omits table bodies (Tables 1-3 in EASL, McPherson, Inker, PMC8938464 are absent from the md).
