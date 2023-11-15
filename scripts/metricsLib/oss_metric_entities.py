"""
Module that defines objects to model oss metric entities. i.e. objects that
store data and have methods concerning the concept of entities that we would
like to gather metric data for. 
"""
import re
import json
import os
import pathlib
import requests
from metricsLib.constants import PATH_TO_METRICS_DATA, PATH_TO_REPORTS_DATA, TIMEOUT_IN_SECONDS


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
    def __init__(self,name, augur_endpoint):
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
    
    #TODO: should this logic be moved to the hit_metric method?
    def get_parameters_for_metric(self,metric):
        """
        Get a sub directory of the needed_parameters dict that only holds the parameters
        needed by a metric

        Args:
            metric: SimpleMetric
        
        Returns:
            Dictionary containing the parameters needed for the given metric
        """
        params = {}

        #get the parameter for this metric
        for param in metric.needed_parameters:
            params[param] = self.needed_parameters[param]
        
        return params
    
    def apply_metric_and_store_data(self,metric):
        """
        Pass needed parameters into a metric, hit the metric, and then store the result in
        the metric_data dict.

        Args:
            metric: SimpleMetric
        """
        params = self.get_parameters_for_metric(metric)

        self.store_metrics(metric.get_values(params))

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
    """
    def __init__(self, repo_git_url):
        
        self.url = repo_git_url

        owner, repo_name = self.get_repo_owner_and_name(self.url)

        self.repo_owner = owner

        super().__init__(repo_name,f"https://ai.chaoss.io/api/unstable/owner/{self.repo_owner}/repo/{repo_name}")

        response = requests.post(self.augur_util_endpoint,timeout=TIMEOUT_IN_SECONDS)
        response_json = json.loads(response.text)

        try:
            self.repo_id = response_json[0]["repo_id"]
            self.repo_group_id = response_json[0]["repo_group_id"]
        except Exception:
            self.repo_id = None
            self.repo_group_id = None
        

        #Prepare params
        self.needed_parameters = {
            "repo": self.name,
            "owner": self.repo_owner,
            "repo_id": self.repo_id,
            "repo_group_id": self.repo_group_id
        }

        #Prepare dict of metric data.
        self.metric_data = {
            "url" : self.url,
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

        result = re.search(
            r"https?:\/\/github\.com\/([A-Za-z0-9 \- _]+)\/([A-Za-z0-9 \- _ \.]+)(.git)?\/?$", repo_http_url)

        if not result:
            return None, None

        capturing_groups = result.groups()

        owner = capturing_groups[0]
        repo = capturing_groups[1]

        return owner, repo

    def get_path_to_data(self,parent_path,extension):
        """
        Returns the path to store data given extension
        and parent path

        Args:
            parent_path: parent path to store data
            extension: File extension to use for data format

        Returns:
            String path to data.
        """
        parentPath = os.path.join(parent_path, f"{self.repo_owner}/{self.name}")
        pathlib.Path(parentPath).mkdir(parents=True, exist_ok=True)

        return os.path.join(parent_path, f"{self.repo_owner}/{self.name}/{self.name}_data.{extension}")

    def get_path_to_json_data(self):
        """
        Derive the path for json data using json parent
        path and extension

        Returns:
            String path to data.
        """
        return self.get_path_to_data(PATH_TO_METRICS_DATA,"json")
    
    def get_path_to_report_data(self):
        """
        Derive the path for markdown data using markdown
        parent path and extension

        Returns:
            String path to data.
        """
        return self.get_path_to_data(PATH_TO_REPORTS_DATA,"md")




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

        super().__init__(self.login, "https://ai.chaoss.io/api/unstable/repo-groups")
        response = requests.get(self.augur_util_endpoint,timeout=TIMEOUT_IN_SECONDS)
        response_dict = json.loads(response.text)

        try:
            #Get the item in the list that matches the login of the github org
            group_id = next((item for item in response_dict if item["rg_name"] == self.login),None)
            
            self.repo_group_id = group_id
        
        except ValueError:
            self.repo_group_id = None
        

        self.needed_parameters = {
            "org_login" : self.login,
            "repo_group_id": self.repo_group_id
        }

        self.metric_data = {
            "login" : self.login,
            "rg_id" : self.repo_group_id
        }

        self.previous_metric_data = {}

    def get_path_to_json_data(self):
        """
        Derive the path for json data using json parent
        path and extension

        Returns:
            String path to data.
        """
        parentPath = os.path.join(PATH_TO_METRICS_DATA, f"{self.login}")
        pathlib.Path(parentPath).mkdir(parents=True, exist_ok=True)
        orgPath = os.path.join(parentPath, f"{self.login}_data.json")

        return orgPath