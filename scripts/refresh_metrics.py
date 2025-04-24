"""
Script to run all metrics collection and update operations
"""
import os
import argparse
from metrics_dash_backend_tools import get_all_data, parse_repos_and_orgs_into_objects
from metrics_dash_backend_tools import parse_tracked_repos_file, read_previous_metric_data
from constants import PATH_TO_METADATA, PATH_TO_METRICS_DATA, PATH_TO_GRAPHS_DATA
from metrics_dash_backend_tools.metrics_definitions import SIMPLE_METRICS, ORG_METRICS, ADVANCED_METRICS
from metrics_dash_backend_tools.metrics_definitions import PERIODIC_METRICS, RESOURCE_METRICS



if __name__ == "__main__":
    os.umask(0)

    parser = argparse.ArgumentParser(description='Metrics script to update data')
    parser.add_argument('org', type=str, nargs='?',
                    help='The GitHub Org to update data for.')
    args = parser.parse_args()

    orgs_urls, repo_urls = parse_tracked_repos_file(PATH_TO_METADATA, org=args.org)

    all_orgs, all_repos = parse_repos_and_orgs_into_objects(orgs_urls, repo_urls)

    # Generate json data, report data, and graph data.
    read_previous_metric_data(PATH_TO_METRICS_DATA,all_repos,all_orgs)

    list_of_all_metrics_lists = [SIMPLE_METRICS,ORG_METRICS,ADVANCED_METRICS,PERIODIC_METRICS]

    get_all_data(PATH_TO_METRICS_DATA, PATH_TO_GRAPHS_DATA,all_orgs, all_repos,list_of_all_metrics_lists,RESOURCE_METRICS)
