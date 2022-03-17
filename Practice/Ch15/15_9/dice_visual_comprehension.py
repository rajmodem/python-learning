from unittest import result
from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline


#Create a D6 & D6
die_1 = Die()
die_2 = Die()

results = [die_1.roll() * die_2.roll() for roll_num in range(50000)]
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1,max_result+1)]

#Visualize the results
x_values = list(range(1,max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1} 
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_comprehension.html')