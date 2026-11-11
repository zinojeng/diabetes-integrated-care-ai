# Cross-session 研究協議 v2（2026-11-11，實際執行版）

本協議取代 `workflow/codex_lead.md` 中「尚未取得執行」的狀態：這一版在有網路與 MCP 的 Claude Code Desktop 環境實跑。
語言：zh-TW 為主；疾病、藥名、量表、指標、期刊名用 English。事實性內容必須能回溯到本地全文或 PubMed/Crossref metadata。

## 使用者原始研究問題（所有 sessions 共同上位目標）

1. 目前糖尿病照護**困難點**在哪裡？
2. 整合照護**需要整合哪些東西**？
3. **如何更完整評估糖尿病共病**？
4. **如何用 AI** 做糖尿病照護的整合？
5. 特別聚焦**併發症整合照護**；不只生理，也含**心理層面**。
6. 蒐集**calculator 公式**：量化共病負擔、相關疾病風險、心理指標，並用於預測後續風險。

## 四個獨立 sessions 與所有權

| Session | 主問題 | 可寫入（僅此） |
| --- | --- | --- |
| complications | 困難點、整合需求、併發症／共病評估、整合照護 RCT 與落差 | `sessions/complications/`、`literature/notes/complications/` |
| psychosocial | distress／depression／anxiety／低血糖恐懼／治療負擔／SDOH 與 collaborative care | `sessions/psychosocial/`、`literature/notes/psychosocial/` |
| calculators | 共病負擔、事件風險、心理量表的**精確公式、單位、適用族群、測試向量與 Python 實作** | `sessions/calculators/`、`literature/notes/calculators/`、`calculators/`、`tests/calculators/` |
| methods_ai | AI／CDS／LLM／agent 的臨床證據、方法學偏誤、與整合照護架構 | `sessions/methods_ai/`、`literature/notes/methods_ai/` |

跨目錄的修改一律寫在你的 `handoff.md`，由 lead 整合。**不要 git commit／push／切 branch**（lead 負責 PR 與 merge main）。

## 全文管線（本機實測可用，請照做）

1. 搜尋：`mcp__paper-search__search_pubmed`（`max_results` ≤ 8；回傳可能很大，結果若存檔請用 `jq` 取 `paper_id,doi,title,published_date`，**不要整份讀進 context**）。補網用 `search_europepmc`／`search_crossref`／`search_semantic`；臨床問答可用 `mcp__openevidence__oe_ask`。
2. 全文優先順序（寧可誠實標 abstract-only，也不能偽造全文）：
   - **PMC 開放全文**：`python3 scripts/fulltext_tools.py pmc <PMID|PMCID> --role <role>` → `literature/parsed/<role>/PMCxxxx.md`（使用 NCBI E-utilities 官方 API；`ABSTRACT_ONLY` 表示該文不在 PMC 開放子集）。
   - **PDF**：`mcp__paper-search__download_with_fallback`（`use_scihub=false` 先試，存到 `literature/fulltext/<role>/`）→ 解析：`~/llamaparse-mcp/.venv/bin/python scripts/fulltext_tools.py llamaparse <pdf> --role <role>`（不會把全文倒回 context，只印 receipt）。
   - Sci-Hub（`mcp__scihub__download_pdf`）僅作 2021 年以前論文的最後備援；新論文通常不在庫內。
   - **不得偽裝瀏覽器 User-Agent、繞過 bot 檢查或 CAPTCHA**；PMC／Europe PMC 直連 PDF 回 403 就改走上述 API 或標記 `no_fulltext`。
3. 每份本地全文用 `fulltext_tools.py verify <md> --title ... --author ... --year ...` 檢查（防 Polluted PDF）；`POLLUTED_OR_MISMATCH` 者刪除並記錄。
4. 所有引用的數字、樣本數、HR/OR、公式係數都要能用 `fulltext_tools.py grep <role> <pattern>` 在本地全文找到；找不到就標 `unverified`，不得寫成事實。
5. `literature/fulltext/`、`literature/parsed/` 為 git-ignored（版權）；`literature/receipts/<role>.jsonl` 會提交。
6. API key 只透過環境變數或 `~/.config/llamaparse/api_key` 讀取，**不得**寫進任何檔案、輸出或 commit。

## 可用的 subagents（`~/.claude/agents/`，在你的 session 內用 Agent 工具啟動）

`literature-scout`（找候選＋驗 PMID/DOI）→ `fulltext-fetcher`（取全文，需遵守上方不繞過規則）→ `deep-dive-scout`（第二輪：從本地 References 找共引 seminal papers）→ `drafter`（只引用本地 MD）→ `counter-advocate`（找反證）→ `citation-verifier`／`claim-auditor`／`cross-referencer`（並行稽核）→ `arbitrator`。
自己決定要用哪幾個；小題目不需要全部。每個 subagent 都要求回報實際工具輸出與失敗，不接受「應該可行」。

## 交付物（每個 session）

- `sessions/<role>/report.md`：zh-TW 報告。每個論斷附 `[PMID/DOI]` 與證據標記：📄 = 本地全文已 grep 驗證；📌 = 僅 abstract／metadata（不得做具體數字斷言）。
- `sessions/<role>/evidence_table.csv`：欄位 `id,pmid,doi,first_author,year,journal,design,population,n,intervention_or_exposure,comparator,outcome,effect_with_CI,limitations,access_level,local_file,claim_verified`。
- `sessions/<role>/search_log.md`：每次檢索式、來源、日期、命中數、納入／排除原因與失敗工具輸出（blocked 就寫 blocked）。
- `sessions/<role>/handoff.md`：需要 lead 修改的跨目錄項目；給其他 sessions 的問題（各至少 1 個，具體到「請核對 X 的數字 Y」）。
- 不確定就寫 `UNRESOLVED`，不要用推論補洞；不要合成「全人風險總分」；不要把風險分數當診斷；病歷空白≠陰性。

## 第二階段（lead 之後會用 SendMessage 觸發）

讀其他三個 sessions 的 `report.md` 與 `handoff.md`，針對指派給你的問題寫 `sessions/<role>/crosscheck.md`，每項標 `ACCEPT / REVISE / UNRESOLVED` 並附來源定位。
