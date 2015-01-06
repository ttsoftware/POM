import unittest
from Particle import Particle


class DatasetTest(unittest.TestCase):

    def test_init(self):

        p = Particle(0, 0, 0, 0)

        print len(p.position)


    def test_step(self):

        p = Particle(
            -40.9750481543,
            88.6462764876,
            -3.32917469238,
            7.27437941461
        )

        p.take_step((0,0), 100)