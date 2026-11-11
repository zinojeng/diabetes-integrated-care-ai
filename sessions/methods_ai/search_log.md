# methods_ai 檢索紀錄

日期：2026-11-11（Asia/Taipei）。執行者：methods_ai session（Claude）。命中數為 PubMed E-utilities `esearch` 的 `count`。

## 1. 工具與可用性

| 工具 | 結果 |
| --- | --- |
| `scripts/fulltext_tools.py pmc` | 可用。PMC 開放全文轉 Markdown；`literature/parsed/methods_ai/` 目前共 25 個檔（含 Dundee PDF 與 DIASENTINEL PDF 的 `pdftotext` 輸出，3 個 abstract-only）。 |
| `scripts/fulltext_tools.py verify` | 22 份 `PASS`（title／author／year；其中 O'Connor 為 abstract-only），0 份 `POLLUTED_OR_MISMATCH`。未 verify：3 個 abstract-only／轉載檔（PMC10103205、PMC12690177、PMC12365671）。 |
| `mcp__paper-search__search_pubmed` | **第一輪三個查詢平行呼叫時 2/3 回 `not well-formed (invalid token)`**（同時呼叫造成），單獨呼叫可用。之後改以 PubMed E-utilities（`esearch`＋`esummary`，官方 API）輔助，輸出只留 PMID/PMCID/DOI/title。 |
| Europe PMC REST（自寫輔助） | **HTTP 503**，三個查詢皆失敗，未再重試。 |
| `mcp__paper-search__download_with_fallback`（PMC10103205，`use_scihub=false`） | 失敗：`403 Client Error: Forbidden`（PMC PDF），Unpaywall 無 OA URL（未設 email）。未改走 Sci-Hub（2023 論文）。 |
| 直接 `curl`（誠實 UA `dmic-research-fulltext-tool/1.0`） | `chimei`、`nhri`、`aclanthology`（頁面與 PDF）、`openclaw`、`hermes`、Dundee 機構典藏 PDF 為 HTTP 200；**`nhi.gov.tw`、`wwwv.tsgh.ndmutsgh.edu.tw`、`diabetesjournals.org` 為 HTTP 403**，未偽裝 UA、未嘗試繞過。 |
| `mcp__tavily__tavily_extract`（nhi、tsgh 兩個 URL） | 回空結果（`Detailed Results:` 後無內容）。 |
| `WebSearch` | 可用；僅作 📌 層級（搜尋摘要，不當全文）。 |
| `fulltext_tools.py pmc 21482743`（PMID 輸入） | **工具缺陷**：該 PMID 不在 PMC，卻寫出 `PMC13746208.md`（內容為不相干的 Testican-2 論文）。已刪除檔案；`literature/receipts/methods_ai.jsonl` 內仍有該筆 receipt，請 lead 清除或忽略。ID 解析在 PMID 不在 PMC 時會誤配，建議工具修正。 |
| `mcp__openevidence__*` | 未使用（本輪以原文為主）。 |
| LlamaParse | 未使用（所需文獻皆有 PMC XML 或可直接 `pdftotext`）。 |

## 2. 檢索式

| # | 來源 | 查詢式 | 命中 | 用途／結果 |
| --- | --- | --- | ---: | --- |
| 1 | paper-search PubMed | `retrieval-augmented generation large language model continuous glucose monitoring` | 2 | 取得 Guo 2026（PMID 42544991）、GlyRAG（42804391，僅 abstract，未納入） |
| 2 | PubMed E-utilities | `kidney failure risk equation[ti] AND (diabetes OR validation OR calibration)` | 58 | Grams 2023、Walker 2026 等 |
| 3 | PubMed E-utilities | `ambient AI scribe randomized clinical trial` | 6 | Lukac NEJM AI（41497288）；其餘不納入（非糖尿病、非主要 RCT 或 medRxiv 版本重複） |
| 4 | PubMed E-utilities | `large language model diabetes randomized OR "patient education" accuracy` | 2,494 | 太寬，只看前 8；無糖尿病專屬 RCT，未納入 |
| 5 | PubMed E-utilities | `TRIPOD+AI statement reporting guideline prediction models artificial intelligence` | 5 | Collins 2024／Ewha 轉載（韓文）；採 BMJ PMC11019967 |
| 6 | PubMed E-utilities | `PROBAST+AI tool risk of bias applicability prediction model AI` | 37 | Moons 2025（40127903） |
| 7 | PubMed E-utilities | `large language model retrieval-augmented type 2 diabetes outpatient treatment recommendation fine-tuned` | 0 | 零命中（詞太長），改以 DOI 查詢 |
| 8 | PubMed E-utilities | `10.2196/71541[doi]` | 2 | He 2026（41662664）；另一筆無關（Appl Opt 1969，DOI 欄誤配，略） |
| 9 | PubMed E-utilities | `LLM clinical decision support primary care Kenya randomized treatment failure` | 1 | Agweyu Nat Med 2026（42362867） |
| 10 | PubMed E-utilities | `GPT-4 type 2 diabetes complex cases clinical notes` | 0 | 零命中；該文已由 handoff PMID 41140742 直接取得 |
| 11 | PubMed E-utilities | `machine learning prediction diabetic complications external validation calibration decision curve` | 57 | 篩出 SR（見 #14） |
| 12 | PubMed E-utilities | `Tangri kidney failure risk prediction ... JAMA 2016` / `... JAMA 2011` | 1 / 1 | Tangri 2016（26757465 → PMC4752167）；2011 原始 derivation（21482743）不在 PMC，**未取得全文** |
| 13 | PubMed E-utilities | `diabetes retinopathy artificial intelligence screening randomized trial primary care` | 13 | ACCESS、DRES-POCAI protocol（41118165）、Tanzania RCT（42863478，**NO_PMC，未取得全文**）、Wu 2025 eyecare foundation model（40877476，僅 metadata，未納入） |
| 14 | PubMed E-utilities | `systematic review prediction models diabetes complications machine learning PROBAST risk of bias external validation` | 8 | 納入 Li 2025 (DKD)、Huang 2025 (DR)、Ma 2025 (DPN) |
| 15 | PubMed E-utilities | `machine learning versus conventional risk score cardiovascular diabetes SCORE2-Diabetes OR UKPDS external validation calibration` | 12 | 納入 Su 2024（Taiwan 校準）；其餘為 UKPDS 外部驗證，未讀 |
| 16 | PubMed E-utilities | `machine learning kidney failure prediction type 2 diabetes compared with kidney failure risk equation external validation` | 0 | 零命中；ML 對 KFRE 的直接比較**本輪未找到** |
| 17 | PubMed E-utilities | `fairness algorithmic bias diabetic retinopathy AI subgroup performance skin pigmentation` | 0 | 零命中；公平性證據缺口（見 report §7） |
| 18 | PubMed E-utilities | `alert fatigue clinical decision support override diabetes` | 0 | 零命中；alert fatigue 的糖尿病專屬證據**本輪未找到** |
| 19 | PubMed E-utilities | `Standards of Care in Diabetes-2026 retinopathy neuropathy foot care` | 1 | ADA S12（41358886）；PMC12690177 僅 abstract |
| 20 | PubMed E-utilities | `CGM decision support artificial intelligence randomized HbA1c time in range insulin titration`、`type 2 diabetes AI-driven insulin titration decision support randomized` | 0 / 0 | 零命中（檢索式過窄）；iNCDSS 由 handoff 提供 PMID |
| 21 | WebSearch（standard） | NHIA diabetes risk assessment smart health education pilot | — | 見 §4（📌） |
| 22 | WebSearch（standard） | 三軍總醫院 MEDIC GenAI 平台 上線 2026 | — | **無法佐證**公告（UNRESOLVED） |
| 23 | WebSearch（standard） | Grams 2023 KFRE CKD-EPI 2021 recalibrated coefficients | — | 只得摘要層級；轉用 Dundee 典藏 PDF |

**限制**：未做系統性檢索（單一資料庫為主、無雙人篩選、無完整 PRISMA）。本報告是針對指定問題的定向證據綜整，不是 systematic review。
2026 年文獻（Agweyu、He、Guo、Coristine、Walker、DIASENTINEL）超出模型訓練知識，所有資訊僅來自本輪取得的全文。

## 3. 納入全文清單（已 `verify` PASS 並 grep 驗證）

PMC10784572（ACCESS）、PMC6550188（pivotal）、PMC10692866（voice）、PMC12059970（iNCDSS）、PMC12547058（GPT-4）、PMC12768499（scribe）、PMC13472850（Kenya）、PMC12885450（He）、PMC13430954（Guo）、PMC13022550（TMU 護理）、PMC4752167（Tangri 2016）、PMC13403277（Walker）、Grams2023_KFRE_AAM（Dundee 典藏 PDF，作者接受稿）、PMC11019967（TRIPOD+AI）、PMC11931409（PROBAST+AI）、PMC11911190／PMC12291684／PMC12481961（三篇 ML 預測 SR）、PMC11465834（Su Taiwan）、DIASENTINEL_EMNLP2026（ACL 開放 PDF）、PMC12541539（DRES-POCAI protocol）。共 21 份全文 PASS（另加 O'Connor abstract-only 共 22 份 PASS），其中 19 份用於具體數字斷言。
Abstract-only：PMC3022040（O'Connor 2011）、PMC10103205（Grams 2023 的 PMC 版）、PMC12690177（ADA S12）。
額外：PMC12365671（TRIPOD+AI 韓文轉載，未用）。

可重現核對：`python3 -I literature/notes/methods_ai/claim_checks.py`（輸出見 `claim_checks_output.txt`，0 MISS）。

## 4. 排除與未完成

| 項目 | 原因 |
| --- | --- |
| Tanzania DR AI RCT（PMID 42863478，Lancet Glob Health 2026） | NO_PMC；未取得全文，僅知存在，未做任何數字斷言。 |
| Tangri 2011 JAMA（21482743） | 不在 PMC；原始 derivation 係數無法由本地全文驗證。 |
| Grams 2023 JASN 期刊版 | PMC 版 abstract-only；改讀作者接受稿。 |
| 健保署智慧衛教頁（nhi.gov.tw） | HTTP 403 且 Tavily 回空；僅有搜尋摘要（📌）。 |
| 三總 MEDIC 公告 | HTTP 403 且搜尋無佐證；UNRESOLVED。 |
| 國衛院計畫期間 | 機構典藏頁文字僅見 `Date: 2025`、計畫編號 NSTC114-2314-B400-014；GRB 頁為動態頁，期間未能確認。 |
| ADA S12 AI 敘述 | `diabetesjournals.org` 403；PMC 僅 abstract。 |
| GlyRAG、Wu 2025 eyecare foundation model | 僅 metadata，未納入。 |
