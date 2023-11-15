"""
Module to define methods to create reports
"""
from datetime import date
from metricsLib.constants import REPO_REPORT_TEMPLATE

def calc_percent_difference(latest,prev):
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
    absDiff = abs(latest - prev)

    try:
        dec = absDiff/((latest + prev)/2)
    except ZeroDivisionError:
        dec = 0

    return int(dec * 100)

def generate_repo_report_files(repos):
    """
    This function generates reports for each repo and writes them to file.

    Arguments:
        repos:
            list of repositories to generate reports for.
    """
    for repo in repos:
        print(f"Generating repo report for repo {repo.name}")
        #Create a dictionary of values to calculate for the report
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

        for heading in metric_table_headings:
            prev_record = 0

            if heading in repo.previous_metric_data.keys():
                prev_record = repo.previous_metric_data[heading]

            report_values.update({
                f"latest_{heading}": repo.metric_data[heading],
                f"previous_{heading}": prev_record,
                f"{heading}_diff": repo.metric_data[heading] - prev_record,
                f"{heading}_diff_percent": calc_percent_difference(repo.metric_data[heading], prev_record)
            })

        raw_report = REPO_REPORT_TEMPLATE.format(**report_values)
        with open(repo.get_path_to_report_data(), "w+",encoding="utf-8") as file:
            file.write(raw_report)