import json
from metricsLib.constants import SIMPLE_METRICS, ORG_METRICS
from metricsLib.oss_metric_entities import Repository, GithubOrg


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
        if repo.needed_parameters["repo_group_id"] == org.needed_parameters["repo_group_id"]:
            #Add metric data.
            for key in org_counts.keys():
                raw_count = repo.metric_data.get(key)
                if raw_count:
                    org_counts[key] += raw_count
    
    org.store_metrics(org_counts)


def fetch_all_new_metric_data(all_orgs, all_repos):

    #  Capture the metric data  from all repos
    #  Returns a nested dictionary
    for repo in all_repos:
        # Get info from all metrics for each repo
        for metric in SIMPLE_METRICS:
            repo.apply_metric_and_store_data(metric)

    # Capture all metric data for all Github orgs
    for org in all_orgs:

        metrics_results = {}

        for metric in ORG_METRICS:
            org.apply_metric_and_store_data(metric)

        add_info_to_org_from_list_of_repos(all_repos,org)


def read_previous_metric_data(repos, orgs):
    for org in orgs:
        try:
            with open(org.get_path_to_json_data(), "r") as file:
                prevData = json.load(file)
                org.previous_metric_data.update(prevData)
        except FileNotFoundError:
            print(f"Could not find previous data for records for org {org.login}")

    for repo in repos:
        try:
            with open(repo.get_path_to_json_data(), "r") as file:
                prevData = json.load(file)
                repo.previous_metric_data.update(prevData)
        except FileNotFoundError:
            print(f"Could not find previous data for records for repo {repo.name}")

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
