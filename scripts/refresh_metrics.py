"""
Script to run all metrics collection and update operations
"""
import os
from fetch_public_metrics import get_all_data, parse_repos_and_orgs_into_objects
from fetch_public_metrics import parse_tracked_repos_file, read_previous_metric_data



if __name__ == "__main__":
    os.umask(0)

    orgs_urls, repo_urls = parse_tracked_repos_file()

    all_orgs, all_repos = parse_repos_and_orgs_into_objects(orgs_urls, repo_urls)

    # Generate json data, report data, and graph data.
    read_previous_metric_data(all_repos,all_orgs)
    get_all_data(all_orgs, all_repos)
