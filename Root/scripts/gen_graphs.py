from glob import glob
import json
import os
import re
import pygal

PATH = "_dataVis"
os.chdir(PATH)


#TODO: Just get these metrics from augur instead of storing them in json.
def genOverview():
    treemap = pygal.Treemap()
    treemap.title = 'DSACMS Project Overview Binary TreeMap'

    for file in os.listdir():
        try:
            f = open(file)
            data = json.load(f)
            d = []
            words = file.split("-METRICS")

            for key in data:
                if (data[key] != 0 and data[key] != None):
                    d.append(data[key])
            d.pop(0)

            treemap.add(words[0], d)
        except:
            invalid = []
            invalid.append(file)

    treemap.render_to_file('overview.svg')


def repoSpecific():
    for file in os.listdir():
        try:
            treemap = pygal.Treemap()
            f = open(file)
            data = json.load(f)
            del data["datetime"]

            for key in data:
                if (data[key] != 0 and data[key] != None):
                    treemap.add(key, data[key])

            words = file.split("-METRICS")
            treemap.title = words[0] + " Binary TreeMap"
            treemap.render_to_file(words[0] + "-graph.svg")
            data.clear()

        except:
            invalid = []
            invalid.append(file)


def main():
    genOverview()
    repoSpecific()


if __name__ == "__main__":
    main()
