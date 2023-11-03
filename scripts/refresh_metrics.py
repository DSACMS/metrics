import os
import pathlib
import json
from metricsLib.constants import BASE_PATH, PATH_TO_METADATA, PATH_TO_METRICS_DATA
from fetch_public_metrics import get_all_parsed_data
from clear_old_metrics import clear_all_data

os.umask(0)
# TODO: Create a read repos-to-include.txt
with open(os.path.join(PATH_TO_METADATA, "projects_tracked.json"), "r") as file:
    tracking_file = json.load(file)

repo_urls = []  # Track specific repositories e.g. ['dsacms.github.io']

for _, repo_list in tracking_file["Open Source Projects"].items():
    repo_urls.extend(repo_list)

#Get two lists of objects that hold all the metrics
all_orgs, all_repos = get_all_parsed_data(tracking_file["orgs"], repo_urls)

#Delete old data
clear_all_data()


#Save all metrics to files
for org in all_orgs:
    org_metric_data = json.dumps(org.metric_data,indent=4)

    parentPath = os.path.join(PATH_TO_METRICS_DATA, f"{org.login}")
    pathlib.Path(parentPath).mkdir(parents=True, exist_ok=True)
    orgPath = os.path.join(parentPath, f"{org.login}_data.json")

    with open(orgPath, "w+") as file:
        file.write(org_metric_data)

for repo in all_repos:
    repo_metric_data = json.dumps(repo.metric_data, indent=4)

    parentPath = os.path.join(PATH_TO_METRICS_DATA, f"{repo.repo_owner}/{repo.name}")
    pathlib.Path(parentPath).mkdir(parents=True, exist_ok=True)

    with open(os.path.join(PATH_TO_METRICS_DATA, f"{repo.repo_owner}/{repo.name}/{repo.name}_data.json"), "w+") as file:
        file.write(repo_metric_data)
