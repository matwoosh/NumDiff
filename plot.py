import matplotlib.pyplot as plt


class Plot:
    def __init__(self, arguments, function):
        self.arguments = arguments
        self.function = function

    def plot_function(self, canvas):
        plt.clf()
        canvas.draw()
        x = self.arguments
        y = self.function
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(x, y)
        canvas.draw()



