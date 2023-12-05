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
        item['end_line'] = item.pop('endLine')
        item['start_line'] = item.pop('line')
    
    print(json.dumps(pylint_list))
