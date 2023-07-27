from glob import glob
import datetime
"""
Create WEEKLY-REPORT-<DATE>.json for all the orgs and projects,
and save then inside _data directory.
Similarly for MONTHLY report as well.
Also call report_posts.py module to create _posts reflecting the reports.
"""

from glob import glob
import heapq
import datetime
import json
import os
import re

PATH_TO_METRICS_DATA = "_data"
PATH_TO_METADATA = "_metadata"
PATH_TO_MOCK_DATA = "_mockData"
# PATH_TO_METRICS_POSTS = "_posts"
WEEKLY_MIN_DIFFERENCE = 6 # In Days
MONTHLY_MIN_DIFFERENCE = 27 # In Days

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
        if re_metrics.match(filename):
            all_metrics.append(filename)
    heapq.heapify(all_metrics)
    metric_files = len(all_metrics)
    if metric_files < 2 or metric_files < weeks:
        return False, {}, {}
    files_data = []
    for _ in range(weeks):
        week = heapq.heappop(all_metrics)
        with open(PATH_TO_MOCK_DATA + "/" + week, "r") as file:
            week_data = file.read()
        files_data.append(week_data)
    return files_data


"""
    Input:
      latest type: [int] a specific  metric count from this week 
      previous: [int] a specific metric count from last week
    Output: Returns a boolean and modulo number that represents the highest multiple we passed
"""
def get_highlight_score(latest, previous):
    modulo_flag = False
    modulo_number = 0 
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


# calculates the difference between this week/monthly versus last  week/monthly per metric
def calculate_weekly_diff(files):
    pass

def calculate_we_sum(files):
    pass
        
weekly_files = get_metrics_files(PATH_TO_MOCK_DATA, 2)
latest, previous = weekly_files
print(latest, previous)
