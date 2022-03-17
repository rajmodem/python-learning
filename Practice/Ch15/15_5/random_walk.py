from random import choice
from tkinter import Y

class Randomwalk:
    """A class to generate random walks"""

    def __init__(self, num_points = 5000):
        """Initialize attributes of walk"""
        self.num_points = num_points

        #All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """To get direction and distance for each step"""
        direction = choice([1, -1])
        distance = choice([0,1,2,3,4,5,6,7,8])
        step = direction * distance
        return step

    def fill_walk(self):
        """Calculate all points in the walk"""

        #Keep taking steps until walk reached destination
        while len(self.x_values) < self.num_points:

            #Decide which direction to go and how far in that direction
            x_step = self.get_step()
            y_step = self.get_step()  

            #Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            #Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            