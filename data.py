from math import sin, cos, sqrt, exp

import numpy as np


def function1(x):
    return sin(x)


def function2(x):
    return cos(x)


def function3(x):
    return x ** 2


def function4(x):
    return (x ** 3) - 9 * (x ** 2) + 25 * x - 17


def function5(x):
    return (x ** 4) - 3 * (x ** 2)


def function6(x):
    return sqrt(x)


def function7(x):
    return exp(x)

# list of functions_data in format ("name", function, arguments)
functions = [("sin(x)", function1, np.arange(0, 10, 0.1)),
             ("cos(x)", function2, np.arange(0, 10, 0.1)),
             ("x^2", function3, np.arange(0, 4, 0.1)),
             ("x^3-9x^2+25x-17", function4, np.arange(0, 5, 0.1)),
             ("x^4-3x^2", function5, np.arange(0, 2, 0.01)),
             ("sqrt(x)", function6, np.arange(0, 10, 0.1)),
             ("exp(x)", function7, np.arange(0, 10, 0.1))]

