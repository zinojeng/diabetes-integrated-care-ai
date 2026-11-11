# 修訂紀錄

## 2026-11-11 — 全文驗證、交叉查核與可測試 calculators

- 實際執行四個獨立 sessions（complications、psychosocial、calculators、methods_ai），證據表共 166 筆，約 130 筆有本地全文並以 grep 核對數字；全文與解析檔因版權不提交，只提交 `literature/receipts/`。
- 新增 [整合報告](docs/14-integrated-synthesis.md)，並完成第二階段交叉查核（各 session 的 `crosscheck.md`）。
- 新增 `calculators/dmic_calculators` 與 102 個測試：CKD-EPI 2021、KDIGO、KFRE（Original 與非北美 5 年）、IWGDF、SCORE2-Diabetes（重現官方 Excel）、RECODe、TIMI TRS 2°P 與多個心理與功能量表；取不到係數的工具只保留規格。
- 修正 `scripts/fulltext_tools.py` 的 PMID 對應缺陷（原本可能取到引用該文的文章）。
- 補入 `docs/03` 的陰性與中性試驗、TEAMcare 與 INDEPENDENT 的成分拆解；修正 `docs/08` 的 PMC 連結；`workflow/claim_review.csv` 更新查核狀態。
- 未解決項目：Steno-2 兩篇全文、ADA 2026 第 4 章、JAMA 2016 KFRE 補充附錄、DCSI 計分表、PREVENT 係數、三項台灣公告日期。

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

