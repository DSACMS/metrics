"""
Module to define methods to create reports
"""
from datetime import date
from metricsLib.constants import REPO_REPORT_TEMPLATE, ORG_REPORT_TEMPLATE, DesiredReportBehavior


def calc_percent_difference(latest, prev):
    """
    This function calculates the percent difference between
    two numbers

    Arguments:
        latest: float
            new number 
        prev: float
            old number to compare to new number

    Returns:
        Float between 0 and 100 corresponding to the percent 
        difference.
    """

    abs_diff = abs(latest - prev)

    try:
        dec = abs_diff/((latest + prev)/2)
    except ZeroDivisionError:
        dec = 0

    return dec * 100

def round_to_significant_figures(n, significant_figures):
    """
    Returns the input rounded to the desired number of significant figures

    Arguments:
        n: number

        significant_figures: int
            The number of significant figures to round to.
    
    Returns:
        String of the number formatted to the desired number of significant figures.
    """

    formatted = '{:g}'.format(float('{:.{p}g}'.format(n, p=significant_figures)))

    return formatted


def get_heading_report_values(headings, oss_entity):
    """
    Generates a dictionary of statistics for each 'heading' where
    a heading is a type of data point. i.e. commits_diff versus pull_request_count_diff.

    Arguments:
        headings: dictionary
            dictionary of data point types i.e. 'commits' with desired behavior
        oss_entity: OssEntity
            Data structure representing the entity that the data corresponds to
    
    Returns:
        A dictionary of statistics with many keys for each heading.
    """

    report_values = {}
    for heading, behavior in headings.items():
        prev_record = oss_entity.metric_data[heading]

        if heading in oss_entity.previous_metric_data.keys():
            prev_record = oss_entity.previous_metric_data[heading]
        if prev_record is None:
            #Cast None to 0 for diff calc
            prev_record = 0

        next_record = oss_entity.metric_data[heading]
        if oss_entity.metric_data[heading] is None:
            next_record = 0

        percent_difference = calc_percent_difference(
            next_record, prev_record)

        raw_diff = next_record - prev_record

        diff_color = ''


        #        Truth Table:
        #
        #        +--------------+--------------------------------------+---+-------------------+
        #        | raw_diff > 0 | DesiredReportBehavior.VALUE_INCREASE | _ |      Result       |
        #        +--------------+--------------------------------------+---+-------------------+
        #        |            0 |                                    1 | _ | Red if negative   |
        #        |            1 |                                    0 | _ | Red if negative   |
        #        |            1 |                                    1 |   | Green             |
        #        |            0 |                                    0 | - | Green if negative |
        #        +--------------+--------------------------------------+---+-------------------+


        and_conditional=((raw_diff>0) and (behavior == DesiredReportBehavior.VALUE_INCREASE.value))
        #Use a XOR by using the != operator
        if (raw_diff > 0) != (behavior == DesiredReportBehavior.VALUE_INCREASE.value):
            if raw_diff < 0:
                # Red color
                diff_color = 'color: #d31c08'
        elif and_conditional or ((raw_diff < 0) and not and_conditional):
            # Green color
            diff_color = 'color: #45c527'

        report_values.update({
            f"latest_{heading}": oss_entity.metric_data[heading],
            f"previous_{heading}": prev_record,
            f"{heading}_diff": raw_diff,
            f"{heading}_diff_percent": round_to_significant_figures(percent_difference, 2),
            f"{heading}_diff_color": diff_color,
            f"{heading}_diff_percent_color": diff_color
        })

    return report_values


def write_report_to_file(report_template, report_values, oss_entity):
    """
    Writes a report markdown file to disc after formatting the values provided through 
    a python dictionary.

    Arguments:
        report_template: str
            String that contains unformatted text for the markdown report
        report_values: dict
            Dictionary that contains values to format the text with
        oss_entity: OssEntity
            Oss entity that the report corresponds to the report
    """
    raw_report = report_template.format(**report_values)
    with open(oss_entity.get_path_to_report_data(), "w+", encoding="utf-8") as file:
        file.write(raw_report)


def generate_org_report_files(orgs):
    """
    Generate reports for orgs

    Arguments:
        orgs: collection
            List of orgs to generate reports for
    """

    for org in orgs:
        print(f"Generating report for org {org.name}")

        report_values = {
            "date_stamp": date.today(),
            "repo_owner": org.login
        }

        #Define headings as key value pairs where
        #   key -> value = heading -> desired_behavior
        #
        # DesiredReportBehavior.VALUE_INCREASE means you want the value to go up
        org_metric_table_headings = {
            'commits_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'issues_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'open_issues_count': DesiredReportBehavior.VALUE_DECREASE.value,
            'closed_issues_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'pull_requests_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'open_pull_requests_count': DesiredReportBehavior.VALUE_DECREASE.value,
            'merged_pull_requests_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'closed_pull_requests_count': DesiredReportBehavior.VALUE_DECREASE.value,
            'forks_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'stargazers_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'watchers_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'followers_count': DesiredReportBehavior.VALUE_INCREASE.value
        }

        report_values.update(get_heading_report_values(
            org_metric_table_headings, org))
        write_report_to_file(ORG_REPORT_TEMPLATE, report_values, org)


def generate_repo_report_files(repos):
    """
    This function generates reports for each repo and writes them to file.

    Arguments:
        repos:
            list of repositories to generate reports for.
    """
    for repo in repos:
        print(f"Generating repo report for repo {repo.name}")
        # Create a dictionary of values to calculate for the report


        badge_name = repo.metric_data.get('nadia_badge_name')
        badge_color = repo.metric_data.get('nadia_color')

        if not badge_name or not badge_color:
            badge_color = "#ff0000"
            badge_name = "Unknown"

        report_values = {
            "date_stamp": date.today(),
            "repo_owner": repo.repo_owner,
            "repo_name": repo.name,
            "repo_nadia_badge_name": badge_name,
            "repo_nadia_badge_color": badge_color
        }

        #Define headings as key value pairs where
        #   key -> value = heading -> desired_behavior
        #
        # DesiredReportBehavior.VALUE_INCREASE means you want the value to go up
        metric_table_headings = {
            'commits_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'issues_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'open_issues_count': DesiredReportBehavior.VALUE_DECREASE.value,
            'closed_issues_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'pull_requests_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'open_pull_requests_count': DesiredReportBehavior.VALUE_DECREASE.value,
            'merged_pull_requests_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'closed_pull_requests_count': DesiredReportBehavior.VALUE_DECREASE.value,
            'forks_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'stargazers_count': DesiredReportBehavior.VALUE_INCREASE.value,
            'watchers_count': DesiredReportBehavior.VALUE_INCREASE.value
        }

        report_values.update(get_heading_report_values(
            metric_table_headings, repo))

        write_report_to_file(REPO_REPORT_TEMPLATE, report_values, repo)
