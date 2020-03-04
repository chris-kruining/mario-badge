import rgb

class Renderer:
    stack = []
    w = 0
    h = 0
    bg = 0x00000000
    
    def __init__(self, width, height, background):
        rgb.disablecomp()
        self.w = width
        self.h = height
        self.bg = background
        self.stack = []
        
    def __add__(self, entity):
        self.stack.append(entity)
        
        return self
        
    def _render(self, frame, offset, entities):
        for entity in entities:
            ex = entity.x + offset[0]
            ey = entity.y + offset[1]
        
            for y in range(ey, ey + entity.h):
                if y >= self.h or y < 0:
                    continue
            
                for x in range(ex, ex + entity.w):
                    if entity.wrap == False && x >= self.w or x < 0:
                        continue
                    elif entity.wrap == True:
                        frame[ (y * self.w) + (x % self.w)] = entity.c
                    else:
                        frame[ (y * self.w) + x] = entity.c
            
            if len(entity.children) > 0:
                self._render(frame, (ex, ey), entity.children)

    def render(self):
        rgb.clear()
        
        #Draw background
        frame = [self.bg]*(self.w * self.h)
        
        #Draw entities
        self._render(frame, (0, 0), self.stack)
        
        #Push frame to buffer
        rgb.frame(frame)
