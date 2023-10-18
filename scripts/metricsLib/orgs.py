import os
import json
import requests

from .constants import *

"""This class is used like a json object in that it acts as a dictionary to
store all metrics that also has a constructor and methods for encapsulation
and ease. 

GithubOrg's main purpose as a real python class is to encapsulate the mapping
of db ids in CHAOSS/augur to the orgs we are trying to gather metrics for.

Arguments:
    organization_login: Github org login i.e. 'DSACMS'
"""
class GithubOrg:
    def __init__(self, organization_login):
        self.login = organization_login
        self

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