# 糖尿病全人評估與 AI 跨專業整合照護

AI-assisted whole-person assessment and interdisciplinary diabetes care.

本 repo 整理糖尿病門診的多重複雜度、併發症篩檢與後續治療、台灣共同照護模式，以及 AI／LLM 支援跨專業團隊的研究與系統設計。

糖尿病門診的核心挑戰，是在有限時間內，同時理解病人的血糖、器官疾病、心理狀態、知識與自我照護能力、飲食和生活限制，再把判斷轉成病人做得到、團隊接得住、後續能追蹤的照護計畫。AI 最有價值的用途，是協助跨專業團隊整理資料、辨識需要處理的問題與維持追蹤，讓醫師有更多時間核實風險、理解病人的選擇並共同決策。

這套構想可定位為「AI 輔助糖尿病全人評估與跨專業整合照護」，英文可用 AI-assisted whole-person assessment and interdisciplinary diabetes care。以下以成人第 2 型糖尿病門診為主；第 1 型糖尿病、孕期與兒少需採各自適用的照護路徑。臨床架構參照 ADA 2026 等指引；台灣制度採健保署公開之 2026 年 4 月 1 日生效版本，研究與政策資料查核至 2026 年 11 月 11 日。既有 GitHub 程式評述保留原查核 commit 的範圍。

## 專案狀態

目前內容為文獻整理、臨床工作流程及研究規劃，尚未提供可執行的臨床系統。示例為虛構情境；未納入真實病歷。文中區分隨機試驗、觀察研究、開發評估與院方導入公告。

既有程式專案為 [AI-agent-in-diabetes](https://github.com/zinojeng/AI-agent-in-diabetes)。本 repo 作為臨床需求與證據文件，程式評述僅對應原稿已查核的 commit，詳見[既有專案與待補工作](docs/09-existing-project-and-gaps.md)。

## 下載研究整理

- [完整文獻整合 Markdown](research/DM_AI_Integrated_Literature_Review_20261111.md)：原有11章加上2份深入補充、40筆新增研究/工具紀錄的單檔閱讀版（與原52來源有重疊）。
- [研究資料 ZIP](downloads/DM_AI_Whole_Person_Research_20261111.zip)：完整原稿、分章文件及來源清單；不含期刊全文 PDF。
- [CSV 文獻清單](sources/references.csv)：可用 Excel 或 Numbers 開啟。

## 閱讀導覽

| 文件 | 內容 |
| --- | --- |
| [糖尿病門診的多重複雜度](docs/01-clinic-complexity.md) | 血糖、器官疾病、心理、知識、飲食、社會與行政工作的整合困難。 |
| [台灣現有的跨專業糖尿病照護](docs/02-taiwan-care-model.md) | 共同照護網、糖尿病與 Early CKD 方案，以及團隊角色與追蹤責任。 |
| [整合生理心理與自我照護的臨床研究](docs/03-integrated-care-evidence.md) | TEAMcare、INDEPENDENT、CARRS、JADE、JADE DKD 與台灣 P4P。 |
| [併發症與共病的篩檢](docs/04-complication-screening.md) | 腎臟、眼底、心衰竭、ABI／PAD、足部、神經與心理評估。 |
| [篩檢異常後的治療與轉介](docs/05-treatment-and-referral.md) | 篩檢後的診斷確認、器官保護治療、眼科處置及跨科轉介。 |
| [AI 如何支援跨專業照護流程](docs/06-ai-workflow-architecture.md) | 資料來源、確定性計算、LLM／RAG、共同決策與任務追蹤。 |
| [AI 臨床研究的證據範圍](docs/07-ai-clinical-evidence.md) | 傳統 CDS、LLM 原型、文書助手及臨床試驗的能力與證據界線。 |
| [台灣已有的 AI 與 LLM 應用](docs/08-taiwan-ai-applications.md) | 健保署試辦、奇美、北醫、國衛院與三總的公開案例。 |
| [既有 GitHub 專案的延伸方向](docs/09-existing-project-and-gaps.md) | 既有程式狀態、尚待驗證模型與後續開發項目。 |
| [一頁式診前摘要範例](docs/10-previsit-brief-example.md) | 涵蓋病人目標、疾病與生活困難的虛構門診摘要。 |
| [導入與研究評估](docs/11-implementation-and-evaluation.md) | 離線驗證、靜默測試、受控試辦與團隊／病人負擔指標。 |

## 原稿與來源

- [完整原稿快照](archive/2026-11-11-complete-review.md)：保留原有 78 個內容區塊的順序與文字。
- [文獻與官方來源索引](sources/references.md)：52 個不重複來源網址。
- [來源索引 JSON](sources/references.json)：方便後續檢索與資料整理。
- [來源與版本紀錄](sources/provenance.json)：包含原稿修訂序號、政策版本與程式查核 commit。
- [原始整合頁面](https://chatgpt.com/space/page_24179a2ed7988191b90ecf673bdf4ac8)：存取權依原頁面設定。

## 後續擴充

先以病歷摘要、篩檢完整度與需醫師覆核的異常為第一版範圍，再依驗證結果加入計算工具、治療檢核與團隊追蹤。細節見[導入與研究評估](docs/11-implementation-and-evaluation.md)。

新增章節：[深入研究與整合架構](docs/12-deep-research-update.md)、[Calculator公式與心理量表](docs/13-calculator-specifications.md)。

新增索引：[40筆evidence matrix](sources/evidence_matrix_20261111.csv)、[引用來源](sources/references_update_20261111.md)、[檢索規格](research/SEARCH_PROTOCOL_20261111.md)。既有downloads ZIP是先前固定版本，尚未包含本輪補充；請以main上的Markdown為準。

後續修訂以 `docs/` 為主；`archive/` 保存此版原稿，不隨章節修改而覆寫。新增醫療、政策或軟體敘述時，請記錄來源、適用條件與查核日期。

## 使用範圍

治療與轉介內容用於專業討論及系統設計，臨床處置仍由醫療團隊核實個別病況後決定。指引適應性、台灣核准及健保給付需分別確認。

尚未指定開源授權；引用文獻與第三方軟體依各自權利及授權條款處理。

## Codex主導、Claude Opus5.5跨session協作

最新模型要求：`claude-opus-5-5`。四個獨立sessions分別研究complications、psychosocial、calculators、methods_ai；各自只寫指定輸出目錄，內部可按需使用相同模型subagent。這是上下文及輸出分工，不是OS隔離。普通subagents在父session中查看。

**目前實測未啟動成功**：本輪受管理sandbox限制Claude狀態目錄寫入，且Anthropic等主機DNS失敗。原生trust選擇未能持久保存，尚無registered DMIC sessions、Claude第一份回覆或peer ACK。完整[實測紀錄](workflow/EXECUTION_STATUS_20261111.md)。

在一般Mac Terminal、此repo根目錄執行：

```bash
claude --model claude-opus-5-5
```

完成原生trust、確認實際收到回覆後，輸入`/exit`，再執行：

```bash
python3 scripts/claude_workflow.py start all
claude agents --cwd "$PWD"
```

讀取實際assistant transcript中的模型、session ID與第一份回覆：

```bash
python3 scripts/verify_sessions.py
```

設定模型、看見session登錄或檔案存在，都不等於拿到Opus5.5回覆或完成交叉審查。

同步到指定medical資料夾的工具已備妥，請在一般Mac Terminal執行：

```bash
python3 scripts/install_to_medical.py --copy-local-key
cd /Users/ander/documents/medical/diabetes/integrated_care
claude --model claude-opus-5-5
```

安裝器先備份不同的既有檔，不覆寫Git紀錄；credential只在本機ignored .local保存，從GitHub clone不會取得key。正式研究輸出與來源文件可公開；原始PDF、解析全文、對話runtime及真實病歷不提交。
