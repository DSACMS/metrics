"""
Script to run all metrics collection and update operations
"""
import os
import json
from metricsLib.oss_metric_entities import GithubOrg, Repository
from metricsLib.constants import PATH_TO_METADATA
from fetch_public_metrics import get_all_data
from gen_reports import generate_repo_report_files, generate_org_report_files
from gen_graphs import generate_all_graphs_for_repos, generate_all_graphs_for_orgs


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

        # search for matching org
        org_id = next(
            (x.repo_group_id for x in orgs if x.login.lower() == owner.lower()), None)

        # print(f"!!{org_id}")
        for repo_url in urls:
            repos.append(Repository(repo_url, org_id))
    return orgs, repos


if __name__ == "__main__":
    os.umask(0)
    # TODO: Create a read repos-to-include.txt
    metadata_path = os.path.join(PATH_TO_METADATA, "projects_tracked.json")
    with open(metadata_path, "r", encoding="utf-8") as file:
        tracking_file = json.load(file)

    # Track specific repositories e.g. ['dsacms.github.io']
    repo_urls = tracking_file["Open Source Projects"]

    # Get two lists of objects that will hold all the new metrics
    all_orgs, all_repos = parse_repos_and_orgs_into_objects(
        tracking_file["orgs"], repo_urls)

    # Generate json data, report data, and graph data.
    get_all_data(all_orgs, all_repos)
    generate_repo_report_files(all_repos)
    generate_org_report_files(all_orgs)
    generate_all_graphs_for_repos(all_repos)
    generate_all_graphs_for_orgs(all_orgs)
