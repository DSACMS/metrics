"""
Script to run all report generation from existing data.
"""
import os
import json
from fetch_public_metrics import parse_repos_and_orgs_into_objects
from fetch_public_metrics import parse_tracked_repos_file, read_previous_metric_data
from gen_reports import generate_repo_report_files, generate_org_report_files



if __name__ == "__main__":
    os.umask(0)
    
    orgs_urls, repo_urls = parse_tracked_repos_file()

    all_orgs, all_repos = parse_repos_and_orgs_into_objects(orgs_urls, repo_urls)

    generate_repo_report_files(all_repos)
    generate_org_report_files(all_repos)
