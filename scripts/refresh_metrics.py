import os
import pathlib
import json
from metricsLib.constants import BASE_PATH, PATH_TO_METADATA, PATH_TO_METRICS_DATA
from fetch_public_metrics import fetch_all_new_metric_data, read_previous_metric_data
from gen_reports import generate_repo_report_files
from gen_graphs import generate_repo_solid_guage_issue_graph, generate_repo_sparklines

os.umask(0)
# TODO: Create a read repos-to-include.txt
with open(os.path.join(PATH_TO_METADATA, "projects_tracked.json"), "r") as file:
    tracking_file = json.load(file)

repo_urls = []  # Track specific repositories e.g. ['dsacms.github.io']

for _, repo_list in tracking_file["Open Source Projects"].items():
    repo_urls.extend(repo_list)

#Get two lists of objects that hold all the new metrics
all_orgs, all_repos = fetch_all_new_metric_data(tracking_file["orgs"], repo_urls)

#Update objects to also hold old metrics
read_previous_metric_data(all_repos, all_orgs)


#Save all metrics to files
generate_repo_report_files(all_repos)
generate_repo_solid_guage_issue_graph(all_repos)
generate_repo_sparklines(all_repos)

for org in all_orgs:
    org_metric_data = json.dumps(org.metric_data,indent=4)

    with open(org.get_path_to_json_data(), "w+") as file:
        file.write(org_metric_data)

for repo in all_repos:
    repo_metric_data = json.dumps(repo.metric_data, indent=4)

    with open(repo.get_path_to_json_data(), "w+") as file:
        file.write(repo_metric_data)
