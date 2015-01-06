from __future__ import division
import math
import random
from Particle import Particle


class Container(object):

    VMAX = 10
    radius = 0.0
    center = 0.0, 0.0
    particles = []

    def __init__(self, radius, particle_count=0):
        self.radius = radius

        for i in range(0, particle_count):

            position_x = random.randint(-self.radius, self.radius)
            max_y = math.floor(math.sqrt(radius**2 - position_x**2))

            position_y = random.randint(-max_y, max_y)

            angle = random.randint(0, round(2 * math.pi))
            velocity = random.randint(1, self.VMAX)

            p = Particle(
                positionx=position_x,
                positiony=position_y,
                velocityx=velocity * math.cos(angle),
                velocityy=velocity * math.sin(angle)
            )

            self.particles += [p]