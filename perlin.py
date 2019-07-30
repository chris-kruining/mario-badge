import math
import random

class Perlin1D(object):
    #def __init__(self): pass

    def __call__(self, point):
        return round(random.uniform(-1, 4))