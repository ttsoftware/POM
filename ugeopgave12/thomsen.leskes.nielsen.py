from numpy import arange, linspace
import numpy as np
import matplotlib.pyplot as plt


def step(x, c, k):
    return np.exp(-((x - 8 - c * k) ** 2 / 4))


def get_next(x, h, l):
    if x == 0:
        return l, x+h
    if x == l:
        return x-h, 0
    return x-h, x+h


def u(x, t, c, k, h, l):

    res = {}

    xs = linspace(0, l, num=int(l/h))

    res[0] = step(xs, c, 0)
    res[k] = step(xs, c, k)

    '''
    plt.figure("penis")
    plt.plot(xs, res[0], "b-")

    plt.figure("penis2")
    plt.plot(xs, res[1], "b-")
    plt.show()
    '''

    print res

    for j in arange(2*k, t, k):

        res[j] = []

        for i, v in enumerate(xs):

            left, right = get_next(i, 1, len(xs)-1)

            print i, v
            print left, right

            res[j] += k ** 2 * c ** 2 * (
                (res[j-k][right] / h ** 2)
                - (2 * res[j-k][i] / h ** 2)
                + (res[j-k][left] / h ** 2)
            ) + (2 * res[j-k][i]) - res[j-2*k][i]

    return res[t-1][x]

#       x  t  c  k  h  l
print u(5, 5, 1, 0.9, 0.9, 10)