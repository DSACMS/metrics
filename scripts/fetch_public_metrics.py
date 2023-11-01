import datetime

import json
import os
import requests

from metricsLib.constants import *
from metricsLib.repos import Repository
from metricsLib.orgs import GithubOrg
import re

"""This method serves to iterate through previously collected metric
data that is associated with a repo and derive the cumulative metric data
for the whole organization instead of the repository. 

This is mainly to avoid using more api calls than we have to.

Arguments:
    repo_list: List of all repos with metrics
    org: The github org to add metrics to
"""
def add_info_to_org_from_list_of_repos(repo_list, org):
     
    #Define counts to update based on tracked repositories. 
    org_counts = {"commits_count": 0,
                 "issues_count": 0,
                 "open_issues_count": 0,
                 "closed_issues_count": 0,
                 "pull_requests_count": 0,
                 "open_pull_requests_count": 0,
                 "merged_pull_requests_count": 0,
                 "closed_pull_requests_count": 0,
                 "forks_count": 0,
                 "stargazers_count": 0,
                 "watchers_count": 0
                 }

    #Add repo data to org that repo is a part of
    for repo in repo_list:
        #Check for membership
        if repo.needed_parameters["repo_group_id"] == org.needed_params["repo_group_id"]:
            #Add metric data.
            for key in org_counts.keys():
                raw_count = repo.metric_data.get(key)
                if raw_count:
                    org_counts[key] += raw_count
    
    org.store_metrics(org_counts)


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


def get_all_parsed_data(org_name_list, repo_name_list):

    all_orgs = []
    for org in org_name_list:
        # Track orgs and all its repos e.g. DSACMS
        all_orgs.append(GithubOrg(org))

    all_repos = []
    # Create repo objects
    for repo_url in repo_name_list:
        repo_obj = Repository(repo_url)
        all_repos.append(repo_obj)

    #  Capture the metric data  from all repos
    #  Returns a nested dictionary
    for repo in all_repos:

        print(repo.needed_parameters)
        metrics_results = {}

        # Get info from all metrics for each repo
        for metric in SIMPLE_METRICS:

            params = {}
            # Get the parameter for this metric
            for param in metric.needed_parameters:
                params[param] = repo.needed_parameters[param]

            metrics_results.update(metric.get_values(params))
        # repo_metric_info = output_repository_info(repo)

        repo.store_metrics(metrics_results)

    # print(all_repo_metrics_info)
    for obj in all_repos:
        print(obj.metric_data)

    # Capture all metric data for all Github orgs
    for org in all_orgs:

        metrics_results = {}

        for metric in ORG_METRICS:
            params = {}

            for param in metric.needed_parameters:
                params[param] = org.needed_params[param]

            metrics_results.update(metric.get_values(params))

        org.store_metrics(metrics_results)

        add_info_to_org_from_list_of_repos(all_repos,org)


    for obj in all_orgs:
        print(obj.metric_data)
    
    return all_orgs, all_repos

# DATA_JSON["DSACMS"] = all_repo_metrics_info
#
# Update _metadata/projects_tracked.json
# """
#    Updates the projects_tracked.json file to have all the Github metric data
#    for the desired orgs and repos
# """
# TODO Apply all the orgs and there assigned repos in projects tracked
# PROJECTS_TRACKED['orgs'] = ["DSACMS"]
# PROJECTS_TRACKED['Open Source Projects'] = {"DSACMS": list(repos_tracked)}
#
# with open(os.path.join(BASE_PATH, PATH_TO_METADATA + "/" + "projects_tracked.json"), "w+") as f:
# json.dump(PROJECTS_TRACKED, f)
#
# """
#  Create a new json file Labeled METRICS-DATESTAMP.json
#  Will create a new folder for the given repo and org if
#  it currently does not exist.
# """
# list_of_org_projects = PROJECTS_TRACKED['Open Source Projects']["DSACMS"]
# given_org_data = DATA_JSON["DSACMS"]
# print("given_org_data", given_org_data)
# for repo in list_of_org_projects:
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
