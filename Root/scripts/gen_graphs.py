from glob import glob
import json
import os
import re
import pygal

PATH = "_dataVis"
os.chdir(PATH)
        
def genOverview():
    treemap = pygal.Treemap()
    treemap.title = 'DSACMS Project Overview Binary TreeMap'

    for file in os.listdir():
        try:
            f = open(file)
            data = json.load(f)
            d = []
            for key in data:
                d.append(data[key])
            d.pop(0)
            words = file.split("-METRICS")

            treemap.add(words[0], d)
        except:
            invalid = []
            invalid.append(file)
    
    treemap.render_to_file('overview.svg')

def repoSpecific():
    treemap = pygal.Treemap()

    for file in os.listdir():
        try:
            f = open(file)
            data = json.load(f)
            del data["datetime"]

            for key in data:
                if(data[key] != 0):
                    treemap.add(key, data[key])
            
            words = file.split("-METRICS")
            treemap.title = words[0] + "Binary TreeMap"
            treemap.render_to_file(words[0] + "-graph.svg")

        except:
            invalid = []
            invalid.append(file)

        treemap.render_to_file('overview.svg')

def main():
    genOverview()
    repoSpecific()


if __name__ == "__main__":
    main()