"""
Module that defines objects to model oss metric entities. i.e. objects that
store data and have methods concerning the concept of entities that we would
like to gather metric data for. 
"""
import re
import json
import os
import subprocess
import datetime
import pathlib
import requests
from metricsLib.constants import PATH_TO_METRICS_DATA, PATH_TO_REPORTS_DATA, AUGUR_HOST
from metricsLib.constants import TIMEOUT_IN_SECONDS, PATH_TO_GRAPHS_DATA


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

    def apply_metric_and_store_data(self, metric):
        """
        Pass needed parameters into a metric, hit the metric, and then store the result in
        the metric_data dict.

        Args:
            metric: BaseMetric
        """
        params = self.get_parameters_for_metric(metric)

        self.store_metrics(metric.get_values(params))

    def get_commit_hashes_by_date(self):
        commit_hashes_by_date = {}

        #command to get a list of commit hashes that were made by Github Actions user.
        get_action_commit_history = subprocess.Popen(["git log "
            " --pretty=format:\"%h%x09%an%x09%ad%x09%s\""
            " | grep 'GitHub Actions' |  awk '{print $1;}'"] ,
            stdout=subprocess.PIPE, shell=True)
        
        #Read result of command
        action_commit_history = get_action_commit_history.stdout.read().decode("utf-8").split('\n')

        #Command to get a list of dates for those same commit hashes in the corresponding order
        get_action_commit_history_timestamps = subprocess.Popen(["git log "
            " --pretty=format:\"%h%x09%an%x09%ad%x09%s\""
            " | grep 'GitHub Actions' |  "
            "awk {'print $4 \" \" $5 \" \" $6 \" \" $7 \" \" $8 \" \" $9'}"] ,
            stdout=subprocess.PIPE, shell=True)
        
        action_commit_history_timestamps = get_action_commit_history_timestamps.stdout.read().decode("utf-8").split('\n')

        for commit_index, _ in enumerate(action_commit_history):
            try:
                #Parse data into string
                date_obj = datetime.datetime.strptime(action_commit_history_timestamps[commit_index], '%a %b %d %H:%M:%S %Y %z')
                date = f"{date_obj.year}/{date_obj.month}/{date_obj.day}"

                commit_hashes_by_date[date] = action_commit_history[commit_index]
            except ValueError:
                continue
        
        return commit_hashes_by_date

        
    
    def get_metrics_at_given_date(self, given_date):
        commits_by_date = self.get_commit_hashes_by_date()

        


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
    get_repo_owner_and_name(repo_http_url=""):
        Returns the repo owner and name from the url
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

    def __init__(self, repo_git_url):

        self.url = repo_git_url

        owner, repo_name = self.get_repo_owner_and_name(self.url)

        self.repo_owner = owner

        endpoint = f"{AUGUR_HOST}/owner/{self.repo_owner}/repo/{repo_name}"
        super().__init__(repo_name,endpoint)

        response = requests.post(
            self.augur_util_endpoint, timeout=TIMEOUT_IN_SECONDS)
        response_json = json.loads(response.text)

        try:
            self.repo_id = response_json[0]["repo_id"]
            self.repo_group_id = response_json[0]["repo_group_id"]
        except Exception:
            self.repo_id = None
            self.repo_group_id = None

        # Prepare params
        self.needed_parameters = {
            "repo": self.name,
            "owner": self.repo_owner,
            "repo_id": self.repo_id,
            "repo_group_id": self.repo_group_id
        }

        # Prepare dict of metric data.
        self.metric_data = {
            "url": self.url,
            "owner": self.repo_owner,
            "name": self.name
        }

        self.previous_metric_data = {}

    def get_repo_owner_and_name(self, repo_http_url):
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

    def get_path_to_graph_data(self, graph_name):
        """
        Derive the path for graph data using svg
        parent path and extension

        Returns:
            String path to data.
        """
        id_str = f"{self.repo_owner}/{self.name}"
        data_path = os.path.join(PATH_TO_GRAPHS_DATA, id_str)
        pathlib.Path(data_path).mkdir(parents=True, exist_ok=True)

        fname = f"{self.repo_owner}/{self.name}/{graph_name}_{self.name}_data.svg"
        return os.path.join(PATH_TO_GRAPHS_DATA, fname)


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

        super().__init__(self.login, f"{AUGUR_HOST}/repo-groups")
        response = requests.get(self.augur_util_endpoint,timeout=TIMEOUT_IN_SECONDS)
        response_dict = json.loads(response.text)

        try:
            # Get the item in the list that matches the login of the github org
            group_id = next(
                (item for item in response_dict if item["rg_name"] == self.login), None)

            self.repo_group_id = group_id

        except ValueError:
            self.repo_group_id = None

        self.needed_parameters = {
            "org_login": self.login,
            "repo_group_id": self.repo_group_id
        }

        self.metric_data = {
            "login": self.login,
            "rg_id": self.repo_group_id
        }

        self.previous_metric_data = {}

    def get_path_to_json_data(self):
        """
        Derive the path for json data using json parent
        path and extension

        Returns:
            String path to data.
        """
        parent_path = os.path.join(PATH_TO_METRICS_DATA, f"{self.login}")
        pathlib.Path(parent_path).mkdir(parents=True, exist_ok=True)
        org_path = os.path.join(parent_path, f"{self.login}_data.json")

        return org_path
