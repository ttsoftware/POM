import unittest
from ContainerVisualiser import ContainerVisualiser
from Container import Container


class ContainerVisualiserTest(unittest.TestCase):

    def test_animate(self):

        container = Container(radius=100, particle_count=10)

        visualiser = ContainerVisualiser(container)
        visualiser.animate(1000)

    def test_animate2(self):

        container = Container(radius=1000, particle_count=100)
        print container.average_velocity()
        container.temp_avg_velocity(300)
        print container.average_velocity()
        visualiser = ContainerVisualiser(container)
        visualiser.animate(1000)
