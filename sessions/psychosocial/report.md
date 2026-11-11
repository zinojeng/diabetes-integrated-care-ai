# Psychosocial session 報告：成人糖尿病整合照護中的心理、生活與社會層面

- 日期：2026-11-11（Asia/Taipei）｜角色：psychosocial｜族群：成人 T2D 為主，T1D 另標註
- 性質：**主題式文獻綜整，不是 systematic review**；不代表已部署的臨床系統，也不證明任何設計能改善病人結局。
- 證據標記：📄 = 本地全文已用 grep 驗證（數字能在 `literature/parsed/psychosocial/` 找到）；📌 = 僅 abstract／metadata（不做超出 abstract 的斷言）；`UNRESOLVED` = 本輪無法確認，不用推論補洞。
- 全文狀態：52 筆證據列中，31 筆取得本地全文（PMC E-utilities 28、內建瀏覽器讀取 PMC 網頁 2、curl PDF 1）、21 筆 abstract-only。數字驗證腳本 78 項斷言通過 77，1 項為我的搜尋字串寫法問題（Zhang 2025 原文是 `effect size [ES]=0.30`，已改按原文引用）。
- 逐篇來源、PMID／DOI、限制見 [evidence_table.csv](evidence_table.csv)（列號 P01–P52）；檢索紀錄見 [search_log.md](search_log.md)；跨 session 問題見 [handoff.md](handoff.md)。

## 0. 先給結論（可被反駁的版本）

1. **diabetes distress、depression、anxiety、fear of hypoglycemia 是四個不同的構念**，ADA 2026 也要求分開篩檢（5.45–5.49）📄 P01。但它們彼此重疊，單一量表陽性不能直接換算成另一個診斷。
2. **心理狀態與 HbA1c／併發症／死亡的關聯大多是觀察性相關**。介入試驗顯示：降低 distress 不一定降低 HbA1c（REDEEM、Zu 2024：HbA1c MD 0.02）📄 P04/P11。因此不可把 "distress → HbA1c" 寫成已證實的因果鏈。
3. **「改善 distress」「改善 HbA1c／心血管危險因子」「改善長期器官結局」三層證據強度差很多**：第一層有中等程度的 RCT／meta-analysis 支持（但 GRADE 多為 low／very low）；第二層只在 collaborative care（TEAMcare、部分 INDEPENDENT 時點）可見，且 INDEPENDENT 的 24 個月 HbA1c 無差異；第三層（失明、洗腎、截肢、死亡）**本輪沒有任何心理介入 RCT 以此為主要結局**。
4. **INDEPENDENT 數字差異屬實**：Key Points 與 Table 2 寫對照組 54.7%，Abstract 寫 57.4%；風險差 16.9 與 71.6−54.7 相符，與 71.6−57.4＝14.2 不符。本輪 Crossref／PubMed 查無 erratum。詳見 §3.2。
5. **「PRIDE」本輪無法對應到 diabetes distress 試驗**。能找到的 PRIDE 是 Partnership to Improve Diabetes Education（safety-net 診所 provider 溝通訓練，主要結局 HbA1c，與標準衛教無差異）📌 P13。若 lead 指的是別的試驗，請提供全名；此項記為 `UNRESOLVED`。
6. **台灣直接資料很薄**：找到 PAID-C 驗證（台灣 3 家醫院）、TDDS（台灣新量表）、東台灣 PAID-C 橫斷研究、全國性 NHIRD 世代（T2D 發生憂鬱 HR 1.39、睡眠障礙 HR 1.40）、PHQ-9 台灣初級照護驗證。**沒有找到台灣成人 T2D 的 diabetes distress、anxiety、fear of hypoglycemia、認知障礙之族群盛行率**，記為 `UNRESOLVED`，不用中國大陸數字替代。
7. **AI 的合理角色是「找線索、協助施測與追蹤」，不是「診斷或代填」**。LLM 從病患訊息偵測憂鬱／焦慮症狀的 F1 約 93%，但標籤不是正式診斷、且有困難案例不一致 📄 P51；生成式 AI chatbot 的 meta-analysis 效果量有 95% prediction interval −0.85 至 1.67（含傷害）📄 P50；糖尿病 chatbot 證據多為 pre-post、僅 1 個 RCT 📄 P48。

## 1. 分領域：盛行率、與結局的關聯、相關或因果

> 下表的「ADA 證據等級」是 ADA 2026 Table 5.7（T2D）的 +++／++／+ 分級，反映 ADA 委員會對**相關性證據**的評級，不是因果證據 📄 P01。

| 領域 | 盛行率（全球） | 台灣資料 | 與 HbA1c／併發症／死亡 | 相關 vs 因果 |
| --- | --- | --- | --- | --- |
| **Diabetes distress** | ADA：T2D >60%、T1D >70%（二手引用、量表與切點依賴）📄 P01；Perrin 2017 meta-analysis 36%（55 項研究，n=36,998）📌 P15；中國大陸 T2D 53.2%（門診 42%）📌 P16。**三個數字差異大，來自不同量表／切點，不應混用** | PAID-C 台灣 3 院 n=205：平均 10.95±13.06（0–73.75 區間）📄 P29；TDDS 新量表 n=395 📄 P30/P31；東台灣門診：知識、自我照護、性別、家族史、併發症可預測 DD（R²=0.17）📄 P32。**盛行率 UNRESOLVED** | ADA Table 5.7：HbA1c／大血管／微血管／死亡皆 +++ 📄 P01；憂鬱＋DD 與 HbA1c r=0.23 📌 P18；PAID-C 與 A1C rs=0.15 📄 P29；日本 T2D 登錄 n=3,118：DD 的全因死亡 HR 1.67（1.14–2.43）📌 P19 | 皆為觀察性。**RCT 降低 DD 但 HbA1c 不變**（REDEEM、Zu 2024）→ 因果方向未證實；T1-REDEEM DD 變化與 HbA1c 變化僅 r=0.14 📌 P12 |
| **Depression** | 糖尿病 vs 無糖尿病：T2D 19% vs 11%（OR 1.76）、T1D 22% vs 13%；專科門診 36% 📌 P17；ADA「約四分之一」📄 P01 | NHIRD 配對世代：T2D vs 非糖尿病，新發憂鬱診斷 HR 1.39（1.34–1.43）、睡眠障礙 HR 1.40（1.37–1.44）📄 P33（**是發生率比，不是盛行率；來自診斷碼**）；PHQ-9 台灣初級照護驗證 📌 P34 | ADA +++（A1C、血脂、大小血管、死亡）；日本登錄 depressive symptoms HR 1.40（1.05–1.85）📌 P19；ADA 稱 depression 與 distress 症狀重疊、增加假陽性 📄 P01 | 雙向（憂鬱是 T2D 風險因子；糖尿病增加憂鬱）。Atlantis：憂鬱改善（SMD −0.32）與 HbA1c 改善（−0.33%）**彼此獨立**，remission 不預測 HbA1c 📄 P07 |
| **Anxiety** | ADA 引用 meta-analysis：焦慮症 pooled 28%；焦慮症者 T2D 風險 +19%、T2D 者焦慮症風險 +41% 📄 P01 | **UNRESOLVED**（INDEPENDENT 亞組 GAD-7≥10 為印度）| ADA Table 5.7：A1C、大血管、死亡 +++；微血管僅 + 📄 P01 | 觀察性；與 DD、低血糖症狀重疊 |
| **Fear of hypoglycemia (FoH)** | 本輪**未找到** pooled 盛行率（`UNRESOLVED`）；ADA 稱 "common" 📄 P01。DISCOVER（多國）HFS-W 平均 6.9，上四分位 ≥9 📌 P46 | **UNRESOLVED**（無台灣 HFS-II 驗證文獻；只有大陸 T2D 版）| 嚴重低血糖與較高 FoH、較低幸福感相關（多為橫斷）📌 P23；縱向：自行處理的低血糖後 anxiety／DD／FoH 升高 📄 P24；HFS-W≥9 者 2nd-line IS／insulin 的 HbA1c 反應較差 📌 P46 | 低血糖 → FoH 有縱向支持，但 FoH → 迴避強化治療（clinical inertia）→ HbA1c 的路徑多為觀察性 |
| **Sleep** | T2D 失眠（症狀）39%（34–44），I²=100%，GRADE very low 📄 P21 | NHIRD：T2D 睡眠障礙 HR 1.40 📄 P33（診斷碼）| 失眠與 HbA1c +0.23% 📄 P21；ADA 5.56–5.57 要求篩檢睡眠與 OSA 📄 P01 | 橫斷為主；睡眠障礙亦為 T2D 風險因子（ADA）。**介入是否改善 HbA1c 本輪未做** |
| **Cognitive／functional decline** | T2D 輕度認知障礙 45.0%（36–54），僅 12 項研究、多為亞洲 📌 P22 | **UNRESOLVED** | ADA Table 5.7：認知障礙與所有結局皆 +++；5.54–5.55：定期監測、必要時轉介正式評估 📄 P01；TEAMcare 失能量表（Sheehan）−0.9、QoL 改善 📌 P14 | 方向性模糊：高血糖／低血糖損害認知，認知障礙亦損害自我管理（反向因果）。功能結局不是長期器官結局 |
| **Disordered eating** | T1D：進食障礙 RR 2.47（1.84–3.32）；insulin omission 10.3% 📄 P27；ADA：insulin restriction 中位數 15%；T2D 以 binge eating／night eating 為主，無 pooled 盛行率 📄 P01 | 香港繁中 DEPS-R（T1D）：切點 24，13.2% 高於切點、SCID 診斷 4.4% 📄 P28（**非台灣**）| ADA Table 5.7 T2D：A1C 為 +/−（證據不一致）；T1D insulin omission 與微血管、死亡 +++ 📄 P01 | 篩檢陽性≠診斷（DEPS-R 13.2% vs SCID 4.4%）；ADA 提醒避免輕易貼標籤 📄 P01 |
| **Treatment burden** | 本輪未找到糖尿病族群 pooled 盛行率。DTBQ（18 題）只測**藥物治療方案**負擔 📄 P47 | **UNRESOLVED** | 未納入 ADA 2026 ch.5 的專屬建議（全文 grep "treatment burden" 為 0 次）📄 P01 | 概念與 DD（regimen distress）重疊；REDEEM 顯示 regimen distress 反應最大 📄 P11 |
| **Social needs／SDOH** | ADA：美國糖尿病成人 food insecurity 16% vs 無糖尿病 9%（2023 美國數字）📄 P01 | **UNRESOLVED**（台灣 SDOH 篩檢工具與盛行率本輪未查）| ADA 5.9：評估 SDOH 以設計 DSMES 📄 P01；food insecurity meta-analysis（49 項橫斷）與 FBG／HbA1c **無統計關聯**（OR 1.21，0.95–1.54）📄 P25 | 橫斷、美國為主；SDOH 的因果與可介入性需看介入研究，本輪僅引 ADA review 框架 📄 P26 |

**閱讀提醒**：ADA 稱 DD 盛行率 >60%，但 Perrin 2017 meta-analysis 為 36%——差異可由切點、量表、族群解釋（ADA 的引用本輪未逐篇核對），**報告時應同時呈現範圍並註明切點**，不要挑一個。

## 2. 從篩檢到介入：screening → conversation → clinical assessment → tailored care → reassessment

下表整合 ADA 2026 ch.5（📄 P01）、EASD 2026 diabetes distress 指引（📄 P02）與 collaborative care 試驗的角色設計（📄 P08/P09）。**「責任人」欄是我的綜整建議**：指引只規定「由受過訓練的專業人員」「合格的 behavioral health professional」，**並未**指定台灣的個管師、衛教師、臨床心理師等職稱；台灣職稱對應與健保給付規則本輪未查，標 `UNRESOLVED`。

| 步驟 | 指引原文要點 | 建議責任人（綜整，非指引原文）| AI／系統可做 | AI／系統不可做 |
| --- | --- | --- | --- | --- |
| 1. Screening | ADA 5.43：至少每年，或健康狀態／治療／生活情境改變時；5.45 DD 每年；5.46 焦慮每年；5.47 高低血糖風險者 FoH 每年；5.48 憂鬱每年（有病史者更頻繁）；5.49 併發症診斷或醫療狀態大變時重新篩檢；5.50 飲食失調；5.54 認知；5.56 睡眠 📄 P01。EASD A.3、A.4：用有效且可靠的工具、至少每年及重大生活事件／治療變更 📄 P02 | 衛教師、個管師、護理師或診間助理施測；醫師確認 | 依病歷觸發提醒（新併發症、換藥、HbA1c 惡化）、推送量表連結、追蹤未完成 | 代填答案；把「無紀錄」當陰性 |
| 2. Conversation | EASD A.1、A.2、A.5：每次門診談情緒面；用開放式問題；不論結果都要與當事人探討 📄 P02；ADA：開啟對感受與信念的對話，連結情緒與自我管理 📄 P01 | 醫師、衛教師、個管師 | 提供提問範例 | 取代對話、自動給出情緒診斷 |
| 3. Clinical assessment | ADA：陽性篩檢後做 "comprehensive clinical" 評估，鑑別 distress／憂鬱／焦慮（症狀重疊）📄 P01；Table 5.5 列出轉介情境（陽性篩檢、疑似飲食失調、故意減量胰島素、疑似嚴重精神疾病、自我管理能力下降、代謝手術前後…）📄 P01 | 臨床心理師／精神科醫師／具糖尿病經驗之 behavioral health 專業；疑似進食障礙需熟悉糖尿病生理者 | 整理量表分數趨勢、既往診斷、用藥（如 antipsychotic、可能影響食慾的藥）供評估者參考 | **診斷**憂鬱／焦慮／進食障礙 |
| 4. Tailored care | DD：DSMES、CBT、mindfulness、MI（ADA）；EASD T2D：心理、心理教育、教育介入皆「條件式建議」，GRADE very low／very low／low 📄 P02。共病憂鬱：collaborative care（TEAMcare、INDEPENDENT）。SDOH：依 ADA 5.9 調整 DSMES 設計 | 個管師（care manager）+ 醫師調藥 + 心理師／精神科督導 + 社工（SDOH）| 排程個案討論名單（caseload review）、提醒目標未達 | 自動調整藥物或心理治療處置 |
| 5. Reassessment | EASD A.4／A.6／A.7：定期追蹤、記錄於病歷並告知團隊、與當事人共訂計畫 📄 P02；ADA 5.49：新併發症即重新篩憂鬱；5.45：目標未達、轉換期、出現併發症時重複篩 DD 📄 P01 | 同步驟 1；結果回報給主治醫師 | 追蹤時序、偵測失聯 | 把分數下降當作「已治癒」 |

**實作證據**：INDEPENDENT 的做法是由**無心理健康訓練的 allied health 人員**擔任 care coordinator、EHR decision support、每 2–4 週 caseload review（有 consulting specialist）📄 P09；TEAMcare 為受督導護理師協同家醫科做 treat-to-target 📄 P08。ADA 另指出「長期、系統性處理 DD 並整合於常規照護的結局資料很少」📄 P01。

## 3. 實證：三層結局分開

### 3.1 改善 diabetes distress

| 證據 | 結果 | 備註 |
| --- | --- | --- |
| EASD 2026 配套 SR（Schipper）248 RCT，55,497 人 📄 P03 | T2D：心理介入 SMD −0.31（−0.50, −0.13），N=21，GRADE very low；教育介入 −0.34（−0.56, −0.11），N=3，low。T1D：心理介入 −0.22，CGM −0.26（moderate）| 94 項 some concerns＋71 項 high RoB；指引以 SMD≥0.3 當有臨床意義，T1D 心理介入點估計未達 |
| Zu 2024，16 RCT，1,639 人 📄 P04 | 短期 DD SMD −0.56（−0.90, −0.22）；**長期 SMD −0.45（−0.93, 0.03）不顯著** | 團體、心理師、含科技、基線 DD 高者效果較大 |
| Cochrane Chew 2017，30 RCT，9,177 人 📌 P05 | 心理介入 vs 常規：DRD SMD −0.07（−0.16, 0.03），low | 與 2024／2026 的 meta-analysis 結論**方向不同**（納入試驗與分類方式不同；本輪未做原因分析）|
| REDEEM（T2D，n=392）📄 P11 | 三組（含最小介入）DD 皆顯著下降、組間無差異；高基線 regimen distress 者 DD 特定問題解決較佳 | 無常規照護組，不能把下降全歸因於介入 |
| T1-REDEEM（T1D，n=301）📌 P12 | 兩組 d=1.06，無組間差異 | 僅讀 abstract |
| PRIDE 📌 P13 | 非 DD 試驗（見 §0 第 5 點）| `UNRESOLVED` |
| CBT／DSMES 補充 | ADA 引用 RCT：CBT 改善 DD、A1C、憂鬱至 1 年；mindfulness 加入 DSMES 降低 DD；DSMES 可降 DD 📄 P01（ADA 內文引用，我未逐篇取全文）| |

### 3.2 INDEPENDENT（JAMA 2020）核對：Table 2 的 54.7% vs abstract 的 57.4%，以及 severe hypoglycemia 📄 P09

讀取版本：PMC7435347 作者手稿（`JAMA. 2020 Aug 18;324(7):1–13`）。

| 位置 | 文字（本地 grep 命中）|
| --- | --- |
| Key Points | 「…(71.6% vs 54.7%)」|
| Abstract／Results | 「(71.6% vs 57.4%; risk difference, 16.9% [95% CI, 8.5%-25.2%])」|
| Results 內文 | 「(71.6% vs 54.7%; RD, 16.9% [95% CI, 8.5%-25.2%])」|
| Table 2 第一列（24 個月）| 71.6／54.7，RD 16.9（8.5–25.2）|

- **算術核對**：71.6 − 54.7 = 16.9（與所有 RD 吻合）；71.6 − 57.4 = 14.2（與 RD 不符）。因此 **54.7% 與其餘四處一致，57.4% 較可能是 abstract 的誤植**。但這是我的推論；作者或期刊更正聲明本輪查無（Crossref `update-to` 為空；PubMed `CommentsCorrections` 只有一則 CommentIn）。**請 lead 不要靜默選用其中一個，報告中兩個數字都要保留並註明來源位置**。`UNRESOLVED`：最終出版版本（非作者手稿）是否已更正，未能核對。
- **Severe hypoglycemia**：Abstract 與 Results 皆寫 8（4.1%）vs 0（intervention vs usual care）；同表其他嚴重不良事件：CVD 事件或住院 4（2.0%）vs 7（3.4%）、stroke 0 vs 3（1.4%）、死亡 2（1.0%）vs 7（3.4%）。**嚴重低血糖在介入組出現而對照組為 0，需要在摘要裡與「HbA1c 目標」一起呈現**；試驗並非為偵測嚴重不良事件差異而設計，不能據此推論因果，也不能因死亡數較少宣稱降低死亡。
- **其他關鍵數字**：24 個月 HbA1c 平均 8.7 vs 8.6，差 0.0（−0.3 至 0.4）（Table 2；全時點整體估計 −0.2，−0.4 至 0.1）；secondary（24 個月）：HbA1c 降 ≥0.5 個百分點 51.9% vs 43.2%（RD 8.7，−0.9 至 18.4）；SBP、LDL 無差異；抗憂鬱藥使用 17.3% vs 5.6%；PHQ-9<10（post hoc）95.2% vs 78.0%。作者自述 16 項預先指定次要結局中 12 個月 10 項、24 個月 13 項無統計顯著差異。
- **解讀**：複合主要結局主要由**憂鬱症狀改善**驅動（SCL-20 ≥50% 改善 77.7% vs 63.6%）；心血管危險因子改善在介入結束後（12→24 個月）縮小。TEAMcare 是同一模式的先驅，但族群與系統不同。

### 3.3 改善 HbA1c／心血管危險因子（中介結局）

| 證據 | 結果 |
| --- | --- |
| TEAMcare（NEJM 2010，n=214，12 個月）📄 P08 | HbA1c 差 0.58%、LDL 6.9 mg/dL、SBP 5.1 mmHg、SCL-20 0.40（P<0.001）；介入含胰島素／降壓藥／抗憂鬱藥調整 |
| Atlantis 2014，7 RCT 📄 P07 | collaborative care：憂鬱 SMD −0.32；HbA1c −0.33%（−0.66, −0.00），I²=73% |
| Winkley 2020 HTA（T2D 成人 49 RCT）📌 P06 | 心理介入 HbA1c MD −0.21（−0.31, −0.10）；對憂鬱症狀、BP、BMI 無益 |
| Chew 2017 📌 P05／Zu 2024 📄 P04 | HbA1c −0.14%（邊界）／短期 0.02、長期 −0.27（不顯著）|
| REDEEM 📄 P11 | HbA1c 無變化 |
| 小結 | **降低 DD 或憂鬱 ≠ 降低 HbA1c**；HbA1c 改善主要出現在**同時由團隊執行 treat-to-target 調藥**的 collaborative care，而非單純心理治療。這支持「整合」的必要性，但無法分離心理成分與調藥成分的貢獻 |

### 3.4 改善長期器官結局

本輪**沒有找到**以失明、ESKD、截肢、心肌梗塞或死亡為主要結局的心理或 collaborative care RCT。INDEPENDENT 的死亡／CVD 事件只是不良事件欄位（見 §3.2）；TEAMcare 後續成本與長期追蹤本輪未取全文（`UNRESOLVED`）。觀察性資料（日本登錄、NHIS）顯示心理壓力與死亡相關 📌 P19、📄 P20（P20 為 K6 一般心理壓力，不是 diabetes distress），**不能用來宣稱介入可降低死亡**。

### 3.5 數位／AI 心理介入在糖尿病的證據

| 證據 | 內容 | 層級 |
| --- | --- | --- |
| Wu 2024 糖尿病 chatbot SR+MA 📄 P48 | 25 項研究，僅 1 個 RCT；4 組 pre-post（n=219）HbA1c 降 0.30（0.04–0.55）；僅 2 項（8%）提供心理健康教育 | 自我管理，**非心理結局**；無對照 |
| He 2023 conversational agent SR+MA 📄 P49 | 32 RCT：憂鬱 g=0.29、焦慮 g=0.29、一般壓力 g=0.33，短期 | 一般族群、非糖尿病 |
| Zhang 2025 generative-AI chatbot SR+MA 📄 P50 | 14 RCT：ES 0.30（0.004–0.59），95% PI −0.85 至 1.67 | 一般族群、非糖尿病；預測區間含傷害 |
| Therabot RCT（NEJM AI 2025）📌 P52 | n=210；MDD 症狀降幅 −6.13 vs −2.63（4 週）| 非糖尿病、等候名單對照、短期 |
| EASD 2026 | 技術介入（含 CGM）：T1D 建議 CGM／AID 降 DD（moderate）；T2D 不建議以 CGM 降 DD（very low）📄 P02 | |
| ADA 2026 | 電話、App、視訊、自助式介入「可能有效降低 DD」（原文 can be effective）；5.6 建議提供遠距／數位 DSMES（B）📄 P01 | 內文引用，我未逐篇驗證 |

**結論**：**糖尿病族群的 AI／chatbot 心理介入，在 distress、HbA1c、長期器官結局三層都沒有足夠的對照試驗證據**；一般族群的數據只能當作可行性參考。

## 4. 量表規格（只列計分規格、切點與正式繁中版本出處；不翻造問卷、不假設授權）

> 切點數字的「來源族群」很重要：多數切點在歐美初級照護或糖尿病門診建立。台灣專用切點（尤其 DD 量表）本輪**未找到**。

| 量表 | 計分 | 切點（來源）| 建議臨床回應（綜整，非原文）| 繁體中文／台灣驗證 |
| --- | --- | --- | --- | --- |
| **PHQ-2** | 2 題，每題 0–3（總分 0–6；由 PHQ-9 題目計分推得）| ≥2：IPD meta-analysis PHQ-2 ≥2 接 PHQ-9 ≥10，sens 0.82／spec 0.87 📌 P37；台灣初級照護 PHQ-2 ≥2 sens 0.88／spec 0.82 📌 P34 | 陽性 → 做 PHQ-9 → 臨床評估 | Liu et al., Compr Psychiatry 2011（台灣初級照護，n=1,954；非糖尿病專用）📌 P34 |
| **PHQ-9** | 9 題，每題 0–3，總分 0–27；5／10／15／20 = 輕／中／中重／重度 📌 P35 | ≥10：原始 sens 88%／spec 88% 📌 P35；IPD（半結構式訪談）sens 0.88／spec 0.85 📄 P36；台灣 sens 0.86／spec 0.94 📌 P34 | ≥10 → 臨床評估憂鬱；第 9 題（自傷想法）任何陽性 → 當日安全評估（此點為通用臨床慣例，**本輪未在糖尿病指引全文中逐字驗證**）；與 DD 鑑別 | 同上（Liu 2011）|
| **GAD-7** | 7 題，每題 0–3，總分 0–21（由題數×0–3 推得；原始文獻本輪未取）| ≥10 為 INDEPENDENT 亞組入選門檻 📄 P10；原始 Spitzer 2006（PMID 16717171）本輪未取得全文／abstract | ≥10 → 臨床評估焦慮，與 DD、低血糖症狀重疊鑑別（ADA）📄 P01 | **UNRESOLVED**：未找到台灣 GAD-7 驗證文獻 |
| **DDS-17** | 17 題、6 點量表，平均每題分數；**平均 ≥3 = moderate distress** 📌 P38（DDS-17 發展：Polonsky 2005, PMID 15735199 📌）| 平均 ≥3（僅此一項在本地文件驗證；≥2 的 "some distress" 區間**未驗證**）| ≥3 → 找出高分次量表（emotional burden、physician、regimen、interpersonal）定向處置 | **UNRESOLVED**：未找到台灣正式 DDS-17 版本。Lin 2022 稱台灣病人對香港版 CDDS 有理解困難，另發展 TDDS 📄 P30 |
| **DDS-2** | 2 題（「被糖尿病要求壓垮」「覺得自己常常失敗」）、6 點量表 📌 P38 | 對 DDS-17 平均 ≥3 的 sens .95／spec .85 📌 P38；**DDS-2 自身的陽性切點未在 abstract 明載** `UNRESOLVED` | 陽性 → DDS-17 | 同上 |
| **PAID（20 題）** | **原始 1995 版：六點量表**（Polonsky 1995 abstract）📌 P39。**現行常用：5 點 0–4，總分×1.25 轉為 0–100**。證據：台灣 PAID-C 總分區間 0–73.75、單題平均 ≤1.21 📄 P29（×1.25 與 0–4 為依此推得，需 calculators 對照原始評分手冊確認）| 常見 ≥40 為高 distress：**本地全文中未找到此切點** → `UNRESOLVED` | 高分 → 找最高分題目討論；常見最高分題 Q12「擔心未來與併發症」📄 P29/P32 | PAID-C：Huang et al., Diabetes Care 2010，台灣 3 家醫院，n=205，單因子 CFA 📄 P29（繁／簡體字未於讀取文字中確認）|
| **PAID-5** | 取 PAID 第 3、6、12、16、19 題 📌 P40 | 文獻慣用 ≥8（0–20）：**本地未驗證** `UNRESOLVED`；McGuire 2010 對「distress 辨識」sens 94%／spec 89% 📌 P40 | 陽性 → PAID-20 或 DDS-17 | 未找到單獨 PAID-5 台灣版 |
| **WHO-5** | 5 題，每題 0–5（**越高越好**），原始分 0–25，×4 = 0–100 📄 P42/P43 | 慣用 <50（Hajos 2013 荷蘭糖尿病門診：vs PHQ-9≥10 sens 79%／spec 88%）📌 P41；**大陸 T2D 最佳切點 <42**（vs MINI sens .83／spec .75，AUC .88）📄 P42 → 切點因族群而異。另一份第三方副本印有「原始分 <13 或任一題 0–1 → 做憂鬱評估」，**該副本本輪未取得，僅為搜尋摘要**，`UNRESOLVED` | 低分 → PHQ-9 與臨床評估；WHO-5 是福祉量表，不是憂鬱診斷工具 | 大陸簡體 WHO-5-C 📄 P42；**台灣繁中糖尿病族群驗證未找到** `UNRESOLVED` |
| **WHO-5 缺值規則** | 本輪取得的 WHO-5 表單副本（UConn 轉載）**未印缺值處理規則** 📄 P43 | — | 未查到原始 PRU／WHO 文件的缺值規則 → `UNRESOLVED`，**實作時請當作「有缺值則不計算總分」並由 calculators 另行確認原始文件**，不得自行插補 | — |
| **HFS-II** | 33 題（Behaviour 15 + Worry 18），0–4 五點，總分 0–132 📄 P45；高分＝較恐懼 | **無公認臨床切點**；Gonder-Frederick 以 IRT 評估心理計量，α 總分 0.94 📄 P44 | 高分 → 檢視低血糖史、感知低血糖能力、藥物（sulfonylurea／insulin）、CGM 適用性；ADA 5.47 轉介受過訓練者 📄 P01 | 簡體 Chinese HFS-II（大陸 T2D，23 題 4 因素）📄 P45；**台灣繁中版未找到** |
| **DEPS-R**（T1D）| 16 題，0–5 | 繁中版切點 24（香港）📄 P28 | 陽性 ≠ 診斷（13.2% vs SCID 4.4%）| 香港繁中版 📄 P28 |
| **DTBQ**（治療負擔）| 18 題，3 因子 📄 P47 | 無切點 | 僅測藥物方案 | 大陸版 📄 P47 |
| **TDDS**（台灣）| 0–10 視覺量表，最終 CFA 模型 12 題 📄 P30 | 無已驗證切點 | 研究工具；與 PAID／DDS 不等價 | Lin et al., Front Public Health 2022，n=395 📄 P30 |

**量表選擇備註**：EASD 2026 指引只說 PAID 與 DDS 皆有良好心理計量、彼此高度相關、有多語言版本，並把量表詳述放在 ESM1；主文**沒有**規定切點或推薦單一量表 📄 P02。ADA 2026 ch.5 全文**未點名任何具體量表**，轉向 ADA position statement 與 Behavioral Health Toolkit 📄 P01。

## 5. AI 能做與不能做（引文獻）

**可做（僅限輔助，且仍需臨床審閱）**
1. 從結構化資料與病歷找**線索**：新併發症、換藥、HbA1c 惡化、嚴重低血糖後應觸發重新篩檢（對應 ADA 5.45、5.49）📄 P01。
2. 從病患訊息偵測症狀提及：Kim 2025（糖尿病患者 secure messages）顯示 3／5 個 LLM F1 與 accuracy >90%，Llama 3.1 405B zero-shot 93%；作者結論只到「協助及時篩檢與轉介」，且困難案例有不一致、需真實世界評估 📄 P51。
3. 協助施測與追蹤：排程、提醒、彙整分數趨勢、標示未完成篩檢（是流程功能，**目前沒有證據證明能改善結局**）。

**不可做／證據不支持**
1. **診斷憂鬱、焦慮或進食障礙**：ADA 要求陽性篩檢後由合格專業人員做臨床評估；量表分數與 DEPS-R 等本身就會高估（DEPS-R 13.2% vs SCID 4.4%）📄 P01/P28。LLM 的標籤是訊息層級標註，不是 structured interview 診斷 📄 P51。
2. **代填量表**：量表是自述工具，代填會製造不存在的資料；PHQ-9／WHO-5／PAID 的效度都建立在當事人本人作答 📄 P35/P42。
3. **從病歷空白推斷陰性**：沒有篩檢紀錄≠沒有憂鬱（CLAUDE.md 規則亦同）。
4. **以 chatbot 取代心理介入**：糖尿病 chatbot 證據層級低（1 個 RCT，多為 pre-post）📄 P48；通用心理 chatbot meta-analysis 預測區間跨越 0 且含傷害 📄 P50；Therabot 為短期、非糖尿病、等候名單對照 📌 P52。

## 6. 局限

- 非 systematic review；檢索以 PubMed E-utilities 與 Europe PMC／PMC 為主，未做雙人篩選或正式 RoB。
- 21／52 筆僅 abstract；其中包含 T1-REDEEM、Chew Cochrane、Winkley HTA、Perrin、Farooqi 等**重要**證據，不可據以做 abstract 以外的斷言。
- 未取得 ADA position statement（Young-Hyman 2016）、Polonsky 2005 DDS、Spitzer 2006 GAD-7 的全文。
- 台灣資料缺口見 §0 第 6 點；`PRIDE` 身分、WHO-5 缺值規則、PAID／PAID-5／DDS-2 切點為 `UNRESOLVED`。
- 本報告所有「責任人」與「臨床回應」欄均為綜整建議，未經臨床專家驗證，也沒有任何病人結局數據。

## 7. UNRESOLVED 清單

| # | 項目 | 需要誰 |
| --- | --- | --- |
| U1 | INDEPENDENT 最終出版版本的 54.7% vs 57.4% 是否已更正 | lead／期刊頁面 |
| U2 | 「PRIDE」是否指 White 2020 以外的試驗 | lead |
| U3 | 台灣成人 T2D 的 DD、anxiety、FoH、認知障礙盛行率 | 新增中文／台灣檢索 |
| U4 | PAID 現行 0–4 與 ×1.25、≥40 切點；PAID-5 ≥8；DDS-2 切點；DDS-17 ≥2 區間的原始來源 | calculators（見 handoff）|
| U5 | WHO-5 缺值規則的原始文件 | calculators |
| U6 | GAD-7、DDS-17、HFS-II、WHO-5 的台灣繁中正式驗證 | calculators／新增檢索 |
| U7 | 台灣職稱（個管師、衛教師、臨床心理師、社工）與健保共同照護網給付對應 | lead（台灣制度）|
| U8 | 心理介入對長期器官結局的任何 RCT 證據 | 本輪未見；請 methods_ai 評估證據層級 |

## 8. crosscheck 後修訂（2026-11-11；詳見 [crosscheck.md](crosscheck.md)）

1. **TEAMcare 數字**：§3.3 所引 0.58%／6.9／5.1／0.40 是 abstract 的**未校正變化量差**；Table 2 模型估計為 SCL-20 −0.41、HbA1c −0.56（−0.85, −0.27）、LDL −9.1（−17.5, −0.8）、**SBP −3.4（−6.9, 0.1）不顯著**；SCL-20 ≥50% 降幅 60% vs 30%（📄 P08，表格為手動轉錄節錄）。原始主要結局於 2009-08 資料分析前更改，且未達 290 人目標（實收 214）。
2. **INDEPENDENT 成分**：12 個月 SCL-20 反應 71.5% vs 45.8%、HbA1c ≥0.5 點 62.2% vs 44.7%；**24 個月僅 SCL-20 成分持續顯著（77.7% vs 63.6%）**，HbA1c 反應率差 8.7（−0.9, 18.4）不顯著，SBP／LDL 兩時點皆無差異 📄 P09。複合結局要求憂鬱反應「且」任一代謝指標達標，24 個月的差距主要來自憂鬱成分。→ 「身心共同改善」建議降級為「憂鬱改善明確；HbA1c 僅於介入期內改善」。
3. **§3.5 AI 證據更正**：「糖尿病族群無對照試驗證據」須補充——有兩個小型 RCT 量測 distress：Bruijnes 2023（PMID 37383944，Prolific 線上受試者 n=156、Rasa 非生成式 agent、DDS −0.305 vs 0.002、p=0.019、3 週）與 Nayak 2023（PMID 38039007，n=32，語音 AI 胰島素滴定，PAID-5 差 −3.6［−6.8, −0.4］；介入非心理治療）📄 P53/P54；Kostiuk 2025 為計畫書 P55。仍無臨床族群、足夠樣本、LLM／生成式 AI 且以 distress／憂鬱為主要結局的 RCT。
4. **PAID**：×1.25 → 0–100 與 ≥40 切點在 de Wit 2022 全文確認（📄 P56：≥40 sens 0.95／spec 0.97，低 0–16、中 17–39）；de Wit 把 ≥40 歸因 Welch 1997，但 Welch 1997 abstract 無此數字，一手出處仍 `UNRESOLVED`。PAID-5 ≥8、WHO-5 <13／缺值規則仍 `UNRESOLVED`。
5. **Cochrane Chew 2017** 已取全文（📄 P05：DRD SMD −0.07，−0.16 至 0.03，12 trials，3,315 人）；**T1-REDEEM** 已讀 PMC 頁面（HbA1c 基線→3 個月 P=0.003，兩組無差異；無 usual-care 對照；節錄 📄 P12）。Winkley HTA、Perrin、Levis PHQ-2 仍為 abstract-only。**未使用 Sci-Hub**（需使用者本人許可）。
6. **新增證據 P56–P57**：Ho 2026 meta-analysis（憂鬱＋糖尿病 vs 僅糖尿病）：全因死亡 RR 1.30、併發症 RR 1.28，但**視網膜病變 RR 0.84（0.76–0.94）反而較低**、腎病變 1.09（0.93–1.27）不顯著 📄 P57——ADA Table 5.7 的「微血管 +++」是整體評級，不代表每種器官併發症皆一致。
