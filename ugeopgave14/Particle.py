from __future__ import division
import numpy as np
from Vector import Vector
import math


class Particle(object):
    position = None
    velocity = None
    mass = 10 ** -23

    def __init__(self, positionx, positiony, velocityx, velocityy):
        self.position = Vector(vx=positionx, vy=positiony)
        self.velocity = Vector(vx=velocityx, vy=velocityy)

    def step(self):
        return Vector(
            vx=self.position.vx + 1 * self.velocity.vx,
            vy=self.position.vy + 1 * self.velocity.vy
        )

    def take_step(self, center, radius):
        if not self.willcollide(center, radius):
            self.position = self.step()
        else:
            cx, cy = center
            u = 0.0

            px = self.position.vx
            py = self.position.vy
            vx = self.velocity.vx
            vy = self.velocity.vy

            if vx**2 + vy**2 == 0:
                raise Exception("wat")

            u1 = (-0.5 * math.sqrt(
                (-2 * cx * vx + 2 * px * vx + 2 * py * vy - 2 * vy * cy) ** 2 - 4 * (vx ** 2 + vy ** 2) * (
                    cx ** 2 - 2 * cx * px + px ** 2 - radius ** 2 + py ** 2 - 2 * py * cy + cy ** 2)
            ) + cx * vx - px * vx - py * vy + vy * cy) / (vx ** 2 + vy ** 2)

            u2 = (0.5 * math.sqrt(
                (-2 * cx * vx + 2 * px * vx + 2 * py * vy - 2 * vy * cy) ** 2 - 4 * (vx ** 2 + vy ** 2) * (
                    cx ** 2 - 2 * cx * px + px ** 2 - radius ** 2 + py ** 2 - 2 * py * cy + cy ** 2)
            ) + cx * vx - px * vx - py * vy + vy * cy) / (vx ** 2 + vy ** 2)

            if 1 > u1 > 0:
                u = u1
            if 1 > u2 > 0:
                u = u2

            print "U: " + str(u)

    def willcollide(self, center, radius):
        next_position = self.step()

        return len(
            Vector(p1=center,
                   p2=(next_position.vx, next_position.vy)
            )
        ) > radius