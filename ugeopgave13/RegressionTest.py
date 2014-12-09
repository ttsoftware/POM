import unittest
import matplotlib.pyplot as plt
import numpy as np

from Dataset import Dataset
from Regression import Regression


class RegressionTest(unittest.TestCase):

    def test_linearAnalysis(self):
        set = Dataset()
        set.read_data_points("flueaeg.txt")

        reg = Regression(set)

        xs = reg.linearAnalysis()

        self.assertEqual(
            ((46.0, 100.0), (23.42909090909091, 16.550909090909094)),
            xs
        )

    def test_plot_regress(self):
        set = Dataset()
        set.read_data_points("flueaeg.txt")
 
        reg = Regression(set)

        f = reg.regress()

        (xmin, xmax), (f_xmin, f_xmax) = reg.linearAnalysis()

        xs = np.linspace(
            xmin,
            xmax
        )
        ys = []
        for x in xs:
            ys += [f(x)]

        plt.plot(set.get_x_values(), set.get_y_values(), 'ro')
        plt.plot(xs, ys, 'b-')
        plt.axis([xmin, xmax, f_xmax, f_xmin])
        plt.show()

if __name__ == '__main__':
    unittest.main()
