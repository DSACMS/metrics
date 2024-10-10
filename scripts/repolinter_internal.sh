#!/bin/bash

#The facade directory should have the projects cloned
facade_directory="$1"
report_directory="$2"

VERBOSE="${VERBOSE:-0}"

if [ -z "$facade_directory" ]; then
	echo "Error: facade_directory name is required."
	echo "Usage: ./script.sh REPO_DIRECTORY OUTPUT_DIRECTORY"
	exit 1
fi

if [ -z "$report_directory" ]; then
	echo "Error: report_directory name is required."
	echo "Usage: ./script.sh REPO_DIRECTORY OUTPUT_DIRECTORY"
	exit 1
fi

if ! command -v repolinter 2>&1 >/dev/null
then
    echo "repolinter could not be found"
    exit 1
fi


if ! command -v linguist 2>&1 >/dev/null
then
    echo "github linguist could not be found"
fi

cd $facade_directory
#iterate through each project
for repo in */ ; do
	repo_no_slash=$(echo $repo | sed 's#/##')
	repolinter -f json $repo | jq '. += {"facade_dir": "'$repo'"}' > $report_directory/lint_$repo_no_slash.json
done