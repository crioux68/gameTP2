import pygame.image
import pygame
from grid import MAPHEIGHT, MAPWIDTH
import random
from pygame.locals import *

rand = random.randint

class GANON:
    def __init__(self):
        self.GANON = pygame.image.load('./sprites/ganon_0.png')
        #Make Ganon appear ouside of the map
        self.GANON_POS = [6, 1]
        self.HEALTH = 250
        self.VULNERABLE = True
        self.rect = self.GANON.get_rect()

class BEAST:
    def __init__(self):
        self.SPRITE = pygame.image.load('./sprites/beast.png')
        self.PORTAL = False
        self.PORTAL_APPEAR = True
        self.APPEAR = False 
        self.POS = []
        self.SUMMONED = False
        self.HEALTH = 100
        self.rect = self.SPRITE.get_rect()
        
class PORTAL:
    def __init__(self):
        self.PORTAL = pygame.image.load('./textures/portal/portal_1.png')
        self.POS = [9, 8]
        self.FRAME = 0