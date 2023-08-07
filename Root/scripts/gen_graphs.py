from glob import glob
import heapq
from datetime import datetime
import json
import os
import re
from pathlib import Path
import pygal

PATH = "_dataVis"
os.chdir(PATH)
        
"""
    Input: project: repo directory 
           Weeks refers to the number of files we want.  weeks we wa
    Returns a list of file names listed from most recent to least recent.
"""
def main():
    # Get the latest two metrics for this project which are MIN_DIFFERENCE days apart
    treemap = pygal.Treemap()
    treemap.title = 'Binary TreeMap'

    for file in os.listdir():
        f = open(file)
        data = json.load(f)
        d = []
        for key in data:
            d.append(data[key])
        d.pop(0)
        words = file.split("-METRICS")
        treemap.add(words[0], d)
    
    treemap.render_to_file('output.svg')


if __name__ == "__main__":
    main()