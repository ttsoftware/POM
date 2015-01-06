import numpy as np
from Vector import Vector


class Particle(object):

    position = None
    velocity = None
    mass = 10**-23

    def __init__(self, positionx, positiony, velocityx, velocityy):
        self.position = Vector(vx=positionx, vy=positiony)
        self.velocity = Vector(vx=velocityx, vy=velocityy)

    def step(self):
        return Vector(
            vx=self.position.vx + 1*self.velocity.vx,
            vy=self.position.vy + 1*self.velocity.vy
        )

    def take_step(self, center, radius):
        if not self.willcollide(center, radius):
            print "we took a step jaaaa"
            self.position = self.step()

    def willcollide(self, center, radius):
        next_position = self.step()

        return len(
            Vector(p1=center,
                   p2=(next_position.vx, next_position.vy)
            )
        ) > radius