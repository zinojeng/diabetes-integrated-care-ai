#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
printf '%s\n' '正在檢查本台電腦的 Claude 登入、寫入及連線。'
if ! python3 scripts/project_doctor.py --probe-writes; then
  printf '%s\n' '檢查未通過，尚未啟動研究 sessions。' 'authentication FAIL：在此 Terminal 執行 claude auth login。' 'write FAIL / EPERM：確認這是 Mac mini 的一般 Terminal，勿從受限 agent 子程序重跑。' 'HTTPS FAIL：先確認本台電腦網路；Trust workspace 不會修復網路或外層檔案限制。'
  exit 2
fi
printf '%s\n' '以下進入 Claude 原生互動畫面。若出現 workspace trust 請自行確認。' '請確認收到 READY，然後輸入 /exit；接著會啟動四個獨立研究 sessions。'
claude --model claude-opus-5-5 --permission-mode manual 'Read-only readiness check. Reply only READY. Do not read or edit project files and do not start other agents.'
python3 scripts/claude_workflow.py start all
printf '%s\n' '已完成啟動嘗試；是否收到 Opus 回覆及跨 session ACK 仍需驗證。' '在另一個 Terminal 可執行：python3 scripts/verify_sessions.py'
exec claude agents --cwd "$PWD"
