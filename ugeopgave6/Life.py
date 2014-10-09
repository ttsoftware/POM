

class Life:

    state = []
    imin = 0
    imax = 0
    jmin = 0
    jmax = 0

    def __init__(self, imin, imax, jmin, jmax):
        self.imin = imin
        self.imax = imax
        self.jmin = jmin
        self.jmax = jmax
        pass

    def foerste(self):
        """
        :return:
        """

        for i in range(self.imin, self.imax):
            pass

        return self.imin, self.imax, self.jmin, self.jmax

    def naeste(self):
        """
        :return:
        """
        return 0, 0, 0, 0

    def levende(self):
        """
        :return:
        """
        return 0, 0, 0, 0