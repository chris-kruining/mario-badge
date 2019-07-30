import time
import rgb
from .renderer import Renderer
from .entity import Entity
from .player import Player
from .generator import Generator

#Defenitions
w = 32
h = 8
framerate = 30
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


def generatorCallback(i, n, o):
    global h
    global colors

    if n == -1 and o == 0:
        return Entity(3, 2, i, h - 2, colors['void']), 4
    elif n == 1 and o == 0:
        return Entity(1, 1, i, 5, colors['grass']), None
    elif n == 2 and o == 0:
        return Entity(1, 2, i, 4, colors['pipe']), 3
    elif n == 3:
        return Entity(1, 1, i, 3, colors['block']), None
    elif n == 4:
        return Entity(1, 1, i, 2, colors['block']), None
    else:
        return None, None

#Create entities
mario = Player(1, 1, 5, h - 3, colors['mario'])
sun = Entity(3, 3, w - 3, 0, colors['sun'])
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
gen = Generator(w, world, generatorCallback)

#Create renderer        
renderer = Renderer(w, h, colors['sky'])
renderer += sun
renderer += grass
renderer += ground
renderer += world
renderer += mario

#Generate first part
gen(10)
            
i = 0
while True:
    #"Animate" clouds
    i = (i + 1) % framerate
    if i == 0:
        for cloud in clouds:
            cloud.x = (cloud.x - 1) % w
    
    #Generate next part when 10 pixels before end
    if ((-1 * world.x) % w) == 10:
        gen((-1 * world.x) + w)
        
    #Move world oposite to mario to "walk"
    world.x = world.x - mario.velocity['x']
        
    #Render next frame
    renderer.render()
    
    time.sleep(1 / framerate)
