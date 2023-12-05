import pytest
import json
from metricsLib import metrics_data_structures
import subprocess

def test_base_metric():
    raise NotImplementedError

def run_pylint():
    pylint_out = subprocess.run(['pylint', '--output-format=json', "--init-hook=\"import sys; sys.path.append('scripts/')\"", "scripts/*"],stdout = subprocess.PIPE,check=False)

    pylint_list = json.loads(pylint_out.stdout)

    for item in pylint_list:
        item['annotation_level'] = item.pop('type')

        if item['annotation_level'] == "convention":
            item['annotation_level'] = 'notice'
        elif item['annotation_level'] == "refactor":
            item['annotation_level'] = 'warning'
        item['end_line'] = item.pop('endLine')
        if item['end_line'] is None:
            item['end_line'] = item['line']

        item['start_line'] = item.pop('line')
        item['start_column'] = item.pop('column')
        item['end_column'] = item.pop('endColumn')
        if item['end_column'] is None:
            item['end_column'] = item['start_column']
        item['title'] = item.pop('symbol')

        item.pop('module')
        item.pop('obj')
        item.pop('message-id')
    
    print(json.dumps(pylint_list, indent=2))
