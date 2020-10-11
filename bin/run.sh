#!/usr/bin/env bash

if [[ ! -f .venv/bin/activate ]]; then
  bin/init.sh
fi

source .venv/bin/activate
uvicorn main:app --reload
