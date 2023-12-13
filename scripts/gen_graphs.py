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
    for repo in all_repos:
        print(f"Generating graphs for repo {repo.name}")
        generate_solid_gauge_issue_graph(repo)
        generate_repo_sparklines(repo)


def generate_all_graphs_for_orgs(all_orgs):
    for org in all_orgs:
        print(f"Generating graphs for org {org.name}")
        generate_solid_gauge_issue_graph(org)


def write_repo_chart_to_file(repo, chart, chart_name, custom_func=None, custom_func_params={}):
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
                file.write(custom_func(**custom_func_params))
        except ZeroDivisionError:
            print(
                f"Repo {repo.name} has a division by zero error when trying to make graph")
    # issues_gauge.render_to_file(repo.get_path_to_graph_data("issue_gauge"))


def generate_repo_sparklines(repo):
    """
    This function generates pygals sparklines graphs for a set of Repository objects.

    Arguments:
        repos: the set of Repository objects
    """
    chart = pygal.Line(interpolate='cubic')
    chart.add('', list(repo.metric_data["commits_by_month"].values()))
    chart.x_labels = list(repo.metric_data["commits_by_month"].keys())

    # print("SPARKLINES")
    # print(chart.render_sparkline())
    # I have to do this because sparklinees don't have their own subclass and instead
    # are rendered through a special method of the Line object.
    # TODO: file a pygals issue to make sparklines their own object
    _kwargs_ = {
        "show_x_labels": True,
        "show_y_labels": True,
        "margin": 10
    }
    write_repo_chart_to_file(
        repo, chart, "commit_sparklines", custom_func=chart.render_sparkline, custom_func_params=_kwargs_)


def generate_solid_gauge_issue_graph(oss_entity):
    """
    This function generates pygals solid gauge issue/pr graphs for a set of Repository objects.

    Arguments:
        oss_entity: the OSSEntity to create a graph for.
    """

    issues_gauge = pygal.SolidGauge(inner_radius=0.70, legend_at_bottom=True)

    def percent_formatter(x):
        return '{:0.2f}%'.format(x)
    issues_gauge.value_formatter = percent_formatter

    # Generate graph to measure percentage of issues that are open
    try:
        # calculate portion of issues that are open.
        open_issue_percent = oss_entity.metric_data['open_issues_count'] / \
            oss_entity.metric_data['issues_count']
    except ZeroDivisionError:
        open_issue_percent = 0
    issues_gauge.add(
        'Open Issues', [{'value': open_issue_percent * 100, 'max_value': 100}])

    try:
        # calculate portion of pull requests that are open, merged, and closed
        open_pr_percent = oss_entity.metric_data['open_pull_requests_count'] / \
            oss_entity.metric_data['pull_requests_count']
        merged_pr_percent = oss_entity.metric_data['merged_pull_requests_count'] / \
            oss_entity.metric_data['pull_requests_count']
        closed_pr_percent = oss_entity.metric_data['closed_pull_requests_count'] / \
            oss_entity.metric_data['pull_requests_count']
    except ZeroDivisionError:
        open_pr_percent = 0
        merged_pr_percent = 0
        closed_pr_percent = 0

    # Generate graph to measure portion of pull requests that are open
    issues_gauge.add('Open Pull Requests', [
                     {'value': open_pr_percent * 100, 'max_value': 100}])

    # Generate graph to measure portion of pull requests that are merged or closed.
    issues_gauge.add(
        'Closed and Merged Pull Requests', [
            {'label': "Merged Pull Requests",
                'value': merged_pr_percent * 100, 'max_value': 100},
            {'label': "Closed Pull Requests", 'value': closed_pr_percent * 100, 'max_value': 100}])

    write_repo_chart_to_file(oss_entity, issues_gauge, "issue_gauge")


# TODO: Just get these metrics from augur instead of storing them in json.

# def genOverview():
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
# def repoSpecific():
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
