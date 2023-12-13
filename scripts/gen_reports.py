"""
Module to define methods to create reports
"""
from datetime import date
from metricsLib.constants import REPO_REPORT_TEMPLATE, ORG_REPORT_TEMPLATE


def calc_percent_difference(latest, prev):
    """
    This function calculates the percent difference between
    two numbers

    Arguments:
        latest: float
            new number 
        prev: float
            old number to compare to new number

    Returns:
        Integer between 0 and 100 corresponding to the percent 
        difference.
    """
    abs_diff = abs(latest - prev)

    try:
        dec = abs_diff/((latest + prev)/2)
    except ZeroDivisionError:
        dec = 0

    return int(dec * 100)


def get_heading_report_values(headings, oss_entity):
    report_values = {}
    for heading in headings:
        prev_record = oss_entity.metric_data[heading]

        if heading in oss_entity.previous_metric_data.keys():
            prev_record = oss_entity.previous_metric_data[heading]

        percent_difference = calc_percent_difference(
            oss_entity.metric_data[heading], prev_record)
        raw_diff = oss_entity.metric_data[heading] - prev_record

        diff_color = ''

        if raw_diff > 0:
            # Green color
            diff_color = 'color: #45c527'
        elif raw_diff < 0:
            # Red color
            diff_color = 'color: #d31c08'

        report_values.update({
            f"latest_{heading}": oss_entity.metric_data[heading],
            f"previous_{heading}": prev_record,
            f"{heading}_diff": raw_diff,
            f"{heading}_diff_percent": percent_difference,
            f"{heading}_diff_color": diff_color,
            f"{heading}_diff_percent_color": diff_color
        })

    return report_values


def write_report_to_file(report_template, report_values, oss_entity):
    raw_report = report_template.format(**report_values)
    with open(oss_entity.get_path_to_report_data(), "w+", encoding="utf-8") as file:
        file.write(raw_report)


def generate_org_report_files(orgs):

    for org in orgs:
        print(f"Generating report for org {org.name}")

        report_values = {
            "date_stamp": date.today(),
            "repo_owner": org.login
        }

        org_metric_table_headings = [
            'commits_count',
            'issues_count',
            'open_issues_count',
            'closed_issues_count',
            'pull_requests_count',
            'open_pull_requests_count',
            'merged_pull_requests_count',
            'closed_pull_requests_count',
            'forks_count',
            'stargazers_count',
            'watchers_count',
            'followers_count'
        ]

        report_values.update(get_heading_report_values(
            org_metric_table_headings, org))
        write_report_to_file(ORG_REPORT_TEMPLATE, report_values, org)


def generate_repo_report_files(repos):
    """
    This function generates reports for each repo and writes them to file.

    Arguments:
        repos:
            list of repositories to generate reports for.
    """
    for repo in repos:
        print(f"Generating repo report for repo {repo.name}")
        # Create a dictionary of values to calculate for the report
        report_values = {
            "date_stamp": date.today(),
            "repo_owner": repo.repo_owner,
            "repo_name": repo.name,
        }

        metric_table_headings = [
            'commits_count',
            'issues_count',
            'open_issues_count',
            'closed_issues_count',
            'pull_requests_count',
            'open_pull_requests_count',
            'merged_pull_requests_count',
            'closed_pull_requests_count',
            'forks_count',
            'stargazers_count',
            'watchers_count'
        ]

        report_values.update(get_heading_report_values(
            metric_table_headings, repo))

        write_report_to_file(REPO_REPORT_TEMPLATE, report_values, repo)
