# calculators handoff（給 lead 與其他 sessions）

## A. 需要 lead 修改／決定的跨目錄項目

1. **`scripts/fulltext_tools.py pmc <PMID>` 缺陷**（高優先）：`elink dbfrom=pubmed&db=pmc` 取 `linksets[0].linksetdbs[0].links[0]`，可能是「被引用」集合，導致寫入不相關文章（我遇到 9 篇，例如 FIB-4 的 PMID 對到肝切除回顧）。建議：`linkname=pubmed_pmc`＋驗證回傳標題（或改用 idconv）；且 `literature/receipts/calculators.jsonl` 內有這 9 筆錯誤 receipt（檔案已刪），請決定是否改寫。另外 `jats_to_md` 丟失非 `<sec>` 直屬的 `<table-wrap>`（RECODe 主文因此沒表格；Agent A 已用 `_tables.md` 繞過）。
2. **文件修訂**：`docs/13-calculator-specifications.md` 與 `research/VERIFICATION_CALCULATORS_20261111.md` 建議改為：
   - KFRE：本地僅 Original 5 年（0.9240）與 non-NA 5 年（0.9365）有 grep 證據；2 年值（0.9750／0.9832）與 North-America 值（0.9751／0.8996）**未能在本地原文驗證**（JAMA 403，PMC 補充 proof-of-work）。
   - SCORE2-Diabetes：現在已有完整係數、四區 scale、官方 Excel 向量；footnote（0.9625／0.9795）與計算表（0.9605／0.9776）不一致，以官方 Excel 為準；原模型 eGFR 為 CKD-EPI **2009**。
   - RECODe：9 個 outcome 的係數與 λ／mean 已在主文印出；「每個 outcome 一方程」仍成立；footnote 允許略過缺項（本實作預設拒算）。
   - TIMI：該文是 **TRS 2°P 的 T2D 應用（SAVOR-TIMI 53）**，不是 TRS-AD。
   - FIB-4 切點：本地只在開放二手文獻找到 1.3／2.67／>65 歲 2.0；EASL 2024 與 ADA 2026 的年齡分流表在本地全文不可 grep。
   - DDS-2 出處是 **Ann Fam Med 2008**；DDS-17 英文版為 1–6 分（德文二手為 0–5，不可混用）。
3. **要不要動用 Sci-Hub**：協議允許作 2021 年前論文最後備援（DCSI 2008、Charlson 1987、Karter 2017、WATCH-DM 2019、Sterling 2006、PHQ-9 2001 等）。我**沒有使用**；請 lead 明確決定。若 lead 或使用者能手動提供 PDF（Young 2008 Table 1、Chang 2012 ICD 映射、Karter 2017 points table、WATCH-DM 2019、Tangri 2016 eAppendix 2 p9、PREVENT Supplemental Table S12 與 AHA 更正後係數表），放入 `literature/fulltext/calculators/` 後我可補實作／驗證。
4. **提交範圍**：新增且未追蹤的有 `calculators/`、`tests/calculators/`、`sessions/calculators/`、`literature/notes/calculators/agent*_*.md`（含逐字表格轉錄，約 130 KB；請依版權政策決定是否提交，或只保留 `sessions/calculators/`）、`literature/receipts/calculators.jsonl`。`literature/fulltext/`、`literature/parsed/` 已 git-ignored。我沒有 commit／push。
5. **模型 ID 備註**：本 session 的實際模型是否為 `claude-opus-5-5` 我無法由 session 內證實（系統資訊顯示 `claude-sonnet-5-5`）；依 CLAUDE.md「失效時停止並回報」，請 lead 判斷是否需重開。

## B. 給其他 sessions 的具體問題

### methods_ai（獨立核對 KFRE 版本與單位）
- 請以能開啟 JAMA 2016 supplement 的管道核對 **eAppendix 2 第 9 頁**：(a) 係數 −0.2201／0.2467／−0.5567／0.4510 與中心值 7.036／0.5642／7.222／5.137；(b) Original：2 年 S0 **0.9750**、5 年 **0.9240**；(c) North-America 重校準：2 年 **0.9751**、5 年 **0.8996**；(d) non-North-America：2 年 **0.9832**、5 年 **0.9365**；(e) UACR 單位是否為 mg/g（`ln(UACR mg/g)`）。我只在本地 grep 到 0.9240（PMC7203563 Table 4）與 0.9365（PMC11813909 Table 4 base hazard 0.0635）。
- 請確認我「2 年值 provisional、NA 值 spec_only」的處理；若你核對一致，我會移除 provisional 閘門。
- 請檢查 `calculators/dmic_calculators/ckd.py` 的 `kfre_4var()` 沒有把 eGFR≥60 或 G1–G2 當成合法（目前 `eGFR>=60` 回 `population_ok=False` 並拒算）。

### psychosocial（核對量表版本與 cut-off）
- 請核對：PHQ-9（5/10/15/20）、PHQ-2（≥3）、GAD-7（5/10/15；≥10）、WHO-5（0–5×5，raw×4；raw<13／<50%；高＝好）、PAID-20（現行 0–4 ×1.25；≥40）、PAID-5（0–4，0–20，≥8；題號 3、6、12、16、19）、DDS-2（平均≥3）、DDS-17（1–6 平均；<2／2–2.9／≥3）、HFS-II（0–4；Behavior 15 題 0–60、Worry 18 題 0–72）與你們報告是否一致；特別是 **PAID-20 的 0–4 現行版 vs 1995 六點原版**、**DDS-17 是否另有繁中授權／0–5 版**、**PHQ-9 item 9 的警示是 DMIC 設計選擇（手冊無此規則）**。
- 台灣／繁中正式版：Liu 2011 PHQ-9、PAID-C（PMC2797982）、Taiwan DDS（PMC8968751 是新開發量表，非 DDS-17 翻譯）、WHO-5 中文版、CFS 繁中（Dalhousie 翻譯名單）；請提供你們查到的版本與授權，我不嵌入任何題目文字。
- MoCA：官網 permission 頁（要求訓練）與 FAQ／terms（僅總分可選認證）矛盾；請由 psychosocial 判斷臨床使用條件。

### complications（核對 DCSI／CCI 應用情境）
- 請確認 DCSI／aDCSI 在你們的報告中如何使用（我這邊 **spec_only**，因 Young 2008 Table 1 rubric 與 Chang 2012 ICD 映射沒有任何本地全文）。若你們報告已含可 grep 的 rubric 請提供出處（PMID／PMC＋表格位置）。
- Charlson：請決定整合照護中用 original 1987 還是 Quan 2011，以及是否需要 ICD 映射（Quan 2005 碼表在 `PMC13586706`；本輪未編碼）。糖尿病兩項已用層級輸入避免重複。Quan 2011 renal weight 在三處來源為 1／1／4，請以原文核對。
- 請提供 DCSI／CCI 在台灣（NHIRD）的比較文獻（repo 文件提到 PMID 36977521）是否能取得全文。

## C. 給 lead 的使用提醒
- `value=None` 並不代表正常；請上游/AI 層保留 `reasons_unavailable`，並分開呈現疾病狀態、風險估計、資料完整度、行動狀態。
- 不要把 SCORE2-Diabetes／RECODe／TIMI／KFRE 等結果相加或平均成單一總分；RECODe 每個 outcome 獨立。
- 台灣沒有任何已完成的本地校準證據；SCORE2-Diabetes 必須明確選區（無預設）。
