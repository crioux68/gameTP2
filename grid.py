#these are the import and library required for the map technologie to work properly.
#more may be added with time.
import pygame
import pytmx
from pytmx import load_pygame

#the list of change and bug is in the top of the README.md in the changement_map branch.

#The map is required for it to work
#All the textures added to the textures file need to be there for the map to be properly read.
#Also the texture name must not be change for the existing one otherwise the map will get corrupted.


#This is the config from the config file and can be remove before the integration with the main branch
######################################################################################################
TILESIZE = 50
MAPWIDTH = 30
MAPHEIGHT = 20
pygame.init()
pygame.display.set_caption('LINKS ADVENTURE')
######################################################################################################

#The class for the TILE extention
class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)


#This is for testing purpose and will be remove when it will work with the main file
######################################################################################
pygame.init()
screen = pygame.display.set_mode((MAPWIDTH * TILESIZE,MAPHEIGHT * TILESIZE))
#Load all the data from the map file(object,tiles,layers...)
tmx_data = load_pygame("map.tmx")
#The sprite group for the screen rendering
spriteGroup = pygame.sprite.Group()
######################################################################################

#For loop, for layering the map data on the screen (this is for the tiles and not the object in the map.tmx file)
for layer in tmx_data.visible_layers:
    #The hasattr fonction is for the (has attribute) in the map data(tmx_data)
    if hasattr(layer,"data"):
        for x,y,surf in layer.tiles():
          #Set the position of the tiles in pixel (each tile is 50x50 px)
          pos= (x * 50,y * 50) 
          #This fonction place the tile on the screen
          Tile(pos= pos,surf= surf, groups= spriteGroup)
# This loop look for the onject in the tmx_data variable
for obj in tmx_data.objects:
    #We directly get the x and y position in px from the map so we don't have to multiplies them by 50px
    pos = (obj.x , obj.y)
    #If the object have an image we will render it otherwise we will not cause it will crash
    if obj.image:
        #This fonction place the object on the screen
        Tile(pos = pos, surf = obj.image, groups = spriteGroup)

# This is for testing purpose and will be remove when it will work with the main file
######################################################################################
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("black")
    spriteGroup.draw(screen)
    pygame.display.update()
######################################################################################



#All this code is the old code from the main branch, we didn't remove it for now but when the intergration is complete it can be remove.
########################################################################################################################################

"""
# TILES
DIRT_0 = 0
DIRT_1 = 1
GRASS_0 = 2
GRASS_1 = 3
GRASS_2 = 4
GRASS_3 = 5
GRASS_4 = 6
WATER_0 = 7
WATER_1 = 8
WATER_2 = 9
WALL = 10
TREE_0 = 11
TREE_1 = 12
TREE_2 = 13
FLOOR_0 = 14
FLOOR_1 = 15
FLOOR_2 = 16
FLOOR_3 = 17
FLOOR_4 = 18
FLOOR_5 = 19
FLOOR_6 = 20
FLOOR_7 = 21
FLOOR_8 = 22

# Class to initialize trees and their positions on the board
class Tree:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./textures/trees/tree.png'), (75, 75))
        self.X_POS = 90
        self.Y_POS = 360
        self.rect = pygame.rect.Rect(self.X_POS, self.Y_POS, 75, 75)

class Tree2:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./textures/trees/tree.png'), (75, 75))
        self.X_POS = 50
        self.Y_POS = 80
        self.rect = pygame.rect.Rect(self.X_POS, self.Y_POS, 75, 75)

class Tree3:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./textures/trees/tree.png'), (75, 75))
        self.X_POS = 600
        self.Y_POS = 25
        self.rect = pygame.rect.Rect(self.X_POS, self.Y_POS, 75, 75)        
    
# Class to initialize the temple and its position on the board   
class TEMPLE:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./sprites/temple.png'), (400, 255))
        self.X_POS = 3
        self.Y_POS = 0
        self.rect = pygame.rect.Rect(self.X_POS+320, self.Y_POS+165, 60, 60)

# Class to initialize the chest and its position on the board  
class CHEST():
    def __init__(self):
        # LOCATION OF THE CHEST SPRITE
        self.SPRITE = pygame.transform.scale(pygame.image.load('./sprites/chest_0.png'), (50, 50))
        # POSITION OF THE CHEST ON THE GRID
        self.X_POS = 8
        self.Y_POS = 8
        # CREATE CHEST COLLISION
        self.rect = pygame.rect.Rect(self.X_POS * TILESIZE, self.Y_POS * TILESIZE, 50, 50)

# Class to initialize the START button
class BTNStart():
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./textures/boutons/boutonStart.png'), (150, 75))
        self.X_POS = 425
        self.Y_POS = 125
        self.rect = pygame.rect.Rect(self.X_POS, self.Y_POS, 150, 75)

# Class to initialize the QUIT button
class BTNQuit():
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./textures/boutons/boutonQuit.png'), (150, 75))
        self.X_POS = 425
        self.Y_POS = 230
        self.rect = pygame.rect.Rect(self.X_POS, self.Y_POS, 150, 75)

# Class to initialize the OPTIONS button
class BTNOptions():
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./textures/boutons/boutonOptions.png'), (150, 75))
        self.X_POS = 0
        self.Y_POS = 0
        self.rect = pygame.rect.Rect(self.X_POS, self.Y_POS, 250, 75)

# Class to initialize the RESTART button
class BTNRestart():
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./textures/boutons/boutonRestart.png'), (150, 75))
        self.X_POS = 425
        self.Y_POS = 125
        self.rect = pygame.rect.Rect(self.X_POS, self.Y_POS, 150, 75)        
        

# Command to generate the tree
num_trees = 2
trees = [Tree() for x in range (num_trees)]
trees2 = [Tree2() for x in range (num_trees)]
trees3 = [Tree3() for x in range (num_trees)]

# DICTIONARY LINKING TILES TO THEIR COLORS pygame.image.load('pic.png')
TEXTURES = {
    DIRT_0: pygame.image.load('./textures/dirt0.png'),
    DIRT_1: pygame.image.load('./textures/dirt1.png'),
    GRASS_0: pygame.image.load('./textures/grass0.png'),
    GRASS_1: pygame.image.load('./textures/grass1.png'),
    GRASS_2: pygame.image.load('./textures/grass2.png'),
    GRASS_3: pygame.image.load('./textures/grass3.png'),
    GRASS_4: pygame.image.load('./textures/grass4.png'),
    WATER_0: pygame.image.load('./textures/water0.png'),
    WATER_1: pygame.image.load('./textures/water1.png'),
    WATER_2: pygame.image.load('./textures/water2.png'),
    WALL: pygame.image.load('./textures/wall.png'),
    TREE_0: pygame.image.load('./textures/trees/tree.png'),
    TREE_1: pygame.image.load('./textures/trees/tree_1.png'),
    FLOOR_0: pygame.image.load('./textures/floor0.png'),
    FLOOR_1: pygame.image.load('./textures/floor1.png'),
    FLOOR_2: pygame.image.load('./textures/floor2.png'),
    FLOOR_3: pygame.image.load('./textures/floor3.png'),
    FLOOR_4: pygame.image.load('./textures/floor4.png'),
    FLOOR_5: pygame.image.load('./textures/floor5.png'),
    FLOOR_6: pygame.image.load('./textures/floor6.png'),
    FLOOR_7: pygame.image.load('./textures/floor7.png'),
    FLOOR_8: pygame.image.load('./textures/floor8.png')
}

# Tiles for the outside(beginning)
GRID_OVERWORLD = [
    [GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_2, GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_2, GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_2, GRASS_4, GRASS_3, WATER_0, WATER_1, WATER_0],
    [GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_2, GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_2, GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_2, GRASS_4, GRASS_3, WATER_0, WATER_1, WATER_0],
    [GRASS_0, GRASS_2, GRASS_0, GRASS_0, DIRT_1, DIRT_0, DIRT_1, DIRT_0, DIRT_1, DIRT_0, DIRT_0, GRASS_0, GRASS_0, GRASS_0, GRASS_1, WATER_0, WATER_1, WATER_0, WATER_0, WATER_0],
    [GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_0, GRASS_0, DIRT_0, DIRT_1, DIRT_0, DIRT_0, DIRT_0, GRASS_0, GRASS_2, GRASS_4, GRASS_3, WATER_1, WATER_1, WATER_2, WATER_0, WATER_0],
    [GRASS_2, GRASS_0, GRASS_0, GRASS_2, DIRT_0, DIRT_0, DIRT_1, DIRT_0, DIRT_0, DIRT_0, DIRT_0, GRASS_0, GRASS_1, WATER_0, WATER_0, WATER_0, WATER_1, WATER_0, WATER_0, WATER_0],
    [GRASS_0, DIRT_1, DIRT_0, DIRT_0, DIRT_0, DIRT_0, DIRT_1, DIRT_0, DIRT_1, DIRT_1, DIRT_0, GRASS_0, GRASS_1, WATER_0, WATER_1, WATER_0, WATER_0, WATER_0, WATER_0, WATER_2],
    [GRASS_0, GRASS_0, DIRT_0, DIRT_1, DIRT_0, DIRT_1, DIRT_1, DIRT_0, DIRT_0, DIRT_0, DIRT_0, GRASS_4, GRASS_3, WATER_0, WATER_1, WATER_1, WATER_0, WATER_0, WATER_0, WATER_0],
    [GRASS_0, DIRT_1, DIRT_0, DIRT_0, DIRT_1, DIRT_0, DIRT_0, DIRT_1, DIRT_0, DIRT_1, GRASS_1, WATER_0, WATER_1, WATER_2, WATER_0, WATER_1, WATER_0, WATER_2, WATER_0, WATER_0],
    [GRASS_0, GRASS_2, GRASS_0, GRASS_2, DIRT_0, DIRT_1, DIRT_0, DIRT_0, DIRT_0, GRASS_0, GRASS_1, WATER_0, WATER_0, WATER_0, WATER_0, WATER_0, WATER_0, WATER_0, WATER_1, WATER_0],
    [GRASS_2, GRASS_0, GRASS_0, GRASS_0, DIRT_0, DIRT_0, DIRT_0, DIRT_1, DIRT_0, GRASS_0, GRASS_1, WATER_1, WATER_1, WATER_1, WATER_0, WATER_2, WATER_1, WATER_1, WATER_2, WATER_0],
    [GRASS_0, GRASS_0, GRASS_2, GRASS_0, GRASS_0, GRASS_0, GRASS_2, GRASS_0, GRASS_2, GRASS_0, GRASS_1, WATER_0, WATER_0, WATER_0, WATER_0, WATER_1, WATER_0, WATER_0, WATER_0, WATER_1]
]

# TILES TO BE DISPLAYED IN DUNGEON
GRID_TEMPLE = [
    [FLOOR_8, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_0, FLOOR_0, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_2, FLOOR_7],
    [FLOOR_4, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_3],
    [FLOOR_4, FLOOR_0, WALL, WALL, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, WALL, WALL, FLOOR_0, FLOOR_3],
    [FLOOR_4, FLOOR_0, WALL, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, WALL, FLOOR_0, FLOOR_3],
    [FLOOR_4, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, WALL, WALL, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_3],
    [FLOOR_4, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, WALL, WALL, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_3],
    [FLOOR_4, FLOOR_0, WALL, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, WALL, FLOOR_0, FLOOR_3],
    [FLOOR_4, FLOOR_0, WALL, WALL, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, WALL, WALL, FLOOR_0, FLOOR_3],
    [FLOOR_4, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_0, FLOOR_3],
    [FLOOR_5, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_0, FLOOR_0, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_1, FLOOR_6]
]

# GAME DIMENSIONS, CONFIG
TILESIZE = 50
MAPWIDTH = 200
MAPHEIGHT = 100 
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
"""
########################################################################################################################################