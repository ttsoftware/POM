# -*- coding: utf-8 -*-
from __future__ import division
import copy
import math
import matplotlib.pyplot as plt
import numpy as np
from csvImageRead import *
from operator import sub

def f(x, y):
    return x ** 2 + y ** 2


def gradient(v):
    return gradientx(v), gradienty(v)


def gradientx(v):
    n = len(v)
    vDx = []
    for i in xrange(n):
        vDx.append([])
        for j in xrange(n):
            if i < n - 1:
                vDx[i].append(v[i + 1][j] - v[i][j])
            else:
                vDx[i].append(0.0)
    return vDx


def gradienty(v):
    n = len(v)
    vDy = []
    for i in xrange(n):
        vDy.append([])
        for j in xrange(n):
            if j < n - 1:
                vDy[i].append(v[i][j + 1] - v[i][j])
            else:
                vDy[i].append(0.0)
    return vDy


def gradNorm(vDx, vDy):
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

    for i in xrange(n):
        divv.append([])
        for j in xrange(n):
            divi = None
            divj = None

            if 0 < i < n - 1:
                divi = vDx[i][j] - vDx[i - 1][j]
            elif i == 0:
                divi = vDx[i][j]
            else:
                divi = -vDx[i - 1][j]

            if 0 < j < n - 1:
                divj = vDy[i][j] - vDy[i][j - 1]
            elif j == 0:
                divj = vDy[i][j]
            else:
                divj = -vDy[i][j - 1]

            divv[i].append(divi + divj)

    return divv


def smoothenimage(filename):
    if filename.split(".").pop() == "csv":
        # 1) Indlæser billede
        imagelist = csvImageRead(filename)
        lenn = len(imagelist)

        # 2) Sætter tau = 0.248 og lambda = 0.08
        tau = 0.248
        regulate = 0.09

        # 3) laver 2 NxN billeder, w1 og w2
        w1 = []
        for i in xrange(lenn):
            w1.append([])
            for j in range(lenn):
                w1[i].append(0)
        w2 = copy.deepcopy(w1)
        divW = divergens(w1, w2)
        # 4) beregner y*lambda
        ylambda = regulater(imagelist, regulate)

        sumofimage = []
        # 5) Itererer (dog kun 10 gange
        for i in xrange(20):

            # 5.1) beregner gradienterne
            y1, y2 = (gradient(ylambda))
            dw1, dw2 = (gradient(divW))
            dwx = subtracter(y1,  dw1)
            dwy = subtracter(y2,  dw2)

            # 5.2) beregner normen
            dwnorm = gradNorm(dwx, dwy)

            # 5.3) Foretager descent-skridt
            for i in xrange(lenn):
                for j in xrange(lenn):
                    w1[i][j] = w1[i][j] - dwx[i][j] * tau
                    w2[i][j] = w2[i][j] - dwy[i][j] * tau
                    w1[i][j] = w1[i][j] / (1 + dwnorm[i][j] * tau)
                    w2[i][j] = w2[i][j] / (1 + dwnorm[i][j] * tau)

            # 5.4) Opdater divW med w1 og w2
            divW = divergens(w1, w2)

            # 5.5)
            sumis = 0
            for i in xrange(lenn):
                for j in xrange(lenn):
                    sumis += 0.5 * (ylambda[i][j] - divW[i][j])**2
            sumofimage.append(sumis)

        plt.figure("energi")
        plt.plot(sumofimage, "b")

        x = []
        for i in xrange(lenn):
            x.append([])
            for j in range(lenn):
                firstp = imagelist[i][j]
                secondp = (1/regulate)*divW[i][j]
                x[i].append(firstp - secondp)

        return x
    return "WHY U NO GIVE CSV"


def subtracter(v, w):
    sub = []
    for i in xrange(len(v)):
        sub.append([])
        for j in xrange(len(v)):
            sub[i].append(v[i][j] - w[i][j])

    return sub

def regulater(v, regulation):
    regulated = []
    for i in xrange(len(v)):
        regulated.append([])
        for j in xrange(len(v)):
            regulated[i].append(v[i][j] * regulation)
    return regulated

if __name__ == "__main__":
    imagelist = csvImageRead("Cameraman.csv")
    imagelistnoise = csvImageRead("CameramanNoisy.csv")
    #print imagelistnoise
    # plt.imshow(imagelist, cmap="Greys_r")

    gradx = gradientx(imagelist)
    # print gradx

    grady = gradienty(imagelist)
    #print grady

    norm = gradNorm(grady, gradx)
    #print len(norm)

    diver = divergens(grady, gradx)
    #print len(norm)

    smoothim = smoothenimage("CameramanNoisy.csv")
    #print smoothim
    plt.figure("smoothim")
    plt.imshow(smoothim, cmap="Greys_r")
    plt.figure("grady")
    plt.imshow(grady, cmap="Greys_r")
    plt.figure("gradx")
    plt.imshow(gradx, cmap="Greys_r")
    plt.figure("norm")
    plt.imshow(norm, cmap="Greys_r")
    plt.figure("diver")
    plt.imshow(diver, cmap="Greys_r")
    plt.figure("darealest")
    plt.imshow(imagelistnoise, cmap="Greys_r")
    plt.figure("origin")
    plt.imshow(imagelist, cmap="Greys_r")
    plt.show()
