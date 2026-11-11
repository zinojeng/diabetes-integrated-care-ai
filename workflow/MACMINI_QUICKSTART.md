# Mac mini：啟動與查看研究 sessions

日期：2026-11-11。目標工作路徑 `/Users/ander/documents/medical/diabetes/integrated_care`。

本文件區分「已準備並測試的工具」與「Mac mini 上實際跑過的研究」。本輪未取得 Mac mini 的 session 清單或 Claude 回覆，不能宣稱背景協作已開始。

## 在已連線 Mac mini 的一般 Terminal 啟動

第一次同步並啟動：

```bash
curl -fsS https://raw.githubusercontent.com/zinojeng/diabetes-integrated-care-ai/main/scripts/bootstrap_macmini.sh -o /tmp/dmic-bootstrap.sh && bash /tmp/dmic-bootstrap.sh
```

這個腳本只操作本台主機，不建立 SSH、不改網路權限。若目標是乾淨的既有 Git main，就用 fast-forward 更新；若是已有檔案的非 Git 研究資料夾，會另存來源 checkout，透過原安裝器備份不同檔案後同步。既有 Git 有修改、分支不符或來源不符時停止，不 reset 或強制覆蓋。

啟動器先檢查 CLI、登入、實際 session/transcript 寫入與 HTTPS。通過後進入原生 Claude 畫面；有 trust 提示才處理。收到 READY 後輸入 `/exit`，啟動四個 sessions 並開啟 agent view。這只是連線檢查，不等於研究已完成。

後續在相同資料夾：

```bash
bash start_macmini.command
claude agents --cwd "$PWD"
```

四個 sessions 已存在時不重複建立。舊 session 已停止時，使用畫面列出的 ID attach 原 session，不因檔案存在就再開相同名字。

## 四個角色與實際對話

| Session | 主要工作 | 輸出 |
| --- | --- | --- |
| DMIC-complications | 整合困難、心腎肝眼足、器官結局 | sessions/complications/review.md |
| DMIC-psychosocial | Distress、depression/anxiety、治療與生活負擔 | sessions/psychosocial/review.md |
| DMIC-calculators | 公式、單位、族群、校準、量表 | sessions/calculators/review.md |
| DMIC-methods_ai | AI證據、研究方法、引用與全文查核 | sessions/methods_ai/review.md |

`claude agents --cwd "$PWD"` 列出獨立背景 sessions。選一列按 Enter 可看完整對話，空白輸入列按左鍵回列表；Space 可看摘要。內部 subagents 不會各自成為獨立列；進入父 session 後用 `/tasks` 查看。

```bash
python3 scripts/claude_workflow.py status
python3 scripts/verify_sessions.py
claude logs SESSION_ID
claude attach SESSION_ID
```

`SESSION_ID` 換成實際列出的 ID。verify 工具讀取已保存 assistant transcript，核對 `claude-opus-5-5` 與首份回覆；它不會把畫面上的模型名稱當作成功回覆。跨 session 的 SendMessage 需要對方 ACK；尚無 ACK 時保持 pending。

## Codex 主導的範圍

Codex 負責研究問題、來源核對、回覆爭點、更新整合稿與 GitHub。四個 Claude sessions 可利用原生 ListAgents/SendMessage 相互交換證據；必要時各用同模型 subagent 做個別查核。

**原生 cross-session messaging 連接的是 Claude sessions，並不會自動把這個 ChatGPT/Codex 對話接進去。** 本 repo 的 `feedback` 命令只產生給既有 session 的回饋內容與 attach 指令，尚不是自動傳訊服務。沒有成功送出與回覆收據時，不宣稱 Codex↔Claude 已全自動往返。可先讓本地 sessions 產生 review.md，再由可讀取該資料夾的 Codex 工作階段逐項核對；要長駐自動協調，需另驗證本機訊息介面與執行權限。

## 三種常見阻礙

| 訊息 | 意義 | 對應處理 |
| --- | --- | --- |
| `EPERM` at `.claude/session-env` | 程序不能寫入 Claude 狀態目錄；可能是外層 sandbox、OS 存取權或其他限制 | 用一般 Terminal 做實際寫入檢查；Trust 不會改外層權限。不可直接推論 Unix owner 壞掉，不建議盲目 chmod/chown |
| `Workspace not trusted` | Claude 尚未信任此工作目錄 | 同一目錄開互動式 Claude，處理原生提示；不修改 trust JSON、不用 print/skip-permissions 繞過 |
| `loggedIn: false`／API unreachable | 登入或網路問題 | 在該主機執行 `claude auth login`；先確認 HTTPS。其他主機登入不代表此主機登入 |

本輪實測：MacBook Air 的 Claude 2.1.321；`.claude/session-env` 出現 EPERM、auth status 為 false、agents list 為空。SSH 連 Mac mini 被目前工作階段回報 Operation not permitted。這些結果不能用來推論 Mac mini 的登入與檔案權限。

## MCP、全文與 LlamaParse

啟動器會選取本機已設定的 research_hub、paper-search、google-scholar、scihub、llamaparse。找不到就回報；不憑空建立未知工具端點。優先取得 PMC／publisher 可用全文，記錄 DOI、來源、取得時間與解析工作 ID；未取得全文保持待補。

在 Mac mini 隱藏輸入 LlamaParse key：

```bash
python3 scripts/configure_llamaparse_key.py
```

Key 只存本機 ignored `.local`、權限0600；以標準 `LLAMA_CLOUD_API_KEY` 傳給已設定的 parser，避免只傳未必受支援的 `_FILE` 變數。勿把 key 放到 prompt、命令歷史或 GitHub。配置存在不表示 key 有效，必須有成功 parse job 才能標記 PDF→Markdown 完成。原始全文與解析全文不提交此公開 repo。

## 官方參考

- [Agent view](https://code.claude.com/docs/en/agent-view)
- [Agents and parallel work](https://code.claude.com/docs/en/agents)
- [Cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging)
- [Agent teams](https://code.claude.com/docs/en/agent-teams)：適合由 Claude lead 管理共享任務；此專案採 Codex 分工的四個獨立 sessions，沒有另外啟用 team lead。
- [LlamaParse 官方設定](https://developers.llamaindex.ai/llamaparse/parse/getting_started/)
