import matplotlib.pyplot as plt


class ContainerVisualiser(object):

    container = None

    def __init__(self, container):
        self.container = container

    def animate(self, time_amount):

        plt.ion()
        fig = plt.figure()

        for t in range(0, time_amount):

#            plt.clf()  # remove to see particle path

            barrier = plt.Circle(xy=(0, 0), radius=self.container.radius, color='r', fill=False)
            fig.gca().add_artist(barrier)

            for p in self.container.particles:
                p.take_step(self.container.center, self.container.radius)

                plt.plot(p.position.vx, p.position.vy, ".")  # plot particle p at time t

                # define axes lengths
                plt.xlim(-self.container.radius, self.container.radius)
                plt.ylim(-self.container.radius, self.container.radius)

            plt.draw()

        plt.ioff()