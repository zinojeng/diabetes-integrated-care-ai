# calculators session 報告：Calculator 公式、適用性與可執行實作

日期：2026-11-11。角色：calculators（Claude Opus 5.5 指定；本 session 實際模型 ID 見 session metadata，若與 `claude-opus-5-5` 不符請 lead 判定）。
標記：📄 = 本地全文／官方文件已 grep 驗證；📌 = 僅 abstract／metadata 或僅開放的二手轉載；`spec_only` = **未實作，不產生任何數字**。

> 本報告與 `calculators/`（Python package `dmic_calculators`）是**研究用規格與程式**，不是已部署或已臨床驗證的診療系統。沒有任何病人結局改善的主張。各模型的輸出（疾病負擔、器官分層、事件風險、心理症狀分數）**不可相加或合成為「全人風險總分」**。

## 1. 結論摘要

| 狀態 | 工具 |
| --- | --- |
| **implemented**（係數／公式在本地文件 grep 到，測試通過） | CKD-EPI 2021 cr、cr-cys；KDIGO G/A 與熱圖；KFRE 4-var **Original 5 年**與 **non-North-America 5 年**；IWGDF 2023 分級；SCORE2-Diabetes；RECODe（9 個 outcome）；TIMI TRS 2°P（T2D 應用）；PHQ-9／PHQ-2／GAD-7／WHO-5／DDS-2／DDS-17（總平均）／CFS |
| **implemented_secondary**（僅在開放二手轉載 grep 到，原文付費牆） | Charlson（original 1987、Quan 2011）；FIB-4（含 1.3／2.67／>65 歲 2.0 分流）；APRI（只算值，不解讀）；PAID-20／PAID-5；HFS-II；Mini-Cog；MoCA（只收總分）；FRAIL |
| **provisional**（需明確 `allow_provisional=True`） | KFRE 2 年（Original、non-NA）；UKPDS Risk Engine（CHD／stroke） |
| **spec_only**（不產生數字） | DCSI／aDCSI；age-adjusted Charlson；PREVENT 全部（含 2026-10-14 HbA1c 更正）；WATCH-DM；UKPDS OM2；ADVANCE；Karter 低血糖工具；KFRE North-America 區域版；RECODe 其餘 12 個 microvascular outcome；台灣 ESRD／CKD 點數；EASL 2024／ADA 2026 FIB-4 切點 |

`calculators/dmic_calculators/registry.py` 以機器可讀方式保存上表與每項缺什麼（`tests/calculators/test_registry.py` 驗證 spec_only 項目沒有偷偷實作的函式）。

### 重要的「找不到／被擋」誠實清單

- **JAMA 2016 KFRE eAppendix 2 p9 無法由本 session 開啟**：jamanetwork.com 對誠實 UA 與內建瀏覽器均回 **HTTP 403**；PMC 的 NIHMS 補充檔在 proof-of-work 頁面後；Europe PMC 補充檔 API 回「not open access」。**未繞過**。因此 KFRE 的 S0 只有兩個在本地可 grep：Original 5 年 = 0.9240（`PMC7203563` Table 4 的方程式）、non-NA 5 年 = 1−0.0635 = 0.9365（`PMC11813909` Table 4 base hazard）。2 年值（0.9750／0.9832）與 North-America 值（0.9751／0.8996）只出現在 repo 內 Codex 查核檔，**未能在本地原文 grep**；2 年值經「PMC4752167 所述區域因子使 baseline 風險降 32.9%（2 年）／16.5%（5 年）」交叉一致（0.0250×0.671→0.9832；0.076×0.835→0.9365），故標 `provisional`；North-America 標 `spec_only`。**請 methods_ai 以可開啟 JAMA supplement 的管道獨立核對（見 handoff）。**
- **PREVENT**：係數在 Supplemental Table S12 A–J（xlsx），NCBI 為 proof-of-work、AHA professional.heart.org 對 curl／WebFetch 皆 403。2026-10-14 更正僅有二手摘要，未取得原文，**不實作 HbA1c／full 版本**，且因 base 版係數也拿不到，整組 `spec_only`。
- **DCSI／aDCSI**：Young 2008 在 PMC 僅 abstract（PDF 403，Europe PMC XML HTTP 500）；Chang 2012、Glasheen 2017、Wicke 2019 皆 OA=N；11 篇開放文獻使用 DCSI，沒有一篇印出 rubric（只印「7 類、除 neuropathy 0–1 其餘 0–2、總分 0–13」）。故 `spec_only`，**不憑記憶填 rubric**。
- **Sci-Hub**：協議允許作 2021 年前論文的最後備援，本 session **沒有使用**（版權／來源風險），保留給 lead 明確決定。
- **工具缺陷（給 lead）**：`scripts/fulltext_tools.py pmc <PMID>` 用 `elink` 取第一個 link，可能是「引用／相關」文章而非本文，造成我批次抓取時 9 篇**完全不相關**的 PMC 文章被寫入（已刪除，receipts 仍留錯誤紀錄）；且 `jats_to_md` 會丟失不是 `<sec>` 直接子節點的 `<table-wrap>`（RECODe 主文因此沒有表格）。改傳**精確 PMCID** 並另存 `_tables.md` 可避開。詳見 `search_log.md`。

## 2. 統一輸出與缺值原則

所有函式回傳 `{tool, version, value, units, population_ok, reasons_unavailable, inputs_used, source, details}`；`details.kind` ∈ `disease_burden / organ_function / stratification / risk_estimate / symptom_score / screening_index`，把**疾病狀態、風險估計、資料完整度、行動狀態分開**（資料完整度見 Charlson 的 `data_completeness`／`lower_bound`、IWGDF 的 `at_least/at_most`；行動狀態如 PHQ-9 item 9 `safety` 與量表 `further_assessment` 為**提示而非決策**）。

- 缺值、型別錯誤（含 `bool` 冒充數字、NaN、字串）、非正值、單位不明（同時給兩種單位）→ `value=None` 並寫明原因，**不靜默代入**。`result()` 在有 `reasons_unavailable` 時強制 `value=None`。
- 超出適用族群 → `population_ok=False` 且不輸出（SCORE2-Diabetes 年齡 40–69／既往 CVD；KFRE eGFR≥60；RECODe 年齡 40–79；FIB-4 急性疾病；TIMI 非 T2D）。
- 「未檢查」≠「陰性」：IWGDF、Charlson、FRAIL、TIMI 以 `None` 表示未知；IWGDF 以窮舉未知項判斷分級是否確定，否則回 `None` 並給 `at_least/at_most`。
- RECODe 論文 footnote 允許「略過缺項」，本實作**預設拒算**，只有呼叫者明確 `allow_omit_missing_terms=True` 才略過並標示（未驗證）。
- SCORE2-Diabetes 沒有預設地區（台灣未被指派任何歐洲風險區）；HbA1c 必須 mmol/mol、膽固醇 mmol/L；原模型 eGFR 為 CKD-EPI **2009**，輸入其他公式會有 warning。

## 3. 逐工具規格（本地可驗證項目）

### 3.1 CKD-EPI 2021（`ckd.py`）📄
- 公式（NIDDK 官方頁 L119–L215，NEJM 主文不印常數）：eGFRcr = 142 × min(Scr/κ,1)^α × max(Scr/κ,1)^−1.200 × 0.9938^age × 1.012 [女]；κ 0.7／0.9，α −0.241／−0.302。cr-cys = 135 × min(Scr/κ,1)^α × max(Scr/κ,1)^−0.544 × min(Scys/0.8,1)^−0.323 × max(Scys/0.8,1)^−0.778 × 0.9961^age × 0.963 [女]；α −0.219／−0.144。
- 單位：Scr mg/dL（µmol/L ÷88.4，需只給一種）、Scys mg/L、年齡≥18。輸出 mL/min/1.73 m²。
- 不適用／注意：AKI、極端肌肉量、截肢；**單次 eGFR 不等於 CKD 診斷**；不是未來腎衰竭機率。
- 測試向量：NIDDK Table 1／2 的分段式（獨立寫法）、κ 邊界封閉解、µmol 與 mg/dL 等價。官方頁沒有提供數值算例，因此向量是**公式導出**，不是已發表的數值範例（誠實標示）。

### 3.2 KDIGO G/A 與熱圖（`staging.py`）📄
G1 ≥90、G2 60–89、G3a 45–59、G3b 30–44、G4 15–29、G5 <15；A1 <30、A2 30–300、A3 >300 mg/g（<3／3–30／>30 mg/mmol）。熱圖（目視頁面圖片 `kdigo_p11-011.png` 確認）：G1/G2＝綠／黃／橙（G1 A1 綠、A2 黃、A3 橙；G2 同）；G3a＝黃／橙／紅；G3b＝橙／紅／紅；G4、G5 全紅。ACR 恰為 300：KDIGO 2024 內部寫 30–300（命名表）與 30–299／≥300（他處），輸出 A2 並附 warning。顏色是預後層級，**不是百分比**；需 ≥3 個月持續。

### 3.3 KFRE 4-variable（`ckd.py`）📄/📌
`LP = −0.2201×(age/10−7.036) + 0.2467×(male−0.5642) − 0.5567×(eGFR/5−7.222) + 0.4510×(ln UACR[mg/g]−5.137)`；`risk = 1 − S0^exp(LP)`。係數與中心值在 `PMC7203563` Table 4 與 `PMC11813909` Table 4 grep 驗證。UACR 必須 mg/g（mg/mmol ×8.84，此為肌酸酐分子量換算，非臨床係數）；UACR ≤0 或缺值拒算。適用 CKD G3–G5（eGFR<60，成人）；端點為接受 dialysis／transplant 的 kidney failure，**不是糖尿病腎病變發生率**。無台灣驗證；競爭死亡與新型器官保護藥物未建模。KDIGO 2024 門檻（5 年 3–5%、2 年 >10%、2 年 >40%）為輔助時機的 practice points，**本程式不做自動轉介**。版本狀態見 §1 與 `registry`。

### 3.4 FIB-4／APRI（`liver.py`）📌
FIB-4 = age × AST ÷ [platelets(10⁹/L) × √ALT]（公式見 `PMC13706892` L69；Sterling 2006 付費牆）。切點 <1.3／1.3–2.67／>2.67 與「AASLD 對 >65 歲用 2.0」來自 `PMC13706892` L75 的二手轉載；McPherson 2017 支持 ≥65 歲特異度差。**我自己 grep 不到 Agent 報告所稱「AASLD 2023 原文印 2.67」**（解析文字缺表），因此未採為證據。EASL-EASD-EASO 2024 與 ADA 2026 的年齡分流表本地不可 grep → 這兩套切點為 `spec_only`（程式不宣稱屬於它們）。血小板 10³/µL＝10⁹/L；原始 cells/µL（>2000）拒算並提示。<35 歲 warning、年齡恰為 65 的來源措辭差異 warning、急性疾病排除。APRI = (AST/ULN)×100/platelets，必須提供實驗室 ULN；**不實作 APRI 切點**。FIB-4 低值不排除 T2D 合併多重 cardiometabolic 風險者的進展期纖維化；不是 MASH 確診或肝硬化機率。

### 3.5 IWGDF 2023（`foot.py`）📄
Table 1：0＝無 LOPS 且無 PAD（每年）；1＝LOPS 或 PAD（6–12 月）；2＝LOPS+PAD、LOPS+變形、PAD+變形（3–6 月）；3＝LOPS 或 PAD 且有潰瘍史／下肢截肢／ESRD（1–3 月）。頻率為專家意見。這是照護分層，**不是截肢百分比**。

### 3.6 SCORE2-Diabetes（`cvd.py`）📄
補充文件 Supplementary Methods table 1（L94–L139）係數、中心化（age−60)/5、(SBP−120)/20、TC−6、(HDL−1.3)/0.5、(診斷年齡−50)/5、(HbA1c−31)/9.34、(ln eGFR−4.5)/0.15）、baseline survival 0.9605（男）／0.9776（女）、四個風險區 scale1／scale2，全部 grep 驗證。**官方 Excel（appendix_2.xlsx）8 組輸出（4 區×2 性別，同一組輸入，男性 LP 0.95724968797531651）被重現到小數第 9 位**（男 moderate 13.116444885691047%）。端點：10 年致死／非致死 MI、stroke 或 CVD 死亡；族群：T2D、無既往 CVD、40–69 歲（圖表範圍；derivation 為 >40 歲）、無 severe target-organ damage。補充文件 footnote 的「median baseline survival 0.9625／0.9795」與計算表 0.9605／0.9776 不一致，採官方 Excel 實際使用值。歐洲四區再校準；**台灣不可任選區**；無本地校準。

### 3.7 RECODe（`recode.py`）📄
`risk = 1 − λ^exp(Σβx − mean(Σβx))`（Tables 2–4 footnotes）。實作 9 個有 λ 與 mean 的 outcome：ESRD（0.973／0.23）、severe vision loss（0.921／4.56）、pressure-sensation loss（0.870／4.75）、ASCVD／MI／stroke／CHF／CV 死亡／全因死亡（Table 4）。**論文三個算例（ESRD 8.5%、全因死亡 9%、壓力感覺喪失 13%）重現為 8.53%／9.07%／13.27%**（表格係數取 5 位小數，算例用更高精度，故非逐位相等）。其餘 12 個 microvascular outcome 的 λ／mean 主文未印 → `spec_only`。ACCORD 衍生（年齡 40–79、HbA1c ≥7.5%、CVD 或風險因子），一個 outcome 一條方程，**不可加總**。二元變數編碼（1＝是）依 footnote 算例推定。

### 3.8 TIMI TRS 2°P（T2D 應用，`cvd.py`）📄
`PMC5829964`（Bergmark 2018）：10 項各 1 分（年齡≥75、糖尿病（T2D 永遠 1）、高血壓、現吸菸、PAD、既往 stroke、既往 CABG、心衰竭、eGFR<60（MDRD）、既往 MI），T2D 最低分 1。Table 3 給 SAVOR-TIMI 53 各分組（≤2／3／4／≥5）2 年 KM 事件率；程式輸出分數與**組別參考率（非個人機率）**。來源不一致：Methods「≥75」vs Table 2「>75」（恰 75 歲 warning）。這是 TRS 2°P（**不是** TRS-AD）。

### 3.9 Charlson（`comorbidity.py`）📌
Original 1987（`PMC13721275` Table 1）與 Quan 2011（`PMC13665550` Table A2 與 `PMC13436062` Table 2 兩處一致）權重；`PMC13084228` 把 Quan renal 印成 4（衝突，採兩處一致的 1，附 warning，需對 Quan 2011 原文核對）。輸入以「三個層級群組取最高層」（diabetes：none/uncomplicated/complicated；liver：none/mild/moderate_severe；cancer：none/malignancy/metastatic），所以 diabetes 兩項**結構上不可能重複計分**。任一類別未指定＝未知，不回總分，只給 `lower_bound` 與 `data_completeness`。ICD 對照碼（Quan 2005）在 `PMC13586706` 但本輪未編碼；age-adjusted CCI `spec_only`（兩個開放來源的年齡分段互相不一致）。CCI 是疾病負擔，**不是當代死亡百分比**。

### 3.10 UKPDS Risk Engine（`cvd.py`，provisional）📌
`R(t)=1−exp(−q d^T (1−d^t)/(1−d))`，CHD／stroke 參數見 `PMC3716447`（Yang 2013）Appendix 2–5。該處 `(1 − dt)` 的上標在 XML 即遺失；d^t 是唯一使 R(0)=0 的讀法，但無原文確認 → 需 `allow_provisional=True`。AGE 為**診斷時年齡**；AC 編碼只定義 Afro-Caribbean vs Caucasian／Asian Indian，東亞人未定義（warning）。與 UKPDS Outcomes Model 2 不同；OM2 `spec_only`（Hayes 2013 OA=N，Oxford DTU 頁 403，授權為「Oxford 授權軟體」之二手說法）。

### 3.11 心理與功能量表（`scales.py`）
共通：所有題目必須完整且在範圍內；缺答／越界／非整數 → `None`；**不含題目文字**（請用有授權與繁中驗證的正式版）。缺答處理規則在所有來源中皆 **NOT_FOUND**，所以沒有任何插補。

| 量表 | 計分（本地來源） | 方向 | 切點／行動 | 授權／備註 |
| --- | --- | --- | --- | --- |
| PHQ-9 📄 | 9 題 0–3，0–27（`phq_instructions.txt` L214） | 高＝差 | 5/10/15/20；≥10 yellow flag；item 9 >0 → `safety.item9_positive`（**這是 DMIC 設計選擇，手冊無自動規則**，總分不得覆蓋） | public domain（L336） |
| PHQ-2 📄 | 2 題 0–3，0–6 | 高＝差 | ≥3 → 做 PHQ-9＋面談 | public domain |
| GAD-7 📄 | 7 題 0–3，0–21 | 高＝差 | 5/10/15；≥10 進一步評估 | public domain |
| WHO-5 📄 | 5 題 0–5，raw×4=0–100（WHO 2024） | **高＝好** | raw<13（<50%）→ 進一步評估；完整答題只能是 4 的倍數 | CC BY-NC-SA 3.0 IGO |
| PAID-20 📌 | 0–4 ×20，Σ×1.25=0–100（NDSS） | 高＝差 | ≥40 severe；單題 3–4 分標問題區 | 1995 原版為六點量表（不同）；授權未查到 |
| PAID-5 📌 | 5 題 0–4，0–20 | 高＝差 | ≥8（VUmc 表，二手） | 勿套 ×1.25 |
| DDS-2 📄 | 2 題 1–6，平均 | 高＝差 | 平均 ≥3 | **刊於 Ann Fam Med 2008，非 Diabetes Care** |
| DDS-17 📄 | 17 題 1–6，平均（Fisher 2012） | 高＝差 | <2／2≤x<3／≥3；**用未四捨五入平均**（2.94＝moderate） | 德文二手資料為 0–5 版，**不可混用**；子量表未實作 |
| HFS-II 📌 | Behavior 15 題＋Worry 18 題，0–4，0–60／0–72／0–132 | 高＝多害怕 | 無切點（不編造） | UVA 版權，臨床與非商業研究可用 |
| Mini-Cog 📌 | recall 0–3＋clock 0/2，0–5（作者表單轉載 v.01.19.16） | 高＝好 | <3 陽性；<4 較敏感 | 研究／商業用途需作者許可 |
| MoCA 📌 | 只收評分者填的總分 0–30；教育 ≤12 年且 <30 → +1 | 高＝好 | <26 異常 | 官網 permission 頁（要求訓練）與 FAQ（僅總分時可選）**互相矛盾**；不嵌入任何測驗內容 |
| CFS v2.0 📄 | 臨床判斷 1–9，只驗證與標示 | 高＝更虛弱 | 開發者無數值切點 | 非營利免費；翻譯需許可；<65 歲未驗證 |
| FRAIL 📌 | 5 個 yes/no，0–5 | 高＝差 | 0 robust／1–2 pre-frail／3–5 frail | 各論文題目措辭不同（6 vs 12 個月體重下降等），需固定一版 |

心理量表是**當前症狀／困擾／功能狀態**，不可轉換成未來器官事件風險；各量表 scoring 與 cut-off 請與 psychosocial 報告交叉核對（handoff）。

## 4. calculator 選擇矩陣

證據欄：D＝development；EV＝external validation（有本地全文可見）；TW＝台灣驗證。本 session **沒有任何工具取得台灣本地校準證據**（Taiwan 欄皆「無」，僅列出可能的台灣開發模型）。

| 臨床問題 | 工具（狀態） | 必要輸入（單位） | 時間窗／端點 | 不適用／注意 | 證據等級 |
| --- | --- | --- | --- | --- | --- |
| 共病負擔有多重？ | Charlson original／Quan 2011（secondary） | 14 類（含 3 個層級群組）；ICD 對照未編碼 | 無時間窗；疾病負擔 | 非當代死亡％；未知≠無；DCSI **spec_only** | D：原論文付費牆；EV：無本地；TW：無（台灣 DCSI／CCI 比較 PMID 36977521 未取得全文） |
| 糖尿病特異併發症負擔？ | DCSI／aDCSI | — | — | **spec_only**（rubric 無本地全文） | — |
| 現在腎功能？ | CKD-EPI 2021 cr／cr-cys | 年齡≥18、性別、Scr mg/dL 或 µmol/L、Scys mg/L | 當下 | AKI、肌肉量極端；單次≠CKD | D（官方頁常數）；EV：NEJM 驗證（abstract 層級）；TW：無 |
| CKD 分期與預後層級？ | KDIGO G/A＋熱圖 | eGFR、UACR（mg/g 或 mg/mmol） | 需持續≥3 個月 | 非機率；熱圖顏色來自圖片 | 官方指引 |
| 未來腎衰竭（RRT）風險？ | KFRE 4-var：Original 5y、non-NA 5y（verified）；2y（provisional）；NA（spec_only） | 年齡、性別、eGFR、UACR mg/g | 2／5 年 dialysis／transplant | 僅 CKD G3–G5；不含 AKI、競爭死亡；UACR 非 mg/g 會錯 | D（Tangri 2011，無本地）、EV：Tangri 2016 meta-analysis（31 cohorts）；TW：無（新加坡 SEA 驗證 PMC6894117 為鄰近亞洲） |
| 肝纖維化是否需進一步評估？ | FIB-4（secondary）、APRI（值） | 年齡、AST、ALT（U/L）、血小板 10⁹/L、（APRI 需 ULN） | 當下，分流 | 急性疾病、<35 歲、>65 歲切點不同；T2D 低值不排除 | D：HIV/HCV；EV：McPherson 2017（年齡）；TW：無；EASL／ADA 切點 spec_only |
| 足部潰瘍風險與追蹤頻率？ | IWGDF 2023 | LOPS、PAD、變形、潰瘍史、截肢史、ESRD（皆需明確 True/False） | 追蹤 1–12 月 | 非截肢％；未檢查≠陰性 | 指引（專家意見頻率）；TW：無 |
| T2D 初級預防 10 年 CVD？ | SCORE2-Diabetes | 性別、年齡、診斷年齡、吸菸、SBP、TC、HDL（mmol/L）、HbA1c（mmol/mol）、eGFR、風險區、既往 CVD、TOD | 10 年 MI/stroke/CVD 死 | 40–69；非 secondary prevention；台灣無適用區 | D＋EV（歐洲 5 資料集）；**TW：無**；已重現官方 Excel |
| T2D 多種併發症 10 年風險？ | RECODe（9 outcome 已實作） | 年齡、性別、種族、吸菸、SBP、CVD 史、藥物 4 類、HbA1c%、TC/HDL/Cr mg/dL、UACR mg/g | 10 年各 outcome | 一個 outcome 一方程；ACCORD 族群；不可加總 | D（ACCORD）＋EV（DPPOS 驗證微血管、Look AHEAD 驗證心血管，摘要層級數字）；TW：無（Yang 2024 台灣 EHR 比較僅有績效） |
| 一般群體 CVD/HF（含 HbA1c／UACR）？ | PREVENT | — | 10／30 年 | **spec_only**；2026-10-14 HbA1c 更正未驗證 | D＋EV（設計層面，本地僅主文） |
| 已有動脈粥狀硬化的 T2D 次級風險分層？ | TIMI TRS 2°P（T2D 應用） | 年齡、高血壓、吸菸、PAD、stroke、CABG、HF、eGFR、MI、T2D | SAVOR-TIMI 2 年組別率 | 組別率非個人機率；MDRD eGFR；T2D 需＝是 | EV：SAVOR-TIMI 53＋REACH；TW：無 |
| 初級預防 CHD／stroke（UKPDS 世代）？ | UKPDS Risk Engine（provisional） | 診斷年齡、病程、吸菸、HbA1c、SBP、TC/HDL、AC/AF、horizon | 任意 t（原研究以 10 年為主） | 無既往 CHD/stroke；東亞編碼未定義；d^t 待核 | D：UKPDS（無本地原文）；TW：無 |
| HF 住院風險？ | WATCH-DM | — | 5 年 | **spec_only** | abstract 層級 |
| 低血糖急診／住院風險？ | Karter／Chow 2018 | — | 12 月 | **spec_only**（Karter 點數表本地無；Chow 2018 候選尚未驗證） | — |
| 長期照護需求、心理與功能？ | PHQ-9／GAD-7／DDS／PAID／WHO-5／HFS-II／CFS／FRAIL／Mini-Cog／MoCA | 逐題（見 §3.11） | 各量表回顧期（PHQ/GAD 2 週、DDS 1 月） | 症狀篩檢≠診斷；方向不一致（WHO-5 高＝好）；授權差異 | 計分來源為官方手冊／論文；台灣版本僅指標（PHQ-9 Liu 2011、PAID-C、MoCA 台灣版等），**未驗證繁中版本** |

### 台灣開發的候選模型（皆 spec_only）
- Lin 2017 Sci Rep ESRD 點數（PMID 28860599，Taiwan DCMP）：年齡點數僅印「−2 至 8」而無對照規則，且需 HbA1c／SBP 變異度，Table 4 有「5381」疑似 typo。
- Lin 2022 Sci Rep CKD 點數（PMID 35314714）：score→絕對風險對照在 Supplement S2（未取得）。
- 其他台灣模型（amputation PMID 32446799、stroke PMID 29458073、mortality PMID 33118688、additive CV PMID 41038763）非 OA，未查證。未找到台灣 hypoglycemia／ESKD 方程。

## 5. 測試與執行結果（實際執行）

指令：`python3 -m unittest discover -s tests/calculators`（Python 3.9.6，stdlib）。結果：

```
Ran 102 tests in 0.003s

OK
```

各檔案測試數：test_ckd 20（CkdEpi 7、Kfre 13）、test_cvd 20（Score2Diabetes 9、TimiTrs2p 6、UkpdsRiskEngine 5）、test_recode 12、test_comorbidity 8、test_staging_liver_foot 19（Staging 6、Fib4 8、Iwgdf 5）、test_scales 19（Phq 6、Who5 2、Paid 2、Dds 3、MoreScales 6）、test_registry 4。

向量來源分三類（誠實區分）：
1. **已發表／官方數值**：SCORE2-Diabetes 官方 Excel 的 8 組輸出與 LP（9 位小數）；RECODe 論文三個算例（ESRD 8.5%、全因死亡 9%、壓力感覺喪失 13%，容差內）；PHQ-9 官方手冊算例 16 分；TIMI T2D「最低分 1」、Table 3 組別數與事件率；KFRE LP=0 時風險＝1−S0；KFRE 區域因子與 S0 的一致性檢查。
2. **公式導出的獨立重算**：CKD-EPI（NIDDK 分段式）、KFRE、FIB-4、APRI、UKPDS（q0 封閉解）。這些證明程式實作忠於公式，**不證明公式在本地族群校準**。
3. **邊界與缺值**：每個工具每個必要輸入為 `None`／非正值／越界／型別錯誤／單位歧義 → `None`＋原因；`population_ok=False` 不輸出；spec_only 項目沒有對應函式；沒有輸入就不會輸出數字（registry 測試）。

## 6. 來源不一致與需人工核對

1. KFRE：2 年與 NA 版 S0 無本地原文（handoff 請 methods_ai 核對）。
2. SCORE2-Diabetes：footnote 0.9625／0.9795 vs 計算表／Excel 0.9605／0.9776。
3. Quan 2011 renal：兩處 1、一處 4。
4. TIMI：年齡 ≥75 vs >75。
5. DDS-17：英文 1–6、德文二手 0–5；DDS-2 刊於 Ann Fam Med。
6. MoCA permission 頁與 FAQ 對「是否需認證」矛盾。
7. WATCH-DM 二手表 BMI 列與文字矛盾（0–5 vs 最高 3）。
8. ADA 2026（diabetes ≥65 歲 1.9–2.0）與 AASLD 2023（>65 歲、>2.0）的措辭差異本地無法重驗。

## 7. 限制

- 全部「implemented」只代表**公式忠實實作＋有限範例重現**；沒有任何台灣本地校準或臨床效益驗證，也沒有病人資料。
- 二手轉載（Charlson、FIB-4 切點、PAID、HFS-II、Mini-Cog、MoCA、FRAIL）可能含轉錄錯誤；已標 `implemented_secondary` 並要求對原文核對。
- 缺答規則（問卷）在所有來源皆未找到；若正式版允許缺答處理，須另列規則與有效題數後再改程式。
- 開放的 agent 筆記（`literature/notes/calculators/agent*_tables.md`）含逐字表格轉錄，是否可提交公開 repo 請 lead 依版權政策判斷。
