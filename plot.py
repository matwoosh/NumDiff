import matplotlib.pyplot as plt
from pygsl import deriv


class Plot:
    def __init__(self, function, arguments):
        self.arguments = arguments
        self.function = function

    def plot_function(self, canvas):
        plt.clf()
        canvas.draw()
        x = self.arguments
        y = []
        for number in x:
            y.append(self.function(number, 0))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(x, y)
        canvas.draw()

    def plot_derivative(self, canvas):
        x = self.arguments
        y = []
        for number in x:
            y.append(deriv.central(self.function, number, 1)[0])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(x, y)
        canvas.draw()



