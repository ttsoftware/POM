# coding=utf-8
from numpy import arange, linspace
import numpy as np
import matplotlib.pyplot as plt


def step(x, c, k):
    """
    Dette er vores udtryk for udregning af skridt, med K
    :param x:
    :param c:
    :param k:
    :return:
    """
    return np.exp(-((x - 8 - c * k) ** 2 / 4))


def get_next(x, h, l):
    """
    Denne holder styr på naboerne til et givent x,
    således at hvis vi er i starten/enden af vorea array,
    returneres de korrekte naboer
    :param x:
    :param h:
    :param l:
    :return:
    """
    if x == 0:
        return l, x + h
    if x == l:
        return x - h, 0
    return x - h, x + h


def u(x, t, c, k, h, l):
    """
    Det er her den udregner alle udtryk for x fra tiden t=0 op til t,
    hvor den stiger med k mellem hvert step.
    :param x:
    :param t:
    :param c:
    :param k:
    :param h:
    :param l:
    :return:
    """
    res = {}

    # Antallet af x'er der er i bølgen.
    xs = linspace(0, l, num=int(l / h))

    # Basisværdierne for alle x, til tiden 0 og k
    res[0] = step(xs, c, 0)
    res[k] = step(xs, c, k)

    # Alle tiderne udregnes for alle x
    for j in arange(2 * k, t, k):
        j = round(j, 5)

        res[j] = []

        previous = round(j - k, 5)
        previous_2 = round(j - 2 * k, 5)

        for i, v in enumerate(xs):
            left, right = get_next(i, 1, len(xs) - 1)

            res[j] += [k ** 2 * c ** 2 * (
                (res[previous][right] / h ** 2)
                - (2 * res[previous][i] / h ** 2)
                + (res[previous][left] / h ** 2)
            ) + (2 * res[previous][i])
                       - res[previous_2][i]]

    # Bølgen plottes for alle tidspunkter.
#    for i in res.keys():
#        print i
#        plt.plot(xs, res[i], "b-")


    index_t = res.keys()[t-1]  # Vi kan ikke bruge vores t, fordi vi tager k skridt?

    plt.figure("Die Welle")
    plt.plot(xs, res[index_t], "r-")
    plt.show()

    return res[index_t][x-1]

# x  t  c  k  h  l
#u(5, 10, 1, 0.9, 0.9, 250)
#u(5, 150, 1, 0.9, 0.9, 250)
u(5, 0, 1, 0.9, 0.9, 250)
u(5, 1, 1, 0.9, 0.9, 250)
#u(1, 248, 1, 0.9, 0.9, 250)
