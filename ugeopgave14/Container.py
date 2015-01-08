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


    def average_velocity(self):

        avgVelocity = 0

        for particle in self.particles:
            # use absolute value due to the
            avgVelocity += math.sqrt(particle.velocity.vx**2 + particle.velocity.vy**2)

        return avgVelocity / len(self.particles)

    def pressure(self):

        n = len(self.particles)
        m = 10 ** -23
        v = self.average_velocity()
        a = math.pi * (self.radius**2)

        pressure = (n * m * (v**2))/(2 * a)
        return pressure

    def temp_avg_velocity(self, temp):
        m = 10 ** -23
        kb = 1.380658 * (10**-23)
        avg_velocity_factor = math.sqrt((temp * 2 * kb) / m)
        print avg_velocity_factor
        self.update_velocity(avg_velocity_factor)

    def update_velocity(self, factor):

        for p in self.particles:
            p.factor = factor
            p.scale_for_temp()