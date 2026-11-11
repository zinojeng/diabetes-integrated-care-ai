# 修訂紀錄

## 2026-11-11 — Mac mini啟動檢查與第二輪證據查核

- 新增主機/登入/實際寫入/HTTPS檢查及Mac mini同步啟動入口，遇到EPERM即回報，不改trust或權限。
- 補充ACCESS分母、iNCDSS醫師覆核與共病排除、CARRS追蹤完整度、PREVENT官方更新、WHO-5及DDS計分界線。
- 新增CIC-PDD利用/成本摘要證據，evidence matrix現有41筆；同步整合主文、來源及provenance。
- LlamaParse本機key改以標準環境變數傳入，生成設定先限制0600；未宣稱完成parse。
- 明列Codex與Claude原生session messaging的界線，保留未完成的Mac mini實測與Claude ACK。

## 2026-11-11 — 深入研究、公式查核與Opus5.5工作流程

- 保留原稿與archive，新增整合照護/心理/AI證據、陰性試驗及40筆evidence matrix。
- 加入CKD-EPI、KFRE三種校準、FIB-4、DCSI、心理量表規格與適用限制；未將spec-only模型偽裝為已實作calculator。
- 加入四個獨立Claude sessions、限定輸出與peer ACK規格、實際模型/第一回覆驗證器；測試重複啟動、失敗及未驗證登錄。
- 記錄實測EPERM/DNS/trust持久化失敗；尚無Claude回覆、背景協作或LlamaParse成功解析。
- 使用者明確選擇維持Public；credential與原始全文排除提交。

## 2026-11-11 — GitHub 文件與下載包

- 加入單檔 Markdown 文獻整合稿、研究 ZIP 與 CSV 來源清單。
- README 新增下載與閱讀入口；原始研究內容及其證據限制保留。

## 2026-11-11 — 初始文件整理

- 自最新整合頁面第 2 版匯出完整原稿，保留 78 個區塊。
- 依原有章節拆成 11 份可維護的 Markdown 文件。
- 加入 README、52 個來源網址索引與版本紀錄。
- 區分文件設計、既有程式實作與臨床驗證狀態。
- 本次僅整理既有研究內容，未重新執行全面文獻搜尋或臨床驗證。

