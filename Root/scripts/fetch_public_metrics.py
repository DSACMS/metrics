import datetime

import json
import os
import requests

#  Constructs our POST Request
token = os.getenv("GITHUB_TOKEN")
headers = {"Authorization": f"bearer {token}"}
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_PATH, "graphql_queries.graphql"), "r") as file:
    query = file.read()
url = "https://api.github.com/graphql"
response = requests.post(url, headers=headers, json={"query": query})
public_repo_data = json.loads(response.text)

# Folder Names to send over our projects tracked data
PATH_TO_METRICS_DATA = "_data"
PATH_TO_METADATA = "_metadata"
DATESTAMP = datetime.datetime.now().date().isoformat()


# TODO: Create a read repos-to-include.txt
all_orgs = []  # Track orgs and all its repos e.g. DSACMS
all_repos = []  # Track specific repositories e.g. ['dsacms.github.io']

# PROJECTS_TRACKED makes a json file that stores the list of orgs and their
# repos that we will be collecting metrics for
PROJECTS_TRACKED = {}
orgs_tracked = set()

# Tracks of all the public repositories within our DSACMS organization
repos_tracked = set()

"""
Purpose: repo_data_to_json will convert data from string to json format such that we can 
access the counts for the desired metrics in a repo
Input: Requires a repository name defined from graphql_queries
Returns: json dict of repo data
"""
repos = {}


def repo_data_to_json(repositories):
    for repo in repositories:
        repo_json = json.loads(repo)
        repos[repo] = repo_json


"""
Purpose: Simplifies the format of the  json file to include only the desired metrics
Input: Requires a repository name defined from graphql_queries that is in json format
Returns a dictionary that contains the total counts for commit, 
issue, open issues,closed issues, pull requests, open pull  requests, 
merged pull requests, closed pull requests, forks, stargazers & watchers
"""


def output_repository_info(repositories):
    commits_count = repo["defaultBranchRef"]["commits"]["history"]["totalCount"]
    issues_count = repo["issues"]["totalCount"]
    open_issues_count = repo["openIssues"]["totalCount"]
    closed_issues_count = repo["closedIssues"]["totalCount"]
    pull_requests_count = repo["pullRequests"]["totalCount"]
    open_pull_requests_count = repo["openPullRequests"]["totalCount"]
    merged_pull_requests_count = repo["mergedPullRequests"]["totalCount"]
    closed_pull_requests_count = repo["closedPullRequests"]["totalCount"]
    forks_count = repo["forkCount"]
    stargazers_count = repo.get("startgazers", {}).get("totalCount")
    watchers_count = repo["watchers"]["totalCount"]
    return {"datetime": DATESTAMP,
            "commits_count": commits_count,
            "issues_count": issues_count,
            "open_issues_count": open_issues_count,
            "closed_issues_count": closed_issues_count,
            "pull_requests_count": pull_requests_count,
            "open_pull_requests_count": open_pull_requests_count,
            "merged_pull_requests_count": merged_pull_requests_count,
            "closed_pull_requests_count": closed_pull_requests_count,
            "forks_count": forks_count, "stargazers_count": stargazers_count,
            "watchers_count": watchers_count
            }


# Filter for DSACMS organization dataset
original_organization_data = public_repo_data["data"]["organization"]["original"]["nodes"]
# print(original_organization_data)

# Store  the name of repo and the counts for desired Github metrics
all_repo_metrics_info = {}
# Holds an org name as key and all the metrics per repo in that org
DATA_JSON = {}

#  Capture the metric data  from DSACMS
#  Returns a nested dictionary
for repo in original_organization_data:
    name = repo["name"]
    repos_tracked.add(name)
    repo_metric_info = output_repository_info(repo)
    all_repo_metrics_info[name] = repo_metric_info

# print(all_repo_metrics_info)
print(original_organization_data)
print(type(all_repo_metrics_info))
DATA_JSON["DSACMS"] = all_repo_metrics_info

# Update _metadata/projects_tracked.json
"""
    Updates the projects_tracked.json file to have all the Github metric data 
    for the desired orgs and repos 
"""
# TODO Apply all the orgs and there assigned repos in projects tracked
PROJECTS_TRACKED['orgs'] = ["DSACMS"]
PROJECTS_TRACKED['Open Source Projects'] = {"DSACMS": list(repos_tracked)}

with open(os.path.join(BASE_PATH, PATH_TO_METADATA + "/" + "projects_tracked.json"), "w+") as f:
    json.dump(PROJECTS_TRACKED, f)

"""
  Create a new json file Labeled METRICS-DATESTAMP.json
  Will create a new folder for the given repo and org if 
  it currently does not exist.
"""
list_of_org_projects = PROJECTS_TRACKED['Open Source Projects']["DSACMS"]
given_org_data = DATA_JSON["DSACMS"]
print("given_org_data", given_org_data)
for repo in list_of_org_projects:
    repo_metric_data = given_org_data.get(repo)
    print("repo_metric_data", repo_metric_data, "\n")

    # creates directory if it doesn't exist for a given repo
    owner_dir_path = "{}/{}".format(PATH_TO_METRICS_DATA, "DSACMS")
    repo_dir_path = "{}/{}".format(owner_dir_path, repo)
    os.makedirs(repo_dir_path, exist_ok=True)

    #   # Save the json file with a timestamp
    file_name = "METRICS-" + DATESTAMP + ".json"
    with open(repo_dir_path + "/" + file_name, "w+") as f:
        json.dump(repo_metric_data, f)
    print("LOG: Saving", file_name, "for", repo)
