import os
import json
import requests
import pathlib
from metricsLib.constants import PATH_TO_METRICS_DATA, AUGUR_HOST

"""
This class serves to manage the parameter and metric data of a GithubOrg.
It stores parameter and metric data in two seperate dictionaries for easy JSON 
conversion.

GithubOrg's main purpose as a real python class is to encapsulate the mapping
of db ids in CHAOSS/augur to the orgs we are trying to gather metrics for.

Arguments:
    organization_login: Github org login i.e. 'DSACMS'
"""
class GithubOrg:
    def __init__(self, organization_login):
        self.login = organization_login

        #Get the group id from augur
        augur_util_endpoint = f"{AUGUR_HOST}/repo-groups"

        response = requests.get(augur_util_endpoint)
        response_dict = json.loads(response.text)

        try:
            #Get the item in the list that matches the login of the github org
            group_id = next((item for item in response_dict if item["rg_name"] == self.login),None)
            
            self.repo_group_id = group_id
        
        except ValueError as e:
            self.repo_group_id = None
        

        self.needed_params = {
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