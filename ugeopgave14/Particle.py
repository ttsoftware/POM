import numpy as np
from Vector import Vector


class Particle(object):

    position = None
    velocity = None
    mass = 10**-23

    def __init__(self, positionx, positiony, velocityx, velocityy):
        self.position = Vector(vx=positionx, vy=positiony)
        self.position = Vector(vx=velocityx, vy=velocityy)

    def step(self, delta_t):
        self.position = Vector(
            vx=self.position.vx + delta_t*self.velocity.vx,
            vy=self.position.vy + delta_t*self.velocity.vy
        )