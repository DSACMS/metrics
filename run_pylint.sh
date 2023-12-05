#!/bin/bash
pylint --output-format=json --init-hook="import sys; sys.path.append('scripts/')" scripts/*
exit 0