# coding=utf-8
from __future__ import division
from Dataset import Dataset


class Regression(object):

    data = Dataset()
    _sak = 0
    _sap = 0

    def __init__(self, data):
        self.data = data

    def regress(self):
        """
        Return the regression function
        :return lambda:
        """
        a = self.sap / self.sak

        x_avg = self.x_average()
        y_avg = self.y_average()

        return lambda x: a * (x - x_avg) + y_avg

    def linearAnalysis(self):
        """
        Return the xmin, xmax from the dataset and from our regression.
        :return ((float,float),(float,float)):
        """
        f = self.regress()

        x_min = min(self.data.get_x_values())
        x_max = max(self.data.get_x_values())

        return (x_min, x_max), (f(x_min), f(x_max))

    def x_average(self):
        """
        Average over x
        :return:
        """
        x_values = self.data.get_x_values()
        return sum(x_values) / len(x_values)

    def y_average(self):
        """
        Average over y
        :return:
        """
        y_values = self.data.get_y_values()
        return sum(y_values) / len(y_values)

    @property
    def sak(self):
        """
        Calculate SAK
        :return:
        """
        x_avg = self.x_average()
        for x in self.data.get_x_values():
            self._sak += (x - x_avg) ** 2
        return self._sak

    @property
    def sap(self):
        """
        Calculate SAP
        :return:
        """
        x_avg = self.x_average()
        for x in self.data.get_x_values():
            self._sap += (x - x_avg) * self.data[x]
        return self._sap