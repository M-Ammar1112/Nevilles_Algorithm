from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from scipy.interpolate import make_interp_spline


def neville(xlist, ylist, a):
    n = len(xlist)
    p = n * [0]
    for i in range(n):
        for j in range(n - i):
            if i == 0:
                p[j] = ylist[j]
            else:
                p[j] = ((a - xlist[j + i]) * p[j] + \
                        (xlist[j] - a) * p[j + 1]) / \
                       (xlist[j] - xlist[j + i])


    if n <= 3:
        x = np.array(xlist)
        y = np.array(ylist)
        style.use('ggplot')
        plt.plot(x, y)
        plt.plot(xlist, ylist, 'r*')
        plt.plot(a, p[0], 'g*')
        plt.show()
    else:
        x = np.array(xlist)
        y = np.array(ylist)
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 500)
        Y_ = X_Y_Spline(X_)
        style.use('ggplot')
        plt.plot(X_, Y_)
        plt.plot(x, y)
        plt.plot(xlist, ylist, 'r*')
        plt.plot(a, p[0], 'g*')
        plt.show()

    return p[0]


print(neville([1,2,3,4,8,10,11,15],[5,6,7,9,1,5,2,9], 1.5))
print(np.interp(1.5,[1,2,3,4], [5,6,7,9]))