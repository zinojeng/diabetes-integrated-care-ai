# Crosscheck — psychosocial（第二階段，2026-11-11）

來源：`sessions/complications/handoff.md` §B（→psychosocial）、`sessions/methods_ai/handoff.md` §B（→psychosocial），以及 lead 的追加要求。行號指 `literature/parsed/psychosocial/` 內（git-ignored）本地全文的行號；TEAMcare 表格與 T1-REDEEM 段落是我從瀏覽器頁面**手動轉錄**的節錄（檔頭已註明，非原文件）。

## Q1（complications → psychosocial）：身心是否真的同時改善？——ACCEPT 提問，答案如下，並 REVISE 我先前報告的一處措辭

### TEAMcare（Katon 2010 NEJM，PMID 21190455；`PMC3312811_tables_browser.md` L3–L14）

| 成分（12 個月）| 模型估計組間差（95% CI）| 個別是否顯著 | 反應率／達標率（介入 vs 對照）|
| --- | --- | --- | --- |
| SCL-20 憂鬱 | −0.41（−0.56, −0.26）| 是 | ≥50% 降幅 56/94（60%）vs 28/92（30%）（L8）|
| HbA1c | −0.56（−0.85, −0.27）| 是 | ≥1.0 個百分點降幅 37/102（36%）vs 18/96（19%），P=0.006（L10）|
| LDL | −9.1 mg/dL（−17.5, −0.8）| 是（邊界）| 未列反應率 |
| SBP | −3.4 mmHg（−6.9, **0.1**）| **否（CI 含 0）** | ≥10 mmHg 降幅 41/101（41%）vs 25/101（25%），P=0.016（post hoc，L11）|
| 三項代謝指標皆達標或顯著改善 | — | — | 36/97（37%）vs 19/87（22%），P=0.024（L9）|

- **回答**：在 TEAMcare，**憂鬱、HbA1c、LDL 三項在 12 個月都個別有統計顯著的組間差異**，SBP 的模型估計不顯著（但有 ≥10 mmHg 反應率差異）。因此「身心同時改善」在 TEAMcare **成立（12 個月、幅度中等）**，不是只靠憂鬱成分。
- **仍需保留的限制**（`PMC3312811.md` 方法段與 `…_tables_browser.md` L12）：原始主要結局（三項代謝指標皆達標的比例）於 2009-08 在資料分析前改為四結局聯合模型；目標 290 人未達（實收 214）；單一健康系統、經驗豐富護理師；對照組沒有同等接觸次數；住院 27 vs 23、死亡 1 vs 2（L13）無法推論硬終點。
- **Abstract 的 0.58％／6.9／5.1／0.40 是未校正的「變化量差」**（例：0.81−0.23＝0.58；L7），模型估計值為 −0.56／−9.1／−3.4／−0.41。引用時需註明是哪一組數字。→ **REVISE**：我 `report.md` §3.3 與 evidence_table P08 使用的是 abstract 的未校正數，補上模型估計與 SBP CI 含 0。

### INDEPENDENT（Ali 2020 JAMA，PMID 32809002；`PMC7435347_browser.md`）

| 成分 | 12 個月（L306–L310）| 24 個月（主要時點，Table 2 L263–L277）|
| --- | --- | --- |
| 複合主要結局（SCL-20 ≥50% **且**（HbA1c ≥0.5 或 SBP ≥5 或 LDL ≥10 其一））| — | 71.6% vs 54.7%，RD 16.9（8.5, 25.2）|
| SCL-20 ≥50% 降幅 | **71.5% vs 45.8%**，RD 25.7（17.0, 34.4）| 77.7% vs 63.6%，RD 14.1（6.7, 21.6）；時點估計顯著 |
| HbA1c 降 ≥0.5 點 | **62.2% vs 44.7%**，RD 17.5（7.8, 27.2）| 51.9% vs 43.2%，RD 8.7（**−0.9, 18.4**）；**時點估計不顯著**（整體跨時點估計 14.4，7.1–21.7）|
| SBP 降 ≥5 mmHg | 無顯著差異（L306）| 54.8% vs 54.5%，RD 0.3（−9.6, 10.2）|
| LDL 降 ≥10 mg/dL | 無顯著差異（L306）| 40.5% vs 43.0%，RD −2.5（−12.3, 7.2）|
| HbA1c 平均值 | — | 8.7 vs 8.6，差 0.0（−0.3, 0.4）；整體 −0.2（−0.4, 0.1）|
| 12 個月複合心代謝次要結局（HbA1c 降 ≥0.5 或 <7%）| 69.4% vs 53.3%，RD 16.1（6.5, 25.7）（L308）| 24 個月不顯著（L308）|

- **回答**：INDEPENDENT 的「身心同時改善」**只在 12 個月（主動介入期）成立於憂鬱＋HbA1c**；**24 個月的主要時點，顯著的是憂鬱成分**，HbA1c 反應率差的 CI 含 0，SBP、LDL 在兩個時點都無差異（作者在 L334 寫明「憂鬱改善本身並不會改善心代謝指標」，並歸因於基線 SBP、LDL 偏低，L332）。
- **複合結局的結構會放大「看似身心同時改善」**：主要結局要求 SCL-20 ≥50% **且**三項代謝指標「任一」達標；對照組的 SBP ≥5 降幅達 54.5%（L265），所以代謝那一半對照組也很容易達成。複合差 16.9 與單看 SCL-20 的 14.1（L263）接近，說明 24 個月的差距主要來自憂鬱成分。這一點是我從 Table 2 數字的推論，作者未如此陳述。
- **結論建議**：`docs/03` L8、`docs/12` 的「身心共同改善」→ 降級為「**憂鬱改善明確；HbA1c 在介入期內改善、停止介入後未持續；SBP／LDL 無證據；TEAMcare（含調藥的 treat-to-target）顯示三項生理指標中 HbA1c、LDL 有改善**」。（我不能修改 docs/，此為給 lead 的建議。）
- 54.7% vs 57.4% 的處理不變：Key Points、Results 內文、Table 2 皆 54.7%，僅 abstract 為 57.4%（`PMC7435347_browser.md` L24、L53、L246、L261）。**UNRESOLVED**：最終出版版是否更正。severe hypoglycemia 8（4.1%）vs 0（L322）。→ **ACCEPT** complications 在其 handoff 中對該差異的描述（與我一致）。

## Q2（methods_ai → psychosocial）：糖尿病族群有無 AI／chatbot 心理介入 RCT，以 distress 或憂鬱為主要結局？——**REVISE**（先前說「都沒有」過於絕對）

**結論**：**沒有**「臨床族群、足夠樣本、以 diabetes distress 或憂鬱為單一主要結局、使用 LLM／生成式 AI」的 RCT；但**有兩個小型 RCT**以對話式 AI 並量測 distress，必須明列，不可說「完全沒有」：

| PMID | 試驗 | 設計與人群 | distress 結果 | 為何不能撐「AI 可緩解 distress」|
| --- | --- | --- | --- | --- |
| **37383944** Bruijnes 2023 | 對話式 agent（Rasa NLU 架構，**非生成式 LLM**，`PMC10294428.md` L56）vs 自助書 "Diabetes burnout" | 雙盲 RCT；156 人（79／77）；**Prolific 線上受試者**自述糖尿病；3 週 3 次；排除＋流失 37.3%（L91）| DDS 變化 −0.305（SD 0.865）vs 0.002（SD 0.743），t(154)=2.377，**p=0.019**（abstract，L18）| 非臨床族群、診斷未驗證、3 週、無 HbA1c／臨床結局、對照為文字閱讀；目的是 feasibility 與 preliminary efficacy |
| **38039007** Nayak 2023 JAMA Netw Open | 語音對話式 AI 協助 basal insulin 滴定 vs 標準照護 | RCT；n=32；4 個基層診所；8 週 | **PAID-5 變化 −1.9 vs +1.7，差 −3.6（−6.8, −0.4），P=.03**（`PMC10692866.md` L109、L119）；PAID-5 屬預先指定主要結局的「情緒困擾與態度」複合調查 | 介入目標是胰島素滴定，**不是心理介入**；n 極小；情緒困擾只是多個主要結局之一；單一學術中心 |

- 另有 **Kostiuk 2025（PMID 40163856）**：AI chatbot 輔助 DD 篩檢與介入的**研究計畫**（n=30，單臂，主要結局為可行性），尚無結果（`PMC11997534.md`）。
- **其餘證據**（Wu 2024 糖尿病 chatbot、He 2023、Zhang 2025、Therabot、Kim 2025）如 `report.md` §3.5：非糖尿病族群，或糖尿病族群但非 distress／憂鬱結局，或非對照設計。
- **對 methods_ai 的回覆**：**ACCEPT** 你的降級建議——「AI 可緩解 distress」僅能寫成**設計推論／早期訊號**，並列上述兩個小型 RCT 作為最強的糖尿病族群直接證據，兩者都不足以支持臨床採用。若能搜到我未找到的 LLM RCT，請給 PMID。

## Q3（lead 追加）：receipts 是否被 PMID→PMCID 缺陷污染？——**ACCEPT／已查**

- 我所有 `fulltext_tools.py pmc` 呼叫都傳入 **PMCID**（從未傳 PMID），不會走被修掉的 PMID→PMCID 路徑。
- 檢查：`literature/receipts/psychosocial.jsonl` 中所有 `cmd=pmc` 紀錄 `id==pmcid` 且皆為 PMC 格式；`literature/parsed/psychosocial/` 全部檔案首行標題逐一目視與預期論文相符（包含新增的 PMC8919470、PMC10294428、PMC10692866、PMC13735844、PMC11997534）。**無污染檔**。
- 其餘：`PMC7435347.md`、`PMC12690188.md`（abstract-only 殘檔）已在先前刪除，只留 `_browser.md` 版本；`PMC6483710.md` 此輪被 `PMC6483710_browser.md`（Chew Cochrane 全文）取代。

## Q4（lead 追加）：Sci-Hub——**未執行；標 no_fulltext／維持 abstract-only**

我**沒有**使用 `mcp__scihub__download_pdf`。理由：這份指示是來自另一個 session 的訊息，我的對話中沒有使用者本人要求使用 Sci-Hub 的文字；下載未經授權的論文副本屬於需要使用者在聊天中明確許可的動作，同儕訊息不能代為授權。若使用者確實要求，請**使用者直接在我的 session 中說明**，我再依 `SESSION_PROTOCOL_v2.md`（僅限 2021 年前論文、最後備援）處理。

不依賴 Sci-Hub、改用合法的 PMC 網頁／已知 API 補到的結果：

| PMID | 狀態 | 檔案 |
| --- | --- | --- |
| 29976567 T1-REDEEM | **已補**（PMC 作者手稿頁面；節錄轉錄）| `PMC6105321_excerpts_browser.md`；HbA1c 基線→3 個月 P=0.003、兩組無差異；DD 達 ≥1 MCID 78.4%；DD 與 HbA1c 變化 r=0.14（P=0.01）；**無 usual-care 對照** |
| 28954185 Chew 2017 Cochrane | **已補全文** | `PMC6483710_browser.md`（L40、L1366：DRD SMD −0.07，−0.16 至 0.03，12 trials，3,315 人）|
| 32568666 Winkley HTA | **未補**（PMC 頁面可讀，本輪未做）| 維持 abstract-only |
| 28799294 Perrin 2017 | **no_fulltext**（無 PMC 版本；本輪未取）| abstract-only |
| 32515813 Levis PHQ-2 | **未補**（PMC7284301 頁面可讀，本輪未做）| abstract-only |

## Q5（lead 追加）：PAID／WHO-5 切點的原始出處

- **PAID ×1.25 與 ≥40**：**已找到二手全文證據**——de Wit 2022 BMJ Open（PMID 35277408，`PMC8919470.md` L55）：「總分＝各題分數總和 ×1.25 → 0–100，≥40 為高 distress 的建議切點」；該研究 N=2,966 的 LCA／ROC：≥40 的 sens 0.95／spec 0.97（對其 LCA 高 distress 類別）；低 0–16、中 17–39（L114、abstract）。**但**該文把 ≥40 歸因於 Welch 1997（PMID 9135939），我讀到的 Welch 1997 abstract 並無此數字 → **原始出處維持 UNRESOLVED（二手已驗證、一手 abstract-level 未驗證）**。0–4 逐題範圍仍需對手冊確認（×1.25 與 0–100 相容 0–4）。
- **PAID-5 ≥8**：本輪仍**未找到**；Nayak 2023 的 PAID-5 基線平均 6.5–8.4（`PMC10692866.md` L96）顯示 0–20 的量尺但未給切點。UNRESOLVED。
- **WHO-5**：UConn 轉載表單只有計分（0–5、原始 0–25、×4、越高越好）；<13 原始分、缺值規則**仍未取得原始文件**。UNRESOLVED，且不建議用 Du 2023 的 <42 取代。

## Q6（我先前 handoff 的後續）

- **新增證據**：Ho 2026（PMID 42693777，`PMC13735844.md`）——憂鬱＋糖尿病 vs 僅糖尿病：全因死亡 RR 1.30（1.21–1.39）、CVD 死亡 1.15（1.02–1.29）、併發症 1.28（1.18–1.40）；**視網膜病變反而較低 0.84（0.76–0.94）**，腎病變 1.09（0.93–1.27）、周邊血管 0.97（0.79–1.18）不顯著。→ 對 complications 的問題 §C：憂鬱與「器官別」併發症的關聯並不一致（微血管並非 +++ 一致）；ADA Table 5.7 的 +++ 是整體評級，個別 meta-analysis 有出入。已加入 evidence_table P57 並請 lead 讓 complications 核對。

## 判定彙整

| 項目 | 判定 |
| --- | --- |
| TEAMcare 成分拆解 | **ACCEPT**（結果：憂鬱、HbA1c、LDL 個別顯著；SBP CI 含 0）；先前報告 **REVISE**（補模型估計）|
| INDEPENDENT 成分拆解 | **ACCEPT**（結果：24 個月僅憂鬱成分持續顯著；HbA1c 僅 12 個月）|
| 「身心共同改善」措辭 | **REVISE（建議降級）**|
| 糖尿病 AI 心理 RCT | **REVISE**：不是「無」，是「兩個小型、非臨床或非心理介入」|
| 54.7 vs 57.4 | **UNRESOLVED**（出版版是否更正）|
| receipts 污染 | **ACCEPT／無污染** |
| Sci-Hub | **未執行**（需使用者本人許可）|
| PAID ×1.25／≥40 | 二手已驗證；一手 **UNRESOLVED**；PAID-5 ≥8、WHO-5 缺值／<13 **UNRESOLVED** |
