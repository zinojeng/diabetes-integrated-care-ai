# Search log — psychosocial

日期：2026-11-11（Asia/Taipei）。所有 PubMed 檢索使用 NCBI E-utilities（`esearch`＋`esummary`／`efetch`，User-Agent 為研究工具識別字串，無瀏覽器偽裝）。命中數為當日 PubMed `esearchresult.count`，不是系統性去重後的總數。

## 工具狀態

| 工具 | 狀態 | 實際輸出 |
| --- | --- | --- |
| `mcp__paper-search__search_pubmed` | 可用但回傳過大；`max_results=5` 時整頁摘要全文倒入 context；且部分精確查詢回傳 `{"result":[]}`（例如 `INDEPENDENT trial integrated care ... JAMA 2020` 與 `diabetes distress consensus EASD ADA 2026`）。改用自製 E-utilities 小腳本（腳本在 session scratchpad，未提交）| 見下 |
| NCBI E-utilities `esearch/esummary/efetch` | 可用 | 見下 |
| `scripts/fulltext_tools.py pmc` | 可用；30 個唯一 PMCID 取得全文本體（receipt 共 43 筆，含重複抓取）、9 筆回 `ABSTRACT_ONLY`（PMC 非 OA 子集：INDEPENDENT、ADA ch.5、T1-REDEEM、Chew Cochrane、Winkley HTA、Levis PHQ-2、Kroenke PHQ-9、Fisher DDS-2、White PRIDE）| 見下 |
| `mcp__paper-search__download_with_fallback`（`use_scihub=false`）| **失敗**：`source=pubmed` → "PubMed does not provide direct PDF downloads"；`source=pmc` → `403 Client Error: Forbidden for url: https://pmc.ncbi.nlm.nih.gov:443/articles/PMC7435347/pdf/`；`source=europepmc` → "Could not retrieve details for Europe PMC paper PMC12690188"；Unpaywall 皆 "no OA URL found (or ...UNPAYWALL_EMAIL missing)"。**未使用 Sci-Hub**。| blocked |
| Europe PMC `fullTextXML` REST | **blocked**：對 PMC7435347 等 8 個 `ABSTRACT_ONLY` PMCID 皆 HTTP 500；`search?query=EXT_ID:...` 顯示這些文章 `isOpenAccess=N`（INDEPENDENT、ADA ch.5、T1-REDEEM、Chew、Levis PHQ-2、Kroenke、Fisher DDS2）| blocked（OA 授權限制）|
| PMC OA web service `oa.fcgi` | blocked：404（非 OA 子集）| blocked |
| 內建瀏覽器（Claude Browser）讀 `pmc.ncbi.nlm.nih.gov/articles/PMCxxxx/` 的頁面文字 | 可用（一般瀏覽，未繞過驗證）：INDEPENDENT（60,161 字元）、ADA ch.5（200,505 字元）已存為 `literature/parsed/psychosocial/*_browser.md`；receipt 已記錄 | OK |
| 內建瀏覽器讀 PDF（UConn 轉載 WHO-5 表單）| 無法擷取文字 → 改用 `curl` 下載該公開 PDF 並以 `pdftotext` 轉文字 | OK（curl 200，48,381 bytes）|
| `mcp__tavily__tavily_extract`（psykiatri-regionh.dk WHO-5 頁面）| 回傳空結果（"Detailed Results:" 無內容）| blocked |
| `WebSearch`（standard）| 2 次：「PRIDE trial diabetes distress ...」、「WHO-5 ... scoring missing item ...」；僅用於定位，不作為事實來源 | OK |
| LlamaParse | 未使用（無需解析的本地 PDF；WHO-5 單頁表單以 pdftotext 即可）| n/a |
| OpenEvidence／Google Scholar／Consensus | 未使用 | n/a |

## PubMed 檢索式與命中（皆 2026-11-11）

| # | 檢索式（摘要）| 命中 | 採用 |
| --- | --- | --- | --- |
| 1 | `INDEPENDENT[tiab] AND diabetes[tiab] AND depression[tiab] AND JAMA[ta]` | 4 | 32809002（INDEPENDENT）；其餘排除（非主題）|
| 2 | `Ali MK[au] AND integrated care[tiab] AND depression[tiab] AND diabetes[tiab] AND India` | 4 | 34883269（GAD-7 亞組）；Halliday 2024、Johnson 2020、Rao 2016 為 INDEPENDENT 周邊，未納入 |
| 3 | `Katon[au] AND collaborative care AND depression AND chronic illness AND diabetes AND N Engl J Med[ta]` | 1 | 21190455（TEAMcare NEJM）|
| 4 | `T1-REDEEM OR (type 1 diabetes distress randomized Fisher Hessler)` | 11 | 29976567（T1-REDEEM）；EMBARK 2024（38809903）、Shumway 2019（成本）未納入，列為後續 |
| 5 | `REDEEM diabetes distress randomized trial type 2 diabetes Fisher` | 1 | 23735726（REDEEM）|
| 6 | `PRIDE diabetes distress intervention randomized` | **0** | — |
| 7 | `Partnership to Improve Diabetes Education PRIDE cluster randomized` | 1 | 31919724（White 2020；非 DD 試驗）|
| 8 | `Facilitating Positive Health Behaviors and Well-being ... Standards of Care in Diabetes` | 17 | 41358898（2026 ch.5）；2025 版（39651983）與 erratum 未用 |
| 9 | `Standards of Care in Diabetes 2026 Psychosocial Care` | 69 | 42744915（EASD DD guideline）；其餘多為無關結果 |
| 10 | `diabetes distress meta-analysis randomized psychological interventions type 2 diabetes` | 20 | 39379853、32568666、28954185；Fernández-Rodríguez 2024（eHealth）、Yap 2024（technology）、Oyedeji 2022（non-specialist）列為後續 |
| 11 | `diabetes distress prevalence meta-analysis type 2 diabetes` | 24 | 39892818、37956943；Sinha 2024（印度）、Feleke 2025（非洲）未納入 |
| 12 | `depression diabetes prevalence meta-analysis Taiwan` | 16 | 無相關（回傳 GBD 等）|
| 13 | `collaborative care comorbid depression diabetes systematic review meta-analysis HbA1c Atlantis` | 1 | 24727428 |
| 14 | `collaborative care depression diabetes meta-analysis randomized` | 29 | 無糖尿病專屬新增（Schillok 2025 IPD 為一般憂鬱）|
| 15 | `depression diabetes mortality complications meta-analysis cohort` | 6 | 無相關；改以 #16 |
| 16 | `diabetes distress mortality cohort` | 295（取前 5）| 32949245、34285589 |
| 17 | `diabetes distress glycemic control cross-sectional not depression Fisher 2010` | 219（取前 4）| 未納入（Fisher 2010 未被檢索命中）|
| 18 | `fear of hypoglycemia prevalence type 2 diabetes systematic review` | 4 | 31271669、34596292；**無 FoH pooled prevalence** |
| 19 | `sleep disturbance insomnia type 2 diabetes prevalence meta-analysis` | 5 | 31603475 |
| 20 | `cognitive impairment dementia type 2 diabetes meta-analysis risk` | 36 | 33417039 |
| 21 | `disordered eating diabetes prevalence meta-analysis` | 8 | 38597269 |
| 22 | `treatment burden diabetes questionnaire validation type 2` | 148 | 36919103；42726276（Schipper 2026）|
| 23 | `social determinants of health diabetes scientific review Hill-Briggs` | 5 | 33139407 |
| 24 | `food insecurity type 2 diabetes HbA1c meta-analysis` | 2 | 34726354 |
| 25 | `chatbot conversational agent diabetes randomized trial` | 5 | 39626235 |
| 26 | `conversational agent depression anxiety randomized controlled trial meta-analysis` | 3 | 37115595 |
| 27 | `generative AI chatbot Therabot randomized trial depression` | 20 | 42932588（abstract）、41401240（另一檢索命中）|
| 28 | `large language model PHQ-9 depression screening accuracy` | 10 | 41028413（糖尿病 secure messages）；Shin 2024、Jin 2026 未納入 |
| 29 | `natural language processing electronic health records depression diabetes identify` | 7 | 無可用 |
| 30 | `Taiwan diabetes distress prevalence type 2 diabetes` | 12 | 40351707 |
| 31 | `Taiwanese Diabetes Distress Scale OR "diabetes distress" Taiwan` | 24 | 35372236、36497755 |
| 32 | `Taiwan diabetes depression prevalence nationwide`（pub_date）| 79 | 39029051（Ni 2024）|
| 33 | `Taiwan type 2 diabetes depression anxiety PHQ-9 cross-sectional outpatient clinic` | **0** | — |
| 34 | `Taiwan diabetes distress PAID Chinese version validation` | 2 | 19808922（PAID-C）|
| 35 | `Liu SI Validation of Patient Health Questionnaire ... Taiwan` | 3 | 21111406 |
| 36 | `Chinese version Diabetes Distress Scale validation DDS-17 type 2` | **0** | — |
| 37 | `Generalized Anxiety Disorder-7 Taiwan OR "traditional Chinese" validation` | 26,258（查詢過寬）| 無（回傳無關）→ GAD-7 台灣驗證 UNRESOLVED |
| 38 | `WHO-5 ... Taiwan OR Taiwanese version validation`／`... traditional Chinese OR Taiwan OR Hong Kong` | 352／377,604（OR 查詢過寬）| 38031007（Du 2023 大陸）；Chan 2022（香港醫學教育者，非糖尿病）未納入 |
| 39 | `Hypoglycemia Fear Survey Chinese version validation` | 1 | 32210481（大陸）；台灣／繁中版未找到 |
| 40 | `Hypoglycemia Fear Survey II psychometric Gonder-Frederick` | 2 | 21346182 |
| 41 | `Diabetes Eating Problem Survey-Revised Chinese OR mSCOFF Chinese` | 3 | 37259043（香港繁中）|
| 42 | `hypoglycemia fear Taiwan insulin type 2 diabetes` | 3 | 32003099（DISCOVER；非台灣專屬）|
| 43 | 量表起源（PAID 1995／1997、DDS 2005、DDS-2 2008、PAID-5 2010、PHQ-9 2001、GAD-7 2006、WHO-5 Topp 2015）| 各 1–6 | 7555499、9135939、15735199、18474888、19841892、11556941、16717171（未取內容）、25831962 |
| 44 | `Hajos WHO-5` 等（WHO-5 diabetes screening）| 13 | 23072401 |
| 45 | PHQ-2／PHQ-9 diagnostic accuracy meta-analysis | 65（取前 4）| 30967483、32515813 |

## 納入／排除原則

- 納入：指引、RCT、系統性回顧／meta-analysis、量表原始或正式驗證、有代表性的台灣資料。
- 排除：非糖尿病族群且與 AI／心理 chatbot 無關者；兒少為主者（僅在 T1D 標註時引用）；重複文章；與問題無關的檢索噪音（例如 GBD、OSA 指引）。
- 偏誤與缺口：英文檢索為主、未檢索中文資料庫（airiti／CNKI），因此台灣資料可能被低估；系統性去重與雙人篩選未做。
- 失敗查詢仍保留於表中（#6、#33、#36、#37、#38）。

## 全文驗證紀錄

- `python3 scripts/fulltext_tools.py verify` 對 INDEPENDENT 瀏覽器版 PASS（title／author／year）。其餘由 PMC XML 轉出者其標題與 PMCID 來自 API 本身，未另做污染檢查；瀏覽器版 ADA ch.5 開頭即為 recommendations 5.1…，與標題一致。
- 78 項關鍵斷言由自訂 `verify.py`（session scratchpad，未提交）逐字比對本地全文：77 通過、1 項字串寫法問題（Zhang 2025 `ES=0.30, P=.047` → 原文為 `effect size [ES]=0.30`），已按原文引用。
- Receipts：`literature/receipts/psychosocial.jsonl`（PMC API 抓取由 `fulltext_tools.py` 自動寫入，其中 `PMC7435347`、`PMC12690188` 的 `has_body:false` 紀錄已被瀏覽器版本取代；瀏覽器頁面與 curl PDF 各有一筆手動紀錄，含 sha256）。

## 第二階段補充（crosscheck）

- PubMed（E-utilities）：`(diabetes[ti]) AND (chatbot OR conversational agent OR LLM OR AI[ti]) AND (distress OR depress*) AND RCT[pt]` → 1（Nayak 2023）；`...virtual agent OR digital coach OR AI-based ... distress[ti] OR depress*[ti] OR emotional[ti] OR psychological[ti]` → 2（Bruijnes 2023、Kostiuk 2025 計畫書）；`diabetes distress app randomized ... primary outcome Diabetes Distress Scale` → 0；`"diabetes distress" AND (AI OR ML OR chatbot OR generative)` → 436（取前 10，另得 Ho 2026）；`PAID cut-off score 40 ...` → 1（de Wit 2022）；`PAID-5 cut-off 8 ...` → 1（Schmidt 2018，未讀）；`WHO-5 cut-off 13 raw score ...` → 0。
- 內建瀏覽器讀 PMC 頁面：PMC3312811（TEAMcare 表格）、PMC6483710（Chew，全文 400,459 字元，輸出被工具截在 400,000 字元處）、PMC6105321（T1-REDEEM，僅以 JS 取 HbA1c／DD 段落）。
- **`mcp__scihub__download_pdf`：未執行**（見 crosscheck.md Q4）。Winkley、Perrin、Levis PHQ-2 本輪未再取。
- receipts 檢查：43 筆 pmc 紀錄 `id==pmcid`，全部檔案標題與預期相符，無 PMID→PMCID 污染。
