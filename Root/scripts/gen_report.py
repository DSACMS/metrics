from glob import glob
from datetime import datetime
"""
Create WEEKLY-REPORT-<DATE>.json for all the orgs and projects,
and save then inside _data directory.
Similarly for MONTHLY report as well.
Also call report_posts.py module to create _posts reflecting the reports.
"""

from glob import glob
import heapq
from datetime import datetime
import json
import os
import re

PATH_TO_METRICS_DATA = "_data"
PATH_TO_METADATA = "_metadata"
PATH_TO_MOCK_DATA = "_mockData"
# PATH_TO_METRICS_POSTS = "_posts"
WEEKLY_MIN_DIFFERENCE = 6 # In Days
MONTHLY_MIN_DIFFERENCE = 27 # In Days
github_metrics = ['commits_count', 'issues_count', 'open_issues_count', 
                  'closed_issues_count', 'pull_requests_count', 'open_pull_requests_count',
                    'merged_pull_requests_count', 'closed_pull_requests_count', 'forks_count', 
                    'stargazers_count', 'watchers_count']

"""
    Input: project: repo directory 
           Weeks refers to the number of files we want.  weeks we wa
    Returns a list of file names listed from most recent to least recent.
"""
def get_metrics_files(project, weeks):
    # Get the latest two metrics for this project which are MIN_DIFFERENCE days apart
    re_metrics = re.compile(r"METRICS-\d{4}-\d{2}-\d{2}.json")
    all_metrics = []

    for filename in os.listdir(project):
        # print(filename)
        if re_metrics.match(filename):
            datestamp = datetime.strptime(filename,"METRICS-%Y-%m-%d.json")
            # print(file_date)
            timestamp_float = datestamp.timestamp()
            timestamp_int = int(timestamp_float) * -1 
            all_metrics.append((timestamp_int, filename))

    heapq.heapify(all_metrics)
    metric_files = len(all_metrics)
    if metric_files < 2 or metric_files < weeks:
        return False, {}, {}
    files_data = []
    for _ in range(weeks):
        _, week = heapq.heappop(all_metrics)
        with open(PATH_TO_MOCK_DATA + "/" + week, "r") as file:
            week_data = file.read()
            week_data_json = json.loads(week_data)
        files_data.append(week_data_json)
    return files_data


# calculates the difference between this week/monthly versus last week/monthly per metric
def calculate_weekly_diff(files):
    if len(files) > 2:
        return False, {}
    latest, previous  = files
    weekly_difference = {'datetime': 0, 'commits_count': 0, 'issues_count': 0,
                    'open_issues_count': 0,'closed_issues_count': 0, 'pull_requests_count': 0, 'open_pull_requests_count': 0,
                    'merged_pull_requests_count': 0, 'closed_pull_requests_count': 0, 'forks_count': 0, 
                    'stargazers_count': 0, 'watchers_count': 0 }
    for metric in latest:
        if metric != "datetime" and latest[metric] is not None:
            weekly_difference[metric] = latest[metric] - previous[metric]
    return weekly_difference

"""
    Input:
      latest type: [int] a specific  metric count from this week 
      previous: [int] a specific metric count from last week
    Output: Returns a boolean and modulo number that represents the highest multiple we passed
"""
def get_highlight_score(metric, latest_file, previous_file):
    modulo_flag = False
    modulo_number = 0 
    latest = latest_file[metric]
    previous = previous_file[metric]

    if type(latest) == "str" or latest == None or previous == None:
        return modulo_flag, modulo_number
    #  check if we passed the threshold
    if latest // 100 != previous // 100:
        modulo_flag = True
        modulo_number = max(latest, previous) - max(latest, previous) % 100
    if latest // 1000 != previous // 1000:
        modulo_flag = True
        modulo_number = max(latest, previous) - max(latest, previous) % 1000
    if latest // 10000 != previous  // 10000:
        modulo_flag = True
        modulo_number = max(latest, previous) - max(latest, previous) % 10000
    return modulo_flag, modulo_number


"""
Given two files of type dict, it will calculate the difference 
between latest and previous per each metric
 Input: latest_file: dict {}
        previous_file: dict {}
 Return: highlights: dict {} representing all the highlights per 
         github metric that is not a string or None:
"""
def get_repo_highlights(latest_file, previous_file):
    highlights = {}
    for metric in github_metrics:
        highlights[metric] = get_highlight_score(metric, latest, previous)
    return highlights

"""
   Calculates the total sum across each github metric for this month. 
   Input: files: list [{}, {}, ...]
   Return: monthly_report: dict {}
"""
def calculate_monthly_sum(files):
    if len(files) < 4:
        return False, {}
    monthly_report = {}
    for file in files:
        for metric in file:
            if metric != "datetime" or file[metric] is not None:
                if metric not in monthly_report:
                    monthly_report[metric] = file[metric]
                else:
                    monthly_report[metric] += file[metric]
    return monthly_report

weekly_files = get_metrics_files(PATH_TO_MOCK_DATA, 2)
monthly_files = get_metrics_files(PATH_TO_MOCK_DATA, 4)
latest, previous = weekly_files
WEEKLY_DIFFERENCE = calculate_weekly_diff(weekly_files)
WEEKLY_HIGHLIGHTS = get_repo_highlights(latest, previous)

WEEKLY_DATA_JSON = {"WEEKLY_DIFFERENCE": WEEKLY_DIFFERENCE, "WEEKLY_HIGHLIGHTS": WEEKLY_HIGHLIGHTS}


