import os
import json
import requests
import datetime

from .constants import *


class Repository:
    def __init__(self,repo_git_url,basic_info, advanced_info):
        
        self.name = repo_git_url

        #Use all raw dict items as attributes of the repo.
        for field, metric in basic_info.items():
            #self.field = metric
            #print(f"field: {field}, metric: {metric}")
            setattr(self,field,metric)
        
        for field, metric in advanced_info.items():
            setattr(self,field,metric)