# agentB search / fetch log (date 2026-11-11, role: calculators, agent B)

UA for every curl: `dmic-research-fulltext-tool/1.0`. No Sci-Hub, no paywall scrapers, no challenge bypass.
Local dir abbreviations: OFF = literature/fulltext/calculators/official/ ; PARS = literature/parsed/calculators/

## Identifier lookups (Europe PMC REST, titles only; IDs used to locate, never as facts)
| query | source | outcome |
|---|---|---|
| Kroenke 2003 PHQ-2 | EPMC REST | PMID 14583691, not in PMC -> abstract only saved (OFF/ABSTRACT_Kroenke2003_PHQ2.txt) |
| Spitzer 2006 GAD-7 | EPMC REST | PMID 16717171, not in PMC -> abstract only |
| Fisher 2008 DDS2 | EPMC REST | Found: Fisher 2008 is **Ann Fam Med 6:246** (PMC2384991), NOT Diabetes Care. PMC XML = abstract only; full text obtained from annfammed.org (OK) |
| Polonsky 2005 DDS | EPMC REST | PMID 15735199 not in PMC -> abstract only; diabetesjournals.org = HTTP 403 (BLOCKED) |
| Polonsky 1995 PAID | EPMC REST | PMID 7555499 (first query hit a wrong paper "Responsiveness of PAID" -> discarded) -> abstract only |
| McGuire 2010 PAID-5 | EPMC REST | PMID 19841892 not in PMC -> abstract only |
| Topp 2015 WHO-5 | EPMC REST | PMID 25831962 not in PMC -> abstract only; karger.com = HTTP 403 (BLOCKED) |
| Borson 2000 / 2003 Mini-Cog | EPMC REST | PMID 11113982 / Borson 2003 JAGS -> abstracts only |
| Nasreddine 2005 MoCA | EPMC REST | PMID 15817019 not in PMC -> abstract only |
| Rockwood 2005 CMAJ | EPMC REST + PMC | PMC1188185 abstract only (fulltext_tools.py: ABSTRACT_ONLY) |
| Morley 2012 FRAIL | EPMC REST | PMC4515112 OK full text (NIH manuscript) |
| Morley 2013 JAMDA consensus | EPMC REST | PMC4084863 OK full text incl. Table 2 FRAIL questionnaire |
| Abellan van Kan 2008 IANA | cited in PMC4515112 ref 9 -> PMC12892609 | OK full text, but FRAIL scale is NOT defined in it (grep) |
| Liu 2011 Taiwan PHQ-9 | EPMC REST | PMID 21111406 not in PMC -> abstract only (pointer) |

## fulltext_tools.py pmc (line 1 title checked each time; none mismatched)
PMC2384991 ABSTRACT_ONLY; PMC1188185 ABSTRACT_ONLY; PMC4515112 OK; PMC4084863 OK; PMC12892609 OK; PMC11983946 OK (Ethiopia PAID, secondary); PMC12969205 OK (Indonesia PAID, secondary); PMC8090183 ABSTRACT_ONLY (QI, secondary); PMC8968751 OK (Taiwan DDS, pointer); PMC2797982 OK (PAID-C, pointer); PMC9448521 OK (Chinese PHQ-2/9 review, pointer). PMC1495268 (PHQ-9) was already an abstract-only stub; re-checked: still no body in PMC open subset.

## Official / web fetches (curl)
| URL (short) | result |
|---|---|
| phqscreeners.com/.../201412/instructions.pdf | OK -> OFF/phq_instructions.pdf/.txt (official PHQ+GAD-7 manual) |
| phqscreeners.com/ | OK html (index only) |
| cdn.who.int WHO-5 english original PDF (via WebSearch hit for WHO-UCN-MSD-MHE-2024.01) | OK -> who5_english_original.pdf/.txt (text layer is doubled; use sed line numbers, reads fine on -layout) |
| who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01 | OK html -> who5_pubpage.txt |
| iris.who.int discover/search API (3 queries) | OK HTTP but WHO-5 record not found by IRIS search (unrelated hits discarded); WHO doc taken from who.int/cdn.who.int instead |
| dal.ca CFS page, Permission-for-use, Translations | OK |
| cdn.dal.ca CFS Guidance (2020-Apr-06), Overview (2020-Mar-25), Top Tips v2.0 (2020-Jun-05) PDFs | OK |
| cgjonline.ca Rockwood & Theou 2020 (CFS v2.0 text + licence) | OK (viewer page, then /article/download/463/577 PDF) |
| cmaj.ca/content/173/5/489 | **BLOCKED** HTTP 403 Cloudflare "Attention Required" page (deleted) |
| europepmc.org/articles/PMC1188185?pdf=render | **BLOCKED** HTTP 403 (deleted) |
| pmc.ncbi.nlm.nih.gov/.../PMC1188185/pdf/...pdf | **BLOCKED** proof-of-work "Preparing to download" page (deleted; not bypassed) |
| mocacognition.com / paper / faq / permission / training-certification / reference / terms-of-use / digitaltools | OK (8 pages) |
| mini-cog.com | **BLOCKED** HTTP 403 (not retried/bypassed) |
| sfhp.org Standardized_MiniCog.pdf (third-party host copy, v. 01.19.16, S. Borson) | OK, provenance = third-party reprint |
| buffalo.edu Mini_Cog.pdf | fetched, not needed, deleted |
| diabetesdistress.org | **BLOCKED/timeout** (curl error 28 after 60 s, twice) |
| annfammed.org/content/6/3/246.full | OK (DDS2 full text + DDS17 + DDS2 appendices) |
| diabetes-psychologie.de Beschreibung_DDS.pdf (German instrument description) | OK, secondary |
| diabetes.ca DDS page | 404 (deleted) ; Bristol PAID/DDS compilation PDF 404 (deleted) |
| ndss.com.au PAID page ; ndss.com.au HFS-II PDF | OK |
| vumc.com PAID-1-5 PDF (Snoek-group instructions) | OK |
| pmc.ncbi.nlm.nih.gov PMC4084863 / PMC4515112 html (for Table 2 / Appendix) | OK |
| WebSearch (standard) x5: WHO-5 code; PAID scoring; Mini-Cog scoring; DDS licence; HFS-II licence | used only to find URLs; no statement taken from the search summaries |

## NOT done / not found
- DDS-17/DDS-2 licence terms: no official page reachable (diabetesdistress.org timeout). German secondary says "frei verfuegbar - auf Nachfrage bei den Autoren".
- PAID licence/owner terms: NOT_FOUND (only Joslin-related instructions via VUmc doc with no licence text).
- HFS-II scoring in Gonder-Frederick 2011 text: response scale/formula not stated in PMC3064031 (only in Singapore paper PMC5530240).
- Rockwood 2005 7-point descriptors: BLOCKED (abstract only).
- FRAIL scale in Abellan van Kan 2008: not defined there (local text).
