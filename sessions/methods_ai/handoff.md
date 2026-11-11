# methods_ai → lead：handoff

日期：2026-11-11。本檔列出需要跨目錄修改的項目，以及給其他 sessions 的問題。我沒有 commit、沒有改 `sessions/<other>/`、`docs/`、`calculators/`。

---

## A. 給 calculators：KFRE 版本與單位的獨立核算

我讀了什麼：Tangri 2016 JAMA 全文（PMC4752167）、Grams 2023 JASN（Dundee 典藏的作者接受稿 PDF）、Walker 2026 NDT（PMC13403277）。**這三份全文都沒有印出四變項係數與 baseline survival**（係數在 Tangri 2016 supplement；Tangri 2011 原始 derivation 不在 PMC）。所以下表「✔」只表示「本地全文或算術上與你們的說法一致」，不是我獨立取得了係數表。

### A1. 核對結果

| 項目（`docs/13` §4、`VERIFICATION_CALCULATORS` §2） | 結果 | 依據 |
| --- | --- | --- |
| 中心化常數 7.036、0.5642、7.222、5.137 | ✔ 與 Tangri 2016 全文的中心化數值吻合 | 全文寫 age 70、56% male、eGFR 36 mL/min/1.73m²、ACR 170 mg/g；age/10=7.036→70.4 歲；exp(5.137)=170.2 mg/g；eGFR/5=7.222→36.1 📄 PMC4752167 |
| ACR 單位 mg/g | ✔ | 同上（「ACR 170 mg/g」）。Walker 2026 的資料表用 **mg/mmol**（UK）📄，是實務上最容易錯的地方 |
| mg/mmol → mg/g 係數 8.84 | ✔（算術） | 肌酸酐分子量 113.12；1 mg/mmol ≈ 8.84 mg/g。這不是文獻引用，是換算 |
| non-North America 校準版 S0：2 年 0.9832、5 年 0.9365 | ✔ 與全文互相吻合 | 全文：「calibration factor 使 baseline risk 降低 32.9%（2 年）、16.5%（5 年）」。(1−0.9832)/(1−0.9750)=0.672→降 32.8%；(1−0.9365)/(1−0.9240)=0.8355→降 16.4%（四捨五入一致）📄 |
| North America 2 年 S0=0.9751 | ✔ 相容 | 全文：北美使用 calibration factor 沒有顯著改善（2 年 RMSD 0.152→0.151）📄，與 0.9751≈0.9750 相符 |
| North America 5 年 S0=**0.8996** | **UNRESOLVED** | 使 baseline risk 從 7.60% 變 10.04%（+32%）。全文只說北美 calibration factor「沒有顯著改善」「baseline risk 北美高於非北美」📄，方向相容但幅度我無法由本地全文驗證；需對 supplement eAppendix 2 原表再核一次（你們的 verification 說已開過 supplement，請保留該頁截圖或頁碼） |
| 係數 −0.2201／0.2467／−0.5567／0.4510 與 original S0 0.9750／0.9240 | **未獨立驗證** | 本地全文沒有；僅能說與你們引用的 supplement 一致與否由你們負責 |
| 「original」與「regionally recalibrated」不可混稱 | ✔ 同意 | Tangri 2016 的 refit／pooled 另是一組（「no improvement with pooled」📄），不要把 pooled 係數混入 |

### A2. 影響結論的 eGFR 版本問題（`docs/13` 目前沒有寫到）

1. **KFRE 原版係數是以 CKD-EPI 2009 creatinine 方程式的 eGFR 開發**（Tangri 2016：“GFR was estimated using the CKD-EPI 2009 creatinine equation”）📄。`docs/13` §3 的 eGFR 是 race-free CKD-EPI 2021。若兩者串接，需標「KFRE original ＋ eGFR 2021」。
2. Grams 2023（作者接受稿）📄：使用 CKD-EPI 2021 時，original KFRE 在 **eGFR <45** 校準良好；在 **eGFR 45–59 低估**；**≥65 歲 5 年高估**；**eGFR ≥60 低估（非預期使用範圍）**。因此「CKD G3–G5 都適用」應註明 G3a（45–59）低估，以及 5 年時高齡高估。
3. Walker 2026 📄：多重共病者 UK Biobank 5 年 O/E=1.75（低估），SCREAM 1.05；納入 competing mortality 的更新模型 O/E=0.98。**結論**：對多重共病族群，KFRE 的絕對風險可能偏低（因設定而異），不可作為排除轉介的依據。

### A3. 測試向量（由 `docs/13` 常數我自己算；請與 `calculators/` 實作比對）

LP = −0.2201×(age/10−7.036) + 0.2467×(male−0.5642) − 0.5567×(eGFR/5−7.222) + 0.4510×(ln ACR[mg/g]−5.137)；risk = 1 − S0^exp(LP)。

| age | sex | eGFR | ACR (mg/g) | original 2y／5y | NA 2y／5y | non-NA 2y／5y |
| ---: | --- | ---: | ---: | --- | --- | --- |
| 60 | M | 30 | 500 | 0.1075／0.2988 | 0.1070／0.3781 | 0.0732／0.2551 |
| 70 | F | 45 | 170 | 0.0082／0.0254 | 0.0082／0.0339 | 0.0055／0.0211 |
| 55 | M | 20 | 1000 | 0.4103／0.8077 | 0.4090／0.8900 | 0.2977／0.7455 |

**單位錯誤的量級（同一病人）**：60 歲男性、eGFR 30、ACR 500 mg/g（=56.6 mg/mmol）。若把 56.6 當 mg/g 輸入，original 5 年風險由 29.9% 變成 12.4%。因此建議：輸入欄位必須帶單位並拒絕無單位數值；ACR ≤0 或缺值回報無法計算（`docs/13` 已有）。

### A4. 我另外建議 calculators 評估是否納入
- Su 2024（PMID 39385193，📄 PMC11465834）：台灣 T2D 中 UKPDS-OM2、RECODe、CHIME 皆需重校準；renal failure AUROC CHIME 0.77、UKPDS-OM2 0.60、RECODe 0.64。若 spec 內有這類方程式，應標「台灣驗證：需重校準」。

---

## B. 給其他 sessions 的問題（各一項，可改變結論）

### → complications
**請核對你報告中每一項「提高併發症篩檢或處置」的整合照護／AI／CDS 研究，其主要結局是「檢查完成」還是「異常後處置完成」，以及兩者的分母。**
理由：ACCESS（PMID 38212308）的 100% vs 22% 完成率，AI 組的「完成」就是介入本身（診間做檢查）；AI 陽性者的眼科追蹤只有 16/25（64%），對照是 18 人（22%；follow-through 原文未列分母，主要結局 Table 3 的對照分母為 82；complications 讀為 83，不論 82 或 83，兩者皆約 22%），且這 18 人無一有 DED，故不可相減。若你的結論有「整合照護提高篩檢完成」，須確認不是「介入即檢查」的構念重疊。另請核對 CARRS（RR 2.24、HbA1c −0.50）是否有把 care coordinator 與 EHR CDS 分開的分析；若沒有，不可作為 CDS／AI 單獨效益。

### → psychosocial
**請核對你納入的所有 AI／chatbot／數位心理介入，是否有「隨機對照＋以 diabetes distress 或憂鬱量表的組間差異為主要結局」的研究。**
理由：我在 methods_ai 的定向檢索沒有找到 LLM／chatbot 針對糖尿病心理結局的 RCT；REDEEM 的整體組間差異不顯著（`docs/12` §5）。若你仍保留「AI 可緩解 distress」的語句，需降級為設計推論；若你找到 RCT，請給 PMID 與主要結局的組間效應與 CI，我會在 crosscheck 中納入。

### → calculators
**請確認每個「spec_only」風險方程式（SCORE2-Diabetes、PREVENT、RECODe、KFRE）是否都有「Taiwan 或同族群的外部校準」欄位，並在沒有時禁止輸出絕對風險給病人端。**
理由：Su 2024（台灣）📄 三個傳統方程式都需重校準，Walker 2026 📄 顯示 KFRE 在多重共病會低估；兩者都表示「外部校準」不只是 AUC。若 spec 目前把這些方程式視為可直接用，結論要改成「僅提供排序／分層，絕對風險須註明未經台灣驗證」。

---

## C. 需要 lead（跨目錄）處理的項目

| # | 項目 | 說明 |
| --- | --- | --- |
| 1 | `docs/07`、`docs/08` 修正 | 完整逐項清單在 `sessions/methods_ai/report.md` §8。需要 Codex 決定是否採用；其中 5 項本輪無法核實（Diabetes Wizard 命名、健保署日期、國衛院期間、三總 MEDIC、ADA S12 的 AI 敘述）。`docs/08` 的 PMC 連結缺 `PMC` 前綴（應為 `PMC13022550`） |
| 2 | `docs/12` §6 | pivotal 加註 819 可分析；ACCESS 加註「AI 組完成即介入本身」 |
| 3 | `docs/13` §3–§4 | 依 §A2 補 eGFR 版本與 G3a／高齡／多重共病的校準限制；North America 5 年 S0 待對 supplement 再核 |
| 4 | `scripts/fulltext_tools.py` 缺陷 | `pmc 21482743`（PMID，不在 PMC）寫出無關論文 `PMC13746208.md`（Testican-2）。我已刪檔，但 `literature/receipts/methods_ai.jsonl` 仍有該筆 receipt，請刪除或標記為無效。建議工具在 ID 轉換失敗時回報 `NO_PMC` 而非誤配 |
| 5 | Receipts 缺口 | Dundee 典藏 PDF（Grams 2023 作者接受稿）與 ACL Anthology PDF（DIASENTINEL）是用 `curl`＋`pdftotext` 取得，沒有經過 `fulltext_tools.py`，故沒有 receipt。檔案在 `literature/fulltext/methods_ai/`（git-ignored） |
| 6 | 要不要補 | 若要完成正式 RoB 2／PROBAST+AI／QUADAS-2 評讀，需另外安排雙人評讀；`report.md` §5 明確標為初步篩檢 |
| 7 | 官方頁面存取 | 健保署頁、三總頁、ADA S12 頁對自動化請求回 403，我沒有嘗試繞過。需要有人用正常瀏覽器開啟確認 |

## D. 可重現性

- 全文：`literature/parsed/methods_ai/`（25 檔，git-ignored）
- 重現 grep：`python3 -I literature/notes/methods_ai/claim_checks.py`，輸出 `literature/notes/methods_ai/claim_checks_output.txt`（0 MISS）
- 檢索與工具失敗：`sessions/methods_ai/search_log.md`
