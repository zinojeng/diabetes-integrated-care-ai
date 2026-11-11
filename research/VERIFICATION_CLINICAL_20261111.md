# 糖尿病整合照護：獨立臨床證據查核

查核日期：2026-11-11（Asia/Taipei）。執行者為 Codex 證據查核工作，不代表 Claude 已回覆或完成 cross-session review。

本文件針對既有綜述的 12 項關鍵原始研究進行定向查核，並核對 EASD 2026 distress guideline。以英文查詢 PubMed 索引、PMC 與原始期刊頁；不是 systematic review，沒有全面檢索、雙人篩選、正式 RoB 或可報告的資料庫命中總數。下列「全文」指本次實際讀取的 HTML 相關段落與表格，不代表下載 PDF、讀完所有 supplements 或已完成 LlamaParse。

## 1. 判斷與對本研究的意義

整合照護已有部分器官結局與存活證據；心理照護與生理風險可以一起改善。但本次核對的 AI 證據主要是特定診斷任務、篩檢完成、短期血糖管理與專家評估。不能把 Steno-2 或 CARRS 的效益直接歸因給 generative AI。

對本專案最可檢驗的問題是：AI 加入既有團隊後，能否讓 kidney、eye、foot/vascular 與心理照護缺口更快被確認、分派並完成，同時減少病人及團隊負擔？此為研究設計推論，尚非已驗證療效。

## 2. 十二項研究的查核結果

| 研究與識別碼 | 設計、族群與已核對結果 | 解讀邊界及本次來源層級 |
| --- | --- | --- |
| **Steno-2 2003**；[PMID 12556541](https://pubmed.ncbi.nlm.nih.gov/12556541/)；[DOI](https://doi.org/10.1056/NEJMoa021778) | 160 名 T2D＋microalbuminuria；多重風險介入平均 7.8 年。CVD HR 0.47（95% CI 0.24–0.73）；nephropathy HR 0.39、retinopathy HR 0.42。 | 高風險、較早治療年代、小型多組件試驗；不能分離個別藥物、個管或 AI 的效果。**PubMed 摘要核對**。 |
| **Steno-2 2016 follow-up**；[PMID 27531506](https://pubmed.ncbi.nlm.nih.gov/27531506/)；[DOI](https://doi.org/10.1007/s00125-016-4065-6) | 21.2 年追蹤；原 intensive 組 38 人、conventional 組 55 人死亡，HR 0.55（0.36–0.83）；median survival 差 7.9 年。 | 差異介入為前 7.8 年，其後均採 intensive treatment。不能稱 21 年持續隨機差異治療。**PubMed 摘要核對**。 |
| **ADDITION-Europe 2019**；[PMID 31748169](https://pubmed.ncbi.nlm.nih.gov/31748169/)；[DOI](https://doi.org/10.1016/S2213-8587(19)30349-3) | 3,057 名篩檢發現 T2D，cluster randomisation；10 年 post-hoc 追蹤，3,031 人納入分析。CVD HR 0.87（0.73–1.04）；死亡 HR 0.90（0.76–1.07），皆未顯著。 | 第 5 年後未維持治療差異。用來平衡「更密集必然改善硬結局」的推論。**原期刊摘要核對**。 |
| **TEAMcare 2010**；[PMID 21190455](https://pubmed.ncbi.nlm.nih.gov/21190455/)；[DOI](https://doi.org/10.1056/NEJMoa1003955) | 214 人、14 間基層診所；depression＋控制不佳 diabetes/CHD。護理個管與醫師共同管理，12 個月整體多指標改善；HbA1c 組間改善差 0.58 percentage points、LDL-C 6.9 mg/dL、SBP 5.1 mmHg、SCL-20 0.40 分。 | 主要是中間指標、情緒與生活品質，非 AI 或器官事件試驗。**PubMed 摘要核對；PMC 本次未成功讀取**。 |
| **INDEPENDENT 2020**；[PMID 32809002](https://pubmed.ncbi.nlm.nih.gov/32809002/)；[DOI](https://doi.org/10.1001/jama.2020.11747) | 404 人；12 個月 collaborative care，追蹤至 24 個月。Table 2 與正文的主要複合結果為 71.6% vs 54.7%，RD 16.9 percentage points（8.5–25.2）。Severe hypoglycemia 8 人 vs 0。 | Abstract 仍印 57.4%，與表格/正文不一致，須保留註記。複合終點是情緒改善加至少一項心代謝改善，不能宣稱所有代謝指標均改善。**JAMA HTML 正文及 Table 2 核對**。 |
| **CARRS 2024 follow-up**；[PMID 38829880](https://pubmed.ncbi.nlm.nih.gov/38829880/)；[DOI](https://doi.org/10.1371/journal.pmed.1004335) | 原 1,146 人隨機試驗，6.5 年評估資料可得 854 人（74.5%）；首發 micro/macrovascular 複合 HR 0.72（0.61–0.86）；microvascular HR 0.68（0.56–0.83）。 | Post-hoc；6 站持續、4 站停止介入；macrovascular 組間未明顯不同。個管＋傳統 CDS 的整套效果，不能歸因 LLM。**PLOS HTML methods/results 核對**。 |
| **REDEEM 2013**；[PMID 23735726](https://pubmed.ncbi.nlm.nih.gov/23735726/)；[DOI](https://doi.org/10.2337/dc12-2493) | 392 名非臨床 depression、但有 distress 的 T2D；三種電腦輔助/支持介入。三組 distress 及自我照護改善，整體組間差異不顯著；HbA1c 無改善。 | 支持 distress 作為獨立照護目標；不能把組內改善當成特定高強度介入優效，亦非 generative AI。**PubMed 摘要核對**。 |
| **Autonomous DR pivotal trial 2018**；[PMID 31304320](https://pubmed.ncbi.nlm.nih.gov/31304320/)；[DOI](https://doi.org/10.1038/s41746-018-0040-6) | 900 人收案、既往無 DR；以閱讀中心影像/OCT 為參考。More-than-mild DR sensitivity 87.2%、specificity 90.7%、imageability 96.1%。 | 900 是收案數，不應當作每一指標共同分析分母。證明特定診斷效能，未直接證明失明下降。**PubMed 摘要核對**。 |
| **ACCESS 2024**；[PMID 38212308](https://pubmed.ncbi.nlm.nih.gov/38212308/)；[DOI](https://doi.org/10.1038/s41467-023-44676-z) | 164 名 8–21 歲 T1D/T2D，隨機 81 vs 83 人。主要分析篩檢完成 81/81（100%）vs 18/82（22%）；AI 異常者 16/25（64%）完成後續眼科。 | 1 名對照誤納另一研究被排除；16/25 與全對照 22% 分母條件不同，不能直接解讀成異常轉介的純相對效益。仍有 9/25 異常者未完成追蹤，且未檢驗失明。**PMC HTML 結果及 Table 3 核對**。 |
| **Voice-based basal insulin AI 2023**；[PMID 38039007](https://pubmed.ncbi.nlm.nih.gov/38039007/)；[DOI](https://doi.org/10.1001/jamanetworkopen.2023.40232) | 32 名成人 T2D、8 週；達 optimal insulin dose 中位 15 vs >56 天；insulin adherence 82.9% vs 50.2%。 | 小型、特定 basal-insulin 任務；不能外推至全藥物、全部共病或自由生成處方，也不建立長期安全性。**PubMed 摘要核對**。 |
| **iNCDSS 2025**；[PMID 40332936](https://pubmed.ncbi.nlm.nih.gov/40332936/)；[DOI](https://doi.org/10.1001/jamanetworkopen.2025.8910) | 149 名住院 T2D、3 中心、5 天；TIR 76.4% vs 73.6%，差 2.7 percentage points（−2.7 至 8.0），符合 −6 percentage points 非劣性界值。 | 建議由醫師每日晨會覆核確認；不是無人監督處方。排除嚴重心/肝/腎疾病、心理/精神疾病等，對本專案高度多重共病族群的可推廣性有限。**PMC HTML methods/results 核對**。 |
| **GPT-4 complex T2D 2025**；[PMID 41140742](https://pubmed.ncbi.nlm.nih.gov/41140742/)；[DOI](https://doi.org/10.2337/cd25-0015) | 243 份 clinical notes；專家評估使用抽出的 230 份、分成兩組 115 份執行不同任務。40% reasoning/explanations 被專家認為有幫助。 | 243 不是前瞻介入病人人數；專家認為有幫助不等同臨床改善。**PubMed 摘要＋原期刊索引到的 methods 段落；直接全文頁本次 403，未完整全文核讀**。 |

## 3. 心理與生理整合的實作重點

[EASD 2026 distress guideline](https://pubmed.ncbi.nlm.nih.gov/42744915/)（DOI [10.1007/s00125-026-06840-0](https://doi.org/10.1007/s00125-026-06840-0)）已於 2026-09-15 online publication，卷期為 2026 Dec；目前引用不屬於預先杜撰未發表指引。本次核對 PubMed 摘要。其建議包括情緒對話、validated tools、共同計畫、紀錄、持續監測與心理服務；治療介入的 GRADE recommendations 為 conditional，不能改寫為高確定性普遍療效。

以下為本專案設計推論：

- 把 distress、depression、anxiety 分開記錄；量表結果由病人回答，AI 不代答，不把分數當診斷。
- 每項器官異常都連到實際責任人與完成證據；眼底影像已完成不代表眼科追蹤已完成。
- 以同一團隊、人力及可取得服務為基礎比較有無 AI，避免把新增個管師的效益全部歸功軟體。
- 同時追蹤臨床與負擔：篩檢缺口完成、錯誤/漏項、轉介到診、distress、工時與低血糖。器官衰竭、視力、截肢、住院與死亡另需適當樣本及追蹤。

## 4. 給主綜述的具體修訂清單

| 位置 | 建議 | 判斷 |
| --- | --- | --- |
| `docs/12-deep-research-update.md` §6 ACCESS；整合單檔對應段落 | 補充隨機 81/83 與主要分析 81/82 的不同，保留 16/25 為 AI 異常 subgroup。 | 原 100% vs 22% 正確，但分母可更精確。 |
| 同節 iNCDSS | 加上「建議由醫師覆核確認」及排除嚴重器官、心理疾病。 | 對本專案整合共病適用性屬重要限制。 |
| 同節 GPT-4 | 明寫「243 份 notes；專家評估抽取 230 份分為兩個 115-note task sets」。 | 避免閱讀者以為 243 人接受前瞻介入。 |
| §3 CARRS 延伸研究 | 加入 854/1,146（74.5%）有 6.5 年評估資料。 | 補充延伸分析的追蹤完整度；非宣稱所有終點僅以 complete cases 分析。 |
| §5 INDEPENDENT | 保留 abstract 57.4% 與 Table 2/正文 54.7% 的不一致、以及 severe hypoglycemia 8 vs 0。 | 已有正確註記，不能在精簡摘要時刪掉。 |
| `sources/references_update_20261111.md` ADDITION 10年 | 補 DOI `10.1016/S2213-8587(19)30349-3`。 | 本次由 PubMed 與原期刊摘要核對。 |
| 全文 AI 成效敘述 | 用「本次選定證據不足以證明全人 AI 流程降低硬結局」，避免絕對宣稱全球不存在此研究。 | 定向查核不足以證明不存在。 |

## 5. 可重現的定向查詢與待補工作

查詢以研究名稱/PMID 配對為主：`Steno-2 12556541 27531506`、`TEAMcare 21190455`、`INDEPENDENT 32809002`、`ACCESS 38212308`、`31304320 autonomous artificial intelligence`、`38829880 CARRS`、`23735726 REDEEM`、`38039007 voice insulin`、`40332936 iNCDSS`、`41140742 GPT-4`、`31748169 ADDITION Europe`、`42744915 diabetes distress`。另用 `diabetes multimorbidity artificial intelligence randomized integrated care trial` 查近期線索；沒有把 protocol 或 registry 線索列為已證明療效。

後續優先取得 TEAMcare、REDEEM、voice AI、GPT-4 的全文及 supplements，逐一核對 missing data、分析群、介入元件、利益衝突與臨床安全處理。這些項目目前仍是待補，不會因文獻索引存在就標記完成。
