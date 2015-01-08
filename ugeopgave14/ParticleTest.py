import unittest
from Particle import Particle


class DatasetTest(unittest.TestCase):

    def test_init(self):

        p = Particle(0, 0, 0, 0)

        print len(p.position)

    def test_step1(self):

        p = Particle(
            -83.3685483757,
            -56.9606215782,
            -5.71920888457,
            -1.81401481103
        )

        p.take_step((0, 0), 100)

    def test_step2(self):

        p = Particle(
            5.27467021743,
            -9.44845648513,
            -0.280971148454,
            -0.95971621521
        )

        p.take_step((0, 0), 10)

    def test_step3(self):

        p = Particle(
            -20.9750481543,
            88.6462764876,
            -3.32917469238,
            7.27437941461
        )

        print p.position, p.velocity

        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)

        # we definetly moved away from the barrier
        print p.position, p.velocity

        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)
        p.take_step((0, 0), 100)

        # we hit the barrier again!
        print p.position, p.velocity
        p.scale_for_temperature(0.5)
        print p.position, p.velocity