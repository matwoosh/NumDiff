import matplotlib.pyplot as plt


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
            y.append(self.function(number))
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(x, y)
        canvas.draw()



