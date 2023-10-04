import os
import json
import requests
import datetime

from .constants import *

#Simple metric that can be represented by a count or value.
class SimpleMetric:
    #Url format should be in the vein of 'https://api.github.com/repos/{owner}/{repo}/issues?state=all'
    #then url.format(**data)
    def __init__(self,name,endpoint_url,return_value,params = None,token = None):
        self.name = name
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

#TODO: ask sean about committers endpoint and the data that it returns
#Think about version of simple metric that adds up all of the committers in the range

#TODO: Create class for graphql endpoint that returns a dict with all desired info

#Rest Api is worse than graphql for github.