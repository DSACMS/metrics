#!/bin/bash

organization="$1"
VERBOSE="${VERBOSE:-0}"

if [ -z "$organization" ]; then
	echo "Error: Organization name is required."
	echo "Usage: ./script.sh ORGANIZATION_NAME"
	exit 1
fi

if [[ -z "$GITHUB_TOKEN" ]]; then
	echo "Error: GITHUB_TOKEN environment variable is required."
	exit 1
fi

# set up working directory
cd scripts/

repo_paths=$(jq -r '."Open Source Projects"."'"$organization"'"[]' _metadata/projects_tracked.json)

# set up directories
mkdir -p ossf_reports/

for repo_path in $repo_paths; do
	[ "$VERBOSE" -eq 1 ] && echo "Processing repository: $repo_path"

	repo_name=$(basename $repo_path)

	# run OSSF CLI
	docker run -e GITHUB_TOKEN gcr.io/openssf/scorecard:stable --repo=$repo_path --format=json >"ossf_reports/${repo_name}.json"

	# combine OSSF CLI results with repo metadata
	jq -s '.[0] + {ossf_scorecard: .[1]}' "../app/site/_data/$organization/$repo_name/${repo_name}_data.json" "ossf_reports/${repo_name}.json" >"../app/site/_data/$organization/$repo_name/${repo_name}_ossf.json"
	mv "../app/site/_data/$organization/$repo_name/${repo_name}_ossf.json" "../app/site/_data/$organization/$repo_name/${repo_name}_data.json"

	[ "$VERBOSE" -eq 1 ] && echo "Done processing repository: $repo_path"
done

# clean up
rm -rf ossf_reports/

# print success message
echo "All repositories processed successfully for organization: $organization"
