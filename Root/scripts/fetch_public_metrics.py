import datetime

import json
import os
import requests

from metricsLib.constants import *
from metricsLib.repos import Repository
import re

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


# Filter for DSACMS organization dataset
#original_organization_data = public_repo_data["data"]["organization"]["original"]["nodes"]
# print(original_organization_data)

# Store  the name of repo and the counts for desired Github metrics
all_repo_metrics_info = {}
# Holds an org name as key and all the metrics per repo in that org
DATA_JSON = {}

#  Capture the metric data  from all repos
#  Returns a nested dictionary
for repo in ALL_REPOS:
    #prepare all of the parameters needed for each metric.
    needed_params = {
        "repo" : repo.name,
        "owner" : repo.repo_owner,
        "repo_id" : repo.repo_id,
        "repo_group_id": repo.repo_group_id
    }

    print(needed_params)
    metrics_results = {}
    
    #Get info from all metrics for each repo
    for metric in SIMPLE_METRICS:

        params = {}
        #Get the parameter for this metric
        for param in metric.needed_parameters:
            params[param] = needed_params[param]
        
        metrics_results.update(metric.get_values(params))
    #repo_metric_info = output_repository_info(repo)

    repo.store_metrics(metrics_results)
    all_repo_metrics_info[repo.url] = repo

# print(all_repo_metrics_info)
for info, obj in all_repo_metrics_info.items():
    print(obj.commits_count)
print(type(all_repo_metrics_info))

#DATA_JSON["DSACMS"] = all_repo_metrics_info
#
## Update _metadata/projects_tracked.json
#"""
#    Updates the projects_tracked.json file to have all the Github metric data 
#    for the desired orgs and repos 
#"""
## TODO Apply all the orgs and there assigned repos in projects tracked
#PROJECTS_TRACKED['orgs'] = ["DSACMS"]
#PROJECTS_TRACKED['Open Source Projects'] = {"DSACMS": list(repos_tracked)}
#
##with open(os.path.join(BASE_PATH, PATH_TO_METADATA + "/" + "projects_tracked.json"), "w+") as f:
##    json.dump(PROJECTS_TRACKED, f)
#
#"""
#  Create a new json file Labeled METRICS-DATESTAMP.json
#  Will create a new folder for the given repo and org if 
#  it currently does not exist.
#"""
#list_of_org_projects = PROJECTS_TRACKED['Open Source Projects']["DSACMS"]
#given_org_data = DATA_JSON["DSACMS"]
#print("given_org_data", given_org_data)
#for repo in list_of_org_projects:
#    repo_metric_data = given_org_data.get(repo)
#    print("repo_metric_data", repo_metric_data, "\n")
#
#    # creates directory if it doesn't exist for a given repo
#    owner_dir_path = "{}/{}".format(PATH_TO_METRICS_DATA, "DSACMS")
#    repo_dir_path = "{}/{}".format(owner_dir_path, repo)
#    os.makedirs(repo_dir_path, exist_ok=True)
#
#    #   # Save the json file with a timestamp
#    file_name = "METRICS-" + DATESTAMP + ".json"
#    with open(repo_dir_path + "/" + file_name, "w+") as f:
#        json.dump(repo_metric_data, f)
#    print("LOG: Saving", file_name, "for", repo)
