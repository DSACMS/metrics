import os
import pathlib
import json
from metricsLib.oss_metric_entities import GithubOrg, Repository
from metricsLib.constants import BASE_PATH, PATH_TO_METADATA, PATH_TO_METRICS_DATA
from fetch_public_metrics import fetch_all_new_metric_data, read_previous_metric_data
from gen_reports import generate_repo_report_files

def parse_repos_and_orgs_into_objects(org_name_list, repo_name_list):
    all_orgs = [GithubOrg(org) for org in org_name_list]

    all_repos = [Repository(repo_url) for repo_url in repo_name_list]

    return all_orgs, all_repos


os.umask(0)
# TODO: Create a read repos-to-include.txt
with open(os.path.join(PATH_TO_METADATA, "projects_tracked.json"), "r",encoding="utf-8") as file:
    tracking_file = json.load(file)

repo_urls = []  # Track specific repositories e.g. ['dsacms.github.io']

for _, repo_list in tracking_file["Open Source Projects"].items():
    repo_urls.extend(repo_list)

#Get two lists of objects that will hold all the new metrics
all_orgs, all_repos = parse_repos_and_orgs_into_objects(tracking_file["orgs"], repo_urls)

fetch_all_new_metric_data(all_orgs, all_repos)

#Update objects to also hold old metrics
read_previous_metric_data(all_repos, all_orgs)


#Save all metrics to files
generate_repo_report_files(all_repos)

for org in all_orgs:
    org_metric_data = json.dumps(org.metric_data,indent=4)

    with open(org.get_path_to_json_data(), "w+",encoding="utf-8") as file:
        file.write(org_metric_data)

for repo in all_repos:
    repo_metric_data = json.dumps(repo.metric_data, indent=4)

    with open(repo.get_path_to_json_data(), "w+",encoding="utf-8") as file:
        file.write(repo_metric_data)
