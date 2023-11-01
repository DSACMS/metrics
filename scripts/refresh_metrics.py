import os
import json
from metricsLib.constants import BASE_PATH, PATH_TO_METADATA, PATH_TO_METRICS_DATA
from fetch_public_metrics import get_all_parsed_data

# TODO: Create a read repos-to-include.txt
with open(os.path.join(PATH_TO_METADATA, "projects_tracked.json"), "r") as file:
    tracking_file = json.load(file)

repo_urls = []  # Track specific repositories e.g. ['dsacms.github.io']

for _, repo_list in tracking_file["Open Source Projects"].items():
    repo_urls.extend(repo_list)

#Get two lists of objects that hold all the metrics
all_orgs, all_repos = get_all_parsed_data(tracking_file["orgs"], repo_urls)

print(all_orgs)
print(all_repos)