from unittest import TestCase
from Life import Life
from kursusuge6modul import visLife


class LifeTest(TestCase):

    alive = [(10, 9), (10, 8), (10, 7),
             (9, 9), (9, 8), (9, 7),
             (8, 9), (8, 8), (8, 7),
             (7, 9), (7, 8), (7, 7),
             (6, 9), (6, 8), (6, 7),
             (5, 9), (5, 8), (5, 7),
             (4, 9), (4, 8), (4, 7),
             (3, 9), (3, 8), (3, 7),
             (2, 9), (2, 8), (2, 7),
             (1, 9), (1, 8), (1, 7),
             (0, 9), (0, 8), (0, 7)]

    def test_foerste(self):

        l = Life(0, 20, 0, 20, self.alive)
        xmin, xmax, ymin, ymax = l.foerste()

        self.assertEqual(xmin, 0)
        self.assertEqual(xmax, 20)
        self.assertEqual(ymin, 0)
        self.assertEqual(xmax, 20)

    def test_naeste(self):

        l = Life(0, 20, 0, 20, self.alive)
        l.foerste()
        xmin, xmax, ymin, ymax = l.naeste()

        self.assertEqual(xmin, 0)
        self.assertEqual(xmax, 20)
        self.assertEqual(ymin, 0)
        self.assertEqual(xmax, 20)

    def test_levende(self):

        l = Life(0, 20, 0, 20, self.alive)
        l.foerste()

        self.assertEqual(l.levende(10, 9), True)

    def test_find_edges(self):
        l = Life(0, 20, 0, 20, self.alive)
        l.foerste()

        self.assertEqual(l.find_edges(0, 0), [(0, 1), (1, 1), (1, 0)])

    def test_integration(self):
        l = Life(0, 20, 0, 20, self.alive)
        visLife(l.foerste, l.naeste, l.levende)