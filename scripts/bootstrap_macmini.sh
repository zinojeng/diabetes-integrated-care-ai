#!/bin/bash
# Run by the user in the existing ordinary Mac mini Terminal; no SSH or policy changes.
set -euo pipefail
DMIC_TARGET="${1:-/Users/ander/documents/medical/diabetes/integrated_care}"
DMIC_REPO='https://github.com/zinojeng/diabetes-integrated-care-ai.git'
command -v git >/dev/null
command -v python3 >/dev/null
if [ ! -d /Users/ander ] && [ "$DMIC_TARGET" = '/Users/ander/documents/medical/diabetes/integrated_care' ]; then
  printf '%s\n' '找不到 /Users/ander；請在已連線 Mac mini 的 Terminal 執行。未變更任何專案。'
  exit 2
fi
# A directory without its own .git may still belong to an ancestor repository.
DMIC_PROBE="$DMIC_TARGET"
while [ ! -d "$DMIC_PROBE" ]; do
  DMIC_PROBE="$(dirname "$DMIC_PROBE")"
done
DMIC_PARENT_REPO="$(git -C "$DMIC_PROBE" rev-parse --show-toplevel 2>/dev/null || true)"
DMIC_CANONICAL="$(python3 -c 'import pathlib,sys; print(pathlib.Path(sys.argv[1]).resolve())' "$DMIC_TARGET")"
if [ -n "$DMIC_PARENT_REPO" ] && [ "$DMIC_PARENT_REPO" != "$DMIC_CANONICAL" ]; then
  printf '%s\n' '目的地位於另一個 Git repository 內，已停止，未寫入任何專案。'
  exit 2
fi
sync_checkout() {
  local checkout="$1"
  local origin branch
  origin="$(git -C "$checkout" remote get-url origin)"
  case "$origin" in
    https://github.com/zinojeng/diabetes-integrated-care-ai|https://github.com/zinojeng/diabetes-integrated-care-ai.git|git@github.com:zinojeng/diabetes-integrated-care-ai.git) ;;
    *) printf '%s\n' '目的地屬於其他 repository，已停止。'; return 2 ;;
  esac
  branch="$(git -C "$checkout" branch --show-current)"
  if [ "$branch" != main ] || [ -n "$(git -C "$checkout" status --porcelain --untracked-files=no)" ]; then
    printf '%s\n' '既有 checkout 不在乾淨 main，保留目前工作並停止更新。'; return 2
  fi
  git -C "$checkout" pull --ff-only origin main
}
if [ -e "$DMIC_TARGET/.git" ]; then
  sync_checkout "$DMIC_TARGET"
elif [ -d "$DMIC_TARGET" ] && [ -n "$(ls -A "$DMIC_TARGET")" ]; then
  # Keep a non-git research folder intact as a working mirror; installer backs up differing files.
  DMIC_SOURCE="$DMIC_TARGET/.local/source-checkout"
  mkdir -p "$DMIC_TARGET/.local"
  if [ -e "$DMIC_SOURCE/.git" ]; then
    sync_checkout "$DMIC_SOURCE"
  elif [ -e "$DMIC_SOURCE" ]; then
    printf '%s\n' '來源暫存目錄已存在且非 repository，已停止，未覆寫。'; exit 2
  else
    git clone "$DMIC_REPO" "$DMIC_SOURCE"
  fi
  python3 "$DMIC_SOURCE/scripts/install_to_medical.py" --destination "$DMIC_TARGET"
else
  mkdir -p "$(dirname "$DMIC_TARGET")"
  git clone "$DMIC_REPO" "$DMIC_TARGET"
fi
cd "$DMIC_TARGET"
exec bash start_macmini.command
