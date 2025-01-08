"""
Script to run all report generation from existing data.
"""
import os
from metrics_dash_backend_tools import parse_repos_and_orgs_into_objects
from metrics_dash_backend_tools import parse_tracked_repos_file, read_current_metric_data
from metrics_dash_backend_tools import generate_repo_report_files, generate_org_report_files
from constants import PATH_TO_METADATA, PATH_TO_METRICS_DATA, PATH_TO_REPORTS_DATA, PATH_TO_TEMPLATES



if __name__ == "__main__":
    os.umask(0)

    repo_template_path = os.path.join(PATH_TO_TEMPLATES, "repo_report_template.md")
    org_template_path = os.path.join(PATH_TO_TEMPLATES, "org_report_template.md")

    orgs_urls, repo_urls = parse_tracked_repos_file(PATH_TO_METADATA)

    all_orgs, all_repos = parse_repos_and_orgs_into_objects(orgs_urls, repo_urls)

    read_current_metric_data(PATH_TO_METRICS_DATA,all_repos,all_orgs)
    generate_repo_report_files(PATH_TO_REPORTS_DATA, repo_template_path, all_repos)
    generate_org_report_files(PATH_TO_REPORTS_DATA, org_template_path, all_orgs)
