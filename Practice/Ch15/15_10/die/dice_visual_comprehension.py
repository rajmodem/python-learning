"""
Module to plot dice count vs frequency of result using matplotlib
"""
from itertools import zip_longest
import matplotlib.pyplot as plt
import numpy as np

from die import Die

#Create a D6 & D6
die_1 = Die()
die_2 = Die()

results = [die_1.roll() + die_2.roll() for roll_num in range(100)]
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2,max_result+1)]

x_values = list(range(1,2*(die_1.num_sides)))

#plot the points in the walk
plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.bar(x_values, frequencies, width =1)

#Set the chart title and label axes.
ax.set_title("Dice Values vs Frequency", fontsize=14)
ax.set_xlabel("Value", fontsize = 8)
ax.set_ylabel("Frequency", fontsize = 8)
plt.show()