from __future__ import division
import numpy as np
from Vector import Vector
import math


class Particle(object):

    position = None
    velocity = None
    mass = 10 ** -23
    factor = 1.0

    def __init__(self, positionx, positiony, velocityx, velocityy):
        self.position = Vector(vx=positionx, vy=positiony)
        self.velocity = Vector(vx=velocityx, vy=velocityy)

    def step(self):
        """
        Return the position the particle would have in the next t
        :return:
        """
        return Vector(
            vx=self.position.vx + 1 * self.velocity.vx,
            vy=self.position.vy + 1 * self.velocity.vy
        )

    def take_step(self, center, radius):
        """
        Move the particle in to its position for next t
        Handles collision with container wall
        :param center:
        :param radius:
        :raise Exception:
        """
        if not self.willcollide(center, radius):
            self.position = self.step()
        else:

            print "Collision"

            cx, cy = center
            u = 0.0

            px = self.position.vx
            py = self.position.vy
            vx = self.velocity.vx
            vy = self.velocity.vy

            # we find the following equation by treating (p+v*u-c)^2 as a vector, and dotting it with itself.
            # we solve for u and insert our particle data

            u1 = (-math.sqrt((-2 * cx * vx + 2 * px * vx + 2 * py * vy - 2 * vy * cy) ** 2 - 4 *
                            (vx ** 2 + vy ** 2) * (
            cx ** 2 - 2 * cx * px + px ** 2 - radius ** 2 + py ** 2 - 2 * py * cy + cy ** 2))
                  + 2 * cx * vx - 2 * px * vx - 2 * py * vy + 2 * vy * cy) / (2 * (vx ** 2 + vy ** 2))

            u2 = (math.sqrt((-2 * cx * vx + 2 * px * vx + 2 * py * vy - 2 * vy * cy) ** 2 - 4 *
                            (vx ** 2 + vy ** 2) * (
            cx ** 2 - 2 * cx * px + px ** 2 - radius ** 2 + py ** 2 - 2 * py * cy + cy ** 2))
                  + 2 * cx * vx - 2 * px * vx - 2 * py * vy + 2 * vy * cy) / (2 * (vx ** 2 + vy ** 2))

            u1 = abs(u1)
            u2 = abs(u2)

            # u is chosen
            if 1 >= u1 > 0:
                u = u1
            elif 1 >= u2 > 0:
                u = u2
            else:
                print u1
                print u2
                raise Exception("Could not determine distance to barrier. Particle has possibly slipped outside the container.")

            # pc and projection are position Vectors
            pc = self.position + Vector(self.velocity.vx * u, self.velocity.vy * u)

            projection = Vector(
                px=center,
                py=(pc.vx, pc.vy)
            ).proj((self.position.vx, self.position.vy))

            vp = Vector(
                px=(self.position.vx, self.position.vy),
                py=(projection.vx, projection.vy)
            )
            # p1'
            p_1 = self.position + vp.scale(2 * vp.length)
            # v2 is the vector from pc
            v_2 = Vector(
                px=(pc.vx, pc.vy),
                py=(p_1.vx, p_1.vy)
            ).scale(self.velocity.length)

            self.velocity = v_2

            self.scale_for_temp()
            self.position = pc + self.velocity.scale(self.velocity.length * (1 - u))

    def willcollide(self, center, radius):
        """
        Will the particle collide with the container if the next step is taken?
        :param center:
        :param radius:
        :return:
        """
        next_position = self.step()

        return len(
            Vector(px=center,
                   py=(next_position.vx, next_position.vy)
            )
        ) > radius

    def scale_for_temp(self):
        """
        Increase the particle velocity by a given factor
        """
        self.velocity.vx *= self.factor
        self.velocity.vy *= self.factor
