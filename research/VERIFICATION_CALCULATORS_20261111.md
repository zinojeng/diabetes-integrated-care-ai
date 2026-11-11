# Calculator 獨立查核紀錄

查核日期：2026-11-11（Asia/Taipei）。執行者：Codex calculator verifier；本檔不是 Claude 回覆，也不是臨床 calculator 軟體驗證。

範圍：針對 [calculator 規格](../docs/13-calculator-specifications.md) 的高風險數字、適用族群、量表算法做定向查核。英文檢索，查閱 PubMed、PMC、原發表期刊與官方文件；這是針對既有規格的查核，並未完成系統性回顧或所有模型係數／授權／繁中版本的全面驗證。

## 1. 查核結論與需補充項目

| 項目 | 結論 | 建議修訂 |
| --- | --- | --- |
| KFRE 四變項係數、中心化常數及三組 S0 | 與 JAMA 2016 supplement eAppendix 2 一致 | 保留現有數字。補註北美重校準版本不是「原始版本」的同義字；不能任意選較低風險結果 |
| KFRE 適用 CKD G3–G5、KDIGO 三個門檻 | 核對一致 | 標明為輔助照護時機的 practice points；非自動轉介／開始 dialysis 的命令 |
| FIB-4 公式與單位 | 核對一致 | 將較高齡門檻依來源寫清楚；ADA 2026 為 diabetes 年齡 ≥65 歲建議 1.9–2.0，AASLD 2023 文字為 >65 歲且 cutoff >2.0，不宜合併成完全相同規則 |
| FIB-4 低值解讀 | 原文件已提醒不能保證排除 | 可增列 ADA 2026：T2D 合併多個 cardiometabolic risk factors 時，即使 1.0–1.3 仍可能需要第二階段評估 |
| PREVENT 2026 HbA1c 修正 | 官方更新確實存在 | 可改成「2026-10-14 官方修正已確認；全套係數及官方測試向量尚未逐項驗證」 |
| SCORE2-Diabetes | 族群／地區限制敘述適當 | 保留 spec_only；實作時須固定 HbA1c 的 mmol/mol 與 cholesterol 的 mmol/L，不能直接把 % 或 mg/dL 放入原方程 |
| CCI、DCSI/aDCSI | 疾病負擔與風險百分比的區分適當 | 目前尚無完整、已核對之 CCI/ICD mapping implementation；維持文件規格狀態 |
| 心理量表 | 五工具的基本計分與方向一致 | DDS17 的「2–2.9」需在實作前明確定義小數處理；WHO-5 採官方文字 <50 或 raw <13 |
| 缺值處理 | 原文件「不靜默補零」適當 | 問卷未完成與症狀不存在是不同狀態；各正式版本如有缺答規則須獨立記錄 |

## 2. KFRE：可確認的公式，不同版本須分開保存

四變項線性預測項：

```text
LP = -0.2201 × (age/10 - 7.036)
     +0.2467 × (male - 0.5642)
     -0.5567 × (eGFR/5 - 7.222)
     +0.4510 × (ln[UACR mg/g] - 5.137)
Risk(t) = 1 - S0(t)^exp(LP)
```

| eAppendix 2 的版本 | 2-year S0 | 5-year S0 |
| --- | ---: | ---: |
| Original | 0.9750 | 0.9240 |
| Regionally calibrated original — North America | 0.9751 | 0.8996 |
| Regionally calibrated original — non-North America | 0.9832 | 0.9365 |

來源：[Tangri et al., JAMA 2016](https://jamanetwork.com/journals/jama/fullarticle/2481005)，DOI **10.1001/jama.2015.18202**，PMID **26757465**，Supplement eAppendix 2，第9頁（PDF page index 8）。已直接開啟補充 PDF 核對；不以一般 calculator 網站取代原係數表。原文指出北美重校準並未顯著改善 calibration，故不能把表中存在某版本等同它是所有北美病人的首選。

Age 為年、male 為 1/0、eGFR 為 mL/min/1.73 m²、UACR 為 mg/g、log 為自然對數。UACR mg/mmol 應先乘約 8.84；UACR ≤0 或缺值不直接計算。本公式目標是 CKD 病人接受 dialysis／transplantation 的風險，不能外推為所有糖尿病患者「腎病發生率」。對臺灣的選擇仍須本地 validation/calibration。

[KDIGO 2024](https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf) 的適用框架為 CKD G3–G5。5年 **3–5%** 可輔助 nephrology referral；2年 **>10%** 可輔助 multidisciplinary care 時機；2年 **>40%** 可輔助 KRT education／準備。這些判斷仍與 eGFR、臨床情況及病人選擇併用。

## 3. FIB-4：算式相同，情境與分流規則不同

```text
FIB-4 = age(years) × AST(U/L) /
        [platelets(10^9/L) × sqrt(ALT(U/L))]
```

[Sterling 2006](https://pubmed.ncbi.nlm.nih.gov/16729309/)，DOI **10.1002/hep.21178**，為 HIV/HCV coinfection 模型開發研究；原研究的 cutoffs 不能直接當成所有 MASLD 分流標準。

[ADA 2026 Section 4](https://doi.org/10.2337/dc26-S004)，PMID **41358897**：一般 <1.3 為較低風險；≥1.3 需進一步 LSM／ELF 分流；>2.67 支持轉 liver specialist。Diabetes 年齡 ≥65 歲可採較高低端門檻 1.9–2.0。T2D 且多個 cardiometabolic risk factors 者，1.0–1.3 亦可能需追加評估。正常 ALT 不是跳過 fibrosis 評估的理由。

[AASLD 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10735173/)，PMID **36727674**：文字採 >65 歲、cutoff >2.0；<35歲準確性較低；急性疾病不應使用；T2D 可考慮每1–2年再評估。這些應標明採用來源，而非把兩份指引壓成一條未標版本的規則。

Platelets 10³/µL 與 10⁹/L 數值相同；raw cells/µL 必須除1000。ALT／platelets 必須為正值。輸出是纖維化分流指標，並非 MASH 病理確診或個人未來肝硬化的百分比。

## 4. PREVENT 與 SCORE2-Diabetes：仍維持 spec_only

**PREVENT。** [AHA 官方 calculator](https://professional.heart.org/en/guidelines-and-statements/prevent-calculator) 支援無已知 CVD 者的 10年風險（30–79歲）與30年風險（30–59歲）；CVD、ASCVD、HF 是不同模型，風險不能相加成總 CVD。**2026-10-14 的 HbA1c 修正已由[官方FAQ](https://professional.heart.org/-/media/PHD-Files/Guidelines-and-Statements/PREVENT/PREVENT-Update-FAQ-101426.pdf)確認。** 影響 HbA1c add-on 與 full equations，base／只加 UACR 或 SDI 的版本未受影響。本次沒有逐一轉錄修正後 workbook 全部係數，不能標為 calculator 已驗證。

**SCORE2-Diabetes。** [原始研究](https://pubmed.ncbi.nlm.nih.gov/37247330/)，DOI **10.1093/eurheartj/ehad260**，由歐洲資料開發、校準於四個歐洲風險區域。除一般 CVD 因子外，包含 diabetes 診斷年齡、HbA1c、eGFR。[ESC 2023](https://academic.oup.com/eurheartj/article/44/39/4043/7238227) 的典型適用為40–69歲T2D、無ASCVD／severe target-organ damage。臺灣不能因 geography 不符就任選歐洲「low risk」組。實作前須逐項確認 sex-specific coefficients、interactions、baseline survival、regional transformation及輸入單位。

## 5. 疾病負擔：CCI 與 DCSI/aDCSI

**DCSI = 七領域各自最嚴重等級的總和**；Neuropathy 0/1，其餘領域0/1/2，範圍0–13。[Young 2008](https://pmc.ncbi.nlm.nih.gov/articles/PMC3810070/)，PMID **18197741** 的原始版本包含實驗室與ICD-9資料。[Chang 2012](https://pubmed.ncbi.nlm.nih.gov/23198714/)，PMID **23198714**，驗證的是不含實驗室的aDCSI。兩者不能混用；同一領域多個診斷不是重複加分。

**CCI = Σ(版本指定權重 × 該疾病類別指標)**。[Charlson 1987](https://pubmed.ncbi.nlm.nih.gov/3558716/)，DOI **10.1016/0021-9681(87)90171-8**，支持預後共病分類；沒有支持把其歷史研究中的死亡比例直接輸出給當代臺灣個人。原始權重、age-adjusted版本、ICD映射各需固定。此輪未全面核對完整權重／ICD mapping，不建立可執行版本。

兩工具可作研究調整或病例複雜度描述。缺少診斷資料時應同時顯示資料覆蓋率；「資料中未觀察到」不能自動變成「臨床已排除」。

## 6. 心理量表：當前狀態與照護需求，不是器官事件機率

| 工具 | 本次確認的計分 | 需固定的實作細節 |
| --- | --- | --- |
| PHQ-9 | Σ9題，each 0–3；0–27；嚴重度界線5/10/15/20 | 先確認答題完整性。陽性需臨床評估，不能依總分直接建立diagnosis；第9題另保留人工評估流程 |
| GAD-7 | Σ7題，each 0–3；0–21；界線5/10/15 | 表達近兩週症狀；不能把高分直接當符合完整 GAD 診斷的病程條件 |
| DDS17 | 17題each 1–6，平均分；四個分量表另取平均 | 低<2；高≥3；論文「2–2.9」需明訂小數處理，不讓2.94因程式區間缺口而無分類 |
| PAID20 | 20題each 0–4，總和×1.25，0–100；≥40代表高度 distress | PAID5不得套本公式；也應檢視各題3/4分問題，不只看總分 |
| WHO-5 | 5題each 0–5；raw0–25×4，0–100，越高越好 | 官方門檻<50或raw<13。完整整數題分下實際為raw≤12／percentage≤48；不表示確診depression |

PHQ-9：[Kroenke 2001](https://pmc.ncbi.nlm.nih.gov/articles/PMC1495268/)，PMID **11556941**，DOI **10.1046/j.1525-1497.2001.016009606.x**。GAD-7：[Spitzer 2006](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/410326/)，PMID **16717171**，DOI **10.1001/archinte.166.10.1092**。DDS cutoffs：[Fisher 2012](https://pubmed.ncbi.nlm.nih.gov/22228744/)，DOI **10.2337/dc11-1572**，及[開發團隊計分說明](https://diabetesdistress.org/dd-assess-score-3/)。PAID20：[NDSS 現行說明](https://www.ndss.com.au/health-professionals/supporting-emotional-health/mental-health-questionnaires/paid-scale/)。WHO-5：[WHO 2024 官方文件](https://www.who.int/publications/m/item/WHO-UCN-MSD-MHE-2024.01)，已讀PDF的Scoring段落。

DDS17 小數處理是**實作需預先決定的邊界事項**，不是此輪發現新的臨床cutoff。建議原始平均值完整保存，採<2／2≤x<3／≥3作程式區間並在實作規格中揭露，另由量表負責人確認；顯示四捨五入不得先於分類。

WHO-5 2024 的授權為CC BY-NC-SA 3.0 IGO。各問卷的正式繁中翻譯、授權與缺答算法仍須各自查核；這次不重製完整題目，也不宣稱已完成繁中量表驗證。

## 7. 交付狀態與下一步

本輪確認的是文件中的公式／版本／適用性；沒有病人資料、執行版風險引擎或本地臨床validation。PREVENT、SCORE2-Diabetes、CCI完整mapping仍保留 spec_only。KFRE和FIB-4進入實作前，需用官方或原文數值例、單位換算與資格邊界做驗證；量表須以正式版本、完整答題、保留原始分數及明確人工接手流程進行。

來源與逐項狀態見 [JSON紀錄](../sources/calculator_verification_20261111.json)。

