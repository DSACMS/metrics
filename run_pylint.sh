#!/bin/bash
pylint --init-hook="import sys; sys.path.append('scripts/')" scripts/*
exit 0