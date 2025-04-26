#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_BIN="${PYTHON:-python3}"
VENV_DIR="$PROJECT_ROOT/.venv"

if [[ ! -d "$VENV_DIR" ]]; then
  echo "Cоздаю virtualenv"
  "$PYTHON_BIN" -m venv "$VENV_DIR"
fi
source "$VENV_DIR/bin/activate"

echo "Обновляю pip и ставлю зависимости"
python -m pip install --upgrade pip >/dev/null
python -m pip install -r "$PROJECT_ROOT/requirements.txt"


export PYTHONPATH="${PROJECT_ROOT}${PYTHONPATH:+:$PYTHONPATH}"
cd "$PROJECT_ROOT"
echo "Запускаю pytest"
pytest -q
