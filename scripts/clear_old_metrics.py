import os
import shutil

from metricsLib.constants import PATH_TO_METRICS_DATA


def clear_json_data():
    #os.mkdir(PATH_TO_METRICS_DATA,666)
    os.umask(0)
    shutil.rmtree(PATH_TO_METRICS_DATA)
    os.mkdir(PATH_TO_METRICS_DATA,0o777)


def clear_reports_data():
    pass

def clear_graphs_data():
    pass


def clear_all_data():
    clear_json_data()
    clear_reports_data()
    clear_graphs_data()