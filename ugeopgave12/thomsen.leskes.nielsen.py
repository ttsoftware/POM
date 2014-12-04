import math


def u(x, t, c, k, h):
    return (k**2)*(c**2)*(
            ((math.exp(-((x+h)-8-c*t)**2/4))/h**2)
            - ((2*math.exp(-(x-8-c*t)**2/4))/h**2)
            + ((math.exp(-((x-h)-8-c*t)**2/4))/h**2)
    ) + (2*math.exp(-(x-8-c*t)**2/4)) - (math.exp(-(x-8-c*(t-k))**2/4))


print u(0, 0, 1, k, 1)