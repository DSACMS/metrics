#!/bin/bash

organization="$1"
VERBOSE="${VERBOSE:-0}"

if [ -z "$organization" ]; then
  echo "Error: Organization name is required."
  echo "Usage: ./script.sh ORGANIZATION_NAME"
  exit 1
fi

repo_paths=$(jq -r '."Open Source Projects".'"$organization"'[]' _metadata/projects_tracked.json)

# set up directories
mkdir -p scc_repos/ scc_reports/
cd scc_repos/

for repo_path in $repo_paths; do
	[ "$VERBOSE" -eq 1 ] && echo "Processing repository: $repo_path"

	clone_url="${repo_path}.git"
	repo_name=$(basename $repo_path)

	[ "$VERBOSE" -eq 1 ] && echo "Cloning repository $repo_name from: $clone_url"

	git clone $clone_url > /dev/null 2>&1 || ([ "$VERBOSE" -eq 1 ] && echo "Repo $repo_name already exists")

	if [ -d $repo_name ]; then
		cd $repo_name

		# run scc
		scc --format json > ../../scc_reports/cmsgov_${repo_name}.json # JSON
		# scc > ../../scc_reports/cmsgov_${repo_name}.log # human-readable

		# combine scc results with repo metadata
		jq -s '.[0] + {cocomo: .[1]}' "../../../app/site/_data/$organization/$repo_name/${repo_name}_data.json" "../../scc_reports/cmsgov_${repo_name}.json" > "../../../app/site/_data/$organization/$repo_name/${repo_name}_scc.json"
  		mv "../../../app/site/_data/$organization/$repo_name/${repo_name}_scc.json" "../../../app/site/_data/$organization/$repo_name/${repo_name}_data.json"
		cd ..
	else
		echo "Error! Something went wrong while cloning repo $repo_name"
	fi

	[ "$VERBOSE" -eq 1 ] && echo "Done processing repository: $repo_path"
done

cd ..

# clean up
rm -rf scc_repos/ scc_reports/
