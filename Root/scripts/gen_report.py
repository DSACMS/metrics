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
# PATH_TO_METRICS_POSTS = "_posts"
WEEKLY_MIN_DIFFERENCE = 6 # In Days
MONTHLY_MIN_DIFFERENCE = 27 # In Days



# TODO  Finish getting the 2 most recent  files from a given repo in a given org. 
def get_metrics_files(project, MIN_DIFFERENCE):
    # Get the latest two metrics for this project which are MIN_DIFFERENCE days apart
    re_metrics = re.compile(r"METRICS-\d{4}-\d{2}-\d{2}.json")
    all_metrics = []

    for filename in os.listdir(project):
        if re_metrics.match(filename):
            all_metrics.append(filename)
    heapq.heapify(all_metrics)
    metric_files = len(all_metrics)
    if metric_files < 2:
        return False, {}, {}
    latest_metrics = heapq.heappop(all_metrics)
    previous_metrics = heapq.heappop(all_metrics)


"""
    Input:
      latest type: [int] a specific  metric count from this week 
      previous: [int] a specific metric count from last week
    Output: Returns a boolean and modulo number that represents the highest multiple we passed
"""
def get_highlight_score(latest, previous):
    modulo_flag = False
    modulo_number = 0 # The highlight number crossed by the metric
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

