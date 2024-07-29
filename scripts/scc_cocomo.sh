#!/bin/bash

organization="$1"
VERBOSE="${VERBOSE:-0}"

if [ -z "$organization" ]; then
	echo "Error: Organization name is required."
	echo "Usage: ./script.sh ORGANIZATION_NAME"
	exit 1
fi

# set up working directory
cd scripts/

repo_paths=$(jq -r '."Open Source Projects"."'"$organization"'"[]' _metadata/projects_tracked.json)

# set up directories
mkdir -p scc_repos/ scc_reports/
cd scc_repos/

for repo_path in $repo_paths; do
	[ "$VERBOSE" -eq 1 ] && echo "Processing repository: $repo_path"

	clone_url="${repo_path}.git"
	repo_name=$(basename $repo_path)

	[ "$VERBOSE" -eq 1 ] && echo "Cloning repository $repo_name from: $clone_url"

	git clone $clone_url >/dev/null 2>&1 || ([ "$VERBOSE" -eq 1 ] && echo "Repo $repo_name already exists")

	if [ -d $repo_name ]; then
		cd $repo_name

		# run scc
		# The average wage flag uses the GS scale as referenced below. A low end and high end range is used to estimate the cost of the project.
		# The dryness score (and ULOC table) is also calculated and saved in a separate text file, which is then saved in the JSON as a string.
		# https://www.opm.gov/policy-data-oversight/pay-leave/salaries-wages/salary-tables/pdf/2024/GS.pdf
		scc --avg-wage 51332 --format json2 >../../scc_reports/cmsgov_${repo_name}_low.json   # JSON w/ low end range GS9 step 1 (2024)
		scc --avg-wage 159950 --format json2 >../../scc_reports/cmsgov_${repo_name}_high.json # JSON w/ high end range GS15 step 10 (2024)
		scc --dryness >../../scc_reports/cmsgov_${repo_name}.log                              # human-readable w/ dryness

		# combine the two JSON files into one with low and high wage range
		jq -s '
		{
			languageSummary: .[0].languageSummary,
			estimatedCost_low: .[0].estimatedCost,
			estimatedScheduleMonths_low: .[0].estimatedScheduleMonths,
			estimatedPeople_low: .[0].estimatedPeople,
			estimatedCost_high: .[1].estimatedCost,
			estimatedScheduleMonths_high: .[1].estimatedScheduleMonths,
			estimatedPeople_high: .[1].estimatedPeople
		}
		' ../../scc_reports/cmsgov_${repo_name}_low.json ../../scc_reports/cmsgov_${repo_name}_high.json >../../scc_reports/cmsgov_${repo_name}_combined.json

		# read the contents of log.log into a variable
		dryness_content=$(<../../scc_reports/cmsgov_${repo_name}.log)

		# escape the contents of log.log to make it JSON-safe
		dryness_content=$(jq -Rsa . <<<"$dryness_content")

		# combine the contents into combined_repo.json
		jq --argjson dryness_table "$dryness_content" '. + {dryness_table: $dryness_table}' ../../scc_reports/cmsgov_${repo_name}_combined.json >../../scc_reports/cmsgov_${repo_name}_full.json

		# combine scc results with repo metadata
		jq -s '.[0] + {cocomo: .[1]}' "../../../app/site/_data/$organization/$repo_name/${repo_name}_data.json" "../../scc_reports/cmsgov_${repo_name}_full.json" >"../../../app/site/_data/$organization/$repo_name/${repo_name}_scc.json"
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
