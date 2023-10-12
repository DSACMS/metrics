import os
import json
import requests
import datetime
import re

from .constants import *


class Repository:
    def __init__(self,repo_git_url):
        
        self.url = repo_git_url

        owner, repo_name = self.get_repo_owner_and_name(self.url)

        self.repo_owner = owner
        self.name = repo_name

        #Get the repo_id and group_id.
        augur_util_endpoint = f"https://ai.chaoss.io/api/unstable/owner/{self.repo_owner}/repo/{self.name}"

        response = requests.post(augur_util_endpoint)
        response_json = json.loads(response.text)

        try:
            self.repo_id = response_json[0]["repo_id"]
            self.repo_group_id = response_json[0]["repo_group_id"]
        except Exception as e:
            self.repo_id = None
            self.repo_group_id = None

    def get_repo_owner_and_name(self,repo_http_url):
        """ Gets the owner and repo from a url.

            Args:
                url: Github url

            Returns:
                Tuple of owner and repo. Or a tuple of None and None if the url is invalid.
        """

        result = re.search(r"https?:\/\/github\.com\/([A-Za-z0-9 \- _]+)\/([A-Za-z0-9 \- _ \.]+)(.git)?\/?$", repo_http_url)

        if not result:
            return None, None

        capturing_groups = result.groups()


        owner = capturing_groups[0]
        repo = capturing_groups[1]

        return owner, repo

    def store_metrics(self,info):
        #Use all raw dict items as attributes of the repo.
        for field, metric in info.items():
            #self.field = metric
            #print(f"field: {field}, metric: {metric}")
            setattr(self,field,metric)
        