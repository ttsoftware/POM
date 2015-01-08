import unittest
from Container import Container


class ContainerTest(unittest.TestCase):

    def test_simulation(self):

        container = Container(radius=10, particle_count=1)

        for t in range(0, 100):

            for p in container.particles:

                print "Particle: " + p.position.__str__() + ", " + p.velocity.__str__()

                p.take_step(container.center, container.radius)


    def test_pressure(self):
        container = Container(radius=10, particle_count=10)

        for t in range(0, 4):

            for p in container.particles:

                #print "Particle: " + p.position.__str__() + ", " + p.velocity.__str__()

                p.take_step(container.center, container.radius)

            print container.pressure()