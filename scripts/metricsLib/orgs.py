import os
import json
import requests

from .constants import *


class GithubOrg:
    def __init__(self, organization_login):
        self.login = organization_login

        #Get the group id from augur
        augur_util_endpoint = f"https://ai.chaoss.io/api/unstable/owner/repo_groups"

        response = requests.post(augur_util_endpoint)

        response = requests.post(augur_util_endpoint)
        response_dict = json.loads(response.text)

        try:
            for group in response_dict:
                if group["rg_name"] == self.login:
                    self.repo_group_id = group["repo_group_id"]
                    break
        
        except Exception as e:
            self.repo_group_id = None

    def store_metrics(self,info):
        for field,metric in info.items():
            setattr(self,field,metric)