#!/usr/bin/env bash
set -e

DIRNAME=.venv
REQUIREMENTS=requirements.txt

if [[ ! -d "$DIRNAME" ]]; then
  python3 -m venv $DIRNAME --prompt Fastfeed
fi

if [[ ! -d $DIRNAME ]]; then
  echo "Failed to create virtual environment"
  exit 2
fi

source $DIRNAME/bin/activate
pip install --upgrade pip

if [[ -f "$REQUIREMENTS" ]]; then
  pip install -r "$REQUIREMENTS"
fi
