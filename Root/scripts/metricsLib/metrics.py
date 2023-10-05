import os
import json
import requests
import datetime
from functools import reduce
import operator
from .constants import *

#Simple metric that can be represented by a count or value.
class SimpleMetric:
    #Url format should be in the vein of 'https://api.github.com/repos/{owner}/{repo}/issues?state=all'
    #then url.format(**data)
    def __init__(self,name,endpoint_url,return_values,params = None,token = None):
        self.name = name
        self.return_values = return_values

        if params:
            self.url = endpoint_url.format(**params)
        else:
            self.url = endpoint_url
        

        if token:
            self.headers = {"Authorization": f"bearer {TOKEN}"}
        else:
            self.headers = None
    
    def get_values(self):
        if self.headers:
            response = requests.post(self.url,self.headers)
        else:
            resposnse = requests.post(self.url)
        
        response_json = json.loads(response.txt)
        toReturn = {}

        for val in self.return_values:
            toReturn[val] = response_json[val]
        
        return toReturn

#TODO: ask sean about committers endpoint and the data that it returns
#Think about version of simple metric that adds up all of the committers in the range

#TODO: Create class for graphql endpoint that returns a dict with all desired info

#Rest Api is worse than graphql for github.

class GraphqlMetric:
    #Return value is a dict of lists of strings that match to the keys of the dict.
    """EX:
    {
        commits_count: ["defaultBranchRef","commits","history","totalCount"]
    }
    """
    def __init__(self,name,query,return_values, params = None, token = None, url = "https://api.github.com/graphql"):
        super().__init__(name,url,return_values,params = None, token = token)
        self.params = params
        self.query = query
    
    def get_values(self):
        json_dict = {
            'query' : self.query
        }

        #If there are bind variables bind them to the query here.
        if self.params:

            json_dict['variables'] = self.params
            json_dict['variables'] = json_dict['variables']
            #print(json_dict['variables'])
        
        if self.headers:
            response = requests.post(self.url,headers=self.headers,json=json_dict)
        else:
            response = requests.post(self.url,json=json_dict)
        
        response_json = json.loads(response.txt)

        toReturn = {}

        for val, keySequence in self.params.items():
            # Extract the nested data and store it in a flat dict to return to the user
            toReturn[val] = reduce(operator.getitem,keySequence,response_json)
        
        return toReturn


