# coding=utf-8
from numpy import arange, linspace
import numpy as np
import matplotlib.pyplot as plt


def step(x, c, k):
    return np.exp(-((x - 8 - c * k) ** 2 / 4))


def get_next(x, h, l):
    if x == 0:
        return l, x + h
    if x == l:
        return x - h, 0
    return x - h, x + h


def u(x, t, c, k, h, l):
    res = {}

    xs = linspace(0, l, num=int(l / h))

    res[0] = step(xs, c, 0)
    res[k] = step(xs, c, k)

    for j in arange(2 * k, t, k):
        j = round(j, 5)

        res[j] = []

        previous = round(j - k, 5)
        previous_2 = round(j - 2 * k, 5)

        #print res.keys()
        #print j, previous, previous_2
        #print res[j], res[previous], res[previous_2]

        for i, v in enumerate(xs):
            left, right = get_next(i, 1, len(xs) - 1)

            res[j] += [k ** 2 * c ** 2 * (
                (res[previous][right] / h ** 2)
                - (2 * res[previous][i] / h ** 2)
                + (res[previous][left] / h ** 2)
            ) + (2 * res[previous][i])
                       - res[previous_2][i]]

    index_t = res.keys()[t-1]  # Vi kan ikke bruge vores t, fordi vi tager k skridt?
                               # Ingen ved det. Jeg ved ikke hvad jeg laver
                               # Alle k er løsninger til k
                               # http://pygospasprofession.files.wordpress.com/2013/07/watman.jpg
                               # http://img.1001mem.ru/posts/2891000/2890868.jpg

    # vi har x'er ud af x-aksen
    # vi har u(x, t) op af y-aksen? Det er jeg ret sikker på
    # synes i det ser godt ud?
    # jeg synes det er skide godt.
    # måske.
    # http://www.youtube.com/watch?v=2ZPfgVSrPVY
    for i in res.keys():
        plt.plot(xs, res[i], "b-")

    plt.figure("penis")
    plt.plot(xs, res[0], "b-")
    plt.figure("penis2")
    plt.plot(xs, res[k], "b-")

    plt.show()

    return res[index_t][x-1]

# x  t  c  k  h  l
print u(5, 5, 1, 0.9, 0.9, 10)

# Jeg regnede med at det ville blive præcis 0.00416544575484

# SHIP IIIIIT

# http://www.youtube.com/watch?v=p9yFOG7nqNc