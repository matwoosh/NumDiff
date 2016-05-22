import numpy as np
import matplotlib.pyplot as plt


class Plot:
    def __init__(self, function, arguments):
        self.function = function
        self.arguments = arguments

    def plot_function(self, canvas):
        x = self.arguments
        y = self.function
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(x, y)
        canvas.draw()



