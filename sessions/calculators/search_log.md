# calculators — search_log（2026-11-11）

> 本檔記錄 calculators session 主線程的檢索。三個 subagent 的詳細 log 在 `literature/notes/calculators/agentA_search_log.md`、`agentB_search_log.md`、`agentC_search_log.md`（彙整見下方「Subagent 摘要」）。

## 1. 主線程：PMC E-utilities 批次（`scripts/fulltext_tools.py pmc <PMID>`）

| 查詢（PMID） | 結果 | 處置 |
| --- | --- | --- |
| 18197741 (DCSI) | `PMC3810070` ABSTRACT_ONLY | no_fulltext（不在 PMC 開放子集） |
| 23198714 (aDCSI) | elink 回傳 `PMC13671262`（Arkansas DSMES，**不相關**） | **POLLUTED_OR_MISMATCH → 已刪除**；idconv 查無 PMC |
| 3558716 (Charlson 1987) | elink 回傳 `PMC13746622`（結腸切除，不相關） | 已刪除；無 PMC |
| 21330339 (Quan 2011) | elink 回傳 `PMC13741072`（機器人前列腺切除，不相關） | 已刪除；無 PMC |
| 16224307 (Quan 2005) | `PMC13746842`（Veterans drug shortage，不相關） | 已刪除；ABSTRACT_ONLY |
| 34554658 (CKD-EPI 2021) | `PMC8822996` OK | 本地全文；主文**不含**公式常數（在 supplement/官方頁） |
| 26757465 (KFRE 2016) | `PMC4752167` OK | 本地全文；eAppendix 為 NIHMS docx，PMC 下載受 proof-of-work 擋 → blocked |
| 21482743 (Tangri 2011) | `PMC13746208`（Testican-2，不相關） | 已刪除 |
| 16729309 (Sterling FIB-4) | `PMC13746124`（肝切除回顧，不相關） | 已刪除；無 PMC |
| 12883497 (Wai APRI) | 同上 `PMC13746124` | 已刪除；無 PMC |
| 37947085 (PREVENT) | `PMC10910659` OK | 本地全文；係數在 Supplemental Tables .xlsx（blocked） |
| 37247330 (SCORE2-Diabetes) | `PMC10361012` OK | 本地全文；補充為 OA（Europe PMC 補充檔 API 回 HTTP 500/逾時，見 agentC） |
| 28803840 (RECODe) | `PMC5769867` OK | 本地全文；係數在 NIHMS appendix pdf（blocked） |
| 31519694 (WATCH-DM) | `PMC7364669` ABSTRACT_ONLY | no_fulltext |
| 11556941 (PHQ-9) | `PMC1495268` ABSTRACT_ONLY | no_fulltext |
| 16717171 (GAD-7) | elink 回傳 `PMC13746654`（不相關） | 已刪除；無 PMC |
| 15735199 (DDS) | elink 回傳 `PMC13745953`（不相關） | 已刪除；無 PMC |
| 7555499 (PAID 1995) | elink 回傳 `PMC13733556`（不相關） | 已刪除；無 PMC |
| 22228744 (Fisher 2012 DDS cut-off) | `PMC3263871` OK | 本地全文 |

**重要缺陷（給 lead）**：`scripts/fulltext_tools.py pmc <PMID>` 用 `elink dbfrom=pubmed&db=pmc` 並取 `linksetdbs[0].links[0]`，該集合可能是「被引用／相關文章」而非該文本身，導致上列 9 個**不相關**的 PMC 檔被寫入 `literature/parsed/calculators/` 與 `literature/receipts/calculators.jsonl`（receipt 已含錯誤 pmcid，檔案我已刪除）。建議改用 `linkname=pubmed_pmc` 並驗證回傳標題，或改用 idconv。傳入**精確 PMCID** 即可避開。

## 2. 主線程：其他來源

| 來源 | 動作 | 結果 |
| --- | --- | --- |
| jamanetwork.com/journals/jama/fullarticle/2481005（JAMA 2016 KFRE） | curl（誠實 UA）與內建瀏覽器 | **HTTP 403**（bot 檢查），未繞過 → blocked；eAppendix 2 p9 無法由本 session 直接開啟 |
| `pmc.ncbi.nlm.nih.gov/articles/instance/4752167/bin/NIHMS756538-supplement-appendix.docx` | curl | 回傳 proof-of-work 頁面「Preparing to download…」→ blocked，**未繞過** |
| Europe PMC `…/PMC4752167/supplementaryFiles` 與 `PMC10910659` | REST | 「Article … is not open access one」→ 無補充檔 |
| Europe PMC `…/PMC10361012/supplementaryFiles`（SCORE2-Diabetes OA） | REST，逾時 | HTTP 500（見 agentC 後續） |
| `mcp__paper-search__download_with_fallback`（pmc, use_scihub=false）：PMC3810070、PMC7364669、PMC1495268、PMC5624849 | 4 次 | 全部 `403 Client Error: Forbidden …/pdf/`；unpaywall 無 OA URL → no_fulltext |
| Europe PMC 全文檢索 `"0.2201" AND "0.5567" AND kidney` + OPEN_ACCESS | REST | 命中 4 篇；其中 `PMC11813909`（Bundó-Luque 2024）、`PMC7203563`（Tangri/Lam 2020 AKI-KFRE）、`PMC6894117`（Wang 2019 SEA）已抓取；`PMC6855090` 與 KFRE 無關未使用 |
| Europe PMC 全文檢索 `"0.8996"/"0.9832"/"0.9751"` | REST | 無相關結果（小數點分詞不佳）；NA S0 無法本地驗證 |
| NIDDK 成人 GFR equations 官方頁 | curl 200 → `literature/fulltext/calculators/official/niddk_gfr_adults.txt` | 取得 CKD-EPI 2021 cr 與 cr-cys 全部常數 |

**Sci-Hub**：協議允許作 2021 年前論文最後備援，本 session **未使用**（版權與來源風險；交由 lead 決定是否授權）。

## 3. Subagent 摘要（皆於本 session 內以 Agent 工具啟動；詳細 log 見 `literature/notes/calculators/agent{A,B,C}_search_log.md`）

| Agent | 範圍 | 結果摘要 | 失敗／blocked（實際輸出） |
| --- | --- | --- | --- |
| A（comorbidity／事件模型） | DCSI、Charlson、WATCH-DM、RECODe、Karter、UKPDS、ADVANCE、台灣模型、TIMI | Charlson 權重（original／Quan，二手 3 處）；RECODe 係數（JATS XML 取表）；UKPDS RE 方程（Yang 2013 Appendix）；TIMI 全文；台灣 ESRD／CKD 點數表 | DCSI：Europe PMC fullTextXML HTTP 500、PMC PDF 403（Cloudflare）；Karter PDF 403；Oxford DTU 頁 403；ADVANCE 影像 URL 403/404；Chang 2012、Glasheen、Wicke、Kengne、Hayes 皆 OA=N；刪除 19 篇不相關下載 |
| B（量表） | PHQ/GAD、DDS、PAID、WHO-5、HFS-II、Mini-Cog、MoCA、CFS、FRAIL | 官方 PHQ/GAD 手冊、NDSS PAID、WHO 2024 WHO-5、Dalhousie CFS v2.0、MoCA FAQ、Mini-Cog 轉載表、Morley FRAIL | cmaj.ca 403、Europe PMC／PMC PDF 403／proof-of-work、karger.com 403、diabetesjournals.org 403、mini-cog.com 403；diabetesdistress.org 逾時（兩次） |
| C（器官／分層） | PREVENT、SCORE2-Diabetes、CKD-EPI、KDIGO、FIB-4/APRI、IWGDF、台灣工具 | SCORE2-D OA 補充檔（含官方 Excel）；KDIGO 2024 PDF；IWGDF 2023 PDF；FIB-4/APRI 公式（二手） | professional.heart.org（PREVENT FAQ 與 calculator 頁）403；ADA Standards 2026 S4 403；NCBI 補充檔 proof-of-work（未繞過）；Europe PMC 補充檔 API 第一次 HTTP 500／逾時，後續成功 |

主線程對 subagent 回報的**獨立核對**（grep 實檔）：SCORE2-D 係數與 Excel（符合）；KDIGO 熱圖目視（符合）；IWGDF Table 1（符合）；TIMI 變數表與 Table 3（符合）；Quan renal 權重（兩處 1、一處 4）；**Agent C 稱 AASLD 2023 印有 2.67，我在 `PMC10735173.md` grep 不到（只在 `PMC13706892.md` L75 找到）→ 未採信**；UKPDS XML 確認 `(1 − dt)` 上標遺失。

## 4. 本地全文檢索方式
`python3 scripts/fulltext_tools.py grep calculators '<pattern>'`；本 session 另在 `literature/parsed/calculators/*_tables.md` 以 grep 驗證表格內容（`jats_to_md` 會丟失部分 table-wrap）。官方文件在 `literature/fulltext/calculators/official/`（git-ignored）。
