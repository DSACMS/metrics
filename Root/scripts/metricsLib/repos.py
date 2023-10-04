import os
import json
import requests
import datetime

from .constants import *

#Simple metric that can be represented by a count or value.
class SimpleMetric:
    #Url format should be in the vein of 'https://api.github.com/repos/{owner}/{repo}/issues?state=all'
    #then url.format(**data)
    def __init__(self,endpoint_url,return_value,params = None,token = None):
        self.return_value = return_value

        self.url = endpoint_url.format(**params)
        

        if token:
            self.headers = {"Authorization": f"bearer {TOKEN}"}
        else:
            self.headers = None
    
    def get_value(self):
        if self.headers:
            response = requests.post(self.url,self.headers)
        else:
            resposnse = requests.post(self.url)
        
        return json.loads(response.txt)[self.return_value]



class Repository:
    def __init__(self,repo_git_url,basic_info, advanced_info):
        
        self.name = repo_git

        #Use all raw dict items as attributes of the repo.
        for field, metric in basic_info.items():
            #self.field = metric
            setattr(self,field,metric)
        
        for field, metric in advanced_info.items():
            setattr(self,field,metric)