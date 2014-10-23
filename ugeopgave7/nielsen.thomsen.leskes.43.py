# -*- coding: utf-8 -*-
# Gruppeopgave
# Allan Nielsen, Troels Thomsen, Troels Leskes
# Foelgende opgave omhandler Integration ved Riemannsummer.
# Funktionen r_int(f, a, b, n) approksimerer integralet ved
# at tage summen af arealerne under grafen for funktionen
# som beskrevet i opgaveformuleringens (1).
# Funktionen r_int_mid(f, a, b, n) fungerer paa samme maade
# ved brug af opgaveformuleringens (2).
# grafic(n) bruger pyplot til at udskrive punkter for de tre
# funktioner f, phi og g for et vilkaarligt n.
from __future__ import division
import math
import matplotlib.pyplot as plt

epsilon = 1e-10
# De tre funktioner f, phi og g
fun_f = lambda x: math.cos(x)
fun_phi = lambda x: (1/math.sqrt(2 * math.pi)) * math.exp((-x**2)/2)
fun_g = lambda x: math.sin(1/x)


def r_int(f, a, b, n):
    """
    r_int tager en funktion f, et startpunkt a, et slutpunkt b og
    et antal knudepunkter n til at finde Riemannsummenn.
    :param f: funktion
    :param a: startpunkt
    :param b: slutpunkt
    :param n: knudepunkter
    :return: approksimation for integralet for f
    """
    ans = 0
    step = (b - a) / n
    ti = a + step
    for i in range(0, n):
        ans += abs(ti - a) * f(ti)
        a = ti
        ti += step
    return ans


def r_int_mid(f, a, b, n):
    """
    r_int_mid tager en funktion f, et startpunkt a, et slutpunkt b og
    et antal knudepunkter n til at finde Riemannsummenn ved brug af
    summen (2) fra opgavebeskrivelsen.
    :param f: funktion
    :param a: startpunkt
    :param b: slutpunkt
    :param n: knudepunkter
    :return: approksimation for integralet for f
    """
    ans = 0
    step = (b - a) / n
    ti = a + step
    for i in range(0, n):
        ans += abs(ti - a) * 0.5 * (f(ti) + f(a))
        a = ti
        ti += step
    return ans


def grafic(n):
    """
    grafic tager et antal knudepunkter n og udskriver et pyplot
    over punkterne for hver vaerdi 1,2...n for de tre funktioner
    f, phi og g i de givne intervaller i funktionerne
    r_int og r_int_mid.
    :param n: antallet af knudepunkter
    :return: et pyplot over punkterne
    """
    ans_r_int = []
    ans_r_int_mid = []
    for i in range(1, n + 1):
        ans_r_int += [r_int(fun_f, 0, 2 * math.pi, i)]
        ans_r_int_mid += [r_int_mid(fun_f, 0, 2 * math.pi, i)]
        ans_r_int += [r_int(fun_phi, -10, 10, i)]
        ans_r_int_mid += [r_int_mid(fun_phi, -10, 10, i)]
        ans_r_int += [r_int(fun_g, 0.001, 10, i)]
        ans_r_int_mid += [r_int_mid(fun_g, 0.001, 10, i)]
    plt.plot(ans_r_int, 'ro', ans_r_int_mid, 'g^')
    plt.show()

print 'r_int(f, 0, 2 * pi, 50) = 0.0', r_int(fun_f, 0, 2 * math.pi, 50) - 0.0 < epsilon
print 'r_int(phi, -10, 10, 50) = 1.0', r_int(fun_phi, -10, 10, 50) - 1.0 < epsilon
print 'r_int(g, 0.001, 10, 50) = 2.6335682009', r_int(fun_g, 0.001, 10, 50) - 2.6335682009 < epsilon
print 'r_int_mid(f, 0, 2 * pi, 50) = 0.0', r_int_mid(fun_f, 0, 2 * math.pi, 50) - 0.0 < epsilon
print 'r_int_mid(phi, -10, 10, 50) = 1.0', r_int_mid(fun_phi, -10, 10, 50) - 1.0 < epsilon
print 'r_int_mid(g, 0.001, 10, 50) = 2.70626554283', r_int_mid(fun_g, 0.001, 10, 50) - 2.70626554283 < epsilon

grafic(50)