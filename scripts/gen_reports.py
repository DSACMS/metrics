from datetime import date
from metricsLib.constants import REPO_REPORT_TEMPLATE

def calc_percent_difference(latest,prev):
    absDiff = abs(latest - prev)

    try:
        dec = absDiff/((latest + prev)/2)
    except ZeroDivisionError:
        dec = 0

    return int(dec * 100)

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
            prevRecord = 0

            if heading in repo.previous_metric_data.keys():
                prevRecord = repo.previous_metric_data[heading]

            percent_difference = calc_percent_difference(repo.metric_data[heading], prevRecord)
            raw_diff = repo.metric_data[heading] - prevRecord

            #Black color
            diff_color = '#000000'

            if(raw_diff > 0):
                #Green color
                diff_color = '#45c527'
            elif (raw_diff < 0):
                #Red color
                diff_color = '#d31c08'

            reportValues.update({
                f"latest_{heading}": repo.metric_data[heading],
                f"previous_{heading}": prevRecord,
                f"{heading}_diff": raw_diff,
                f"{heading}_diff_percent": percent_difference,
                f"{heading}_diff_color": diff_color,
                f"{heading}_diff_percent_color": diff_color
            })

        rawReport = REPO_REPORT_TEMPLATE.format(**reportValues)
        with open(repo.get_path_to_report_data(), "w+") as file:
            file.write(rawReport)