import unittest
from Container import Container


class ContainerTest(unittest.TestCase):

    def test_simulation(self):

        container = Container(radius=100, particle_count=1)

        for t in range(0, 5):

            for p in container.particles:

                p.take_step(container.center, container.radius)

                print p.position