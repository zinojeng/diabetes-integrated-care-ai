#!/bin/zsh
set -eu
cd "${0:A:h}"
python3 scripts/claude_workflow.py start all
exec claude agents --cwd "$PWD" --model claude-opus-5-5
