"""
Script to run all graph generation from existing data.
"""
import os
from metrics_dash_backend_tools import parse_repos_and_orgs_into_objects
from metrics_dash_backend_tools import parse_tracked_repos_file, read_current_metric_data
from metrics_dash_backend_tools import generate_all_graphs_for_repos, generate_all_graphs_for_orgs
from constants import PATH_TO_METADATA, PATH_TO_METRICS_DATA, PATH_TO_GRAPHS_DATA


if __name__ == "__main__":
    os.umask(0)

    orgs_urls, repo_urls = parse_tracked_repos_file(PATH_TO_METADATA)

    all_orgs, all_repos = parse_repos_and_orgs_into_objects(orgs_urls, repo_urls)

    read_current_metric_data(PATH_TO_METRICS_DATA, all_repos,all_orgs)
    generate_all_graphs_for_orgs(PATH_TO_GRAPHS_DATA, all_orgs)
    generate_all_graphs_for_repos(PATH_TO_GRAPHS_DATA, all_repos)
