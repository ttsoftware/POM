from __future__ import division
import numpy as np


class Vector(object):

    vx = 0.0
    vy = 0.0
    length = 0.0

    def __init__(self, vx=None, vy=None, px=None, py=None):
        """
        Create a new Vector instance either with vector values vx and vy
        or with points tuples p1 and p2
        :param vx: float
        :param vy: float
        :param px: tuple
        :param py: tuple
        :raise Exception:
        """
        if vx is not None and vy is not None:
            self.vx = vx
            self.vy = vy
        elif px is not None and py is not None:
            p1x, p1y = px
            p2x, p2y = py
            self.vx = p2x - p1x
            self.vy = p2y - p1y
        else:
            raise Exception("Invalid parameters")

        self.length = np.sqrt(self.vx ** 2 + self.vy ** 2)

    def __len__(self):
        return self.length

    def scale(self, s):
        return Vector(
            vx=(self.vx / self.length) * s,
            vy=(self.vy / self.length) * s
        )

    def __add__(self, other):
        """
        Add two Vector types together
        :param other:
        :return: Vector
        """
        return Vector(vx=(self.vx + other.vx), vy=(self.vy + other.vy))

    def dot(self, other):
        """
        Other must be type Vector
        :param other: Vector
        :return: Vector
        """
        return self.vx * other.vx + self.vy * other.vy

    def proj(self, p):
        """
        We pretend that the point is a vector?
        :param p: tuple
        :return:
        """
        px, py = p
        l = ((self.vx * px + self.vy * py) / self.length)
        r = Vector(vx=self.vx / self.length, vy=self.vy / self.length)

        return Vector(
            vx=r.vx * l,
            vy=r.vy * l
        )

    def __str__(self):
        return "(" + str(self.vx) + ", " + str(self.vy) + ")"