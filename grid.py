import pygame
import random

# TILES
DIRT_0 = 0
DIRT_1 = 1
GRASS_0 = 2
GRASS_1 = 3
GRASS_2 = 4
WATER_0 = 5
WATER_1 = 6
WATER_2 = 7
WALL = 8
TREE_0 = 9
TREE_1 = 10
TREE_2 = 11

class Tree:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./textures/trees/tree.png'), (125, 125))
        self.X_POS = random.randint(50, 300)
        self.Y_POS = random.randint(50, 450)

class TEMPLE:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./sprites/temple.png'), (250, 250))
        self.X_POS = 6
        self.Y_POS = 1

num_trees = 15
trees = [Tree() for x in range (num_trees)]

# DICTIONARY LINKING TILES TO THEIR COLORS pygame.image.load('pic.png')
TEXTURES = {
    DIRT_0: pygame.image.load('./textures/dirt0.png'),
    DIRT_1: pygame.image.load('./textures/dirt1.png'),
    GRASS_0: pygame.image.load('./textures/grass0.png'),
    GRASS_1: pygame.image.load('./textures/grass1.png'),
    GRASS_2: pygame.image.load('./textures/grass2.png'),
    WATER_0: pygame.image.load('./textures/water0.png'),
    WATER_1: pygame.image.load('./textures/water1.png'),
    WATER_2: pygame.image.load('./textures/water4.png'),
    WALL: pygame.image.load('./textures/wall.png'),
    TREE_0: pygame.image.load('./textures/trees/tree.png'),
    TREE_1: pygame.image.load('./textures/trees/tree_1.png'),
}

# TILES TO BE DISPLAYED
GRID = [
    [GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_2, GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_2, GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_2, GRASS_0, WATER_0, WATER_1, WATER_0],
    [GRASS_0, GRASS_2, GRASS_0, GRASS_0, DIRT_1, DIRT_0, DIRT_1, DIRT_0, DIRT_1, DIRT_0, DIRT_0, DIRT_1, DIRT_0, GRASS_0, GRASS_0, WATER_0, WATER_1, WATER_0, WATER_0, WATER_0],
    [GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_0, DIRT_0, DIRT_1, DIRT_0, DIRT_0, GRASS_0, GRASS_0, GRASS_0, GRASS_2, GRASS_0, WATER_1, WATER_1, WATER_2, GRASS_0, GRASS_0],
    [GRASS_2, GRASS_0, GRASS_0, GRASS_2, DIRT_0, DIRT_0, DIRT_1, DIRT_0, DIRT_0, DIRT_0, GRASS_0, GRASS_0, GRASS_0, WATER_0, WATER_0, WATER_0, WATER_1, GRASS_0, GRASS_2, GRASS_0],
    [GRASS_0, DIRT_1, DIRT_0, DIRT_0, DIRT_0, DIRT_0, DIRT_1, DIRT_0, DIRT_1, DIRT_1, GRASS_0, GRASS_0, GRASS_0, WATER_0, WATER_1, GRASS_0, GRASS_2, GRASS_0, GRASS_0, GRASS_0],
    [DIRT_1, DIRT_0, DIRT_0, DIRT_1, DIRT_0, DIRT_1, DIRT_1, DIRT_0, DIRT_0, DIRT_0, DIRT_0, DIRT_1, DIRT_0, WATER_0, WATER_1, WATER_1, WATER_0, GRASS_0, GRASS_2, GRASS_0],
    [DIRT_0, DIRT_1, DIRT_0, DIRT_0, DIRT_1, DIRT_0, DIRT_0, DIRT_1, DIRT_0, DIRT_1, DIRT_1, WATER_0, WATER_1, WATER_2, WATER_0, WATER_1, WATER_0, WATER_0, GRASS_0, GRASS_0],
    [GRASS_0, GRASS_2, GRASS_0, GRASS_2, DIRT_0, DIRT_1, DIRT_0, DIRT_0, DIRT_0, DIRT_0, DIRT_0, WATER_0, WATER_0, WATER_0, WATER_0, WATER_0, WATER_0, GRASS_0, GRASS_2, GRASS_0],
    [GRASS_2, GRASS_0, GRASS_0, GRASS_0, DIRT_0, DIRT_0, DIRT_0, DIRT_1, DIRT_0, DIRT_1, DIRT_0, WATER_1, WATER_1, WATER_1, WATER_0, WATER_2, WATER_1, WATER_0, GRASS_0, GRASS_0],
    [GRASS_0, GRASS_0, GRASS_2, GRASS_0, DIRT_0, DIRT_1, DIRT_0, DIRT_0, DIRT_1, DIRT_0, DIRT_0, WATER_0, WATER_0, WATER_0, WATER_0, WATER_1, WATER_0, WATER_0, WATER_0, GRASS_2]
]

# GAME DIMENSIONS, CONFIG
TILESIZE = 50
MAPWIDTH = 20
MAPHEIGHT = 10 
pygame.init()
pygame.display.set_caption('LINKS ADVENTURE')
# MAPHEIGHT + 125 for inventory
DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

# COLORS
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)
GREEN = (60, 179, 113)
RED = (178, 0, 0)