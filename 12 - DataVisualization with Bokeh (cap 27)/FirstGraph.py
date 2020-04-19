# Making a basic linegraph

# import Bokeh
from bokeh.plotting import figure
from bokeh.io import output_file, show

# some data
x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,10,5,1,9,5,2,7,3,2,3]

# prepare output file
output_file("line.html")

# create figure object
f = figure()
f.line(x,y)
show (f)
