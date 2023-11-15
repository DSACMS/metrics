"""
Module to define methods to create pygals graphs
"""
import pygal

def generate_all_graphs_for_repos(all_repos):
    """
    Function to generate and save all graphs for the input
    repos.

    Arguments:
        all_repos: Repos to generate graphs for.
    """
    generate_repo_solid_guage_issue_graph(all_repos)
    generate_repo_sparklines(all_repos)

def write_repo_chart_to_file(repo,chart,chart_name, custom_func=None):
    """
    This function's purpose is to save a pygals chart to a path derived from the 
    repository object passed in.

    Arguments:
        repo: the Repository object that the chart is about
        chart: the pygals chart object
        chart_name: the name to save the chart as
        custom_func: an optional custom function to render the pygals chart with
    """

    with open(repo.get_path_to_graph_data(chart_name), "wb+") as file:
        try:
            if not custom_func:
                file.write(chart.render())
            else:
                file.write(custom_func())
        except ZeroDivisionError:
            print(f"Repo {repo.name} has a division by zero error when trying to make graph")
    #issues_guage.render_to_file(repo.get_path_to_graph_data("issue_guage"))



def generate_repo_sparklines(repos):
    """
    This function generates pygals sparklines graphs for a set of Repository objects.

    Arguments:
        repos: the set of Repository objects
    """
    for repo in repos:
        chart = pygal.Line(interpolate='cubic')
        chart.add('', list(repo.metric_data["commits_by_month"].values()))

        #print("SPARKLINES")
        #print(chart.render_sparkline())
        
        #I have to do this because sparklinees don't have their own subclass and instead
        #are rendered through a special method of the Line object.
        #TODO: file a pygals issue to make sparklines their own object
        write_repo_chart_to_file(repo, chart, "commit_sparklines",custom_func=chart.render_sparkline)


def generate_repo_solid_guage_issue_graph(repos):
    """
    This function generates pygals solid guage issue/pr graphs for a set of Repository objects.

    Arguments:
        repos: the set of Repository objects
    """

    for repo in repos:
        issues_guage = pygal.SolidGauge(inner_radius=0.70)
        percent_formatter = lambda x: '{:0.2f}%'.format(x)
        issues_guage.value_formatter = percent_formatter

        try:
            open_issue_percent = repo.metric_data['open_issues_count'] / repo.metric_data['issues_count']
        except ZeroDivisionError:
            open_issue_percent = 0
        issues_guage.add('Open Issues', [{'value': open_issue_percent * 100, 'max_value': 100}])
        
        try:
            open_pr_percent = repo.metric_data['open_pull_requests_count'] / repo.metric_data['pull_requests_count']
            merged_pr_percent = repo.metric_data['merged_pull_requests_count'] / repo.metric_data['pull_requests_count']
            closed_pr_percent = repo.metric_data['closed_pull_requests_count'] / repo.metric_data['pull_requests_count']
        except ZeroDivisionError:
            open_pr_percent = 0
            merged_pr_percent = 0
            closed_pr_percent = 0

        issues_guage.add('Open Pull Requests', [{'value': open_pr_percent * 100, 'max_value': 100}])
        issues_guage.add(
            'Closed and Merged Pull Requests', [
                {'value': merged_pr_percent * 100, 'max_value': 100},
                {'value': closed_pr_percent * 100, 'max_value': 100}])
        
        write_repo_chart_to_file(repo, issues_guage, "issue_guage")
        
        
# TODO: Just get these metrics from augur instead of storing them in json.

#def genOverview():
#    treemap = pygal.Treemap()
#    treemap.title = 'DSACMS Project Overview Binary TreeMap'
#
#    for file in os.listdir():
#        try:
#            f = open(file)
#            data = json.load(f)
#            d = []
#            words = file.split("-METRICS")
#
#            for key in data:
#                if (data[key] != 0 and data[key] != None):
#                    d.append(data[key])
#            d.pop(0)
#
#            treemap.add(words[0], d)
#        except:
#            invalid = []
#            invalid.append(file)
#
#    treemap.render_to_file('overview.svg')
#
#
#def repoSpecific():
#    for file in os.listdir():
#        try:
#            treemap = pygal.Treemap()
#            f = open(file)
#            data = json.load(f)
#            del data["datetime"]
#
#            for key in data:
#                if (data[key] != 0 and data[key] != None):
#                    treemap.add(key, data[key])
#
#            words = file.split("-METRICS")
#            treemap.title = words[0] + " Binary TreeMap"
#            treemap.render_to_file(words[0] + "-graph.svg")
#            data.clear()
#
#        except:
#            invalid = []
#            invalid.append(file)
