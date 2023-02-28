import pygame.image
from grid import MAPHEIGHT, MAPWIDTH, TILESIZE
import random

rand = random.randint

class SWORD():
    def __init__(self):
        self.NAME = 'SWORD'
        self.IMAGE = pygame.image.load('./sprites/sword.png')
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (35, 35))
        self.POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.PLACED = True

class WAND:
    def __init__(self):
        self.NAME = 'WAND'
        self.IMAGE = pygame.image.load('./sprites/wand.png')
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (35, 35))
        self.POS = [8, 8]
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
        self.POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.PLACED = True

class KEY:
    def __init__(self):
        self.NAME = 'KEY'
        self.IMAGE = pygame.image.load('./sprites/Key.png')
        self.IMAGE = pygame.transform.scale(self.IMAGE, (35, 35))
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (25, 25))
        self.X_POS = 2
        self.Y_POS = 2
        self.POS = [2, 2]
        self.PLACED = True
        self.rect = pygame.rect.Rect(self.X_POS * TILESIZE, self.Y_POS * TILESIZE, 35, 35)

class BOW:
    def __init__(self):
        self.NAME = 'BOW'
        self.IMAGE = pygame.transform.scale(pygame.image.load('./sprites/bow.png'), (50, 75))
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (35, 20))
        self.POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.PLACED = True

