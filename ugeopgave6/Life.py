class Life:
    state = {}

    imin = 0
    imax = 0
    jmin = 0
    jmax = 0

    def __init__(self, imin, imax, jmin, jmax):
        self.imin = imin
        self.imax = imax
        self.jmin = jmin
        self.jmax = jmax

    def foerste(self):
        """
        :return:
        """
        for i in range(self.imin, self.imax):
            for j in range(self.jmin, self.jmax):
                self.state[(i, j)] = False

                if (i, j) in [(10, 6), (10, 7), (10, 8), (9, 8), (8, 7)]:
                    self.state[(i, j)] = True
                #if (i, j) in [(0, 0), (0, 1), (1, 0)]:
                #    self.state[(i, j)] = True

        return self.imin, self.imax, self.jmin, self.jmax

    def naeste(self):
        """
        :return:
        """
        next_state = {}

        # now we can iterate over all (i,j) nodes
        for i in range(self.imin, self.imax):
            for j in range(self.jmin, self.jmax):
                # find all connected edge nodes
                edges = self.find_edges(i, j)
                edges_alive = 0

                for x, y in edges:
                    if self.state[(x, y)]:
                        edges_alive += 1

                if edges_alive in [2, 3] and self.state[(i, j)]:
                    # survive next state
                    next_state[(i, j)] = True  # Should already be True?
                elif edges_alive is 3 and not self.state[(i, j)]:
                    # survice next state
                    next_state[(i, j)] = True
                else:
                    next_state[(i, j)] = False

        self.state = next_state

        return self.imin, self.imax, self.jmin, self.jmax

    def levende(self, i, j):
        """
        :return:
        """
        return self.state[(i, j)]

    def find_edges(self, i, j):
        """
        Returns the edge nodes connected to (i,j),
        which exists inside of our coordinate set.
        Returns at most 8 edges.
        :param i:
        :param j:
        """
        potential_edges = [
            (i - 1, j + 1),
            (i, j + 1),
            (i + 1, j + 1),
            (i - 1, j),
            # (i, j),
            (i + 1, j),
            (i - 1, j - 1),
            (i, j - 1),
            (i + 1, j - 1)
        ]

        real_edges = []
        for x, y in potential_edges:
            if self.imax > x >= self.imin \
                    and self.jmax > y >= self.jmin\
                    and (x, y) not in real_edges:
                real_edges += [(x, y)]

        return real_edges