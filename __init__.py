import time
import rgb
from .renderer import Renderer
from .entity import Entity
from .player import Player
from .perlin import Perlin1D

genned = 0
def gen(x):
    global perlin
    global world
    global genned
    global w
    
    if x <= genned:
        return
        
    genned += w

    overflow = 0
    for i in range(x, x + w):
        if overflow > 0:
            overflow -= 1
        
        n = perlin(i)
        
        if n == -1 and overflow == 0:
            void = Entity(3, 2, i, h - 2, colors['void'])
            world += void
            overflow = 4
        elif n == 1 and overflow == 0:
            block = Entity(1, 1, i, 5, colors['grass'])
            world += block
        elif n == 2 and overflow == 0:
            block = Entity(1, 2, i, 4, colors['pipe'])
            world += block
            overflow = 3
        elif n == 3:
            block = Entity(1, 1, i, 3, colors['block'])
            world += block
        elif n == 4:
            block = Entity(1, 1, i, 2, colors['block'])
            world += block

#Defenitions
w = 32
h = 8
colors = {
    'sky': 0x087c80ff,
    'sun': 0xffee4fff,
    'coin': 0xe3cd05ff,
    'pipe': 0x00ff00ff,
    'void': 0x111111ff,
    'mario': 0xff0000ff,
    'block': 0xa36a08ff,
    'cloud': 0xccccccff,
    'grass': 0x005500ff,
    'ground': 0x634004ff,
}

#Create entities
mario = Player(1, 1, 5, h - 3, colors['mario'])
sun = Entity(3, 3, w - 4, 1, colors['sun'])
grass = Entity(w, 1, 0, h - 2, colors['grass'])
ground = Entity(w, 1, 0, h - 1, colors['ground'])
world = Entity(0, 0, 0, 0, 0x00000000)
clouds = [
    Entity(3, 2,  2, 1, colors['cloud'], True),
    Entity(3, 2,  9, 0, colors['cloud'], True),
    Entity(3, 2, 17, 1, colors['cloud'], True),
    Entity(3, 2, 25, 2, colors['cloud'], True),
]

for cloud in clouds:
    world += cloud

perlin = Perlin1D()

gen(10)

#Create renderer        
renderer = Renderer(w, h, colors['sky'])
renderer += sun
renderer += grass
renderer += ground
renderer += world
renderer += mario


            
i = 0
while True:
    if i == 0:
        for cloud in clouds:
            cloud.x = (cloud.x - 1) % w
            
    if ((-1 * world.x) % w) == 10:
        gen((-1 * world.x) + w)
        
    world.x = world.x - mario.velocity['x']
        
    renderer.render()
    
    i = (i + 1) % 10
    
    time.sleep(.1)
