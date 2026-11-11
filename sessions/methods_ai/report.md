# methods_ai：AI 在糖尿病照護的證據版圖與方法學審查

查核日期：2026-11-11（Asia/Taipei）。執行者：methods_ai session（Claude）；Codex 為最後確認者。
標記：📄 = 本地全文已 `grep` 驗證（可用 `python3 -I literature/notes/methods_ai/claim_checks.py` 重現，0 MISS）；📌 = 僅 abstract／搜尋摘要／metadata，不做具體數字斷言；`UNRESOLVED` = 未能核實。
範圍聲明：這是針對指定問題的**定向證據綜整**，不是 systematic review（單一資料庫為主、無雙人篩選、無 PRISMA）。本文件**沒有完成**正式 RoB 2／ROBINS-I／PROBAST／QUADAS-2 評讀表；§5 的表格是「單一審查者、依全文段落做的初步篩檢」，不得引用為已標準化評讀。

---

## 0. 一頁結論

1. **證據層級越往下越薄。** 診斷準確度（autonomous DR AI）與流程完成度（ACCESS）有隨機或前瞻證據；中間生物指標只有小型或短期 RCT（voice insulin、iNCDSS、傳統 EHR CDS）；本輪**沒有找到**任何 AI 介入在糖尿病族群上以 hard endpoint（失明、ESKD、截肢、心血管事件、死亡）為主要結果的試驗。「整合式多 agent」在糖尿病併發症照護上沒有公開的隨機評估。
2. **LLM／RAG 的糖尿病研究幾乎全是離線評估**：專家評分、文字相似度、vignette。GPT-4 複雜 T2D 病例中，40% 的推理被專家認為有幫助，但判斷「計畫是否理想」的 specificity 只有 35%，且 25% 的解釋含 decontextualized 陳述。Kenya 的 LLM 輔助試驗（非糖尿病）14 天治療失敗無顯著差異。
3. **標籤要小心**：voice insulin 的 VBAI 本身是「rules-based and deterministic」的滴定協議，AI 部分是語音介面；ACCESS 的 100% 完成率有一部分是「介入本身就是做檢查」的構念效應；DR pivotal 的 900 是收案數，分析樣本是 819。
4. **風險預測**：ML 預測糖尿病併發症的系統性回顧一致顯示外部驗證少、PROBAST 高 bias（DR 15/15、DPN 15/15 高 risk of bias；DKD 26 項研究僅 8 項有外部驗證）。傳統 calculators 在台灣族群也需要重校準（Su 2024）。ML 對 KFRE 等傳統 calculators 的直接頭對頭比較，本輪檢索**未找到**。
5. **既有文件須修正**：`docs/07`、`docs/08` 的主要數字大致正確，但有 3 類問題：(a) 遺漏關鍵限定（CI、分母、事前規格）；(b) 一個 PMC 連結格式錯誤；(c) 5 項敘述本輪無法獨立核實（見 §8）。
6. **Kenya 試驗的原始數字與 aOR 方向在來源中不一致**（原始失敗率 LLM 組較高，但 aOR 0.77），解讀時必須保留此註記（§2.4、§8）。

---

## 1. 四層證據對照表

| 層級 | 本輪納入的代表研究 | 可以說什麼 | 不能說什麼 |
| --- | --- | --- | --- |
| ① Diagnostic accuracy | Autonomous DR pivotal（PMID 31304320）📄 | 在 819 名可分析者中，mtmDR sensitivity 87.2%、specificity 90.7%、imageability 96.1% | 降低失明；900 並非每個指標的分母 |
| ② Workflow／process | ACCESS RCT（38212308）📄；ambient scribe RCT（41497288）📄；TMU 護理交班（41819121）📄；iNCDSS 的醫師負擔未量測 | 眼底檢查完成率、文書時間 | 照護品質或病人結局改善 |
| ③ Intermediate biomarkers | iNCDSS（40332936）📄；voice insulin（38039007）📄；O'Connor CDS（21242556）📌 | TIR、達標時間、HbA1c／BP 的短期差異 | 長期併發症減少；voice 的 adherence 是自填 |
| ④ Patient-important outcomes | 無 AI-糖尿病試驗。非 AI 對照：Steno-2、CARRS、ADDITION（見 `docs/12`，本輪未重驗） | 僅能說「整合照護（非 AI）有部分硬終點證據」 | 不得把 Steno-2／CARRS 效益歸因給 AI |

另有一類**非療效證據**：LLM 離線評估（He 2026、Guo 2026、Wang 2025、DIASENTINEL）——是模型輸出品質，不屬於以上四層。

---

## 2. 實證版圖（逐層）

### 2.1 Diagnostic accuracy

- **Pivotal（Abràmoff 2018，PMID 31304320）📄**：前瞻、10 個 primary care 站點，以 Wisconsin FPRC 為參考。900 人收案、892 人完成、**819 人可完整分析（92%）**，198 人（23.8%）有 mtmDR。Sensitivity 87.2%（95% CI 81.8–91.2）、specificity 90.7%（88.3–92.7）、imageability 96.1%（94.6–97.3）。未分析的 73 人在 lens status 等條件上與可分析者不同（可分析者 89.6% 為 pseudophakic／無 lens opacity，不可分析者 52.1%），所以效能適用於「影像可取得」的族群。
- **限制**：沒有失明或視力終點；排除既往有 DR 史者。QUADAS-2 未做正式評讀（§5.3 只列初步觀察）。
- **DRES-POCAI（Diaz 2025，41118165）📄**是 protocol（open-label 平行 RCT，FQHC），**沒有結果**，不得當作療效證據。
- **Tanzania DR AI RCT（Cleland，Lancet Glob Health 2026，42863478）**：僅 metadata，未取得全文，不做任何斷言。

### 2.2 Workflow／process outcomes

- **ACCESS（Wolf 2024，38212308）📄**：8–21 歲 T1D／T2D，單一學術兒童糖尿病中心；預先註冊 NCT05131451；分層 permuted-block 隨機。164 人隨機（81 vs 83），主分析 81 vs 82（1 名對照因誤納另一研究被排除）。眼底檢查完成 81/81（100%）vs 18/82（22%）。AI 判 DED present 的 25 人中 16 人（64%，95% CI 43–81）完成眼科轉介。
  - **構念問題**：AI 組的「完成」就是在診間做完 AI 檢查，對照組要靠轉介並到院外完成。這證明「把檢查帶到病人面前」有效，但不能拆出「AI 判讀」本身的貢獻。
  - **分母不可混用**：16/25（AI 陽性者）與對照 18 人（22%；全部對照者，原文 follow-through 未列分母，主要結局 Table 3 為 18/82；此 18 人無一有 DED）不是同條件比較；仍有 9/25 AI 陽性者沒有完成眼科追蹤。
  - 沒有視力或失明終點；單一中心、青少年，不能外推到高齡多重共病。
- **Ambient scribe（Lukac，NEJM AI 2025，41497288）📄**：238 位門診醫師、14 專科，單一學術機構、僅英文、2024-11-04 至 2025-01-03（約 2 個月）。Nabla 組 time-in-note −9.5%（95% CI −17.2 至 −1.8；P=0.02；事先設定的多重校正 α=0.025）；DAX −1.7%（−9.4 至 +5.9；P=0.66）。
  - DAX 使用於 33.5% 的就診、Nabla 29.5%；約 15% 的處置組醫師從未使用。
  - 燃盡等問卷屬次要終點，**作者未做假設檢定**，僅報估計值與 CI。
  - 作者自述試驗登記為「postcommencement」（開始後才登記）。
  - 不是糖尿病試驗；−9.5% 是相對變化，不是 percentage points。
- **台北醫學大學體系護理交班 LLM（Coristine，JMIR 2026，41819121）📄**：TMUH、萬芳、雙和三院；前後比較（2024-09 基線 log vs 2024-10 至 12 月導入後）。每位病人交班文件完成時間平均由 3.45–4.32 分鐘降至 1.17–2.54 分鐘；節省「每月 474–981 小時」是以病人量**估算**，不是實測。無對照組，基線僅一個月（作者自述基線不穩）。非糖尿病、非隨機。
- **Kenya（Agweyu，Nat Med 2026，42362867）📄**同時屬 §2.4。

### 2.3 Intermediate biomarkers

- **iNCDSS（Ying，JAMA Netw Open 2025，40332936）📄**：3 家中國醫學中心的住院 T2D，單盲、non-inferiority（margin −6 percentage points）、5 天。149 人隨機（75 vs 74），13 人中途停止；TIR（70–180 mg/dL）76.4% vs 73.6%，差 2.7 pp（95% CI −2.7 至 8.0），下界高於 −6。ML 為基礎的胰島素滴定建議，**每日由醫師覆核**；comparator 是資深內分泌醫師，不是 usual care。排除嚴重器官疾病與心理／精神疾病；平均 HbA1c 9.0%；5 天住院資料不能外推到門診長期。次要終點未預先設 NI margin（作者稱屬 exploratory）。**在解析全文未找到試驗登記編號，UNRESOLVED。**
- **Voice-based AI basal insulin（Nayak，JAMA Netw Open 2023，38039007）📄**：MIVA 試驗，open-label、decentralized、computer-generated permuted-block。39 人隨機、**32 人**完成收案並進入分析。達 optimal dose 中位 15 天（IQR 6–27）vs >56 天；adherence 82.9% vs 50.2%（差 32.7%，95% CI 8.0–57.4）。
  - 原文：VBAI「was rules based and deterministic」，由臨床醫師在入口網站選擇滴定協議——AI 角色是語音互動，不是自行決定劑量。
  - 限制：n=32；對照組日誌不完整，需回溯病歷；adherence 為自填；觀察 8 週且以 FBG 而非 HbA1c；**解析全文未找到登記編號（UNRESOLVED）**。
- **O'Connor 2011（Ann Fam Med，21242556）📌（PMC 僅 abstract）**：clinic-randomized、11 診所、41 位醫師、2,556 名病人，EHR CDS 針對 HbA1c／BP／LDL 高於目標者。HbA1c −0.26%（95% CI −0.47 至 −0.06；P=.01），SBP 控制維持 80.2% vs 75.1%（P=.03），LDL 無改善（P=.62）。這是傳統規則型 CDS，不是 AI。
- **CGM-AI 決策支援**：本輪檢索（#20）零命中；沒有找到以 HbA1c／TIR 為主要結果的 CGM-LLM／RAG 隨機試驗。Guo 2026 與 GlyRAG（僅 metadata）屬離線評估（§3）。

### 2.4 Patient-important outcomes

- 在糖尿病族群，本輪**沒有**找到以硬終點為主要結果的 AI 介入試驗（UNRESOLVED：非全面檢索，不能證明不存在）。
- **最接近的是 Kenya 14 天治療失敗（非糖尿病）📄**：16 間 Penda Health 診所，103 位 clinical officer 為集群（52 vs 51），9,691 人收案、**9,347 人進入主要分析**（LLM 4,693 vs 對照 4,654）。治療失敗 102（2.2%）vs 94（2.0%）；**aOR 0.77（95% CI 0.55–1.08，P=0.13，已調整 facility 與 clinical officer）**。
  - 來源內部矛盾：原始比例 LLM 組較高，但 aOR 小於 1。以原始表格自行計算的未調整 OR 約 1.08（我的計算，非作者報告）。作者以 facility／clinical officer 隨機截距調整，文中未解釋方向差異的來源。**引用時兩組數字與 aOR 須並列，不得只寫其一。**
  - 試驗針對 50% 相對降低（2%→1%）設計；作者估計真實效應介於每千人少 13 例到多 1 例。9,702 個合格就診中排除 254 件（協議不遵從，含 45 件因 EMR 設定錯誤使對照醫師接觸到 AI Consult）與 90 件失訪（LLM 組 61、對照 29，**失訪不平衡**）。
  - 結論：未顯示減少 14 天治療失敗，未發現安全訊號；但信賴區間寬，不能解讀為「無效」。

---

## 3. LLM／RAG／agentic workflow

| 研究 | 做了什麼 | 結果（📄） | 層級與限制 |
| --- | --- | --- | --- |
| **Wang 2025（41140742）GPT-4 複雜 T2D** | 243 份 UCSF 複雜 T2D 臨床筆記；zero-shot GPT-4 抽取目標、判斷計畫是否理想、提出改進；5 位 diabetologist 評審；230 份抽樣分成兩組各 115 份 | 計畫判斷（115 份）accuracy 64%、precision 80%、recall 73%、**specificity 35%**；40% 推理被認為有幫助；hallucination：decontextualized 29/115（25%）、nonfactual 7/115（6%）、self-conflicting 1/115（1%） | 離線專家評估；無病人結局；單一三級中心；「有幫助」是專家主觀判斷 |
| **He 2026（41662664）JMIR Form Res** | 3 個小型模型（Llama 3.1-8B、Qwen3-8B、GLM4-9B）以 LoRA 在 West China Hospital 2022 年 1–2 月門診病歷微調，嵌入 RAG 原型 | GLM4-9B BLEU-4 67.93（SD 2.74）、ROUGE-1 44.30、ROUGE-L 37.67；5 位內分泌醫師盲評 300 條建議（Likert），微調後 usefulness 平均 >4 | **作者自述僅受控環境、未前瞻驗證**；BLEU／ROUGE 衡量的是與歷史醫囑的文字重疊，不等於臨床正確；單一機構 |
| **Guo 2026（42544991）RAG-CGM counseling** | 檢索增強 LLM 對話代理，12 個合成 CGM 個案，6 位英國資深糖尿病臨床醫師，盲源評分 | 288 則回應、864 筆評分；CA 4.37（SD 0.57）vs 臨床醫師 3.58（SD 0.90），差 0.782（95% CI 0.692–0.872）；重大安全疑慮各 3 件（0.7%） | vignette 設計、CA 回應較長、小型評審團；作者明言不能用於自主治療決策。對比的是**臨床醫師在研究情境下撰寫的文字**，不是實際看診溝通 |
| **DIASENTINEL（EMNLP 2026 Demos，pp. 320–329）** | Far Eastern Memorial Hospital 單院資料；on-premise 多 agent：校準風險模型＋ADA 指引 RRF 檢索＋規則／LLM entailment 驗證 | 一年新發 T2D 風險：held-out n=4,982，AUROC 0.737（0.694–0.773），Brier 0.054；p=0.5 時 sensitivity 0.473、PPV 0.162、F1 0.242；XGBoost AUROC 0.731、LR 0.697（CI 重疊）；entailment judge 在 20+20 合成配對上 sensitivity 80%／specificity 100% | 系統展示論文；驗證測試為合成錯誤注入（小樣本）；無臨床結局或使用者研究；作者自述子群公平性「future work」 |
| **Lukac 2025 scribe** | 見 §2.2 | 醫師回報 inaccuracies「occasionally」（DAX 2.7，Nabla 2.8，5 分制） | 偶發不準確屬安全面訊號，仍需人工覆核 |

**幻覺與安全性的實測量尺（供 §7 使用）**：Wang 2025 的三類 hallucination 分類（decontextualized／nonfactual／self-conflicting）、DIASENTINEL 的錯誤注入式驗證、Guo 的 safety flag、Lukac 的 inaccuracy／bias Likert。目前沒有統一量表；各研究定義不同，不能跨研究合併率。

---

## 4. 整合式（跨 EHR、共病、併發症）AI 架構的公開描述

| 來源 | 公開描述 | 證據層級 |
| --- | --- | --- |
| DIASENTINEL 📄 | 端到端參考架構：資料抽取→風險函數→指引檢索→報告生成→驗證 agent→醫師 ACCEPT／OVERRIDE | 系統展示；範圍是「一年新發 T2D」，不涵蓋已確診者的併發症管理 |
| 奇美 A+ Copilots 📄（網頁） | 2023-11 起分批導入；A+ Doctor／Nurse／Pharmacist／Nutritionist／Patient Safety；藥事 copilot 自 2024-04 | 微軟合作刊載的新聞稿（署名 Chen May Yee，圖片註明 for Microsoft），無硬資料；頁面無 diabetes 字串。藥師「每日看診人數 15→30」為院方受訪說法；護理師燃盡分數下降來自約 20 名護理師的初步問卷。2024-05 約 36,000 次使用、3,500 位使用者 |
| 北醫體系護理交班 📄 | 見 §2.2 | 前後比較 |
| 健保署糖尿病風險評估與智慧衛教 📌 | 2026-03-04 公布；40 間診所（北 7、中 29、南 4）；與台北醫學大學、國衛院、四個糖尿病專業學會及 Google 合作；AI-on-DM 風險模型；結合 DCSI 與生成式 AI 衛教；經健康存摺顯示。Google 稱單案處理由 20 分鐘降至 25 秒、90 分鐘內可篩 20,000 人 | **僅搜尋摘要（官方頁面 HTTP 403，Tavily 回空）**；效率數字為廠商說法；搜尋未找到成效評估 |
| 國衛院糖尿病 LLM 對話機器人計畫 📄（頁面） | 計畫名「基於大語言模型的糖尿病照護對話機器人於病患提問回答品質及糖尿病長期照護的效益評估」，編號 NSTC114-2314-B400-014，Date 2025；摘要寫明目的為評估回答適切性與病情控制效益 | 研究計畫描述，無結果；`docs/08` 所寫「2025 年 8 月至 2026 年 7 月」未在頁面文字中找到（UNRESOLVED） |
| 三總 MEDIC GenAI 📌 | 無法佐證（HTTP 403；搜尋只找到 2023 年三總與微軟的醫療大數據專案） | UNRESOLVED |
| OpenClaw／Hermes Agent | 官方頁面可連線（HTTP 200） | 僅確認頁面存在；為通用軟體，非臨床證據。「Globart」未找到官方來源，維持原文件「不列為已確認方案」 |

**判讀**：公開描述中，真正有量化評估的只有「文書時間」類（護理交班、scribe）；跨 EHR 的整合式架構缺少臨床結局、錯誤率、alert 負擔、轉診閉環的公開量測。

---

## 5. 方法學審查

### 5.0 聲明

以下表格由單一審查者依本地全文段落做**初步篩檢**，採 RoB 2 的五個 domain 命名，但**未走 signalling-question 演算法、未雙人獨立、未取得試驗方案與統計分析計畫**；因此不構成「已完成 RoB 2 評讀」。PROBAST／QUADAS-2 同理。若 lead 需要可引用的標準化評讀，需另外安排正式評讀。

### 5.1 RCT 的初步 RoB 2 風格篩檢（不是正式評讀）

| 研究 | D1 隨機化 | D2 偏離介入 | D3 缺失資料 | D4 結果測量 | D5 選擇性報告 | 主要顧慮 |
| --- | --- | --- | --- | --- | --- | --- |
| ACCESS 📄 | 分層 permuted block，無明顯顧慮 | 無法盲化（介入即檢查）；ITT 描述 | 對照 1 人因誤納排除 | **構念顧慮**：AI 組的「完成」就是介入本身 | 預先登記 NCT05131451 | 結果指標與介入重疊 |
| Voice insulin 📄 | 電腦產生 permuted block | open-label | 39 人隨機、32 人分析，7 人未入分析的原因與組別在已讀段落未逐一核對 | adherence 自填；對照日誌不完整 | **未找到登記編號** | 小樣本、自填、補查病歷 |
| iNCDSS 📄 | 區塊隨機＋密封不透明信封 | 單盲；醫師覆核每日建議 | 13/149 中途停止（7 vs 6），有多重插補敏感度分析 | CGM TIR 為客觀 | **未找到登記編號**；次要終點無 NI margin | comparator 為資深醫師、5 天 |
| Scribe RCT 📄 | covariate-constrained randomization | 無法盲化；約 15% 處置組從未使用 | ITT 分析 | time-in-note 為 EHR 客觀指標；問卷為自填 | 登記在開始後；次要終點未做檢定 | 單一機構、2 個月 |
| Kenya 📄 | 以 clinical officer 為集群 | 45 件對照醫師因 EMR 設定錯誤接觸 AI Consult；同機構內交流污染（作者承認） | **失訪不平衡（61 vs 29）**；254 件因協議不遵從排除 | 專家小組盲於分組判定 | 已登記 PACTR202502499779176 | 原始比例與 aOR 方向不一致；以 50% 相對降低設計，對小效應檢定力不足 |

### 5.2 因果語句、effect direction、CI、終點層級核對

| 項目 | 核對結果 |
| --- | --- |
| ACCESS：「提高篩檢與追蹤」 | 完成率差異為 randomized 主要結果；追蹤 64% vs 22% 屬次要且分母不同，不得寫成純 AI 效應 |
| Scribe：「減少文書時間」 | 僅 Nabla 達顯著；DAX 不顯著；兩者合併不能寫「scribe 減少時間」 |
| iNCDSS：「優於／相當於醫師」 | 只能寫「非劣於」（lower bound −2.7 > −6）；差 2.7 pp 的 CI 含 0，不是優效 |
| Voice insulin：「改善血糖」 | 主要指標為達標時間與 adherence；HbA1c 未作主要結果，勿寫成改善 HbA1c |
| Kenya：「無效」或「有效」 | 兩者皆不成立：aOR 0.77（0.55–1.08），CI 含 1；原始比例方向相反（§2.4） |
| GPT-4：「專家認為有幫助」 | 40% 的推理有幫助 ≠ 臨床改善；對「可再改進的計畫」的辨識（specificity）僅 35%，需另檢視誤判型態 |
| He 2026：「strong potential」 | 作者結論用語；指標為 BLEU／ROUGE＋專家 Likert，非臨床結局 |
| Guo 2026：「品質高於臨床醫師」 | 僅限 vignette、盲源評分、研究情境；不能寫成取代臨床溝通 |
| DIASENTINEL：「reliable／auditable」 | 驗證測試為合成注入，n=12+12 與 20+20；風險模型 PPV 0.162 |

### 5.3 診斷準確度（QUADAS-2 風格觀察，非正式）

Pivotal：參考標準為獨立閱讀中心（降低 reference standard 偏誤）；可分析比例 92%，不可分析者在 lens status 分布不同（患者選擇／流程偏誤風險）；排除既往 DR 史者影響適用性。

### 5.4 預測模型（PROBAST+AI 視角）

PROBAST+AI 有「模型開發」16 個與「模型評估」18 個 signalling questions，各含 participants、predictors、outcome、analysis 四個 domain（📄 Moons 2025）。本輪沒有以此工具對任何單一模型做正式評讀。以下是**他人**以 PROBAST 做的評讀結果：DR 預測 15/15 高 risk of bias（📄 Huang 2025）、DPN 15/15 高 risk of bias（📄 Ma 2025）；DKD 的 SR 也使用 PROBAST，並指出僅 8/26 做外部驗證（📄 Li 2025）。

### 5.5 報告規範（TRIPOD+AI、CONSORT-AI、DECIDE-AI）

- 📄 Scribe 試驗自述依 SPIRIT-AI 設計、依 CONSORT-AI 報告；Guo 2026 自述依 DECIDE-AI 規劃報告。ACCESS 與 voice 自述依 CONSORT。
- Kenya 與 iNCDSS 全文中 CONSORT-AI 僅見於參考文獻或未見，**不能宣稱其符合**。
- He 2026、Wang 2025、TMU 護理交班、DIASENTINEL 的全文中均未見 TRIPOD+AI／DECIDE-AI 檢查表。
- 以上為「是否自述採用」，不是我對報告完整度的稽核。

---

## 6. 風險預測的 AI 版本與傳統 calculators

| 證據 | 內容 | 層級 |
| --- | --- | --- |
| Li 2025（40099258）📄 | 26 項 ML DKD 預測研究；94 個模型；25 項有內部驗證、**僅 8 項有外部驗證**；pooled AUC 內部 0.839（0.787–0.890）、外部 0.830（0.784–0.877）；子群：傳統迴歸型 0.797（0.777–0.816）、ML 0.811（0.785–0.836）、deep learning 0.863（0.825–0.900） | SR；高異質；CI 部分重疊，不足以宣稱深度學習顯著優於傳統迴歸 |
| Huang 2025（40717809）📄 | DR 預測 15 個模型，AUC 0.700–0.960，**全部高 risk of bias** | SR |
| Ma 2025（41024051）📄 | DPN ML 15 項研究；僅 3 項有內外部驗證；6 項報完整 AUC，pooled 0.773（0.707–0.839；I² 99.14%）；校準僅 6 項報告；**全部高 risk of bias** | SR |
| Su 2024（39385193）📄 | 台灣真實世界 T2D：UKPDS-OM2、RECODe、CHIME 方程式；renal failure AUROC CHIME 0.77、UKPDS-OM2 0.60、RECODe 0.64；三者皆高估 renal failure 風險，RECODe 低估 micro／macroalbuminuria；重校準後 slope／intercept 改善 | 傳統 calculators 的**外部校準問題**，非 AI |
| Tangri 2016（26757465）📄 | KFRE 31 cohorts、721,357 人；C 0.90（2 年）、0.88（5 年）；非北美需 calibration factor（基線風險降 32.9%／16.5%） | 傳統方程式的跨區校準 |
| Walker 2026（41288315）📄 | KFRE 在 CKD＋多重共病：UK Biobank 5 年 O/E 1.75（低估）、SCREAM 1.05；納入 competing mortality 的更新模型 O/E 0.98 | 多重共病族群需注意 competing risk |
| DIASENTINEL 📄 | LLM 系統的風險函數 AUROC 0.737，與 XGBoost 0.731 相近；PPV 0.162（盛行率約 6%） | 單院，無外部驗證 |

**對 calculators 的比較結論**：
1. 沒有找到 ML 與 KFRE／SCORE2-Diabetes／PREVENT 的頭對頭、同族群、同終點比較（#16 零命中）；因此「AI 預測優於傳統 calculators」在本輪是 **UNRESOLVED**。
2. 無論 AI 或傳統，**校準**是最常被忽略的環節；Su 2024 與 Walker 2026 顯示傳統方程式在台灣或多重共病族群需重校準。
3. Decision curve／淨效益：三篇 SR 的摘要沒有彙整 decision-curve；本輪未驗證任一模型的 decision-curve。
4. 公平性：DIASENTINEL 自述未評估；其他研究的公平性分析本輪檢索（#17）零命中。

---

## 7. 多 agent 評估方案（**研究設計推論，不是證據**）

目的：把「錯誤、alert fatigue、轉診完成、公平性」放進同一個預先註冊的評估，避免只報告文書時間或專家滿意度。

### 7.1 設計骨架

1. **階段**：先 shadow mode（agent 輸出不呈現給醫師，只與金標準比對），再 DECIDE-AI 式小規模真實使用，最後 stepped-wedge 或 cluster randomized（以診所或個管師為集群；Kenya 顯示同機構內污染會稀釋效應，應以團隊為單位）。
2. **主要終點只選一個，且屬於閉環完成**（見 7.4），其餘分層為次要與探索；事先指定樣本數依據，勿像 Kenya 假設 50% 相對降低。
3. **每個 agent 單獨量測**，再量測整體鏈路（抽取 agent→風險 agent→衝突檢查 agent→任務派發 agent→驗證 agent），否則無法定位錯誤來源。

### 7.2 錯誤

| 指標 | 定義 | 取得方式 |
| --- | --- | --- |
| 抽取正確率 | 欄位層級（藥名、劑量、日期、eGFR、UACR、眼底結論）與人工 chart review 的一致率；錯誤分「遺漏」、「誤置日期」、「單位錯誤」 | 分層抽樣雙人複核，報 Cohen's κ |
| 幻覺分類 | 沿用 Wang 2025 三類（decontextualized／nonfactual／self-conflicting）外加「無來源引用」 | 專家盲評＋自動 entailment 檢查（需報 sensitivity／specificity，DIASENTINEL 的 80%／100% 是小樣本合成） |
| 驗證層效能 | 以**注入錯誤**的真實脈絡（非僅合成）測量攔截率與誤報率 | seeded-error 測試集，預先公開 |
| 臨床嚴重度 | 錯誤依潛在傷害分級；near-miss 與到達病人者分開計 | 安全委員會判讀 |
| 病歷空白處理 | 「資料缺失」與「陰性」須分開輸出；任何把空白當陰性的輸出計為嚴重錯誤 | 規則檢查 |

### 7.3 Alert fatigue

| 指標 | 定義 |
| --- | --- |
| 每 100 次門診的 alert 數、每位個管師每日任務數 | 分母明確 |
| Actionable rate | 觸發後在預定時限內有人工處置的比例 |
| Override／dismiss 率及理由 | 分「不適用」、「已處理」、「忽略」 |
| 時間成本 | 每個 alert 處理時間；醫師額外負擔問卷 |
| 嚴重 alert 的回應延遲 | 例如急性症狀、低血糖事件的處理時間 |
| 閾值敏感度 | 在不同閾值下列出 alert 負擔與漏掉的真陽性，而非單一操作點（DIASENTINEL PPV 0.162 說明低盛行率時 alert 多半是假陽性） |

### 7.4 轉診完成（閉環）

1. 主要指標：**從異常發現到「有人完成處置並回傳結論」的比例與時間**，分段：異常確認→開立→預約→到診→結果回傳→處置（照 ACCESS 提醒，開立轉介≠完成）。
2. 分母必須同時報**全部符合條件者**與**AI 判陽性者**，避免 ACCESS 式分母不一致。
3. 對照：同團隊、同人力、無 AI 的對照期或對照診所；單位時間內新增個管師需計入，否則人力效應被歸給軟體。
4. 配套負擔：病人交通／費用、到診延誤、重複檢查。

### 7.5 公平性

| 項目 | 方法 |
| --- | --- |
| 子群 | 年齡、性別、語言、教育／識能、保險類別、居住地（城鄉）、是否有照顧者、數位使用能力 |
| 模型層 | 子群 AUROC、**校準**（slope／intercept）、PPV、miss rate；子群 ungradable／不可判讀比例 |
| 流程層 | 閉環完成率、等待時間、alert 觸發率在子群間的差異 |
| 判準 | 事先指定可接受差距與統計方法；報告 CI；樣本不足的子群明講無法評估，而非省略 |
| 引用基準 | PROBAST+AI 與 TRIPOD+AI 都要求報告子群表現與適用性 |

### 7.6 報告

預先註冊；主要／次要／探索分層；失敗與停用都報告；人工覆核的比例與時間要報；生成式輸出要保存版本、提示與檢索來源。

---

## 8. 既有文件須修正清單

「查核」欄：✔ 數字一致；△ 一致但缺關鍵限定；✘ 錯誤或不能支持；? 本輪無法核實。

### 8.1 `docs/07-ai-clinical-evidence.md`

| # | 位置 | 原文要點 | 查核 | 建議修正 |
| --- | --- | --- | --- | --- |
| 1 | Diabetes Wizard 列 | 「11 間診所、2,556 名、HbA1c −0.26 個百分點」 | △ | 數字✔（O'Connor 2011，PMID 21242556，📌 abstract）。補：clinic-randomized、41 位醫師、95% CI −0.47 至 −0.06；SBP 控制維持 80.2% vs 75.1%；**LDL 無改善（P=.62）**；試驗期 2006-10 至 2007-05。 |
| 2 | 同列 | 「Diabetes Wizard」名稱；「規則引擎…嵌入診前工作流程」「伴隨流程改變」 | ? | 這些描述不在可取得的 abstract 中，PMC 僅 abstract；本輪**不能核實**。改為 abstract 可驗證的描述（針對 HbA1c／BP／LDL 高於目標者的 EHR CDS），或補上全文來源。連結 PMC3022040 僅為摘要。 |
| 3 | JMIR 2026 列 | 單一機構、受控開發評估、未前瞻驗證 | ✔ 📄 | 補：3 個小型模型（Llama 3.1-8B、Qwen3-8B、GLM4-9B）；資料為 West China Hospital 2022 年 1–2 月；最佳 GLM4-9B BLEU-4 67.93；5 位內分泌醫師評 300 條。 |
| 4 | Ambient AI scribe 列 | 238 位、Nabla −9.5%、DAX 未顯著 | △ 📄 | 補：95% CI −17.2 至 −1.8（P=0.02，多重校正 α=0.025）；DAX −1.7%（−9.4 至 +5.9）；單一學術機構、僅英文、約 2 個月；約 15% 處置組從未使用；試驗開始後才登記；−9.5% 為相對變化；期刊 NEJM AI。 |
| 5 | Kenya Nat Med 列 | 16 間、9,691 人、14 天治療失敗無顯著差異 | △ 📄 | 補：進入主要分析 9,347 人；失敗 102/4,693（2.2%）vs 94/4,654（2.0%），**aOR 0.77（0.55–1.08）**——原始比例方向與 aOR 不一致，須並列；試驗以 50% 相對降低設計，CI 寬；失訪不平衡（61 vs 29）；作者結論「LLM assistance was safe」。 |
| 6 | DIASENTINEL 列 | 院內資料、風險模型、指引檢索與報告驗證；一年新發 T2D | △ 📄 | 補：EMNLP 2026 System Demonstrations（pp. 320–329）；單院資料（Far Eastern Memorial Hospital）；AUROC 0.737（0.694–0.773）、Brier 0.054，p=0.5 時 sensitivity 0.473、PPV 0.162；驗證測試為合成注入；無臨床結局；公平性未評估。 |
| 7 | 眼底影像 AI 列 | 引用 ADA S12，「需接續不可判讀與異常轉介流程」 | ? | ADA 頁面 HTTP 403；PMC12690177 僅 abstract。**S12 是否直接寫此句本輪無法核實**。建議另附 pivotal（PMID 31304320）與 ACCESS（38212308）作為可驗證來源。 |
| 8 | OpenClaw／Hermes 列 | 通用軟體，非糖尿病證據 | ✔ | 兩個連結本輪 HTTP 200，僅確認存在；結論維持。 |
| 9 | 缺漏 | 表內無已驗證的糖尿病 AI RCT | △ | 建議加入 pivotal（87.2%／90.7%／819 可分析）、ACCESS、voice insulin（rules-based）、iNCDSS、並標示分層。`docs/12` §6 已有，建議互相引用。 |

### 8.2 `docs/08-taiwan-ai-applications.md`

| # | 位置 | 原文要點 | 查核 | 建議修正 |
| --- | --- | --- | --- | --- |
| 1 | 健保署段 | 「2026 年 6 月公布的英文資料」「40 家參與診所」「2026 年 3 月活動發表」 | ? 📌 | 搜尋摘要：2026-03-04 公布、40 間診所（北 7／中 29／南 4）。**「6 月公布」未佐證**（頁面 403）。補：合作方含台北醫學大學、國衛院、四個專業學會與 Google；風險模型稱 AI-on-DM；Google 稱 20 分鐘降至 25 秒的是廠商說法。需有人用可存取的瀏覽器開官方頁確認日期與措辭。 |
| 2 | 奇美段 | 跨資料庫、四職類、藥事與飲食建議 | ✔ 📄（網頁） | 補：來源是 Microsoft 合作刊載的新聞稿（2024-07-12）；2023-11 起導入；頁面無糖尿病內容；文中稱醫院「尚無硬資料」。 |
| 3 | 北醫段 | 連結 `pmc.ncbi.nlm.nih.gov/articles/13022550` | ✘（連結） | 缺 `PMC` 前綴，應為 `PMC13022550`（PMID 41819121，DOI 10.2196/81604）。數字：基線 2024-09 vs 導入後 2024-10 至 12 月，3.45–4.32 → 1.17–2.54 分鐘；節省小時為估算；三院為台北醫學大學附設醫院、萬芳、雙和。 |
| 4 | 國衛院段 | 「2025 年 8 月至 2026 年 7 月」 | ? | 機構典藏頁僅見 `Date: 2025` 與編號 NSTC114-2314-B400-014；計畫期間未在頁面文字中找到（GRB 為動態頁）。改為「2025 年度計畫」或補 GRB 來源。 |
| 5 | 三總 MEDIC 段 | 「2026 年 11 月 4 日公告，11 月 2 日上線」 | ? | 院方頁 HTTP 403，搜尋亦無佐證。**不得當成已核實**；保留時註明「院方公告，未能獨立查核」。 |
| 6 | 缺漏 | 台灣的 DIASENTINEL | △ | DIASENTINEL 作者隸屬遠東紀念醫院（📄），為台灣單院 LLM＋風險模型案例，建議列入並註明為系統展示。 |
| 7 | 缺漏 | 台灣族群 calculators 校準 | △ | Su 2024（39385193）顯示 UKPDS-OM2／RECODe／CHIME 在台灣 T2D 需重校準，可補於「DCSI 與風險」段。 |

### 8.3 順帶發現（不在指定檔案，供 lead 轉給 Codex）

- `docs/12` §6：pivotal 的「900 人」建議加註「819 人可完整分析」。
- `docs/12` §6：ACCESS 建議加註「AI 組的完成即介入本身」。
- `docs/13` §4（KFRE）：見 `handoff.md`。

---

## 9. UNRESOLVED 清單

1. 健保署頁面日期與措辭（403）。2. 三總 MEDIC 公告。3. 國衛院計畫期間。4. ADA S12 對 AI 的確切敘述。5. Diabetes Wizard 命名與流程設計。6. iNCDSS、voice insulin 的試驗登記編號（解析全文未見，可能在補充資料）。7. ML 對傳統 calculators 的頭對頭比較。8. Tangri 2011 原始 derivation 的係數（不在 PMC）。9. KFRE North America 5 年 S0=0.8996 無法由本地全文驗證（§handoff）。10. Tanzania DR RCT 全文。11. 糖尿病族群的 AI 硬終點試驗是否存在（定向檢索未找到，不等於不存在）。

## 10. 對上位研究問題的意義

- 「整合式 AI」的合理定位是：**已驗證、受控的單一任務元件**（DR 篩檢、CGM 判讀輔助、文書草稿、規則型滴定）＋**人工覆核的閉環任務管理**，而不是自由生成處方的全人 agent。
- 設計 agent 時，每個輸出應帶來源與缺失狀態；風險分數不得當診斷；不得合成跨疾病全人風險總分。
- 若要把本專案做成可評估的系統，§7 的方案可直接作為研究設計草稿，但目前沒有證據顯示它能改善病人結局。
