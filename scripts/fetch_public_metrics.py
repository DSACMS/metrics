"""
Module to define methods that fetch data to store in the oss metric
entity objects.
"""
import json
from metricsLib.metrics_definitions import SIMPLE_METRICS, ORG_METRICS
from metricsLib.metrics_definitions import PERIODIC_METRICS, RESOURCE_METRICS


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
            repo.apply_metric_and_store_data(metric, repo)

    # Capture all metric data for all Github orgs
    for org in all_orgs:
        print(f"Fetching metrics for org {org.name} id #{org.repo_group_id}")
        for metric in ORG_METRICS:
            org.apply_metric_and_store_data(metric)
        add_info_to_org_from_list_of_repos(all_repos, org)


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

    Arguments:
        orgs: orgs to write to file
        repos: repos to write to file
    """

    for org in orgs:
        org_metric_data = json.dumps(org.metric_data, indent=4)

        with open(org.get_path_to_json_data(), "w+", encoding="utf-8") as file:
            file.write(org_metric_data)

    for repo in repos:
        repo_metric_data = json.dumps(repo.metric_data, indent=4)

        with open(repo.get_path_to_json_data(), "w+", encoding="utf-8") as file:
            file.write(repo_metric_data)
