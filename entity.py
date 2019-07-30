class Entity(object):
    w = 0
    h = 0
    x = 0
    y = 0
    c = 0x111111ff
    wrap = False
    children = []
        
    def __init__(self, width, height, xPos, yPos, color, wrap = None):
        self.w = width
        self.h = height
        self.x = xPos
        self.y = yPos
        self.c = color
        self.children = []
        
        if wrap != None:
            self.wrap = wrap
            
    def __add__(self, child):
        self.children.append(child)
        
        return self