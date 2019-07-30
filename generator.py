from .perlin import Perlin1D

class Generator(object):
    w = 0
    p = None
    c = None
    perlin = None
    genned = 0

    def __init__(self, witdh, parent, callable):
        self.w = witdh
        self.c = callable
        self.p = parent
        self.perlin = Perlin1D()
        self.genned = 0

    def __call__(self, x):        
        if x <= self.genned:
            return
            
        self.genned += self.w

        overflow = 0
        for i in range(x, x + self.w):
            if overflow > 0:
                overflow -= 1
            
            n = self.perlin(i)
            
            e, o = self.c(i, n, overflow);
            
            if e != None:
                self.p += e
                
            if o != None:
                overflow = o