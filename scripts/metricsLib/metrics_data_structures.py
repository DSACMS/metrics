"""
Module to define classes of metrics that gather data given parameters
"""
import json
import datetime
from functools import reduce
import operator
import requests
from metricsLib.constants import TIMEOUT_IN_SECONDS, GH_GQL_ENDPOINT

# Simple metric that can be represented by a count or value.


class BaseMetric:
    """
    This serves as the base class to define a metric.
    A metric accepts parameters and returns data with the
    get_values method.

    Url format should be in the vein of
    'https://api.github.com/repos/{owner}/{repo}/issues?state=all'
    then url.format(**data)

    ...

    Attributes
    ----------
    name : str
        name of the metric
    needed_parameters : dict
        Dictionary holding parameters that are needed to hit a metric
    endpoint_url : str
        Api endpoint to use to get information
    return_values : dict
        Mapping dict to define the json info to store and the format to store it in
    token: str
        Api token to use for auth
    method: str
        Request method, GET or POST

    Methods
    -------
    hit_metric(params={}):
        Format url with parameters and fetch the data from it
    get_values(params={}):
        Fetch data from url using parameters and format the data
        before returning it.
    """

    def __init__(self, name, needed_params, endpoint_url, return_values, token=None, method='GET'):
        self.name = name
        self.return_values = return_values
        self.url = endpoint_url

        self.needed_parameters = needed_params
        self.method = method
        if token:
            self.headers = {"Authorization": f"bearer {token}"}
        else:
            self.headers = None

    def hit_metric(self, params=None):
        """
        Format the url with parameters and fetch the data from it.

        Args:
            params: dict
                Dictionary of parameters to apply to endpoint.
        """
        request_params = params
        if params and len(params) > 0 and self.method == 'GET':
            self.url = self.url.format(**params)
            request_params = None

        if self.headers:
            _args_ = (self.method, self.url)
            _kwargs_ = {
                "params": request_params,
                "headers": self.headers,
                "timeout": TIMEOUT_IN_SECONDS
            }
            response = requests.request(*_args_,**_kwargs_ )
        else:
            response = requests.request(
                self.method, self.url, params=request_params, timeout=TIMEOUT_IN_SECONDS)

        response_json = json.loads(response.text)

        return response_json

    def get_values(self, params=None):
        """
        Fetch data from url using parameters and format the data
        before returning it.

        Args:
            params: dict
                Dictionary of parameters to apply to endpoint.
        """
        metric_json = self.hit_metric(params=params)
        to_return = {}

        for return_label, api_label in self.return_values:
            to_return[return_label] = metric_json[api_label]

        return to_return


class GraphQLMetric(BaseMetric):
    """
    Class to define a metric that gets data from a graphql endpoint.

    The format of the return_values var also uses lists to extract the 
    desired value.
    EX:
    {
        commits_count: ["defaultBranchRef","commits","history","totalCount"]
    }

    ...

    Attributes
    ----------
    query : str
        String that corresponds to the relevant graphql query

    Methods
    -------
    get_values(params={}):
        Fetch data from url using parameters and format the data
        before returning it.
    """
    # Return value is a dict of lists of strings that match to the keys of the dict.

    def __init__(self, name, needed_params, query, return_vals, token=None, url=GH_GQL_ENDPOINT):
        super().__init__(name, needed_params, url, return_vals, token=token)
        self.query = query

    def get_values(self, params=None):
        """
        Fetch data from url using parameters and format the data
        before returning it.

        Args:
            params: dict
                Dictionary of parameters to apply to endpoint.
        """
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
                self.url, headers=self.headers, json=json_dict, timeout=TIMEOUT_IN_SECONDS)
        else:
            response = requests.post(
                self.url, json=json_dict, timeout=TIMEOUT_IN_SECONDS)

        response_json = json.loads(response.text)

        to_return = {}

        if "data" not in response_json.keys():
            if "message" not in response_json.keys():
                raise requests.exceptions.InvalidJSONError(
                    response_json['errors'][0]['message'])
            else:
                raise requests.exceptions.InvalidJSONError(
                    response_json['message'])

        print(f"Response_JSON: {response_json}")
        print(f"Return values: {self.return_values}")
        for val, key_sequence in self.return_values.items():
            # Extract the nested data and store it in a flat dict to return to the user
            to_return[val] = reduce(
                operator.getitem, key_sequence, response_json)

        return to_return

class SumMetric(BaseMetric):
    """
    Class to define a metric that returns a returned list 
    from an endpoint
    ...

    Methods
    -------
    get_values(params={}):
        Fetch data from url using parameters, format and sum the data
        before returning it.
    """
    def __init__(self, name, needed_params, endpoint_url,return_val, token=None, method='GET'):
        super().__init__(name, needed_params, endpoint_url,
                         return_val, token=token, method=method)

    def get_values(self, params=None):
        return {self.return_values: len(self.hit_metric(params=params))}



class ListMetric(BaseMetric):
    """
    Class to define a metric that returns a returned list 
    from an endpoint
    ...

    Methods
    -------
    get_values(params={}):
        Fetch data from url using parameters, format and sum the data
        before returning it.
    """
    def __init__(self, name, needed_params, endpoint_url, return_values, token=None, method='GET'):
        super().__init__(name, needed_params, endpoint_url,
                         return_values, token=token, method=method)

    def get_values(self, params=None):
        metric_json = self.hit_metric(params=params)

        to_return = {}

        for return_label, api_label in self.return_values:
            to_return[return_label] = [item[api_label]
                                     for item in metric_json]

        return to_return




class RangeMetric(ListMetric):
    """
    Class to define a metric that returns the sum of a returned list 
    from an endpoint
    ...

    Methods
    -------
    get_values(params={}):
        Fetch data from url using parameters, format and sum the data
        before returning it.
    """

    def __init__(self, name, needed_params, endpoint_url, return_values, token=None, method='GET'):
        super().__init__(name, needed_params, endpoint_url,
                         return_values, token=token, method=method)

    def get_values(self, params=None):
        """
        Fetch data from url using parameters and format the data
        before returning it.

        Sums up the result lists of ListMetric's get_values method
        and returns

        Args:
            params: dict
                Dictionary of parameters to apply to endpoint.
        
        Returns:
            Dictionary containing the desired values in the requested mapping
        """

        return_dict = super().get_values(params=params)#self.hit_metric(params=params)

        to_return = {}

        for return_label, _ in return_dict.items():
            to_return[return_label] = sum(return_dict[return_label])

        return to_return



class CustomMetric(BaseMetric):
    """
    Class to define a metric that is parsed in a custom way defined
    by a function that takes the metric_json returned by the endpoint as
    an argument. 

    ...

    Methods
    -------
    get_values(params={}):
        Fetch data from url using parameters, format and sum the data
        before returning it. Using the custom parsing function passed in.
    """
    def __init__(self, name, needed_parameters, endpoint_url, func, token=None, method='GET'):
        super().__init__(name, needed_parameters,
                         endpoint_url, None, token=token, method=method)
        self.parse_function = func

    def get_values(self, params=None):
        metric_json = self.hit_metric(params=params)

        return self.parse_function(metric_json=metric_json, return_values=self.return_values)


# Custom parse functions
def parse_commits_by_month(**kwargs):
    """
    Parse the raw json returned by the commits endpoint into
    a dictionary that groups commit counts for a repository by
    month.

    Args:
        kwargs: dict
            Keyword arguments used by the parsing function,
    
    Returns:
        Dictionary containing the desired values in the requested mapping
    """

    metric_json = kwargs['metric_json']

    commits_by_month = {}

    # print(metric_json)
    for commit in metric_json:
        # Get the month and year of the commit
        datetime_str = commit['commit']['author']['date']
        date_obj = datetime.datetime.strptime(
            datetime_str, '%Y-%m-%dT%H:%M:%SZ')
        month = f"{date_obj.year}/{date_obj.month}"
        # print(month)

        # Add up the commits for each month and return
        if commits_by_month.get(month):
            commits_by_month[month] += 1
        else:
            commits_by_month[month] = 1

    return {"commits_by_month": commits_by_month}
