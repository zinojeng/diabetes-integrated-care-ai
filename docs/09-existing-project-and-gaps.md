# 既有 GitHub 專案的延伸方向

**你的 GitHub 已提供這個系統的決策支援核心。** 依 [README](https://github.com/zinojeng/AI-agent-in-diabetes/blob/6180c4f2a56ae50ca5b6ec22e4795f7922a63a3f/README.md) 與核心程式檢視，目前已有資料型別、併發症辨識、分期／計算模組、照護缺口、用藥建議、醫師決策與診前摘要；這些是程式層級的實作，不表示已完成院內系統串接或臨床驗證。

| 項目 | 目前可確認的狀態 | 後續需要補上的工作 |
| --- | --- | --- |
| 資料整合 | 函式將傳入的病人、檢驗與檢查資料整理成共同物件。 | 真實 HIS／LIS／眼科等介接、單位與代碼對應、有效用藥及外院資料核對。[程式](https://github.com/zinojeng/AI-agent-in-diabetes/blob/6180c4f2a56ae50ca5b6ec22e4795f7922a63a3f/src/dm_care_pipeline/data_integration.py) |
| 確定性工具 | 已有 CKD G／A、FIB-4、BNP、ABI／TBI、低血糖與足部規則。 | 逐項核對指引及適用條件，建立臨床參考案例；Tier A 是專案內部分類，並非證據等級或認證。 |
| Tier B 預測模型 | WATCH-DM、PREVENT、KFRE、Karter 等目前是介面，回傳需要外部驗證模型，數值為空。 | 接入正確公式／係數及版本，再做程式比對與在地效能驗證。[共用骨架](https://github.com/zinojeng/AI-agent-in-diabetes/blob/6180c4f2a56ae50ca5b6ec22e4795f7922a63a3f/src/dm_care_pipeline/calculators/tier_b/_base.py) |
| FIB-4 分流 | 目前使用 1.3，對年齡 <35 或 >65 加警語。 | 將採用指引的高齡門檻、>2.67 分支與檢驗情境納入版本化規則。[程式](https://github.com/zinojeng/AI-agent-in-diabetes/blob/6180c4f2a56ae50ca5b6ec22e4795f7922a63a3f/src/dm_care_pipeline/calculators/fib4.py) |
| 整體風險 | `RuleBasedRiskCalculator` 明確標為示意方法。 | 不將其輸出當成經驗證的臨床風險；正式流程應替換或停用該結果。[程式](https://github.com/zinojeng/AI-agent-in-diabetes/blob/6180c4f2a56ae50ca5b6ec22e4795f7922a63a3f/src/dm_care_pipeline/risk.py) |
| 診前報告 | 已有摘要組裝與證據索引。 | 補病歷文字擷取、症狀與心理量表、實際介面及可用性驗證。[程式](https://github.com/zinojeng/AI-agent-in-diabetes/blob/6180c4f2a56ae50ca5b6ec22e4795f7922a63a3f/src/dm_care_pipeline/pre_visit_brief.py) |
| Agent 與族群管理 | README 明載尚無 LLM／多 agent 編排與跨病人批次管理。 | 在既有引擎外加受控呼叫層；族群排序另做驗證。 |

第一版適合先交付「病歷摘要＋篩檢完整度＋需醫師覆核的異常」。在用藥模組中，「沒有開某藥」應先顯示為待評估項目，並核對適應症、禁忌、血鉀與腎功能、過敏、耐受性、費用及病人偏好，再由醫師決定是否構成可改善的治療缺口。

用藥檢核可涵蓋合適 ASCVD／CKD／HF 情境下具有證據的 SGLT2 inhibitor、GLP-1 RA，以及適用時的 ACE inhibitor／ARB、finerenone 與降血脂治療；不同藥物的適用條件分開判斷。系統應產生附理由的評估提示，由醫師核對個人狀況後決定。[ADA 心血管](https://doi.org/10.2337/dc26-S010)、[ADA 腎臟](https://doi.org/10.2337/dc26-S011)

