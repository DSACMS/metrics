from glob import glob
import json
import os
import re
import pygal

PATH = "_dataVis"
os.chdir(PATH)


def generate_repo_solid_guage_issue_graph(repos):
    for repo in repos:
        issues_guage = pygal.SolidGauge(inner_radius=0.70)
        percent_formatter = lambda x: '{:.10g}%'.format(x)
        issues_guage.value_formatter = percent_formatter

        issues_guage.add('Open Issues', [{'value': repo.metric_data['open_issues_count'], 'max_value': repo.metric_data['issues_count']}])

        issues_guage.add('Open Pull Requests', [{'value': repo.metric_data['open_pull_requests_count'], 'max_value': repo.metric_data['pull_requests_count']}])
        issues_guage.add(
            'Closed and Merged Pull Requests', [
                {'value': repo.metric_data['merged_pull_requests_count'], 'max_value': repo.metric_data['pull_requests_count']},
                {'value': repo.metric_data['closed_pull_requests_count'], 'max_value': repo.metric_data['pull_requests_count']}])
        
        issues_guage.render_to_file(repo.get_path_to_graph_data("issue_guage"))

# TODO: Just get these metrics from augur instead of storing them in json.
def genOverview():
    treemap = pygal.Treemap()
    treemap.title = 'DSACMS Project Overview Binary TreeMap'

    for file in os.listdir():
        try:
            f = open(file)
            data = json.load(f)
            d = []
            words = file.split("-METRICS")

            for key in data:
                if (data[key] != 0 and data[key] != None):
                    d.append(data[key])
            d.pop(0)

            treemap.add(words[0], d)
        except:
            invalid = []
            invalid.append(file)

    treemap.render_to_file('overview.svg')


def repoSpecific():
    for file in os.listdir():
        try:
            treemap = pygal.Treemap()
            f = open(file)
            data = json.load(f)
            del data["datetime"]

            for key in data:
                if (data[key] != 0 and data[key] != None):
                    treemap.add(key, data[key])

            words = file.split("-METRICS")
            treemap.title = words[0] + " Binary TreeMap"
            treemap.render_to_file(words[0] + "-graph.svg")
            data.clear()

        except:
            invalid = []
            invalid.append(file)


def main():
    genOverview()
    repoSpecific()


if __name__ == "__main__":
    main()
