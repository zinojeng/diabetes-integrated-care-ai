# 糖尿病整合照護研究：Codex 主導

研究英文文獻，主要用 zh-TW 撰寫；medical terms 與 drugs names 用 English。
目前指定 Claude Opus 5.5：`claude-opus-5-5`。所有 sessions/subagents 相同模型，失效時停止並回報，不自動改模型。

Codex 決定研究問題、彙整、逐項答覆及最後確認；Claude 做獨立研究、交叉質疑與回答。
先讀 README.md、AGENTS.md、workflow/codex_lead.md、research/SEARCH_PROTOCOL_20261111.md。
研究內容不是已部署的臨床診療系統；不要把設計或專家評分寫成病人結局已改善。
不得從病歷空白推斷陰性、從風險分數推斷確診，也不能合成未驗證的全人風險總分。
每個 session 只寫自己的 sessions/<role>/、literature/notes/<role>/；跨目錄需要交由 Codex。
完整文獻、解析輸出、credentials 與真實病歷不能提交公開 repo。

`claude agents --cwd "$PWD"` 顯示獨立背景 sessions；subagents 在所屬 session 內查看。
Workspace trust 必須在 Claude 原生互動提示中處理；不得用配置、print mode 或 skip-permissions 繞過。
