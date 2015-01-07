import unittest
from ContainerVisualiser import ContainerVisualiser
from Container import Container


class ContainerVisualiserTest(unittest.TestCase):

    def test_animate(self):

        container = Container(radius=100, particle_count=10)

        visualiser = ContainerVisualiser(container)
        visualiser.animate(100)