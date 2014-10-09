# -*- coding: utf-8 -*-
"""
    Vi har valgt at
"""


class Life:
    state = {}
    init_alive = []

    imin = 0
    imax = 0
    jmin = 0
    jmax = 0

    def __init__(self, imin, imax, jmin, jmax, init_alive):
        """
        Initialize the static grid, and define which nodes are alive initially
        :param imin:
        :param imax:
        :param jmin:
        :param jmax:
        :param init_alive:
        """
        self.imin = imin
        self.imax = imax
        self.jmin = jmin
        self.jmax = jmax
        self.init_alive = init_alive

    def foerste(self):
        """
        Modifies the state to reflect self.init_alive.
        Returns the static grid.
        :return:
        """
        for i in range(self.imin, self.imax):
            for j in range(self.jmin, self.jmax):
                self.state[(i, j)] = False
                if (i, j) in self.init_alive:
                    self.state[(i, j)] = True
        return self.imin, self.imax, self.jmin, self.jmax

    def naeste(self):
        """
        Modifies the state and kills/revives according to the two given rules
        Returns the static grid
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
                    # die if no rule applies
                    next_state[(i, j)] = False

        self.state = next_state

        return self.imin, self.imax, self.jmin, self.jmax

    def levende(self, i, j):
        """
        Returns whether or not the given node (i,j) is alive
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