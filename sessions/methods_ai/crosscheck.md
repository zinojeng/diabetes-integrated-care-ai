# methods_ai 交叉查核（第二階段）

日期：2026-11-11。範圍：`sessions/complications/handoff.md` §B（→methods_ai）、`sessions/psychosocial/handoff.md` §D（→methods_ai）、lead 補充的三件事。
標記沿用：📄 = 本地全文已 `grep` 驗證（`python3 -I literature/notes/methods_ai/claim_checks.py`，0 MISS）；📌 = 僅 abstract／搜尋摘要。
本輪新取全文（`literature/parsed/methods_ai/`）：PMC12485036、PMC11653048、PMC12707440、PMC9293940、PMC10906435、PMC11176869、PMC7677021、PMC6450247。檢索式見末尾附錄。

---

## 一、complications → methods_ai

### Q1：成人 T2D 的 AI／CDS／LLM 隨機試驗，主要結局為「異常後處置完成」，且 CDS 能與人力協調拆開？

**判定：ACCEPT（complications 的保守結論成立）＋補充證據。**

定向檢索**沒有找到**符合全部條件的試驗：成人 T2D 專屬、AI／LLM、主要結局為轉介完成或治療起始、分母為全部隨機人數、CDS 單獨成立。最接近的是下列 CDS-only 試驗，**皆為規則型或方程式型 CDS，不是 AI／LLM**：

| 試驗 | 族群與設計 | CDS 是否單獨 | 結局與結果 | 與提問條件的差距 |
| --- | --- | --- | --- | --- |
| **CKD-DETECT**（Goldhaber，Am J Med 2026，PMID 42031191）📌 abstract | 成人 T2D、近 12 個月無 UACR 且無 CKD；醫師隨機；400 人（NCT05342545，Bayer 資助） | 是（僅 alert，無協調員） | 主要：90 天內 UACR 開單 36.0% vs 11.5%，OR 5.71（2.58–12.64）。次要：新 CKD 3–5 診斷 1 vs 2 人；轉介腎臟科與 CKD 藥物處方**皆 0 件** | 結局是**開檢查**，不是異常後處置完成；追蹤與事件數太少，下游完成度無法評估；廠商資助；僅 abstract |
| **Samal 2022**（Kidney Med，PMC9293940）📄 | 波士頓 10 間診所，CKD G3–G5，5,590 人，區塊隨機（NCT02990897） | 是；以 KFRE 5 年風險＋建議，點擊才顯示 | 主要（6 個月監測檢驗）與介入無關聯；KFRE >10% 子群腎臟科轉介：介入 118/419（28.2%）vs 對照 161/421（38.2%），差 −10.1 pp，P=0.01（對照組較高） | 非 T2D 專屬；非 AI；連結僅被點擊 122 次（使用率極低）；作者承認診所內污染 |
| **Sperl-Hillen 2024**（Kidney Med，PMC10906435）📄 | 32 間中西部診所，CKD G3–G4＋≥1 個照護缺口，6,420 人，集群隨機（NCT03890588） | 是；對病人與臨床醫師的個人化建議 | 6 個缺口指標皆無顯著差異；腎臟科轉介或就診 38.7% vs 36.1%（RR 1.02，0.79–1.32）；ACEi／ARB 開立 RR 0.95（0.76–1.18） | 非 T2D 專屬；非 AI；COVID-19 期間，使用障礙 |
| **O'Connor 2011**（PMC3022040）📌 | 糖尿病，11 診所，2,556 人 | 是 | 中間指標（HbA1c −0.26%）有改善 | 結局是中間指標，不是處置完成 |

**對 complications 結論的影響**：
1. 兩個 CKD CDS-only 隨機試驗在**轉介／處置完成**上皆為中性或相反方向，且使用率低；這支持「不可把 CDS 單獨當成閉環」。
2. CKD-DETECT 說明 CDS-only 在 T2D 可明顯增加**檢查開單**；若 complications 的措辭是「CDS 可增加篩檢」，有 T2D 證據（📌）；但「增加處置完成」沒有證據。
3. 建議的最終句型（你已提出）可維持：「AI／CDS 可增加篩檢完成；對處置完成與硬終點未證實，且不能取代人力協調」。唯一補充：把「增加篩檢完成」限定為**檢查開單／執行**，不含異常後處理。
4. 限制：我的檢索不是全面搜尋（無 PRISMA），上述是定向命中；不能證明符合條件的試驗不存在。

### Q2：ACCESS 對照組 18/82 vs 18/83

**判定：REVISE（我的 handoff 與 report 的措辭已更正）。**
- `PMC10784572` 的 Table 3（n=163）：AI 81/81（100%）、對照 **18/82（22%）**；164 人隨機（81 vs 83），1 名對照被排除（📄）。
- Secondary 的 follow-through 段（L51）只寫「control arm, 18 participants visited the ECP … 22%（95% CI 14–32%）and none had DED」，**沒有印出分母**；22%（14–32）與 18/82 數值吻合，**無法由文字區分 82 或 83**。complications 讀的 L47–51 與我讀的是同一段；我不能證實 83。
- 共同結論不變：對照的 18 人無一有 DED，AI 陽性者 16/25，兩個 follow-through 比例分母不同（全部對照者 vs 僅 AI 陽性者），不可相減；此處的原文差異 42%（21–63）是作者自己報告的，但其可解釋性受此限制。
- 已修正：`sessions/methods_ai/handoff.md` §B 與 `report.md` §2.2。

---

## 二、psychosocial → methods_ai

### Q1：三篇各屬哪個證據層級？可否舉反例？

**判定：ACCEPT（「糖尿病族群尚無 AI 心理介入在三層結局都有對照試驗證據」成立）＋一個需註記的部分反例。**

| 來源 | 實際屬性 | 對應層級 | 備註 |
| --- | --- | --- | --- |
| **Kim 2025**（PMID 41028413，npj Digit Med，PMC12485036）📄 | 離線分類評估；Stanford 2013–2024 secure messages；606 則基準訊息（No=300、Yes=306）；標籤由一位研究者先標、一位精神科醫師確認，**僅兩人一致者入基準**；Llama 3.1 405B zero-shot F1／accuracy 93%（abstract）；另有 challenging 子集 N=39 | ① 偵測／分類效能（與一個自建基準比，**不是**診斷準確度研究） | 見 Q3 |
| **Wu 2024**（PMID 39626235，JMIR，PMC11653048）📄 | 系統性回顧＋meta-analysis；25 篇；**僅 1 篇 RCT**；HbA1c meta-analysis 為 **4 組 pre-post、219 人**，MD 0.30（95% CI 0.04–0.55），明寫「compared with the baseline」；搜尋至 2023-01-01 | ③ 血糖，但為**無對照的前後比較**；不屬 ② 心理結局（僅 2 篇/8% 提供心理健康教育） | 方向：基準值減後測值＝HbA1c 下降 0.30；psychosocial 寫 −0.30 與此一致。不能當成對照試驗效果 |
| **Zhang 2025**（JMIR，PMC12707440）📄 | GenAI 心理健康 chatbot 的 SR＋multilevel meta-analysis（14 RCT、19 比較、N=6,314），**一般族群**，全文**無 diabetes 字串** | ② 症狀結局（非糖尿病） | 見 Q2 |
| **Therabot RCT**（PMID 42932588）📌 abstract | N=210，MDD／GAD／CHR-FED 成人，4 週 vs waitlist | ② 症狀結局（非糖尿病） | 非糖尿病族群；本輪僅 abstract |

**反例檢索**（附錄 #4–#5）：
- **MacNeill 2024**（PMID 38814681，JMIR Form Res，PMC11176869）📄：RCT，68 人（關節炎或糖尿病），Wysa 4 週 vs **無介入**對照，PHQ-9／GAD-7／PSS-10；摘要報告處置組憂鬱與焦慮組內下降、對照無變化；試驗登記 NCT04620668。**部分反例**：含糖尿病參與者且主要結局為憂鬱／焦慮；但**不是糖尿病專屬**、4 週、n=68、無介入對照、摘要以組內變化為主，且糖尿病子群未獨立分析。可以註記「混合慢性病族群的小型 RCT，方向為有益，不能外推到糖尿病 distress」。
- **Gong 2020**（PMID 33151154，PMC7677021）📄：成人 T2D、AI 對話代理 My Diabetes Coach，187 人 RCT，12 個月；HbA1c 淨差 −0.04%（95% CI −0.45 至 0.36）不顯著；HRQoL 差 0.04（0.00–0.07）。**屬 ③＋生活品質，不是 distress／憂鬱**。
- 未找到：糖尿病族群、以 distress（PAID／DDS）或憂鬱量表組間差為主要結局的 AI／LLM RCT。

**建議措辭**：「糖尿病族群：AI 對話代理有 HbA1c 無效的 RCT（Gong 2020）；混合慢性病的小型 RCT 顯示憂鬱／焦慮下降（MacNeill 2024）；糖尿病專屬、以 distress 為主要結局的 AI 試驗本輪未找到。」

### Q2：Zhang 2025 的 prediction interval 含負值——可否降級為「平均上可能有益、單一試驗可能有害」？

**判定：ACCEPT 降級；但「單一試驗可能有害」要改寫。**

本地全文核對（📄）：
- 主要效應 ES=0.30，P=.047，95% CI 0.004–0.59，**95% PI −0.85 至 1.67**，14 RCT、N=6,314；CI 下界幾乎貼 0。
- 異質性：焦慮子群 τ²=0.857；憂鬱子群 τ²=0.225、I²≈90%；整體殘餘異質性 Q(35)=230.41，P<.001。
- 發表偏誤：funnel plot 不對稱；Vevea-Woods 選擇模型 LRT χ²(2)=11.25，P=.004，「P<.025 的研究被納入的可能性約為 3.54 倍」。**全文數字內部不一致**：未調整 g=0.41，調整後卻是 g=0.54（SE 0.26，P=.04），文字卻稱「smaller and nonsignificant change」——方向與敘述矛盾，引用調整值前需當作 UNRESOLVED，並建議不要引用該調整值。
- RoB：作者稱 RoB 2／ROBINS-I「moderate」；**協議是修稿期間（2025-09-18）才追溯登記**；搜尋至 2025-03。
- 族群為一般心理健康，不是糖尿病。

建議措辭：「在一般族群，GenAI chatbot 平均效應小（ES 0.30，CI 幾乎含 0）、異質性高且有發表偏誤訊號；95% PI（−0.85 至 1.67）表示在新情境中的真實效應**可能為正也可能為負**，故證據確定性低、不可外推到糖尿病」。**不要**寫成「單一試驗可能有害」——PI 是「未來新研究的真實效應範圍」，不等於已有某個試驗顯示有害；若要談有害，需看個別試驗的安全性報告。

### Q3：Kim 2025——標註來源、樣本數、外部驗證集，以及能支持什麼

**判定：REVISE（psychosocial 需下修「偵測線索」的強度）。**

本地全文核對（📄）：
- **資料**：Stanford Health Care 及 22 個附屬中心，2013–2024，糖尿病（ICD-10 E08–E13）病人的 secure messages，路由到內科、家醫、初級照護的 PMAR。基準共 **606 則**（No 300、Yes 306）。
- **標註**：陽性例＝來自**同時有憂鬱或焦慮診斷**的糖尿病病人，且**先以症狀關鍵字加負面情緒篩出**，由第一位研究者標為 preliminary，再由精神科醫師確認「是否需要進一步評估」；陰性例＝糖尿病但**無**憂鬱／焦慮診斷者的訊息。只有兩位審閱者一致的訊息入基準。
- **所以標籤不是 PHQ／DSM 診斷，也不是病人自陳量表**，而是「兩位審閱者認為需要進一步評估」。
- **外部驗證集**：**全文未見獨立的外部驗證集**；模型與提示策略（prompt、persona、temperature、zero-/few-shot）是在同一基準上比較、選最佳者（作者自述「to identify the best-performing model」），因此 93% 屬**在同一基準上選擇後的樂觀估計**。
- **譜系偏誤**：陽性例經關鍵字＋負面情緒挑選、陰性例來自無診斷者，兩群本身差異大；真實 portal 流量中大量訊息兩者皆非（例如一般的行政或用藥詢問），盛行率與難度都不同。作者另設 challenging 子集（N=39）作為較難案例，並自述「inconsistencies in challenging cases warrant further real-life assessment」。
- **PHQ-4 模式**：reasoning 模型在 PHQ-4 模式明顯變差（o1 F1 0.61 vs 0.81；DeepSeek R1 0.51 vs 0.90，P<.0001）。
- **結論**：只支持「LLM 可在一個關鍵字挑選、兩人標註的基準上區分有／無憂鬱焦慮語言」。**不支持**：篩檢敏感度／特異度、PPV、對 distress 的偵測、病人結局，或用於自動轉介。若要寫「偵測線索」，限定為「優先順序排序輔助，需人工評估，自殺風險須即時人工處理，不可自動化略過」。

---

## 三、lead 補充：先前 5 項「無法核實」的再嘗試

方法：WebSearch（standard／extended），不繞過任何 403；僅作 📌（搜尋摘要）。Tavily 在本輪不可用（MCP 斷線）。

| # | 項目 | 結果 | 判定 |
| --- | --- | --- | --- |
| 1 | Diabetes Wizard 命名 | 搜尋摘要稱該 EHR 系統名為 Diabetes Wizard，依 ICSI 指引的詳細演算法；試驗 2006-10 至 2007-05、11 診所、41 位醫師、2,556 人；HbA1c −0.26%；SBP 控制維持 80.2% vs 75.1%；LDL 無改善；醫師使用率 62.6%；摘要明言支持而非取代臨床判斷 | **命名 ACCEPT（📌 搜尋摘要）**。「規則引擎」可由「clinical algorithms」支持；「嵌入診前工作流程」仍未見原文（UNRESOLVED，建議刪去或補全文）。`docs/07` 可保留「Diabetes Wizard」 |
| 2 | 健保署日期與內容 | 多篇中文新聞（INSIDE、TechNews、iThome 等）：2024 年 5 月健保署與 Google、國衛院、北醫簽約啟動 AI-on-DM；40 診所（北 7、中 29、南 4）；民眾端健康存摺、醫師端家醫大平台含 DCSI；衛教助理基於 Gemini，需使用者授權。**上線時間來源間不一致**（TechNews 稱已上線，較早報導預告約 3 月）。我先前的搜尋摘要稱 2026-03-04 的活動 | **內容 ACCEPT（📌）；「2026 年 6 月公布」仍 UNRESOLVED**（英文頁面 403，未能確認該頁日期）。建議 `docs/08` 改為「2024 年 5 月啟動專案；2026 年的場域驗證／活動發布，日期依官方頁確認」，並補 Google、國衛院、北醫為合作方 |
| 3 | 國衛院計畫期間 | 搜尋找不到該計畫（NSTC114-2314-B400-014）的專屬頁面；僅見其他 NSTC114 計畫（如長庚的 B182-049，起訖 2025-08-01 至 2026-07-31），可見 NSTC114 常見年度，但**不能套用到本計畫** | **UNRESOLVED**；建議 `docs/08` 寫「2025 年度（NSTC114）計畫，期間待確認」 |
| 4 | 三總 MEDIC | 兩次搜尋（含 extended）皆無 MEDIC GenAI 公告；僅有 2023 年三總與微軟的醫療大數據專案、AI/IoT 中心等舊資訊 | **UNRESOLVED**；`docs/08` 此項需註明「院方公告，未能獨立查核」或移除 |
| 5 | ADA S12 對 AI 的敘述 | 搜尋摘要引述 S12：FDA 核准的 AI 演算法是適當的篩檢策略，影像可由專業人員、閱片中心技術人員或 FDA 核准的 AI 判讀；另一二手摘要稱異常或影像品質差者應以親診散瞳完整眼科檢查追蹤。「12.6」編號僅見於廠商部落格，**不採用** | **ACCEPT（📌，二手＋部分引句）**：`docs/07` 的「需接續不可判讀與異常轉介」與二手摘要相符，但 PMC12690177 僅 abstract，需官方頁正文確認原文措辭 |

---

## 四、行政項目

1. **無效 receipt**：`literature/receipts/methods_ai.jsonl` 內 `id=21482743 → PMC13746208` 那筆已刪除（33→32 行）。
2. **本輪 handoff 修正**：ACCESS 對照分母措辭（見 §一 Q2）。
3. **新增可重現核對**：`claim_checks.py` 增補 7 個全文的數字檢查，0 MISS。

## 五、對最終結論的影響（給 lead）

| 項目 | 影響 |
| --- | --- |
| 「AI／CDS 能提高併發症篩檢」 | 可寫，但限定為「檢查開單／執行」（CKD-DETECT、ACCESS）；處置完成無證據，CDS-only 的腎臟科轉介試驗中性或相反 |
| 「AI 可偵測心理困擾」 | Kim 2025 只到「同一基準上選擇後的分類效能」，不得寫成篩檢 |
| 「chatbot 對心理有效」 | 一般族群證據小且不確定（PI 含負值＋發表偏誤）；糖尿病專屬缺口維持 |

## 附錄：本輪檢索式（PubMed E-utilities，definitive count 為 esearch count）

| # | 查詢 | 命中 | 備註 |
| --- | --- | ---: | --- |
| 1 | `"decision support"[tiab] AND diabetes[tiab] AND (randomized OR randomised)[tiab] AND (albuminuria OR "kidney disease")[tiab]` | 13 | 納入 Samal、Sperl-Hillen CKD、CKD-DETECT |
| 2 | `"decision support"[tiab] AND diabetes[tiab] AND (randomized OR cluster)[tiab] AND (retinopathy OR "eye exam"…)[tiab]` | 2 | 僅得 CARRS 延伸研究，無符合者 |
| 3 | `"clinical decision support"[tiab] AND "type 2 diabetes"[tiab] AND randomized[tiab] AND (prescribing OR "treatment intensification" OR SGLT2)[tiab]` | 1 | 無符合（deprescribing nudge process evaluation） |
| 4 | `(chatbot OR "conversational agent" OR "large language model")[tiab] AND diabetes[tiab] AND (distress OR depression)[tiab] AND randomized[tiab]` | 3 | MacNeill 2024 |
| 5 | `(chatbot OR "conversational agent")[tiab] AND diabetes[tiab] AND randomized[tiab]` | 13 | Gong 2020；其餘多為回顧或 protocol |
| 6 | 較寬的自然語言查詢（未加欄位標籤的三個嘗試） | 0 或雜訊 | 結果不可用，已棄用，未納入 |
| 7 | WebSearch × 5 | — | 見 §三 |
