from aircraft_class import *


class Planes(Aircraft):
    def __init__(self, planenum = '', planetype=''):
        super().__init__()
        self.planenum = planenum
        self.planetype = planetype
        self.wings = True
        self.jets = True

    def glide(self):
        return 'woah, im like flying, without flying, woah'





