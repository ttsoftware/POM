
class Container(object):

    r = 0.0
    c = ()
    particles = []

    def __init__(self, r, c=(0.0, 0.0), particle_count=0):
        self.r = r
        self.c = c