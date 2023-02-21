import pygame.image
import pygame
from grid import MAPHEIGHT, MAPWIDTH
import random
from pygame.locals import *

rand = random.randint

class GANON:
    def __init__(self):
        self.GANON = pygame.image.load('./sprites/ganon.png')
        self.GANON_POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.HEALTH = 250
        self.VULNERABLE = True

class BEAST:
    def __init__(self):
        self.SPRITE = pygame.image.load('./sprites/beast.png')
        self.PORTAL = False
        self.PORTAL_APPEAR = True
        self.APPEAR = False 
        # self.X_POS = random.randint(50, 300)
        # self.Y_POS = random.randint(50, 450)
        self.POS = []
        self.SUMMONED = False
        self.HEALTH = 100
        self.rect = self.SPRITE.get_rect()
        
        #self.hitbox = (self.POS[0], self.POS[1], 50, 50)
        


class PORTAL:
    def __init__(self):
        self.PORTAL = pygame.image.load('./textures/portal/portal_1.png')
        self.POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.FRAME = 0