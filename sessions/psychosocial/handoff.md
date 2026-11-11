# Handoff — psychosocial

日期：2026-11-11。本檔只列「需要 lead 修改的跨目錄項目」與「給其他 sessions 的具體問題」。我沒有寫入 `sessions/psychosocial/`、`literature/notes/psychosocial/` 以外的受版控檔案；`literature/parsed/psychosocial/`、`literature/fulltext/psychosocial/` 為 git-ignored，`literature/receipts/psychosocial.jsonl` 會被提交（僅含 hash 與 ID，無全文）。

## A. 需要 lead 處理（跨目錄）

1. **`workflow/claim_review.csv`（若由 lead 維護）請新增兩列**
   - INDEPENDENT（PMID 32809002）：對照組主要結局百分比 Key Points／Results／Table 2 皆 54.7%，Abstract 為 57.4%；RD 16.9 與 54.7 相符；Crossref／PubMed 查無更正。狀態建議 `UNRESOLVED`（最終出版版是否已更正）。證據：`sessions/psychosocial/report.md` §3.2。
   - PAID 版本：1995 原版六點量表（PMID 7555499 abstract）vs 現行 0–4（台灣 PAID-C 總分區間 0–73.75，PMID 19808922）。兩者不可混稱。
2. **README／證據索引**：請勿把「ADA：T2D diabetes distress >60%」與「Perrin 2017：36%」擇一寫入；兩者並列並註明切點與量表依賴（`report.md` §1）。
3. **`PRIDE` 身分**：本輪唯一找到的 PRIDE 是 Partnership to Improve Diabetes Education（PMID 31919724；主要結局 HbA1c，與標準衛教無差異），不是 diabetes distress 試驗。請確認 lead 原意；若有別的全名請回傳，我再補。
4. **台灣資料缺口**：下列項目本輪英文 PubMed 檢索未找到，建議由 lead 授權另行檢索中文資料庫（airiti、CNKI）或衛福部／國健署資料：成人 T2D 的 diabetes distress 盛行率、anxiety、fear of hypoglycemia、認知障礙；台灣繁中 GAD-7、DDS-17、HFS-II、WHO-5（糖尿病族群）正式驗證；健保糖尿病共同照護網／P4P 中個管師、衛教師、營養師、心理師可執行與給付的角色。這些我在報告中全部標 `UNRESOLVED`，沒有拿中國大陸數字代替台灣。
5. **全文與管線**：INDEPENDENT 與 ADA 2026 ch.5 的全文是用內建瀏覽器讀 PMC 網頁文字取得（`PMC…_browser.md`，receipt 已記錄），因為 PMC E-utilities 回 `ABSTRACT_ONLY`、PDF 直連 403、Europe PMC 回 500／非 OA。此路徑沒有偽裝 UA 或繞過驗證，但請 lead 決定是否納入 `SESSION_PROTOCOL_v2.md` 的正式備援順序。
6. 未解決需要全文但未取得者（abstract-only，不得做超出 abstract 的斷言）：T1-REDEEM（29976567）、Cochrane Chew 2017（28954185）、Winkley HTA（32568666）、Perrin 2017（28799294）、Farooqi 2022（34810141）、Hayashino 2020（32949245）、Levis PHQ-2（32515813）。若 lead 要在最終報告引用其細節，需再取。

## B. 給 calculators 的具體核對請求（量表版本／cut-off）

請對照**原始評分手冊或原始論文**（不是二手摘要）核對並回覆 ACCEPT／REVISE／UNRESOLVED，各附來源定位：

1. **PAID 現行評分**：每題 0–4、總分 ×1.25 → 0–100，是否為官方現行規格？我只有間接證據（台灣 PAID-C 總分 0–73.75、單題平均 ≤1.21，PMID 19808922）；原始 1995 版為六點量表（PMID 7555499 abstract）。請在你的公式裡**分開兩個版本的 ID**，不得混稱。
2. **PAID 的 distress 切點**：常見「總分 ≥40」的原始出處為何？本地全文中**找不到**，在我的表中標 `UNRESOLVED`。
3. **PAID-5**：題目是否為 PAID 第 3、6、12、16、19 題（PMID 19841892 abstract 如此寫）；切點常寫 ≥8（0–20 範圍）：請給原始出處，我的表中標 `UNRESOLVED`。
4. **DDS-17／DDS-2**：DDS-17「平均每題 ≥3 = moderate distress」我在 DDS-2 發展論文 abstract 驗到（PMID 18474888）；請核對 ≥2（"some"）區間與 DDS-2 本身的陽性切點（abstract 未載）。
5. **WHO-5**：我驗證了 0–5 計分、原始 0–25、×4、越高越好（UConn 轉載表單、Du 2023）。請核對：(a) 官方切點是**原始分 <13** 還是**百分比 <50**（13×4＝52，與 50 不等價）；(b) 缺值處理規則（我取得的副本沒有印）；(c) 大陸 T2D 最佳切點 <42（PMID 38031007）不宜取代 <50 的預設。
6. **PHQ-9 第 9 題陽性的臨床動作**與 **GAD-7 原始 cut-off 5／10／15**：我只有間接出處（Kroenke 2001 abstract、INDEPENDENT 亞組用 GAD-7≥10）；GAD-7 原始論文（PMID 16717171）我沒有取得全文。
7. 台灣正式繁中版本：PHQ-9／PHQ-2（Liu 2011，PMID 21111406）與 PAID-C（Huang 2010，PMID 19808922）已找到；GAD-7、DDS-17、HFS-II、WHO-5 的台灣版本我**沒找到**——若你在檢索時看見，請回報 PMID。
8. 實作提醒：任何心理量表 calculator 都只能輸入「本人作答的逐題分數」；缺題不得插補、病歷空白不得當成 0 分或陰性；輸出標籤為「篩檢陽性／陰性」，不是診斷。

## C. 給 complications 的問題（心理與器官照護連結）

ADA 2026 5.45 與 5.49 只寫「出現併發症時」重新篩檢 DD、憂鬱（📄 `report.md` §2），**沒有按器官分層**。請問：你的報告中，哪些併發症事件（例如新診斷增殖性視網膜病變或視力喪失、eGFR 進入 G4／開始透析、足潰瘍／截肢、心肌梗塞／心衰竭、嚴重低血糖住院）有**直接證據**顯示隨後的憂鬱／DD／認知功能惡化，並且證據是縱向還是橫斷？請給 PMID 與具體數字，無證據者標 `UNRESOLVED`。這會決定「新併發症後觸發心理重新評估」是 ADA 的通則，還是需要分器官的規則。另請核對：我引用的 ADA Table 5.7（DD、憂鬱與微血管併發症 +++）是「相關性證據評級」，你的報告是否有相衝突的個別研究？

## D. 給 methods_ai 的問題（心理 AI 介入的證據層級）

我目前把證據分三層並分開報告：(1) 篩檢／偵測準確度；(2) 使用者端症狀（distress、憂鬱）改善；(3) HbA1c／長期器官結局。目前我手上的證據是：Kim 2025 糖尿病 secure messages 的 LLM 偵測（回溯性、標籤非正式診斷，F1 約 93%，PMC12485036）；Wu 2024 糖尿病 chatbot（僅 1 個 RCT，4 組 pre-post HbA1c −0.30，PMC11653048）；一般族群 Zhang 2025（14 RCT，ES 0.30，95% PI −0.85 至 1.67，PMC12707440）與 Therabot RCT（非糖尿病，4 週，PMID 42932588 abstract）。請問：
1. 你認為這些各自屬於哪個證據層級／哪一層結局？我若稱「糖尿病族群尚無 AI 心理介入在三層結局都有對照試驗證據」，你是否能舉出反例（糖尿病族群的 RCT，且主要結局為 distress 或憂鬱）？請給 PMID。
2. Zhang 2025 的 prediction interval 含負值，是否足以在報告中要求把「chatbot 有效」降級為「平均上可能有益、單一試驗可能有害」？請核對其 RoB 與 publication bias 結論。
3. 對 Kim 2025：我只做了摘要層級（F1／accuracy）與限制判讀；請獨立核對其標註來源、樣本數與是否含外部驗證集，並說明它支持「偵測線索」到什麼程度。

## E. 與我自己相關、仍待查的補強（非跨目錄）

- 取得 T1-REDEEM 與 Chew 2017 全文後，重新核對 §3.1 的 Chew 與 2026 SR 結論方向差異原因。
- 補 EMBARK（PMID 38809903，Hessler 2024）、Fernández-Rodríguez 2024（eHealth DD/depression）、Yap 2024（technology-based DD）三篇的全文，作為數位介入對 DD 的直接證據。
- 取 TEAMcare 長期追蹤與成本資料（本輪未取）。
