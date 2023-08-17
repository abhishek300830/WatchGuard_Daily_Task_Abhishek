from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas
 
output_file("Practice-100-Python-Questions\Section-3\\bokeh_plot.html")
data = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
f = figure()
f.circle(x=data["x"], y=data["y"])
 
show(f)