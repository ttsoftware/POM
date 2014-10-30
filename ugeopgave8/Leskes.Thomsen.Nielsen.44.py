# -*- coding: utf-8 -*-
import math
import matplotlib.pyplot as plt
from csvImageRead import *


def f(x, y):
    return x ** 2 + y ** 2


def gradient(v):
    return gradientx(v), gradienty(v)


def gradientx(v):
    n = len(v)
    vDx = []
    for i in range(n):
        vDx.append([])
        for j in range(n):
            if j < n - 1:
                vDx[i].append(v[i - 1][j] - v[i - 1][j - 1])
            else:
                vDx[i].append(0.0)
    return vDx


def gradienty(v):
    n = len(v)
    vDy = []
    for i in range(n):
        vDy.append([])
        for j in range(n):
            if j < n - 1:
                vDy[i].append(v[i][j - 1] - v[i - 1][j - 1])
            else:
                vDy[i].append(0.0)
    return vDy


def norm(vDx, vDy):
    n = len(vDx)
    normen = []
    if len(vDx) == len(vDy):
        for i in range(n):
            normen.append([])
            for j in range(n):
                normen[i].append(math.sqrt(vDx[i][j] ** 2 + vDy[i][j] ** 2))
    return normen


def divergens(vDx, vDy):
    n = len(vDx)
    divv = []

    if len(vDx) == len(vDy):

        for i in range(n):
            divv.append([])

            for j in range(n):
                divi = None
                divj = None

                if 1 < i < n - 1:
                    divi = vDx[i][j] - vDx[i - 1][j]
                elif i == 1:
                    divi = vDx[i][j]
                else:
                    divi = -vDx[i - 1][j]

                if 1 < j < n - 1:
                    divj = vDy[i][j] - vDy[i - 1][j]
                elif j == 1:
                    divj = vDy[i][j]
                else:
                    divj = -vDy[i - 1][j]

                divv[i].append(divi + divj)
    return divv


def smoothenimage(filename):
    if filename.split(".")[1] == "csv":
        # 1) Indlæser billede
        imagelist = csvImageRead(filename)
        # 2) Sætter tau = 0.248 og lambda = 0.08
        tau = 0.248
        regulate = 0.08
        # 3) laver 2 NxN billeder, w1 og w2
        w1 = []
        for i in range(0, len(imagelist)):
            w1.append([])
            for j in range(0, len(imagelist)):
                w1[i].append(0)
        w2 = w1
        divW = divergens(w1, w2)
        # 4) 
        ylambda = imagelist.__imul__(regulate)
        print(imagelist)
        print(ylambda)


if __name__ == "__main__":
    imagelist = csvImageRead("Cameraman.csv")
    imagelistnoise = csvImageRead("CameramanNoisy.csv")
    # plt.imshow(imagelist, cmap="Greys_r")

    gradx = gradientx(imagelist)
    #print gradx

    grady = gradienty(imagelist)
    #print grady

    norm = norm(grady, gradx)
    #print len(norm)

    diver = divergens(grady, gradx)
    #print len(norm)

    #smoothenimage("CameramanNoisy.csv")
    plt.imshow(imagelist, cmap="Greys_r")
    plt.show()
