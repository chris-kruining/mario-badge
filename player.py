import buttons
import defines
from .entity import Entity

class Player(Entity):
    velocity = {'x':0, 'y':0}
    
    def __init__(self, width, height, xPos, yPos, color):
        super().__init__(width, height, xPos, yPos, color)
        
        buttons.register(defines.BTN_A, self._up)
        buttons.register(defines.BTN_LEFT, self._left)
        buttons.register(defines.BTN_RIGHT, self._right)
        
    def applyForce(self, x, y):
        self.velocity['x'] = x
        self.velocity['y'] = y
        
    def tick(self): pass
        
    def _up(self, is_down): self.y += (-2 if is_down else 2)
        
    def _left(self, is_down): self.velocity['x'] = (-1 if is_down else 0)
        
    def _right(self, is_down): self.velocity['x'] = (1 if is_down else 0)