import pytest
import json
from metricsLib import metrics_data_structures
import subprocess

def test_base_metric():
    raise NotImplementedError

def run_pylint():
    #Run pylint command and parse json
    pylint_out = subprocess.run(['pylint', '--output-format=json', "--init-hook=\"import sys; sys.path.append('scripts/')\"", "scripts/*"],stdout = subprocess.PIPE,check=False)

    pylint_list = json.loads(pylint_out.stdout)


    #Parse pylint format into GitHub Checks Annotation format
    for item in pylint_list:
        #Rename error type to annotation_level
        item['annotation_level'] = item.pop('type')

        #translate pylint terms to github terms
        if item['annotation_level'] == "convention":
            item['annotation_level'] = 'notice'
        elif item['annotation_level'] == "refactor":
            item['annotation_level'] = 'warning'
        
        #if end fields are empty, make them the same as the start
        item['end_line'] = item.pop('endLine')
        if item['end_line'] is None:
            item['end_line'] = item['line']

        item['start_line'] = item.pop('line')
        item['start_column'] = item.pop('column')
        item['end_column'] = item.pop('endColumn')
        if item['end_column'] is None:
            item['end_column'] = item['start_column']
        item['title'] = item.pop('symbol')

        #Don't include columns if annotation spans multiple lines
        if item['start_line'] != item['end_line']:
            item.pop('start_column')
            item.pop('end_column')
        item.pop('module')
        item.pop('obj')
        item.pop('message-id')
    
    to_return = pylint_list[:50]#json.dumps(pylint_list, indent=2)
    #Print max of 50 terms since thats the max for GitHub
    print(json.dumps(to_return, indent=2))
