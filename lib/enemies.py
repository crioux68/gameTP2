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
        self.BEAST = pygame.image.load('./sprites/beast.png')
        self.PORTAL = False
        self.PORTAL_APPEAR = True
        self.APPEAR = False 
        self.X_POS = random.randint(50, 300)
        self.Y_POS = random.randint(50, 450)
        self.POS = []
        self.SUMMONED = False
        self.HEALTH = 100
        self.rect = Rect(self.POS, self.POS, 50, 50)
        red = (178, 0, 0)
        # self.rect = pygame.draw.rect(self.BEAST, blue, pygame.Rect(self.X_POS, self.Y_POS, 100, 100))

    

class PORTAL:
    def __init__(self):
        self.PORTAL = pygame.image.load('./textures/portal/portal_1.png')
        self.POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.FRAME = 0