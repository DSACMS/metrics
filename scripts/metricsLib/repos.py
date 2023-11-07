import re
import json
import os
import requests
import pathlib
from metricsLib.constants import PATH_TO_METRICS_DATA, PATH_TO_REPORTS_DATA
#// TODO: ADD NAME AND DESC.



class Repository:
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
        self.name = repo_name

        # Get the repo_id and group_id.
        augur_util_endpoint = f"https://ai.chaoss.io/api/unstable/owner/{self.repo_owner}/repo/{self.name}"

        response = requests.post(augur_util_endpoint)
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

    def store_metrics(self, info):
        self.metric_data.update(info)

    def get_path_to_data(self,parent_path,extension):
        parentPath = os.path.join(parent_path, f"{self.repo_owner}/{self.name}")
        pathlib.Path(parentPath).mkdir(parents=True, exist_ok=True)

        return os.path.join(parent_path, f"{self.repo_owner}/{self.name}/{self.name}_data.{extension}")

    def get_path_to_json_data(self):
        return self.get_path_to_data(PATH_TO_METRICS_DATA,"json")
    
    def get_path_to_report_data(self):
        return self.get_path_to_data(PATH_TO_REPORTS_DATA,"md")