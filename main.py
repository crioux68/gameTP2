import pygame, sys
from pygame.locals import *
from lib import enemies, heroes, items
from grid import *
import random
from key_events import KeyEvents
import math

# CHECK IF THE TILE IS AN OBSTACLE
def CheckIfObstacles(posTileX, posTileY):
    try:
        # CHECK IF THE TILE IS WATER
        if GRID_OVERWORLD[posTileY][posTileX] == WATER_0:
            #print("water 0")
            return True
        if GRID_OVERWORLD[posTileY][posTileX] == WATER_1:
            #print("water 1")
            return True
        if GRID_OVERWORLD[posTileY][posTileX] == WATER_2:
            #print("water 2")
            return True
        if GRID_OVERWORLD[posTileY+1][posTileX] == GRASS_1 and GRID_OVERWORLD[posTileY][posTileX+1] == GRASS_4 and GRID_OVERWORLD[posTileY][posTileX+2] == GRASS_3 and GRID_OVERWORLD[posTileY][posTileX-1] != DIRT_1:
            #print("grass 1")
            return 2
        if GRID_OVERWORLD[posTileY][posTileX] == GRASS_3:
            #print("grass 3")
            return True
        if GRID_OVERWORLD[posTileY][posTileX] == GRASS_4:
            #print("grass 4")
            return True
    except IndexError:
        return True


# INSTANCES OF GAME OBJECTS
PLAYER = heroes.LINK(5,5,75,75)
key_events = KeyEvents(PLAYER)
WAND = items.WAND()
GOLD = items.GOLD()
SWORD = items.SWORD()
SHIELD = items.SHIELD()
BOW = items.BOW()
GANON = enemies.GANON()
PORTAL = enemies.PORTAL()
TEMPLE = TEMPLE()
MIDNA = heroes.MIDNA()
CHEST = items.CHEST()
KEY = items.KEY()
tree = Tree()

# GROUPINGS OF RELATED GAME OBJECTS
GAME_ITEMS = [WAND, SWORD, SHIELD, KEY]
GAME_WEAPONS = [WAND, BOW]
PUZZLE = [CHEST]
BEAST_LIST = []
orbs_list = []

# OTHER CONFIG
INVFONT = pygame.font.SysFont('FreeSansBold.ttf', 20)
HEALTHFONT = pygame.font.SysFont('FreeSansBold.ttf', 40)
portal_path = './textures/portal/portal_'
portal_images = [portal_path + str(p) + '.png' for p in range(1, 7)]

"""
TIMED EVENTS
"""
# GANON MOVEMENT
pygame.time.set_timer(USEREVENT, 200)
# SPAWN BEAST
pygame.time.set_timer(USEREVENT + 1, 10000)
# INCREMENT BEAST PORTAL FRAMES
pygame.time.set_timer(USEREVENT + 2, 300)
# MOVE BEASTS
pygame.time.set_timer(USEREVENT + 3, 500)
# ORB TRAVEL ON PATH
pygame.time.set_timer(USEREVENT + 4, 100)

#class to change the stage
class gameState():
    def __init__(self) -> None:
        self.state = 'main_game'

    def main_game(self, tree, TEMPLE):
        GANON_VULNERABLE_IF = [beast for beast in BEAST_LIST if beast.APPEAR == True]

        if len(GANON_VULNERABLE_IF) < 1:
            GANON.VULNERABLE = True
        else:
            GANON.VULNERABLE = False

        """
        RENDERING GRID, SPRITES, AND VIEWS
        """
        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURFACE.blit(TEXTURES[GRID_OVERWORLD[row][column]], (column*TILESIZE, row*TILESIZE))

        DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))
        PLAYER.hitbox = (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE, 50, 50)    
        pygame.draw.rect(DISPLAYSURFACE, (255,   0,   0), PLAYER.hitbox, 4)

        # RENDER TEMPLE
        DISPLAYSURFACE.blit(TEMPLE.SPRITE, (TEMPLE.X_POS*TILESIZE, TEMPLE.Y_POS*TILESIZE))
        pygame.draw.rect(DISPLAYSURFACE, (255,   0,   0), TEMPLE, 4)

        # RENDERING ARMED ITEMS WITH PLAYER SPRITE
        if PLAYER.WEAPON:
            DISPLAYSURFACE.blit(PLAYER.WEAPON.IMAGE_ARMED, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

        # RENDER BEASTS AND PORTAL
        for beast in BEAST_LIST:
            if beast.PORTAL_APPEAR:
                DISPLAYSURFACE.blit(pygame.image.load(portal_images[beast.PORTAL.FRAME]), (beast.PORTAL.POS[0]*TILESIZE, beast.PORTAL.POS[1]*TILESIZE))
            if beast.APPEAR:
                DISPLAYSURFACE.blit(beast.SPRITE, (beast.POS[0]*TILESIZE, beast.POS[1]*TILESIZE))
                # beast.rect = pygame.rect.Rect(beast.POS[0], beast.POS[1], 100,100)
                pygame.draw.rect(DISPLAYSURFACE, (255,   0,   0),
                                beast.rect, 4)

        # RENDER ITEMS
        for item in GAME_ITEMS:
                if item.PLACED == True:
                    DISPLAYSURFACE.blit(item.IMAGE, (item.POS[0]*TILESIZE, item.POS[1]*TILESIZE))
        
        for chests in PUZZLE:
                if chests.PLACED == True:
                    DISPLAYSURFACE.blit(item.IMAGE, (item.POS[0]*TILESIZE, item.POS[1]*TILESIZE))

        # RENDER ORBS
        for orb in orbs_list:
            if orb.POS == GANON.GANON_POS and GANON.VULNERABLE:
                print('GANON HEALTH', GANON.HEALTH)
                GANON.HEALTH -= 10
            for beast in BEAST_LIST:
                    if orb.POS == beast.POS:
                        beast.APPEAR = False
                        BEAST_LIST.remove(beast)
                        orbs_list.remove(orb)
            if orb.POS[0] > MAPWIDTH or orb.POS[0] < 0 or orb.POS[1] > MAPHEIGHT or orb.POS[1] < 0: 
                orbs_list.remove(orb)

            DISPLAYSURFACE.blit(orb.IMAGE, (orb.POS[0]*TILESIZE, orb.POS[1]*TILESIZE))

        # RENDER PLAYER INVENTORY
        INVENTORY_POSITION = 250
        for item in PLAYER.PLAYER_INV:
            DISPLAYSURFACE.blit(item.IMAGE, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+35))
            INVENTORY_POSITION += 10 
            INVENTORY_TEXT = INVFONT.render(item.NAME, True, WHITE, BLACK)
            DISPLAYSURFACE.blit(INVENTORY_TEXT, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+15))
            INVENTORY_POSITION += 100

        # RENDER PLAYER HEALTH BAR
        PLAYER_HEALTH_BAR_TEXT = HEALTHFONT.render('LINK HEALTH:', True, GREEN, BLACK)
        DISPLAYSURFACE.blit(PLAYER_HEALTH_BAR_TEXT, (15, MAPHEIGHT*TILESIZE-500))
        DISPLAYSURFACE.blit(HEALTHFONT.render(str(PLAYER.HEALTH), True, GREEN, BLACK), (225, MAPHEIGHT*TILESIZE - 500))

        # RENDER GANON HEALTH BAR
        PLAYER_MANA_BAR_TEXT = HEALTHFONT.render('GANON HEALTH:', True, RED, BLACK)
        DISPLAYSURFACE.blit(PLAYER_MANA_BAR_TEXT, (650, MAPHEIGHT*TILESIZE-500))
        DISPLAYSURFACE.blit(HEALTHFONT.render(str(GANON.HEALTH), True, RED, BLACK), (900, MAPHEIGHT*TILESIZE-500))

        # RENDER TREES
        for tree in sorted(trees, key=lambda t: t.Y_POS):
            DISPLAYSURFACE.blit(tree.SPRITE, (tree.X_POS, tree.Y_POS))
            pygame.draw.rect(DISPLAYSURFACE, (255,   0,   0),
                                tree, 4)
            
        if tree.rect.colliderect(PLAYER.rect):
                print('le joueur a fesser un arbre')

        elif TEMPLE.rect.colliderect(PLAYER.rect):
            print('le joueur a fesser le temple')
            self.state = 'puzzle_room'
            TEMPLE.rect = None
            pygame.display.flip()

        for event in pygame.event.get():

            keys = pygame.key.get_pressed()
            key_events.global_events()
        
            if event.type == QUIT:
                key_events.quit()
        
            if keys[K_w] and keys[K_t]:
                key_events.key_w()

            col = False

            PLAYER.rect = pygame.rect.Rect(PLAYER.hitbox)

            for beast in BEAST_LIST:
                if PLAYER.rect.colliderect(beast.rect):  
                    col = True              
                    print("beast - index in list: " + str(BEAST_LIST.index(beast)))

            # Le problème ici, c'est que Link reste collé sur le temple quand il fonce dedans. Aussi, pygame dit que les arbres n'ont pas de rect...
            #if PLAYER.rect.colliderect(TEMPLE.rect) : #or PLAYER.rect.colliderect(tree.rect)
                #col = True


            # Dans les 4 cas de déplacement ci-bas, j'ai réinitialisé col à False après qu'il n'ait pas pu avancer.

            # MOVE RIGHT
            if (keys[K_RIGHT]) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0] + 1), int(PLAYER.PLAYER_POS[1])) == 2:
                    #print(str(PLAYER.PLAYER_POS[0]))
                    key_events.key_right()
                elif CheckIfObstacles(int(PLAYER.PLAYER_POS[0] + 1), int(PLAYER.PLAYER_POS[1])) == True or col == True:
                    col = False
                    pass
                else:
                    key_events.key_right()
                    #print(GRID[int(PLAYER.PLAYER_POS[1])])
                
            #    print("x:" + str(int(PLAYER.PLAYER_POS[0])) + ", y:" + str(int(PLAYER.PLAYER_POS[1])))
            #    print(str(CheckIfObstacles(int(PLAYER.PLAYER_POS[0]), int(PLAYER.PLAYER_POS[1]))))
        
            # MOVE LEFT
            if (keys[K_LEFT]) and PLAYER.PLAYER_POS[0] > 0:
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0] - 1), int(PLAYER.PLAYER_POS[1])) == True or col == True:
                    col = False
                    pass
                else:
                    key_events.key_left() 
        
            # MOVE UP
            if (keys[K_UP]) and PLAYER.PLAYER_POS[1] > 0:
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0]), int(PLAYER.PLAYER_POS[1] - 0.25)) == True or col == True:
                    col = False
                    pass
                else:
                    key_events.key_up()
        
            # MOVE DOWN
            if (keys[K_DOWN]) and PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1:
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0]), int(PLAYER.PLAYER_POS[1] + 0.25)) == True or CheckIfObstacles(int(PLAYER.PLAYER_POS[0]), int(PLAYER.PLAYER_POS[1] + 0.25)) == 2 or col == True:
                    col = False
                    pass
                else:
                    key_events.key_down()

                # print(GRID[int(PLAYER.PLAYER_POS[1])])
        
            # PLACING DOWN ITEMS
            if (keys[K_SPACE]):
                key_events.key_space()
        
            # FIRE ORB FROM WAND
            if (keys[K_f]):
                if PLAYER.WEAPON == WAND:
                    orbs_list.append(heroes.ORB(math.ceil(PLAYER.PLAYER_POS[0]), math.ceil(PLAYER.PLAYER_POS[1]), PLAYER.DIRECTION))

            """
            TIMED EVENTS
            """

            # GANON W/PORTAL MOVEMENT
            if (event.type == USEREVENT):
                if PORTAL.FRAME < 5:
                    PORTAL.FRAME += 1
                else:
                    x = random.randint(1, 9)
                    y = random.randint(1, 9)
                    PORTAL.POS = [x, y]
                    #Make sure Ganon stay on map
                    ganonRandPOSx = GANON.GANON_POS[0]+random.randint(-1,1)
                    ganonRandPOSy = GANON.GANON_POS[1]+random.randint(-1,1)
                    if (GANON.GANON_POS[0] < 0 and GANON.GANON_POS[0] > 10) or (GANON.GANON_POS[1] < 0 and GANON.GANON_POS[1] > 10):
                        if GANON.GANON_POS[0] < -3:
                            GANON.GANON_POS[0]+=10
                            print('Ganon is out the map on the side')
                        elif GANON.GANON_POS[1] > 13:
                            GANON.GANON_POS[1] -=10
                            print('Ganon is out the map on the top or bottom')
                        else:
                            ganonRandPOSx+=1
                            ganonRandPOSy+=1
                    else:
                        #print('Ganon is Ok x position = : '+ str(ganonRandPOSx) + ' poisition en y : ' + str(ganonRandPOSy))
                        pass
                    # GANON.GANON_POS = [GANON.GANON_POS[0]+random.randint(-1,1), GANON.GANON_POS[0]+random.randint(-1,1)]
                    GANON.GANON_POS = [ganonRandPOSx, ganonRandPOSy]
                    #print('x = ' + str(GANON.GANON_POS[0]) + ' y = ' + str(GANON.GANON_POS[1]))
                    PORTAL.FRAME = 1
            
            # BEAST OBJECT GENERATOR 
            elif (event.type == USEREVENT + 1):
                NEW_BEAST = enemies.BEAST()
                NEW_BEAST.PORTAL = enemies.PORTAL()
                BEAST_LIST.append(NEW_BEAST)

        # BEAST W/PORTAL GENERATOR 
            elif (event.type == USEREVENT + 2):
                for beast in BEAST_LIST:
                    if beast.PORTAL_APPEAR and beast.PORTAL.FRAME < 5:
                        beast.PORTAL.FRAME += 1
                    elif not beast.SUMMONED:
                        beast.PORTAL_APPEAR = False
                        beast.APPEAR = True
                        beast.SUMMONED = True
                        beast.POS = [beast.PORTAL.POS[0], beast.PORTAL.POS[1]]
                        beast.rect.left = beast.POS[0] * TILESIZE
                        beast.rect.top = beast.POS[1] * TILESIZE
                        #print("Left: " + str(beast.rect.left) + " Top: " + str(beast.rect.top))
            
            # BEASTS MOVEMENTS HUNT PLAYER
            elif (event.type == USEREVENT + 3):
                for beast in BEAST_LIST:
                    if beast.APPEAR:
                        if PLAYER.PLAYER_POS == beast.POS:
                            PLAYER.HEALTH -= 0
                        for coordinate in range(len(beast.POS)):
                            # if tree.treePOS[coordinate] == beast.POS[coordinate]:
                            #     beast.POS[coordinate]-=1
                            #     print('collision avec arbre')
                            #col = tree.rect.colliderect(beast)
                            #print("coordinate: " + str(beast.POS[coordinate]))
                            beast.rect = pygame.rect.Rect(beast.rect.left, beast.rect.top, 75, 75)
                            # col = beast.rect.colliderect(tree)
                            col = tree.rect.colliderect(beast.rect) or TEMPLE.rect.colliderect(beast.rect) or PLAYER.rect.colliderect(beast.rect)
                            if PLAYER.PLAYER_POS[coordinate] > beast.POS[coordinate]:
                                if col == True:
                                    beast.POS[coordinate]-=0.1 * 2
                                    # print('collision avec arbre')
                                    # beast.rect = beast.rect.move(beast.POS[0]*-1 * 2, beast.POS[1] * 2)
                                    beast.rect.update(beast.POS[0] * TILESIZE, beast.POS[1] * TILESIZE, 75, 75)
                                else:
                                    beast.POS[coordinate] += 0.5
                                    # beast.rect = beast.rect.move(beast.POS[0]*-1 * 2, beast.POS[1] * 2)
                                    beast.rect.update(beast.POS[0] * TILESIZE, beast.POS[1] * TILESIZE, 75, 75)
                            else:
                                if col == True:
                                    beast.POS[coordinate]+=0.1 * 2
                                    # print('collision avec arbre')
                                    # beast.rect = beast.rect.move(beast.POS[0]*-1 * 2, beast.POS[1] * 2)
                                    beast.rect.update(beast.POS[0] * TILESIZE, beast.POS[1] * TILESIZE, 75, 75)
                                else:
                                    beast.POS[coordinate] -= 0.5
                                    # beast.rect = beast.rect.move(beast.POS[0]*-1 * 2, beast.POS[1] * 2)
                                    beast.rect.update(beast.POS[0] * TILESIZE, beast.POS[1] * TILESIZE, 75, 75)

                            # col = PLAYER.rect.colliderect(beast.rect)
                            # if col == True:
                            #     beast.POS[coordinate] = beast.POS[coordinate]

                                        
            
            # ORB PATH MOVEMENT ANIMATION
            elif (event.type == USEREVENT + 4):
                for orb in orbs_list:
                    if orb.DIRECTION == 'd':
                        orb.POS[1] += 1
                    elif orb.DIRECTION == 'u':
                        orb.POS[1] -= 1
                    elif orb.DIRECTION == 'l':
                        orb.POS[0] -= 1 
                    elif orb.DIRECTION == 'r':
                        orb.POS[0] += 1

            # PICKUP ITEM CONDITIONS
            for item in GAME_ITEMS:
                if PLAYER.PLAYER_POS == item.POS and item.PLACED:
                    PLAYER.PLAYER_INV.append(item)
                    item.PLACED = False
                    if item in GAME_WEAPONS:
                        PLAYER.WEAPON = item

        

        # RENDER GANON AND PORTAL
        DISPLAYSURFACE.blit(pygame.image.load(portal_images[PORTAL.FRAME]), (GANON.GANON_POS[0]*TILESIZE, GANON.GANON_POS[1]*TILESIZE))
        DISPLAYSURFACE.blit(GANON.GANON, (GANON.GANON_POS[0]*TILESIZE, GANON.GANON_POS[1]*TILESIZE))
        
        pygame.display.update()

        if GANON.HEALTH <= 0:
            GAME_OVER = True
            print('GAME OVER, YOU WIN!')
        
        if PLAYER.HEALTH <= 0:
            GAME_OVER = True
            print('GAME OVER, YOU LOSE')     

    def puzzle_room(self):
        #TODO mettre la grid du temple
        #TODO mettre Link dans le temple 
        pygame.display.flip()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            key_events.global_events()
        
            if event.type == QUIT:
                key_events.quit()
        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURFACE.blit(TEXTURES[GRID_TEMPLE[row][column]], (column*TILESIZE, row*TILESIZE))

    def state_manager(self):
        if self.state == 'main_game':
            self.main_game(Tree, TEMPLE)
        elif self.state == 'puzzle_room':
            self.puzzle_room()

# GAME VARIABLE               
GAME_OVER = False
GAME_STATE = gameState()

# draw the canvas of the map
# RENDER GAME GRID
pygame.display.init()
window = (MAPWIDTH, MAPHEIGHT) 
background = pygame.Surface(window)
#### Populate the surface with objects to be displayed ####
pygame.draw.rect(background,(0,255,255),(20,20,40,40))
pygame.draw.rect(background,(255,0,255),(120,120,50,50))

# GAME LOOP
while not GAME_OVER:
    GAME_STATE.state_manager()

# END OF GAME LOOP