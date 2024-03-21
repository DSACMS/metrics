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
        generate_donut_graph_line_complexity_graph(repo)


def generate_all_graphs_for_orgs(all_orgs):
    """
    Function to iterate through all orgs and generate graphs for each of them

    Arguments:
        all_orgs: Orgs to generate graphs for.
    """
    for org in all_orgs:
        print(f"Generating graphs for org {org.name}")
        generate_solid_gauge_issue_graph(org)
        generate_time_xy_issue_graph(org, "new_issues_by_day_over_last_six_months")


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
        repo, chart, "commit_sparklines",
        custom_func=chart.render_sparkline, custom_func_params=_kwargs_)


def generate_time_xy_issue_graph(oss_entity,data_key):
    """
    This function generates pygals xy time graph for new issue creation over a time period.

    Arguments:
        oss_entity: the OSSEntity to create a graph for
        data_key: key of the dictionary to use to generate the time graph
    """

    graph_data_dict = oss_entity.metric_data[data_key]

    dates_list = [record[0] for record in graph_data_dict]
    issues_list = [record[1] for record in graph_data_dict]

    xy_time_issue_chart = pygal.Line(x_label_rotation=20)
    xy_time_issue_chart.x_labels = dates_list
    xy_time_issue_chart.add("Issues", issues_list)

    write_repo_chart_to_file(oss_entity, xy_time_issue_chart, data_key)


def generate_donut_graph_line_complexity_graph(oss_entity):
    """
    This function generates pygals line complexity donut graph
    for a set of Repository objects.

    Arguments:
        oss_entity: The OSSEntity to create a graph for. an 
            OSSEntity is a data structure that is typically
            a repository or an organization.
    """

    donut_lines_graph = pygal.Pie(inner_radius=0.65,legend_at_bottom=True)
    donut_lines_graph.title = "Composition of Lines of Code"


    num_blank_lines = oss_entity.metric_data['total_project_blank_lines']
    donut_lines_graph.add('Total Blank Lines', num_blank_lines)

    num_comment_lines = oss_entity.metric_data['total_project_comment_lines']
    donut_lines_graph.add('Total Comment Lines', num_comment_lines)

    num_total_lines = oss_entity.metric_data['total_project_lines']
    num_remaining_lines = (num_total_lines - num_comment_lines) - num_blank_lines
    donut_lines_graph.add('Total Other Lines', num_remaining_lines)

    write_repo_chart_to_file(oss_entity, donut_lines_graph, "total_line_makeup")


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
