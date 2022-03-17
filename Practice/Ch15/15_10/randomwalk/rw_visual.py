"""
Module to plot scattered random walk using plotly
"""
from matplotlib.pyplot import show
from plotly.graph_objs import Bar, Layout
from plotly import offline
import plotly.express as px
from random_walk import Randomwalk

#keep making new walks, as long as the program is active
while True:
    #Make a random walk
    rw = Randomwalk()
    rw.fill_walk()

    #plot the points in the walk
    point_numbers = range(rw.num_points)
    fig = px.scatter(rw.x_values,rw.y_values)
    fig.show()
    #ax.scatter(rw.x_values,rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

    #Emphasize the first and last points
    #ax.scatter(0, 0, c='green', edgecolors='none', s=300)
    #ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=300)

    keep_running = input("Make another walk ?(y/n):")
    if keep_running == 'n':
        break