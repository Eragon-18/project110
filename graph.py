import plotly.figure_factory as ff 
import random
import pandas as pd 
import csv
import statistics
import plotly.graph_objects as go 

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

def findRandom(counter):
    ds = []
    for i in range(0,counter):
        ri = random.randint(0,len(data))
        value = data[ri]
        ds.append(value)
    mean = statistics.mean(ds)
    return mean

def showFig(ml):
    df = ml
    m = statistics.mean(ml)
    print("Mean of sampling distribution = ", m)
    fig = ff.create_distplot([df],["reading_time"], show_hist = False)
    fig.add_trace(go.Scatter(x = [m,m], y = [0,1], mode = "lines", name = "Mean"))
    fig.show()

def findstddev():
    ml2 = []
    for i in range(0,100):
        setOfMeans2 = findRandom(30)
        ml2.append(setOfMeans2)
    stddev2 = statistics.stdev(ml2)
    print("Standard deviation of sampling distribution = ", stddev2)

def setup():
    ml = []
    for i in range(0,1000):
        setOfMeans = findRandom(100)
        ml.append(setOfMeans)
    showFig(ml)

setup()