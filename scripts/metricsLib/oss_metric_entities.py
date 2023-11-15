import re
import json
import os
import pathlib
import requests
from metricsLib.constants import PATH_TO_METRICS_DATA, PATH_TO_REPORTS_DATA


class OSSEntity:
    def __init__(self,name, augur_endpoint):
        self.name = name
        self.augur_util_endpoint = augur_endpoint

        self.needed_parameters = {}
        self.metric_data = {}
        self.previous_metric_data = {}
    
    def store_metrics(self, info):
        self.metric_data.update(info)
    
    def get_parameters_for_metric(self,metric):
        params = {}

        #get the parameter for this metric
        for param in metric.needed_parameters:
            params[param] = self.needed_parameters[param]
        
        return params
    
    def apply_metric_and_store_data(self,metric):
        params = self.get_parameters_for_metric(metric)

        self.store_metrics(metric.get_values(params))

class Repository(OSSEntity):
    """
    This class serves to manage the parameter and metric data of a Repository.
    It stores parameter and metric data in two seperate dictionaries for easy JSON 
    conversion.
    
    Repository's main purpose as a real python class is to encapsulate the mapping
    of the db ids in augur to the repos we are trying to gather metrics for.
    
    Arguments:
        repo_git_url: Github url
    
    """
    def __init__(self, repo_git_url):
        
        self.url = repo_git_url

        owner, repo_name = self.get_repo_owner_and_name(self.url)

        self.repo_owner = owner

        super().__init__(repo_name,f"https://ai.chaoss.io/api/unstable/owner/{self.repo_owner}/repo/{repo_name}")

        response = requests.post(self.augur_util_endpoint)
        response_json = json.loads(response.text)

        try:
            self.repo_id = response_json[0]["repo_id"]
            self.repo_group_id = response_json[0]["repo_group_id"]
        except Exception as e:
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
        parentPath = os.path.join(parent_path, f"{self.repo_owner}/{self.name}")
        pathlib.Path(parentPath).mkdir(parents=True, exist_ok=True)

        return os.path.join(parent_path, f"{self.repo_owner}/{self.name}/{self.name}_data.{extension}")

    def get_path_to_json_data(self):
        return self.get_path_to_data(PATH_TO_METRICS_DATA,"json")
    
    def get_path_to_report_data(self):
        return self.get_path_to_data(PATH_TO_REPORTS_DATA,"md")




class GithubOrg(OSSEntity):
    """
    This class serves to manage the parameter and metric data of a GithubOrg.
    It stores parameter and metric data in two seperate dictionaries for easy JSON 
    conversion.

    GithubOrg's main purpose as a real python class is to encapsulate the mapping
    of db ids in CHAOSS/augur to the orgs we are trying to gather metrics for.

    Arguments:
        organization_login: Github org login i.e. 'DSACMS'
    """
    def __init__(self, organization_login):
        self.login = organization_login

        super().__init__(self.login, "https://ai.chaoss.io/api/unstable/repo-groups")
        response = requests.get(self.augur_util_endpoint)
        response_dict = json.loads(response.text)

        try:
            #Get the item in the list that matches the login of the github org
            group_id = next((item for item in response_dict if item["rg_name"] == self.login),None)
            
            self.repo_group_id = group_id
        
        except ValueError as e:
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

    def store_metrics(self,info):
        self.metric_data.update(info)
    
    def get_path_to_json_data(self):
        parentPath = os.path.join(PATH_TO_METRICS_DATA, f"{self.login}")
        pathlib.Path(parentPath).mkdir(parents=True, exist_ok=True)
        orgPath = os.path.join(parentPath, f"{self.login}_data.json")

        return orgPath