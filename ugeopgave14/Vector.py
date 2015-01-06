from __future__ import division
import numpy as np


class Vector(object):

    vx = 0.0
    vy = 0.0
    length = 0.0

    def __init__(self, vx=None, vy=None, p1=None, p2=None):
        """
        Create a new Vector instance either with vector values vx and vy
        or with points tuples p1 and p2
        :param vx: float
        :param vy: float
        :param p1: tuple
        :param p2: tuple
        :raise Exception:
        """
        if vx is not None and vy is not None:
            self.vx = vx
            self.vy = vy
        elif p1 is not None and p2 is not None:
            p1x, p1y = p1
            p2x, p2y = p2
            self.vx = p2x - p1x
            self.vy = p2y - p1y
        else:
            raise Exception("AAAAAAAAAAARRRRRRRRHGHHHHHHHHHHHHH")

        self.length = np.sqrt(self.vx ** 2 + self.vy ** 2)

    def __len__(self):
        return self.length

    def scale(self, s):
        self.vx = (self.vx / self.length) * s
        self.vy = (self.vy / self.length) * s

    def __add__(self, other):
        return Vector(vx=(self.vx + other.vx), vy=(self.vy + other.vy))

    def dot(self, other):
        return self.vx * other.vx + self.vy * other.vy

    def proj(self, p):
        """
        Wat?
        :param p: tuple
        :return:
        """
        pass

    def __str__(self):
        return "(" + str(self.vx) + ", " + str(self.vy) + ")"