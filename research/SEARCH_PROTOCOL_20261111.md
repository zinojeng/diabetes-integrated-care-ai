# PubMed 主題檢索與查核規格

日期：2026-11-11，Asia/Taipei。問題：AI如何支援糖尿病併發症、多重共病及心理照護的整合？主要為成人T2D，T1D/兒少研究保留但明列外推限制。

## 實際執行範圍

本輪以英文網路檢索定位PubMed索引與primary sources，並讀取可取得的PubMed摘要、PMC/期刊HTML及指定公式補充附錄。使用下列主題與研究名稱補充搜尋，採目的式選取anchor studies與反證。未產生完整PubMed資料庫匯出、去重總數、雙人逐篇篩選或正式RoB表；本報告是主題式深入綜整，**不是systematic review**。

本機`paper-search/search_pubmed`實測送出`diabetes integrated care complications randomized`，max_results=5；因`eutils.ncbi.nlm.nih.gov` DNS失敗，沒有取得結果。`research_hub`在啟動時發生Rust system-configuration NULL panic，未取得搜尋或下載結果。LlamaParse MCP可列出工具，但無已下載PDF可送件，API key尚未透過成功解析驗證。網路全文閱讀不等於PDF已下載，也不等於已LlamaParse。

## 可重跑 PubMed 檢索式

以下為**可重現查詢規格**，不將其尚未成功取得的count/PMID list標成已執行。搜尋時不限制English出版語言，只用English terms；截止日期先用2026-11-11，再人工核對electronic publication date，避免排除已上線但紙本卷期在未來的文章。

### Q1 整合照護與困難

```text
("Diabetes Mellitus"[Mesh] OR diabetes[tiab]) AND
("Delivery of Health Care, Integrated"[Mesh] OR integrated care[tiab]
 OR collaborative care[tiab] OR multidisciplinary[tiab] OR interdisciplinary[tiab]) AND
(barrier*[tiab] OR multimorbidity[tiab] OR treatment burden[tiab]
 OR complication*[tiab] OR clinical inertia[tiab])
```

### Q2 多重因子處理與併發症

```text
("Diabetes Mellitus, Type 2"[Mesh] OR type 2 diabetes[tiab]) AND
(multifactorial[tiab] OR integrated care[tiab] OR care coordination[tiab]) AND
(kidney[tiab] OR cardiovascular[tiab] OR retinopathy[tiab]
 OR neuropathy[tiab] OR foot[tiab] OR amputation[tiab] OR mortality[tiab])
```

### Q3 心理與生理共同照護

```text
("Diabetes Mellitus"[Mesh] OR diabetes[tiab]) AND
(diabetes distress[tiab] OR depression[tiab] OR anxiety[tiab]
 OR psychosocial[tiab] OR fear of hypoglycemia[tiab]) AND
(collaborative care[tiab] OR integrated care[tiab]
 OR randomized controlled trial[pt] OR guideline[pt])
```

### Q4 AI整合

```text
(diabetes[tiab] OR diabetic[tiab]) AND
("Artificial Intelligence"[Mesh] OR autonomous AI[tiab]
 OR clinical decision support[tiab] OR large language model*[tiab]
 OR retrieval augmented generation[tiab] OR agentic[tiab]) AND
(complication*[tiab] OR screening[tiab] OR care coordination[tiab]
 OR retinopathy[tiab] OR insulin[tiab] OR psychosocial[tiab])
```

### Q5 Calculator development及validation

```text
(diabetes[tiab] OR chronic kidney disease[tiab]) AND
(RECODe[tiab] OR SCORE2-Diabetes[tiab] OR KFRE[tiab]
 OR kidney failure risk equation[tiab] OR DCSI[tiab] OR aDCSI[tiab]
 OR PHQ-9[tiab] OR GAD-7[tiab] OR diabetes distress scale[tiab]
 OR PAID[tiab] OR WHO-5[tiab] OR FIB-4[tiab]) AND
(development[tiab] OR validation[tiab] OR calibration[tiab] OR scoring[tiab])
```

另逐篇名稱追查Steno-2、ADDITION-Europe、J-DOIT3、TEAMcare、INDEPENDENT、CARRS、JADE、ACCESS與原始量表/公式，避免一般關鍵字遺漏經典文獻。

## 納入及萃取規則

優先指南、RCT、prospective diagnostic/validation與有比較組的實施研究；觀察研究與回顧分開標示。每篇保留design、population、n、setting、intervention/comparator、time、primary/secondary/post-hoc、effect/CI、harms、bias、PMID/DOI及access level。陰性結果、來源內部不一致和工具失敗均保留。未拿到的全文寫abstract_only，不宣稱完整附錄查核。

本輪正式Claude交叉審查未完成。Codex平行研究協助的結果不能冒充Claude Opus回覆；最後主文由Codex整理及查核。實際狀態見[execution status](../workflow/EXECUTION_STATUS_20261111.md)。
