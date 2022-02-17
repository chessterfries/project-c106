import csv
import numpy as np
import plotly.express as px

def getDataSource(data_path):
    cups_of_coffee = []
    hours_of_sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))
    
    return {"x": cups_of_coffee, "y": hours_of_sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee in ml and the amount of sleep in hours is: ", correlation[0,1])

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours", color = "week")
        fig.show()

def setup():
    data_path = "C:/Users/gulsh/Pictures/Whitehat Jr/Projects/Project C106 Python/cups of coffee vs hours of sleep.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()