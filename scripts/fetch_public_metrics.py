"""
Module to define methods that fetch data to store in the oss metric
entity objects.
"""
import os
import json
from metricsLib.metrics_definitions import SIMPLE_METRICS, ORG_METRICS, ADVANCED_METRICS
from metricsLib.metrics_definitions import PERIODIC_METRICS, RESOURCE_METRICS
from metricsLib.oss_metric_entities import GithubOrg, Repository
from metricsLib.constants import PATH_TO_METADATA

def parse_tracked_repos_file(org=None):
    """
    Function to parse projects_tracked.json

    Returns:
        Tuple of lists of strings that represent repos and orgs
    """

    # TODO: Create a read repos-to-include.txt
    metadata_path = os.path.join(PATH_TO_METADATA, "projects_tracked.json")
    with open(metadata_path, "r", encoding="utf-8") as file:
        tracking_file = json.load(file)

    # Only parse the desired org if an org was passed as an argument
    if org:
        repo_urls = {
            org : tracking_file["Open Source Projects"][org]
        }
        return [org], repo_urls

    repo_urls = tracking_file["Open Source Projects"]

    # Get two lists of objects that will hold all the new metrics
    return tracking_file["orgs"], repo_urls

def parse_repos_and_orgs_into_objects(org_name_list, repo_name_list):
    """
    This function parses lists of strings into oss metric entities and
    returns lists of corresponding oss metric entitiy objects.

    Arguments:
        org_name_list: list of logins for github orgs
        repo_name_list: list of urls for git repositories with groups labeled

    Returns:
        Tuple of lists of oss metric entity objects
    """
    orgs = [GithubOrg(org) for org in org_name_list]

    repos = []  # [Repository(repo_url) for repo_url in repo_name_list]

    for owner, urls in repo_name_list.items():
        print(owner)
        # search for matching org
        org_id = next(
            (x.repo_group_id for x in orgs if x.login.lower() == owner.lower()), None)

        # print(f"!!{org_id}")
        for repo_url in urls:
            repos.append(Repository(repo_url, org_id))
    return orgs, repos

def get_all_data(all_orgs, all_repos):
    """
    Call relevant methods on orgs and repos

    Arguments:
        all_orgs: List of all orgs to gather metrics for
        all_repos: List of all repos to gather metrics for
    """
    fetch_all_new_metric_data(all_orgs, all_repos)
    read_previous_metric_data(all_repos, all_orgs)
    write_metric_data_json_to_file(all_orgs, all_repos)


def add_info_to_org_from_list_of_repos(repo_list, org):
    """
    This method serves to iterate through previously collected metric
    data that is associated with a repo and derive the cumulative metric data
    for the whole organization instead of the repository. 

    This is mainly to avoid using more api calls than we have to.

    Arguments:
        repo_list: List of all repos with metrics
        org: The github org to add metrics to
    """
    # Define counts to update based on tracked repositories.
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

    # Add repo data to org that repo is a part of
    for repo in repo_list:
        # Check for membership
        #print(repo.needed_parameters["repo_group_id"])
        #print(org.needed_parameters["repo_group_id"])
        if repo.needed_parameters["repo_group_id"] == org.needed_parameters["repo_group_id"]:
            # Add metric data.
            for key, _ in org_counts.items():
                raw_count = repo.metric_data.get(key)
                if raw_count:
                    org_counts[key] += raw_count

    org.store_metrics(org_counts)


def fetch_all_new_metric_data(all_orgs, all_repos):
    """
    This method applies all desired methods to all desired repos 
    and orgs. It applies and stores all the metrics

    This is mainly to avoid using more api calls than we have to.

    Arguments:
        all_orgs: List of all orgs to gather metrics for
        all_repos: List of all repos to gather metrics for
    """

    #  Capture the metric data  from all repos
    #  Returns a nested dictionary
    for repo in all_repos:
        print(f"Fetching metrics for repo {repo.name}, id #{repo.repo_id}.")
        # Get info from all metrics for each repo
        for metric in SIMPLE_METRICS:
            repo.apply_metric_and_store_data(metric)

        for metric in PERIODIC_METRICS:
            repo.apply_metric_and_store_data(metric)

        for metric in RESOURCE_METRICS:
            repo.apply_metric_and_store_data(metric, oss_entity=repo)

        for metric in ADVANCED_METRICS:
            repo.apply_metric_and_store_data(metric)

    # Capture all metric data for all Github orgs
    for org in all_orgs:
        print(f"Fetching metrics for org {org.name} id #{org.repo_group_id}")
        for metric in ORG_METRICS:
            org.apply_metric_and_store_data(metric)
            print(metric.name)
        add_info_to_org_from_list_of_repos(all_repos, org)

def read_current_metric_data(repos,orgs):
    """
    Read current metrics and load previous metrics that 
    were saved in .old files.

    Arguments:
        orgs: orgs to read data for.
        repos: repos to read data for.
    """

    for org in orgs:

        path = org.get_path_to_json_data()
        #generate dict of previous and save it as {path}.old
        #previous_metric_org_json = json.dumps(org.previous_metric_data, indent=4)

        with open(f"{path}.old","r",encoding="utf-8") as file:
            previous_metric_org_json = json.load(file)

        #generate dict of current metric data.
        org.previous_metric_data.update(previous_metric_org_json)


        with open(path, "r", encoding="utf-8") as file:
            #file.write(org_metric_data)
            print(path)
            current_metric_org_json = json.load(file)

        org.metric_data.update(current_metric_org_json)

    for repo in repos:
        #previous_metric_repo_json = json.dumps(repo.previous_metric_data, indent=4)
        path = repo.get_path_to_json_data()

        with open(f"{path}.old","r",encoding="utf-8") as file:
            #file.write(previous_metric_repo_json)
            previous_metric_repo_json = json.load(file)

        repo.previous_metric_data.update(previous_metric_repo_json)


        with open(path, "r", encoding="utf-8") as file:
            #file.write(repo_metric_data)
            metric_repo_json = json.load(file)

        repo.metric_data.update(metric_repo_json)


def read_previous_metric_data(repos, orgs):
    """
    This method reads the previously gathered metric data and 
    stores it in the OSSEntity objects passed in.

    This is for the reports that compare changes since last collection.

    Arguments:
        repos: List of all orgs to read metrics for
        orgs: List of all repos to read metrics for
    """
    for org in orgs:
        try:
            with open(org.get_path_to_json_data(), "r", encoding="utf-8") as file:
                prev_data = json.load(file)
                org.previous_metric_data.update(prev_data)
        except FileNotFoundError:
            print("Could not find previous data for records for org" +
                  f"{org.login}")   


    for repo in repos:
        try:
            with open(repo.get_path_to_json_data(), "r", encoding="utf-8") as file:
                prev_data = json.load(file)
                repo.previous_metric_data.update(prev_data)
        except FileNotFoundError:
            print("Could not find previous data for records for repo" +
                  repo.name)


def write_metric_data_json_to_file(orgs, repos):
    """
    Write all metric data to json files.
    
    Keep old metrics as a .old file.

    Arguments:
        orgs: orgs to write to file
        repos: repos to write to file
    """

    for org in orgs:

        path = org.get_path_to_json_data()
        #generate dict of previous and save it as {path}.old
        previous_metric_org_json = json.dumps(org.previous_metric_data, indent=4)

        with open(f"{path}.old","w+",encoding="utf-8") as file:
            file.write(previous_metric_org_json)

        #generate dict of current metric data.
        org_dict = org.previous_metric_data
        org_dict.update(org.metric_data)
        org_metric_data = json.dumps(org_dict, indent=4)

        #print(org_metric_data)

        with open(path, "w+", encoding="utf-8") as file:
            file.write(org_metric_data)

    for repo in repos:
        path = repo.get_path_to_json_data()

        previous_metric_repo_json = json.dumps(repo.previous_metric_data, indent=4)

        with open(f"{path}.old","w+",encoding="utf-8") as file:
            file.write(previous_metric_repo_json)

        repo_dict = repo.previous_metric_data
        repo_dict.update(repo.metric_data)
        repo_metric_data = json.dumps(repo_dict, indent=4)


        with open(path, "w+", encoding="utf-8") as file:
            file.write(repo_metric_data)
