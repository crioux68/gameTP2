import pygame.image
import pygame.rect
from grid import *

class LINK:
    def __init__(self, x, y, width, height):
        self.SPRITE_POS = pygame.image.load('./sprites/link/link_f6.png')
        self.PLAYER_POS = [x, y]
        self.PLAYER_INV = []
        self.WEAPON = False
        self.HEALTH = 100
        self.MANA = 200
        

        self.rect = self.SPRITE_POS.get_rect()
        self.hitbox = (self.PLAYER_POS[0], self.PLAYER_POS[1], width, height)
                
        self.DIRECTION = False
        self.TRANSFORM = False
        
        self.WOLF = pygame.image.load('./sprites/wolf/wolf_f0.png')
    
    def TRANSFORMING(self):
        self.TRANSFORM = not self.TRANSFORM

class ORB:
    def __init__(self, X, Y, DIRECTION):
        self.IMAGE = pygame.transform.scale(pygame.image.load('./sprites/orb.png'), (25, 25))
        self.POS = [X, Y]
        self.DIRECTION = DIRECTION
        self.radius = 25