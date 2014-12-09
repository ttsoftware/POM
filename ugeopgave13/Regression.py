from Dataset import Dataset


class Regression:

    data = Dataset()

    def __init__(self, data):
        self.data = data

    def regress(self):
        sak = self.sak()
        sap = self.sap()

        a = sap / sak

        x_avg = self.x_average()
        y_avg = self.y_average()

        return lambda x: a * (x - x_avg) + y_avg

    def linearAnalysis(self):

        f = self.regress()

        x_min = min(self.data.get_x_values())
        x_max = max(self.data.get_x_values())

        return (x_min, x_max), (f(x_min), f(x_max))

    def x_average(self):
        x_values = self.data.get_x_values()
        return sum(x_values) / len(x_values)

    def y_average(self):
        y_values = self.data.get_y_values()
        return sum(y_values) / len(y_values)

    def sak(self):
        x_avg = self.x_average()
        sak = 0
        for x in self.data.get_x_values():
            sak += (x - x_avg) ** 2
        return sak

    def sap(self):
        x_avg = self.x_average()
        sap = 0
        for x in self.data.get_x_values():
            sap += (x - x_avg) * self.data.get(x)
        return sap