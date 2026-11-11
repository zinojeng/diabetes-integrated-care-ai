# complications search log（2026-11-11，Asia/Taipei）

工具：PubMed E-utilities（`esearch`/`esummary`/`efetch`，stdlib 腳本，位於 session scratchpad，未入 repo）、`scripts/fulltext_tools.py pmc`、`mcp__paper-search__download_with_fallback`、`mcp__paper-search__search_pubmed`（1 次，輸出為含完整 abstract 的長 JSON，之後改用精簡 esummary 腳本以節省 context）。
所有 count 為 PubMed 當下命中數（未去重、未人工二次篩選）。納入＝列入 `evidence_table.csv`；「候選未納」＝看過標題／摘要但與成人 T2D 整合照護主題不符。

## A. 錨定試驗（以 PMID 直接核對）

| 檢索 | 來源 | 命中 | 結果 |
| --- | --- | --- | --- |
| `12556541[uid] OR 18256393[uid] OR 27531506[uid] OR 21705063[uid] OR 31748169[uid] OR 29079252[uid] OR 27398874[uid] OR 38829880[uid] OR 33929522[uid] OR 35333363[uid] OR 27399144[uid] OR 32049836[uid] OR 21190455[uid] OR 32809002[uid]` | PubMed esummary | 14/14 | 全部解析；取得 DOI／PMCID／標題（供全文配對與防污染） |
| `38212308[uid] OR 18197741` 與 `Young BA[au] AND DCSI`、`Chang HY[au] AND adapted DCSI` | PubMed | 4 + 2 + 1 | ACCESS（PMC10784572）、Young 2008（PMC3810070）、Chang 2012 aDCSI（23198714，無 PMC，未取全文）。第一個 OR 檢索中 `3810070[uid]` 被誤當 PMID 而命中無關文章（Rogers 1986 等），已排除，改以 `Young BA[au]` 檢索得正確 PMID 18197741 |

## B. 主題檢索

| # | 檢索式（精簡） | 命中 | 納入／備註 |
| --- | --- | --- | --- |
| B1 | `(multidisciplinary OR "integrated care" OR "team-based care" OR "care coordination") AND "type 2 diabetes" AND (systematic review[pt] OR meta-analysis[pt]) AND 2020:2026[dp]` | 96 | 納入 Konnyu 2023 Cochrane QI（37254718）；其餘 SGLT2i／肥胖／基因等為語意偏離，**不納入** |
| B2 | `"clinical inertia" AND type 2 diabetes AND (cohort OR retrospective) AND (Khunti OR treatment intensification)` | 56 | 納入 Paul 2015（26249018）；候選未納：Wan 2020、Suzuki 2023、Kaewbut 2022、Romera 2020、Alvis-Guzman 2024（區域性／次要） |
| B3 | `SGLT2 … underuse … CKD OR HF OR ASCVD prescribing gap`（自由文字） | 385,742 | **失敗：檢索式太寬，回傳為心衰竭綜述**；改用 B7–B9 |
| B4 | `albuminuria testing rates type 2 diabetes UACR screening completion`（自由文字） | 0 | 自由文字被 PubMed 以 AND 全詞比對而 0 命中；改用 `[tiab]` 欄位限定 |
| B5 | `diabetic retinopathy screening adherence referral completion follow-up after positive screen`（自由文字） | 0 | 同上（自由文字全詞 AND 0 命中）；改用 B11 |
| B6 | `albuminuria testing[tiab] AND diabetes[tiab] AND (guideline[tiab] OR screening[tiab]) AND (rate[tiab] OR proportion[tiab])` | 13 | 納入 Albekery 2025（41345917）、Chu 2022（36434513）；候選未納：Ferrè 2023 KHE（37680649）、McCormick 2026（澳洲，無 PMC）、Kam 2022 QI |
| B7 | `SGLT2 inhibitors[tiab] AND underutilization[tiab] AND diabetes[tiab] AND kidney[tiab]` | 5 | 納入 Levin-Iaina 2025（41031090）；候選未納：Barrot-de la Puente 2025（CKD 篩檢描述）、Taylor 2025（Cureus）、Alhomoud 2025（老年處方型態，未讀） |
| B8 | `SGLT2[tiab] AND prescribing[tiab] AND eligible[tiab] AND type 2 diabetes[tiab] AND heart failure[tiab]` | 13 | 候選：Bermudez 2023（HF，非 T2D 專屬）、Young 2023（UK 指引適應症，未讀）、Raat 2025（Belgium，無 PMC）。**HF 專屬缺口未補** |
| B9 | `SGLT2 inhibitor[tiab] AND prescription[tiab] AND … AND chronic kidney disease[tiab] … AND (eligible OR indication)` | 3 | 納入 Gregg 2023（36702340）、Stefanska 2026（42723263） |
| B10 | `GLP-1 receptor agonist[tiab] AND SGLT2[tiab] AND atherosclerotic cardiovascular disease[tiab] AND … (use[ti] OR utilization[ti] OR prescribing[ti])` | 3 | 納入 Bolden 2025（40275941）；Lim 2023（36582120，無 PMC，未納） |
| B11 | `diabetic retinopathy[tiab] AND screening[tiab] AND adherence[tiab] AND systematic review[pt]` | 8 | 納入 Fu 2026（42270111）、Rahmati 2024（39094991，abstract-only）；其餘為葡萄牙方案／AI 成本／CONSORT-AI 等，不納 |
| B12 | `multimorbidity[tiab] AND type 2 diabetes[tiab] AND treatment burden[tiab]` | 13 | 納入 Lin 2024（38858619） |
| B13 | `diabetes[tiab] AND multimorbidity[tiab] AND systematic review[pt] AND 2019:2026[dp]` | 64 | 納入 Bolt 2024（39572394）；其餘偏離 |
| B14 | `diabetic foot[tiab] AND multidisciplinary[tiab] AND amputation[tiab] AND meta-analysis[pt]` | 10 | 納入 Blanchette 2020（32192509）、Meloni 2024（38461443，abstract-only） |
| B15 | `diabetes[ti] AND continuity of care[tiab] AND (mortality OR hospitali*) AND systematic review[pt]` | 2 | 納入 Chan 2021（34217212） |
| B16 | `Diabetes Complications Severity Index[tiab] AND Charlson[tiab] AND (validation OR performance OR comparison)` | 2 | 納入 Hu 2023（36977521）；Liao 2021 不相關 |
| B17 | `multimorbidity index[tiab] AND type 2 diabetes[tiab] AND (comparison OR validation OR systematic review)` | 1 | Igland 2024 Rx-risk（38548358）：已取得 metadata，**未讀、未納** |
| B18 | `Standards of Care in Diabetes 2026[ti] AND comprehensive medical evaluation[tiab]` | 1 | ADA 2026 Sec.4（41358897）；PMC 僅 abstract → `UNRESOLVED` |
| B19 | `cardiovascular-kidney-metabolic syndrome[tiab] AND type 2 diabetes[tiab] AND (prevalence OR NHANES)` | 17 | 命中皆為綜述／非 T2D 專屬；改走 B21 |
| B20 | `type 2 diabetes[ti] AND multimorbidity[ti] AND prevalence[tiab] AND systematic review[pt]` | 1 | 納入 Ferede 2025（41382017） |
| B21 | `Taiwan[tiab] AND diabetes[tiab] AND (shared care OR multidisciplinary OR integrated care) AND (end-stage OR dialysis OR kidney)` | 25 | 納入 Tsai 2025（40570007）。**未找到 Taiwan DM 共同照護網 (shared care) 專屬論文** → `UNRESOLVED` |
| B22 | `diabetes[tiab] AND FIB-4[tiab] AND MASLD[tiab] AND (primary care OR screening) AND (referral OR elastography)` | 54 | 納入 Qadri 2024（38334817）；EASL 指引等為指引，未納 |
| B23 | `diabetic peripheral neuropathy[tiab] AND screening[tiab] AND (underdiagnosed OR foot examination) AND primary care[tiab]` | 1 | 不相關（painful DPN 流程），不納；**IWGDF 指引未檢索** |
| B24 | `clinical inertia[ti] AND diabetes[ti] AND (systematic review[pt] OR meta-analysis[pt])` | 1 | 納入 Almigbal 2023（36676805） |
| B25 | `eye examination[tiab] AND diabetes[tiab] AND randomized[tiab] AND (referral completion OR adherence to referral OR follow-up eye)` | 0 | 無命中；成人 T2D「轉介完成」隨機試驗未見 → 報告列為缺口 |
| B26 | `diabetes[ti] AND (health literacy OR social determinants) AND (screening OR guideline-concordant) AND systematic review[pt]` | 5 | 納入 Lee 2020（32720345，PMC 僅 abstract）、Brewster 2020（31968127，abstract-only）；Woodward 2024 自我管理質性 SR 未讀 |

## C. 全文取得

成功（PMC JATS→md，`literature/parsed/complications/`）：PMC3312811、PMC6561084、PMC11198027、PMC8087959、PMC8956973、PMC5058873、PMC7035087（首次 HTTP 429，間隔 2 秒重試後成功）、PMC5506099、PMC3136726、PMC10233616、PMC12781434、PMC13264893、PMC11165743、PMC7083052、PMC13287621、PMC4528846、PMC9700954、PMC12477010、PMC13731052、PMC10293070、PMC12018204、PMC10069524、PMC8254900、PMC12802173、PMC9866102、PMC12200875、PMC11058902、PMC11581819、PMC10784572。
僅 abstract（XML 無本文）：PMC7435347（INDEPENDENT）、PMC12690184（ADA 2026 Sec.4）、PMC3810070（Young 2008 DCSI）、PMC7518886（Lee 2020）。
PubMed efetch abstract：PMID 12556541、18256393、31748169、29079252、32809002、38461443、31968127、39094991（`PMID<id>_abstract.md`，receipt 記 `status: abstract_only`）。

### 失敗與污染事件（原樣保留）

1. **`fulltext_tools.py pmc <PMID>` 解析錯誤：** `12556541`→PMC13738796（實為 2026 年 IRT 建模論文）、`18256393`→PMC13731741（2026 年 "Complication Prevention Beyond Glycaemic Control" 綜述）、`31748169` 與 `29079252` 皆→PMC13693898（2026 年 J-DOIT3 流行病學分析）。原因：`elink` 回傳的 `linksetdbs[0]` 為引用關係集合而非本文。**四檔已刪除，receipt 行已移除**；其餘以 PMID 解析者（21190455、27398874、38829880、33929522、35333363、27399144、27531506、21705063）已用 esummary 標題核對一致。
2. `mcp__paper-search__download_with_fallback`（`use_scihub=false`）對 32809002、29079252、31748169、12556541、18256393 全部失敗：`primary: PubMed does not provide direct PDF downloads … | unpaywall: no OA URL found (or PAPER_SEARCH_MCP_UNPAYWALL_EMAIL/UNPAYWALL_EMAIL missing)`。
3. 未使用 Sci-Hub、未使用 LlamaParse（無 PDF 可解析）、未使用 Tavily／OpenEvidence（本輪不需要；亦因其會把查詢送至外部服務，故未送出任何專案內容）。

## D. 驗證

`literature/notes/complications/grep_verification.md`：40 份本地檔案、236 項字串比對，0 FAIL（首次執行 7 項 FAIL 皆為查驗字串與原文的標點、Unicode 連字號或大小寫差異，修正查驗字串後通過；未更改任何報告數字）。
防污染：以 esummary 標題比對 PMCID（見 C-1）；`fulltext_tools.py verify` 未逐檔執行，以 esummary 標題＋ grep 內容替代 → 如 lead 需要可補跑。

## E. 第二階段（crosscheck）追加檢索與全文

### E1. Sci-Hub 最後備援（依 `SESSION_PROTOCOL_v2.md` 第 2 步）

| 論文 | `mcp__scihub__download_pdf` | 解析 |
| --- | --- | --- |
| 10.1016/S2213-8587(19)30349-3（ADDITION 10 y） | OK via sci-hub.ru，487,738 bytes | LlamaParse 89,038 字元；`verify` PASS |
| 10.1016/S2213-8587(17)30327-3（J-DOIT3） | OK via sci-hub.ee，547,643 bytes | LlamaParse 94,284；`verify` PASS |
| 10.1001/jama.2020.11747（INDEPENDENT） | OK via sci-hub.ee，474,185 bytes | LlamaParse 98,006；`verify` PASS |
| 10.1056/NEJMoa021778（Steno-2 2003） | **Permission denied by auto-mode classifier（Walled Content from a Copy）** | no_fulltext，未重試 |
| 10.1056/NEJMoa0706245（Steno-2 2008） | **同上被拒** | no_fulltext，未重試 |

### E2. 縱向：併發症事件後憂鬱／DD／認知（回應 psychosocial §C）

| # | 檢索式（精簡） | 命中 | 納入／備註 |
| --- | --- | --- | --- |
| E-a | `diabetes[ti] AND depression[ti] AND (incident OR onset) AND (amputation OR foot ulcer)` | 3 | 納入 Horsbøl 2024（38157285）、Pan 2012（22850257）、Williams 2011（20801060，反向）|
| E-b | `diabetic foot ulcer[tiab] AND depression[tiab] AND (cohort OR longitudinal OR prospective)` | 20 | 納入 Winkley 2012（22057196）、Westby 2020（32315474）、Pedras 2022（33100065）；其餘為關聯性或非 T2D 專屬，未納 |
| E-c | `diabetic retinopathy[tiab] AND (depression OR distress) AND (longitudinal OR prospective OR incident OR vision loss)` | 50 | **視力喪失→DD／憂鬱的縱向研究未檢出**（命中多為不相關）；納入 Li 2025（39720611，反向）|
| E-d | `diabetic kidney disease[tiab] AND depression[tiab] AND (longitudinal OR cohort OR incident) AND (dialysis OR eGFR)` | 1 | 不相關（beta-blocker 與透析），**透析／G4 後憂鬱縱向研究未檢出** |
| E-e | `diabetes[ti] AND (MI OR HF) AND depression AND (incident OR bidirectional OR meta-analysis)` | 17 | 納入 Zareini 2024（37815600）；候選未納：Chen 2023、Wang 2018、Xu 2023（橫斷／反向）|
| E-f | `severe hypoglycemia[tiab] AND (depression OR dementia OR cognitive) AND type 2 diabetes[tiab] AND (cohort OR longitudinal)` | 19 | 納入 Alkabbani 2023（36516080）、Li 2022（33678721）；GRADE 認知試驗（40388190）屬降糖藥比較，未納 |
| E-g | `diabetes complications[ti] AND depression[ti] AND (SR OR MA)` | 2 | 納入 Nouwen 2019（31215077）；de Groot 2001 太舊未納 |

新增 PMC 全文：PMC11493809、PMC11665660、PMC9359896（`fulltext_tools.py pmc <PMCID>`，標題核對一致）。新增 PubMed abstract：38157285、22850257、22057196、31215077、32315474、36516080、33100065、20801060。Phase 2 grep 驗證：見 `grep_verification.md`（含一次查驗字串打字錯誤的更正，數字未動）。
