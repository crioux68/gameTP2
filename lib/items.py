import pygame.image
from grid import MAPHEIGHT, MAPWIDTH, TILESIZE
import random

rand = random.randint

class SWORD():
    def __init__(self):
        self.NAME = 'SWORD'
        self.IMAGE = pygame.image.load('./sprites/sword.png')
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (35, 35))
        self.POS = [2, 3]
        self.rect = [self.POS[0] * TILESIZE, self.POS[1] * TILESIZE, 35, 35]
        self.PLACED = True

class WAND:
    def __init__(self):
        self.NAME = 'WAND'
        self.IMAGE = pygame.image.load('./sprites/wand.png')
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (35, 35))
        self.X_POS = 8
        self.Y_POS = 8
        self.POS = [self.X_POS, self.Y_POS]
        self.rect = [self.X_POS * TILESIZE, self.Y_POS * TILESIZE, 35, 35]
        self.PLACED = True

class GOLD:
    NAME = 'BITCOIN'
    IMAGE = pygame.image.load('./sprites/gold_coin.png')
    POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
    PLACED = True

class SHIELD:
    def __init__(self):
        self.NAME = 'SHIELD'
        self.IMAGE = pygame.image.load('./sprites/shield.png')
        self.POS = [1, 3]
        self.rect = [self.POS[0] * TILESIZE, self.POS[1] * TILESIZE, 35, 35]
        self.PLACED = True


class KEY:
    def __init__(self):
        self.NAME = 'KEY'
        # DEFINE KEY'S SPRITE
        self.IMAGE = pygame.image.load('./sprites/Key.png')
        self.IMAGE = pygame.transform.scale(self.IMAGE, (35, 35))
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (25, 25))
        # KEY'S POSITION ON THE GRID
        self.X_POS = 5
        self.Y_POS = 8
        self.POS = [self.X_POS, self.Y_POS]
        # PLACED ON THE GRID
        self.PLACED = True
        # CREATE KEY'S COLLISION
        self.rect = pygame.rect.Rect(self.X_POS * TILESIZE, self.Y_POS * TILESIZE, 50, 50)

class BOW:
    def __init__(self):
        self.NAME = 'BOW'
        self.IMAGE = pygame.transform.scale(pygame.image.load('./sprites/bow.png'), (50, 75))
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (35, 20))
        self.POS = [1, 2]
        self.rect = [self.POS[0] * TILESIZE, self.POS[1] * TILESIZE, 35, 35]
        self.PLACED = True

