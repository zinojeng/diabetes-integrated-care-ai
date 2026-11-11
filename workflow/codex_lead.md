# Codex 主導與 Claude 交叉審查

## 分工與交付

| 獨立 session | 工作 | 交叉查核重點 |
| --- | --- | --- |
| DMIC-complications | 困難點、整合照護、心腎肝眼足、RCT 與實施障礙 | methods_ai 核對硬終點與因果推論；calculators 核對分層用途 |
| DMIC-psychosocial | distress、depression、anxiety、治療負擔、collaborative care | calculators 核對量表版本；complications 核對心理與器官照護連結 |
| DMIC-calculators | 公式、單位、族群、時間窗、校準、授權 | methods_ai 獨立查係數；psychosocial 查心理分數解讀 |
| DMIC-methods_ai | AI 臨床證據、方法、引用與全文查核 | 對其他 sessions 提出最可能改變結論的問題 |

## 工作順序

1. Codex 提供問題與原始來源；先獨立搜尋、逐篇筆記，再做 evidence table。
2. Claude 記錄工具、檢索式、時間、實際輸出。無法執行就寫 blocked，不以擬定流程代替。
3. 每個 session 完成獨立判讀後以 ListAgents 發現 peers，SendMessage 最多兩輪。
4. 回覆原 message_id 的 ACK 才算收到；進一步同意需附來源定位與理由。
5. Claude 回覆 Codex：ACCEPT／REVISE／UNRESOLVED；Codex 查核影響公式、數字與主結論的項目。
6. Codex 維護 workflow/claim_review.csv；未決問題保留在報告，不把多模型一致視為真值。
7. 文獻與程式分支提交、PR、merge main 由 Codex 執行；Claude 不自行推送。

## 必核對的 claim

- JADE risk factor improvement 不等於臨床事件下降。
- Steno-2 及 CARRS 延伸追蹤的研究設計、持續介入情況。
- INDEPENDENT abstract 與 Table 2 對照比例不一致，保留差異。
- KFRE baseline survival 的 Original／2016 regional 版本及 UACR 單位。
- PAID 現行 0–4 計分與原始 1995 六點版本不可混稱。
- DCSI 七領域上限 13，neuropathy 最高 1。
- AI 診斷準確度、篩檢完成、HbA1c/TIR、長期器官結局分開報告。

## 狀態定義

prepared → launched → registered → independent_review → exchange_sent → exchange_acknowledged → codex_reviewed。
任何階段可 blocked。沒有後續證據不可跳級；缺少 review.md 不能稱審查完成。

目前準備四個 sessions 的啟動規格；實測背景啟動遇 Workspace not trusted，尚無 Claude review 或 ACK。
