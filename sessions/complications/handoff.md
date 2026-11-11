# complications → lead：handoff

日期：2026-11-11。我沒有 commit／push／切 branch，沒有修改 `sessions/<other>/`、`docs/`、`workflow/`、`scripts/`、`sources/`、`calculators/`。下列為需 lead 處理的跨目錄項目與給其他 sessions 的問題。

---

## A. 需 lead 修改的跨目錄項目

### A1. `scripts/fulltext_tools.py`：PMID→PMCID 解析會取回「引用該文的文章」（污染風險，**高**）

- 位置：`cmd_pmc()`，`elink.fcgi?dbfrom=pubmed&db=pmc&id=<PMID>`，取 `data["linksetdbs"][0]["links"][0]`。
- 實測失效：PMID 12556541（Steno-2 2003）→ PMC13738796（2026 年 IRT 建模論文）；18256393 → PMC13731741；31748169、29079252 → 同一個 PMC13693898（2026 年 J-DOIT3 流行病學分析）。`linksetdbs[0]` 並非固定為 `pubmed_pmc`（本文），可能是 `pubmed_pmc_refs`（被引用）。
- 建議：遍歷 `linksetdbs`，只接受 `linkname == "pubmed_pmc"`；或改用 `esummary` 的 `articleids[idtype=pmc]`；並在寫檔前用 `<article-meta>` 的 PMID 與輸入比對，不符則 `NO_PMC`。同步提醒其他 sessions：凡經 PMID 呼叫 `pmc` 者請用標題比對。
- 我已刪除 3 個錯誤檔（PMC13738796／PMC13731741／PMC13693898）並移除 `literature/receipts/complications.jsonl` 中對應 4 行；其他 sessions 的 receipts 若有類似行，請 lead 檢查。

### A2. 5 篇無開放全文（PubMed abstract 為止）

Steno-2 2003（12556541）、Steno-2 2008（18256393）、ADDITION 10 年（31748169）、J-DOIT3（29079252）、INDEPENDENT（32809002，PMC 只有 Key Points）。`download_with_fallback` 失敗（Unpaywall 無 OA 或未設 email）。**未使用 Sci-Hub**（繞過付費牆，非我能決定）。如需補全文，請 lead／使用者明示是否授權，或由有機構權限者提供 PDF 後走 LlamaParse。

### A3. 文件修正（逐行見 `report.md` 第 7 節）

- `docs/03-integrated-care-evidence.md`：L7、L8、L9、L10、L11、L12 補充；整表補 Steno-2、ADDITION、J-DOIT3、Cochrane QI（陰性／中性）。**未發現硬性數字錯誤。**
- `workflow/claim_review.csv`：`claude_status` 建議值 — C01 `verified_fulltext`、C03 `partially_verified`（Table 2 取不到）、C04 `partially_verified`（改引 Hu 2023 PMC10069524 L49 為 aDCSI 13 點；Young 2008 PMC3810070 無本文）、C06 `verified_fulltext`（**ACCESS 為青少年 8–21 歲**）、C10 `verified_fulltext`。
- `sources/evidence_matrix_20261111.csv`：L4 ADDITION-Europe 2011 補 DOI `10.1016/S0140-6736(11)60698-3`；L12 Taiwan newly diagnosed P4P 補 DOI `10.1097/MD.0000000000019139`。

### A4. 需要有全文權限者核對（UNRESOLVED）

1. ADA Standards of Care 2026 Section 4（PMID 41358897）完整建議內容。
2. IWGDF 指引、HF／PAD／認知／frailty 的整合照護證據（本輪未檢索或未找到）。
3. Taiwan 糖尿病共同照護網專屬論文（B21 檢索未命中）。

---

## B. 給其他 sessions 的問題（各一項，足以改變綜合結論）

### → methods_ai
**能否找到任何「成人 T2D」隨機試驗，其 AI／CDS／LLM 介入的主要或預先設定次要結局是「異常篩檢後處置完成」（轉介完成、治療起始）且用「全部隨機人數」當分母——並且 CDS 被單獨拆出（沒有人類照護協調員）？**
為何會改變結論：我手上的整合照護證據（CARRS、INDEPENDENT、JADE、TEAMcare）全是「軟體＋人力」綑綁。CARRS 全文自述 “unable to examine the relative effectiveness of individual intervention components”（PMC6561084 limitations 段）📄；JADE-DKD 中只有報告＋電話提醒（empowered care）相對 usual care RR 0.95（0.80–1.12）無益，加入固定團隊後才有效（RR 1.20，1.03–1.40）📄。ACCESS 的 AI 組完成篩檢 100%，但 AI 陽性者 16/25（64%）完成追蹤；對照組「22%」的 follow-through 是 **18/83**（你們 handoff 寫 18/82，ACCESS n=83，請以 PMC10784572 L47–51 為準），且該 18 人無一有 DED，因此兩個 follow-through 數字分母不同、不可相減；若沒有「CDS 單獨效益」或「下游完成度」的成人 T2D 隨機證據，綜合結論就只能寫「AI 可增加篩檢完成；對處置完成與硬終點未證實，且不能取代人力協調」。

### → calculators
**請核對 aDCSI 的計分規則與外部驗證數字，並說明「缺資料」的處理：**
(1) Hu 2023（PMID 36977521，PMC10069524 L49）：aDCSI 為 **13 點**、七類並發症各 0–2、**neuropathy 0–1**——請與你們實作的項目→分數對照表逐項核對（Young 2008 原始 DCSI 的 Table 1 我取不到本文）；並確認你們是否把 DCSI 與 aDCSI 混稱。
(2) 同篇台灣 1,002,589 人：aDCSI all-cause 死亡 HR 1.21（1.20–1.21）、C-index 0.760／0.794／0.781（all-cause／CVD／diabetes death），CCI HR 1.18（1.17–1.18）。請確認這些數字是否可寫入 spec 的「外部參考」欄，並註明它是**診斷碼型、以死亡校準、無 BMI／吸菸／檢驗值**，不是 UACR／eGFR 的函數。
(3) 為何會改變結論：Chu 2022 顯示 59% 的 CKD 病人沒有 albuminuria 測試（PMID 36434513）📄；UACR 測試率合併值 22%（固定）／49%（隨機，CI 7–93%）（PMID 41345917）📄。**KFRE 與 UACR 相關公式的多數病人將缺 UACR；請確認 spec 是「缺值＝無法計算並產生待辦」，而不是以 0 或中位數代入，且 aDCSI 的「無診斷碼」不得輸出為 0 分的「無並發症」。**

### → psychosocial
**請從 INDEPENDENT（PMID 32809002）全文 Table 2／Table 3 與 TEAMcare（PMID 21190455，PMC3312811 Table 2–3）取出複合結局的各成分：SCL-20 ≥50% 降低的達成率、以及 HbA1c −0.5／SBP −5／LDL −10 各自的組間差異，並回答「心理與生理是否真的同時改善，還是複合結局主要由憂鬱成分驅動」。**
為何會改變結論：INDEPENDENT 的 abstract 顯示 16 項預先設定次要結局中，12 個月 10 項、24 個月 13 項無顯著組間差異；且 abstract 71.6% vs 57.4% 與 Key Points 71.6% vs 54.7% 並存（RD 16.9 與 54.7 吻合）；severe hypoglycemia 8（4.1%）vs 0。我只有 abstract／Key Points（PMC 無本文）。若心代謝成分並未獨立達顯著，`docs/03` L8 與 `docs/12` 的「身心共同改善」就需降級為「憂鬱改善，代謝成分混合」。TEAMcare 的同題請以全文 Table 核對（我確認了 HbA1c 差 0.58%、LDL 6.9 mg/dl、SBP 5.1 mmHg、SCL-20 0.40 的合併模型結果，但沒有拆各成分的達成率）。

---

## C. 讓 lead 整合時可直接使用的一句話結論（皆已有 `report.md` 來源）

1. 整合照護對代理指標一致但 modest；硬終點證據少且條件依賴（Steno-2 正向；ADDITION、J-DOIT3、JADE 中性；CARRS 長期僅續行站點、僅微血管有益）。
2. 流程斷點（UACR、轉介、SGLT2i、DR 追蹤）是目前最強的困難點量化；各研究分母與制度不同，不可串成單一漏斗。
3. 「報告／評估」本身無效，需要有人負責的團隊迴圈（JADE-DKD empowered care vs team-based）。
4. 台灣 P4P 觀察研究不得當因果證據（aHR 0.58 且依從梯度）。
