#!/bin/bash
#pylint --output-format=json --init-hook="import sys; sys.path.append('scripts/')" scripts/*
python scripts/run_pylint.py
exit 0