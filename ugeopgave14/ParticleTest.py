import unittest
from Particle import Particle


class DatasetTest(unittest.TestCase):

    def test_init(self):

        p = Particle(0, 0, 0, 0)

        print len(p.position)