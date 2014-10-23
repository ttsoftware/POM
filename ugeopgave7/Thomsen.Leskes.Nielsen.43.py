from __future__ import division
import math
import matplotlib.pyplot as plt
import numpy as np

def rInt(f, a, b, n):
    delta_ab = b - a
    interval = delta_ab/n
    ti = a + interval
    Esum = []
    for i in range(0, n):
        Esum.append(abs(interval) * f(ti))
        ti += interval
    return Esum

def rIntMid(f, a, b, n):
    delta_ab = b - a
    interval = delta_ab/n
    ti = a + interval
    Esum = []
    for i in range(0, n):
        Esum.append(abs(interval) * 0.5 * (f(ti) + f(ti - interval)))
        ti += interval
    return Esum



if __name__ == "__main__":
    n = 1000
    a_f, b_f = (0, 2*math.pi)
    def f(x):
        return math.cos(x)

    a_oe, b_oe = (-10, 10)
    def oe(x):
        return (1/math.sqrt(2 * math.pi))*math.exp((-x**2)/2)

    a_g, b_g = (0.001, 10)
    def g(x):
        return math.sin(1/x)

    rintf = rInt(f, a_f, b_f, n)
    rintoe = rInt(oe, a_oe, b_oe, n)
    rintg = rInt(g, a_g, b_g, n)

    rintmidf = rIntMid(f, a_f, b_f, n)
    rintmidoe = rIntMid(oe, a_oe, b_oe, n)
    rintmidg = rIntMid(g, a_g, b_g, n)

def genplotvalues(n):
    vals = []
    for i in range(0, n):
        vals.append(rint)


    n = range(n)

    plt.plot(n, rintf, "g--", n, rintoe, "go", n, rintg, "g^", n, rintmidf, "r^", n, rintmidoe, "r--", n, rintmidg, "ro")
    plt.ylabel('some numbers')
    plt.show()