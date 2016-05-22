import numpy as np

def function1(data):
    return [x ** 2 for x in data]


def function2(data):
    return [(x ** 3) + 2 * (x ** 2) for x in data]


def function3(data):
    return [(x ** 4) - 3 * (x ** 2) for x in data]

functions = [("sin(x)", np.arange(0, 10, 0.1), np.sin(np.arange(0, 10, 0.1))),
             ("cos(x)", np.arange(0, 10, 0.1), np.cos(np.arange(0, 10, 0.1))),
             ("x^2", np.arange(0, 10, 0.1), function1(np.arange(0, 10, 0.1))),
             ("x^3+2x^2", np.arange(0, 10, 0.1), function2(np.arange(0, 10, 0.1))),
             ("x^4-3x^2", np.arange(0, 10, 0.01), function3(np.arange(0, 10, 0.01))),
             ("sqrt(x)", np.arange(0, 10, 0.1), np.sqrt(np.arange(0, 10, 0.1))),
             ("exp(x)", np.arange(0, 10, 0.1), np.exp(np.arange(0, 10, 0.1)))]