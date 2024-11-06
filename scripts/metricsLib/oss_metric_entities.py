"""
Module that defines objects to model oss metric entities. i.e. objects that
store data and have methods concerning the concept of entities that we would
like to gather metric data for. 
"""
import re
import json
import os
import datetime
import pathlib
import requests
from requests.exceptions import ReadTimeout
from metricsLib.constants import PATH_TO_METRICS_DATA, PATH_TO_REPORTS_DATA, AUGUR_HOST
from metricsLib.constants import TIMEOUT_IN_SECONDS, PATH_TO_GRAPHS_DATA


def get_repo_owner_and_name(repo_http_url):
    """ Gets the owner and repo from a url.

        Args:
            url: Github url

        Returns:
            Tuple of owner and repo. Or a tuple of None and None if the url is invalid.
    """

    # Regular expression to parse a GitHub URL into two groups
    # The first group contains the owner of the github repo extracted from the url
    # The second group contains the name of the github repo extracted from the url
    # 'But what is a regular expression?' ----> https://docs.python.org/3/howto/regex.html
    regex = r"https?:\/\/github\.com\/([A-Za-z0-9 \- _]+)\/([A-Za-z0-9 \- _ \.]+)(.git)?\/?$"
    result = re.search(regex, repo_http_url)

    if not result:
        return None, None

    capturing_groups = result.groups()

    owner = capturing_groups[0]
    repo = capturing_groups[1]

    return owner, repo


def get_timebox_timestamps():
    """ 
        Gets timeboxed timestamps for the time the 
        function was ran.

        Returns:
            Dictionary of key timestamps and the desired period
            for metrics
    """
    # Get timeboxed metrics
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(weeks=4)
    month_ago = today - datetime.timedelta(weeks=24)

    # Perpare params for weekly timebox
    periodic_params = {
        "period": "day",
        "end_date": today.strftime('%Y/%m/%d'),
        "begin_week": week_ago.strftime('%Y/%m/%d'),
        "begin_month": month_ago.strftime('%Y/%m/%d')
    }

    return periodic_params


class OSSEntity:
    """
    This serves as the base class to define an OSSEntity. An OSSEntity is an 
    object that represents some open source thing that we want to get
    information about. For example a Github Repository

    ...

    Attributes
    ----------
    name : str
        name of the entity
    augur_endpoint : str
        endpoint to use to connect to the corresponding object in the augur db
    needed_parameters : dict
        Dictionary holding parameters that are needed to hit a metric
    metric_data: dict
        The dictionary that actually stores data returned by metrics
    previous_metric_data: dict
        The dictionary that stores the previous data from the previous metric JSON

    Methods
    -------
    store_metrics(info={}):
        Alias to update the metric_data dict with metric data
    get_parameters_for_metric(metric):
        Get a sub directory of the needed_parameters dict that only holds the parameters
        needed by a metric
    apply_metric_and_store_data(metric):
        Pass needed parameters into a metric, hit the metric, and then store the result in
        the metric_data dict.
    """

    def __init__(self, name, augur_endpoint):
        self.name = name
        self.augur_util_endpoint = augur_endpoint

        self.needed_parameters = {}
        self.metric_data = {}
        self.previous_metric_data = {}

    def store_metrics(self, info):
        """
        Alias to update the metric data dict with metric data.

        Args:
            info: dict
                Dictionary containing the metric to update the
                metric data with.
        """
        self.metric_data.update(info)

    # TODO: should this logic be moved to the hit_metric method?
    def get_parameters_for_metric(self, metric):
        """
        Get a sub directory of the needed_parameters dict that only holds the parameters
        needed by a metric

        Args:
            metric: BaseMetric

        Returns:
            Dictionary containing the parameters needed for the given metric
        """
        params = {}

        # get the parameter for this metric
        for param in metric.needed_parameters:
            params[param] = self.needed_parameters[param]

        return params

    def apply_metric_and_store_data(self, metric, *args, **kwargs):
        """
        Pass needed parameters into a metric, hit the metric, and then store the result in
        the metric_data dict.

        Args:
            metric: BaseMetric
        """
        params = self.get_parameters_for_metric(metric)

        kwargs['params'] = params

        try:
            self.store_metrics(metric.get_values(*args, **kwargs))
        except (TimeoutError, ReadTimeout) as e:
            print(f"Timeout for repo {self.name} with metric {metric.name}")
            print(f"Error: {e}")
        except ConnectionError as e:
            print(f"Connection error for repo {self.name} with metric {metric.name}")
            print(f"Error: {e}")


class Repository(OSSEntity):
    """
    This class serves to manage the parameter and metric data of a Repository.
    It stores parameter and metric data in two seperate dictionaries for easy JSON 
    conversion.

    Repository's main purpose as a real python class is to encapsulate the mapping
    of the db ids in augur to the repos we are trying to gather metrics for.

    ...

    Attributes
    ----------
    url : str
        url where the repository is hosted.
    repo_owner : str
        Org that owns the repo, also could be a User
    repo_id : int
        database id of the repo in Augur
    repo_group_id: int
        id for the org that owns the repo in Augur

    Methods
    -------
    get_path_to_data(parent_path="",extension=""):
        Returns the path to store data given extension
        and parent path
    get_path_to_json_data():
        Derive the path for json data using json parent
        path and extension
    get_path_to_report_data():
        Derive the path for markdown data using markdown
        parent path and extension
    get_path_to_graph_data():
        Derive the path for svg data using svg parent path
        and extension
    """

    def __init__(self, repo_git_url, owner_id):

        self.url = repo_git_url

        owner, repo_name = get_repo_owner_and_name(self.url)

        self.repo_owner = owner

        #print(f"owner id: {owner_id}")
        #print(repo_git_url)

        #if owner_id is None:
        #    endpoint = f"{AUGUR_HOST}/repos"
        #else:
        #    endpoint = f"{AUGUR_HOST}/repo-groups/{owner_id}/repos"
        endpoint = f"{AUGUR_HOST}owner/{owner.lower()}/repo/{repo_name}"
        super().__init__(repo_name, endpoint)

        response = requests.get(
            self.augur_util_endpoint, timeout=TIMEOUT_IN_SECONDS)
        response_json = json.loads(response.text)

        print("--------")
        print(endpoint)
        print(response_json)
        print("--------")
        repo_val = response_json[0]

        # print(f"!!!{repo_val}")
        # for x in response_json:
        #    print(f"|{x['repo_name'].lower()}=={repo_name.lower()}|")
        # print(repo_val)
        self.repo_id = repo_val['repo_id']

        #print(f"repo id: {self.repo_id}")
        if owner_id is not None:
            self.repo_group_id = owner_id
        else:
            self.repo_group_id = repo_val['repo_group_id']


        # print(f"BEGIN: {today.strftime('%Y/%m/%d')}")
        # Prepare params
        self.needed_parameters = {
            "repo": self.name,
            "owner": self.repo_owner,
            "repo_id": self.repo_id,
            "repo_group_id": self.repo_group_id
        }

        self.needed_parameters.update(get_timebox_timestamps())

        # Prepare dict of metric data.
        self.metric_data = {
            "url": self.url,
            "owner": self.repo_owner,
            "name": self.name
        }

        self.previous_metric_data = {}

    def get_path_to_data(self, parent_path, extension):
        """
        Returns the path to store data given extension
        and parent path

        Args:
            parent_path: parent path to store data
            extension: File extension to use for data format

        Returns:
            String path to data.
        """
        data_path = os.path.join(
            parent_path, f"{self.repo_owner}/{self.name}")
        pathlib.Path(data_path).mkdir(parents=True, exist_ok=True)

        filename = f"{self.repo_owner}/{self.name}/{self.name}_data.{extension}"
        return os.path.join(parent_path, filename)

    def get_path_to_json_data(self):
        """
        Derive the path for json data using json parent
        path and extension

        Returns:
            String path to data.
        """
        return self.get_path_to_data(PATH_TO_METRICS_DATA, "json")

    def get_path_to_report_data(self):
        """
        Derive the path for markdown data using markdown
        parent path and extension

        Returns:
            String path to data.
        """
        return self.get_path_to_data(PATH_TO_REPORTS_DATA, "md")

    def get_path_to_resource_data(self, resource_name, fmt="png"):
        """
        Derive the path for resource data using svg
        parent path and extension

        Returns:
            String path to data.
        """

        id_str = f"{self.repo_owner}/{self.name}"
        data_path = os.path.join(PATH_TO_GRAPHS_DATA, id_str)
        pathlib.Path(data_path).mkdir(parents=True, exist_ok=True)
        fname = f"{self.repo_owner}/{self.name}/{resource_name}_{self.name}_data.{fmt}"
        return os.path.join(PATH_TO_GRAPHS_DATA, fname)

    def get_path_to_graph_data(self, graph_name):
        """
        Derive the path for graph data using svg
        parent path and extension

        Returns:
            String path to data.
        """

        return self.get_path_to_resource_data(graph_name, fmt="svg")


class GithubOrg(OSSEntity):
    """
    This class serves to manage the parameter and metric data of a GithubOrg.
    It stores parameter and metric data in two seperate dictionaries for easy JSON 
    conversion.

    GithubOrg's main purpose as a real python class is to encapsulate the mapping
    of db ids in CHAOSS/augur to the orgs we are trying to gather metrics for.

    ...

    Attributes
    ----------
    login : str
        login of the org
    repo_group_id: int
        id for the org that owns the repo in Augur

    Methods
    -------
    get_path_to_json_data():
        Derive the path for json data using json parent
        path and extension
    """

    def __init__(self, organization_login):
        self.login = organization_login

        print(f"AUGUR_HOST: {AUGUR_HOST}")
        super().__init__(self.login, f"{AUGUR_HOST}/repo-groups")

        try:
            response = requests.get(
                self.augur_util_endpoint, timeout=TIMEOUT_IN_SECONDS)
            response_dict = json.loads(response.text)
        except Exception:
            print("It looks like Augur is down! Not able to get Augur data!")
            response_dict = {}

        try:
            print(self.login)
            # Get the item in the list that matches the login of the github org
            gen = (item for item in response_dict if item["rg_name"].lower() == self.login.lower())
            group_id = next(gen, None)

            self.repo_group_id = group_id['repo_group_id']
        except Exception:
            self.repo_group_id = None

        self.needed_parameters = {
            "org_login": self.login,
            "repo_group_id": self.repo_group_id
        }
        print(self.needed_parameters)

        self.needed_parameters.update(get_timebox_timestamps())

        self.metric_data = {
            "login": self.login,
            "name": self.name,
            "rg_id": self.repo_group_id
        }

        self.previous_metric_data = {}

    def get_path_to_data(self, super_parent_path, extension):
        """
        Derive the path for data using parent
        path and extension

        Returns:
            String path to data.
        """
        parent_path = os.path.join(super_parent_path, f"{self.login}")
        pathlib.Path(parent_path).mkdir(parents=True, exist_ok=True)
        org_path = os.path.join(parent_path, f"{self.login}_data.{extension}")

        return org_path

    def get_path_to_json_data(self):
        """
        Derive the path for json data using json parent
        path and extension

        Returns:
            String path to data.
        """
        return self.get_path_to_data(PATH_TO_METRICS_DATA, "json")

    def get_path_to_report_data(self):
        """
        Derive the path for report data using parent
        path and extension

        Returns:
            String path to data.
        """
        return self.get_path_to_data(PATH_TO_REPORTS_DATA, "md")

    def get_path_to_resource_data(self, resource_name, fmt="png"):
        """
        Derive the path for graph data using parent
        path and extension

        Returns:
            String path to data.
        """

        parent_path = os.path.join(PATH_TO_GRAPHS_DATA, f"{self.login}")
        pathlib.Path(parent_path).mkdir(parents=True, exist_ok=True)
        fname = f"{self.login}_{resource_name}.{fmt}"
        org_path = os.path.join(parent_path, fname)

        return org_path

    def get_path_to_graph_data(self, chart_name):
        """
        Derive the path for graph data using parent
        path and extension

        Returns:
            String path to data.
        """

        return self.get_path_to_resource_data(chart_name, fmt="svg")
