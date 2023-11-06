from datetime import date
from metricsLib.constants import REPO_REPORT_TEMPLATE

def calc_percent_difference(latest,prev):
    absDiff = abs(latest - prev)
    dec = absDiff/((latest + prev)/2)

    return dec * 100

def generate_repo_report_files(repos):

    for repo in repos:
        #Create a dictionary of values to calculate for the report
        reportValues = {
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
            reportValues.update({
                f"latest_{heading}": repo.metric_data[heading],
                f"previous_{heading}": repo.previous_metric_data[heading],
                f"{heading}_diff": repo.metric_data[heading] - repo.previous_metric_data[heading],
                f"{heading}_diff_percent": calc_percent_difference(repo.metric_data[heading], repo.previous_metric_data[heading])
            })

        rawReport = REPO_REPORT_TEMPLATE.format(**reportValues)
        with open(repo.get_path_to_report_data(), "w+") as file:
            file.write(rawReport)