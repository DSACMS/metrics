"""
Script to run all graph generation from existing data.
"""
import os
import json
from fetch_public_metrics import parse_repos_and_orgs_into_objects
from fetch_public_metrics import parse_tracked_repos_file, read_current_metric_data
from gen_graphs import generate_all_graphs_for_repos, generate_all_graphs_for_orgs



if __name__ == "__main__":
    os.umask(0)

    orgs_urls, repo_urls = parse_tracked_repos_file()

    all_orgs, all_repos = parse_repos_and_orgs_into_objects(orgs_urls, repo_urls)

    read_current_metric_data(all_repos,all_orgs)
    generate_all_graphs_for_orgs(all_orgs)
    generate_all_graphs_for_repos(all_repos)
