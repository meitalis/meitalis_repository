import numpy as np
from matplotlib import pylab as plt

def x2(x1):
    return 4 +  x1 / 6

def get_plot(func, xs):
    ys = []
    for x in xs:
        ys.append(func(x))
    ys = np.array(ys) # <-- moved outside the for loop
    plt.plot(xs, ys)
    plt.show()

xs = np.arange(2.0, 5.0, 0.1)
get_plot(x2, xs)