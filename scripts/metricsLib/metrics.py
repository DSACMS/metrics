import os
import json
import requests
from requests import exceptions
import datetime
from functools import reduce
import operator

# Simple metric that can be represented by a count or value.


class SimpleMetric:
    # Url format should be in the vein of 'https://api.github.com/repos/{owner}/{repo}/issues?state=all'
    # then url.format(**data)
    def __init__(self, name, needed_parameters, endpoint_url, return_values, token=None, method = 'GET'):
        self.name = name
        self.return_values = return_values
        self.url = endpoint_url

        self.needed_parameters = needed_parameters
        self.method = method
        if token:
            self.headers = {"Authorization": f"bearer {token}"}
        else:
            self.headers = None

    def hit_metric(self,params=None):
        requestParams = params
        if params and len(params) > 0 and self.method == 'GET':
            self.url = self.url.format(**params)
            requestParams = None

        if self.headers:
            response = requests.request(self.method,self.url,params=requestParams,headers=self.headers)
        else:
            response = requests.request(self.method,self.url,params=requestParams)

        response_json = json.loads(response.text)

        return response_json

    def get_values(self, params=None):
        
        metric_json = self.hit_metric(params=params)
        toReturn = {}

        for returnLabel, apiLabel in self.return_values:
            toReturn[returnLabel] = metric_json[apiLabel]

        return toReturn

# TODO: ask sean about committers endpoint and the data that it returns
# Think about version of simple metric that adds up all of the committers in the range

# TODO: Create class for graphql endpoint that returns a dict with all desired info

# Rest Api is worse than graphql for github.


class GraphqlMetric(SimpleMetric):
    # Return value is a dict of lists of strings that match to the keys of the dict.
    """EX:
    {
        commits_count: ["defaultBranchRef","commits","history","totalCount"]
    }
    """

    def __init__(self, name, needed_parameters, query, return_values, token=None, url="https://api.github.com/graphql"):
        super().__init__(name, needed_parameters, url, return_values, token=token)
        self.query = query

    def get_values(self, params=None):
        json_dict = {
            'query': self.query
        }

        # If there are bind variables bind them to the query here.
        if params:

            json_dict['variables'] = params
            json_dict['variables'] = json_dict['variables']
            # print(json_dict['variables'])

        if self.headers:
            response = requests.post(
                self.url, headers=self.headers, json=json_dict)
        else:
            response = requests.post(self.url, json=json_dict)

        response_json = json.loads(response.text)

        toReturn = {}

        print(response_json)
        if "data" not in response_json.keys():
            if "message" not in response_json.keys():
                raise requests.exceptions.InvalidJSONError(
                    response_json['errors'][0]['message'])
            else:
                raise requests.exceptions.InvalidJSONError(
                    response_json['message'])

        for val, keySequence in self.return_values.items():
            # Extract the nested data and store it in a flat dict to return to the user
            toReturn[val] = reduce(
                operator.getitem, keySequence, response_json)

        return toReturn

# A metric that returns a single value from a list of values
# Used for endpoints that return an iterable.


class RangeMetric(SimpleMetric):
    def __init__(self, name, needed_parameters, endpoint_url, return_values, token=None, method = 'GET'):
        super().__init__(name, needed_parameters, endpoint_url, return_values, token=token,method=method)

    def get_values(self, params=None):
        metric_json = self.hit_metric(params=params)

        toReturn = {}

        for returnLabel, apiLabel in self.return_values:
            toReturn[returnLabel] = sum([item[apiLabel]
                                        for item in metric_json])

        return toReturn

class ListMetric(SimpleMetric):
    def __init__(self, name, needed_parameters, endpoint_url, return_values, token=None, method = 'GET'):
        super().__init__(name, needed_parameters, endpoint_url, return_values, token=token,method=method)

    def get_values(self, params=None):
        metric_json = self.hit_metric(params=params)

        toReturn = {}

        for returnLabel, apiLabel in self.return_values:
            toReturn[returnLabel] = [item[apiLabel]
                                        for item in metric_json]

        return toReturn

class CustomMetric(SimpleMetric):
    def __init__(self, name, needed_parameters, endpoint_url,func, token=None, method = 'GET'):
        super().__init__(name, needed_parameters, endpoint_url, None, token=token,method=method)
        self.parse_function = func
    
    def get_values(self,params=None):
        metric_json = self.hit_metric(params=params)

        return self.parse_function(metric_json=metric_json,return_values=self.return_values)



#Custom parse functions
def parse_commits_by_month(*args, **kwargs):

    return_values = kwargs['return_values']
    metric_json = kwargs['metric_json']

    commits_by_month = {}

    for commit in metric_json:
        #Get the month and year of the commit
        datetime_str = commit['commit']['author']['date']
        date_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ')
        month = f"{date_obj.year}/{date_obj.month}"
        #print(month)

        #Add up the commits for each month and return
        if commits_by_month.get(month):
            commits_by_month[month] += 1
        else:
            commits_by_month[month] = 1

    return {"commits_by_month": commits_by_month}
