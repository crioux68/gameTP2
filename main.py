import pygame, sys
from pygame import mixer
from pygame.locals import *
from lib import enemies, heroes, items
from grid import *
import random
from key_events import KeyEvents
import math
from importlib.metadata import version

# INIT THE SOUND EFFECT MANAGER
pygame.mixer.init()

# CHECK THE VERSION OF PYGAME INSTALLED LOCALLY
MINIMUM_PYGAME_VERSION = [2, 1, 3]
PYGAME_VERSION = version('pygame').split('.')

PYGAME_VERSION_INT = (int(PYGAME_VERSION[0]) * 100) + (int(PYGAME_VERSION[1]) * 10) + int(PYGAME_VERSION[2])
MINIMUM_PYGAME_VERSION_INT = (int(MINIMUM_PYGAME_VERSION[0]) * 100) + (int(MINIMUM_PYGAME_VERSION[1]) * 10) + int(MINIMUM_PYGAME_VERSION[2])

if (PYGAME_VERSION_INT < MINIMUM_PYGAME_VERSION_INT):
    print("The version of pygame: " + version('pygame') + " is invalid \n The minimum version is " + str(MINIMUM_PYGAME_VERSION[0]) + "." + str(MINIMUM_PYGAME_VERSION[1]) + "." + str(MINIMUM_PYGAME_VERSION[2]) +"\n Please run: pip install --upgrade pygame")
    exit()

# CHECK AND UPDATE THE VERSION OF PYGAME IN REQUIREMENTS.TXT
new_requirements = []

with open('requirements.txt') as txt:
    lines = txt.readlines()
    for line in lines:
        module = line.split('==')
        if module[0] == "pygame":
            moduleVersion = module[1].split('.')
            new_line = "pygame=="
            new_line += str(MINIMUM_PYGAME_VERSION[0]) + "." + str(MINIMUM_PYGAME_VERSION[1]) + "." + str(MINIMUM_PYGAME_VERSION[2])
            new_requirements.append(new_line)
        else:
            new_requirements.append(line)

with open('requirements.txt', "w") as txt:
    for line in new_requirements:
        txt.write(line)

# CHECK IF THE TILE IS AN OBSTACLE
def CheckIfObstacles(posTileX, posTileY, zone):
    if zone == 'overworld':
        try:
            # CHECK IF THE TILE IS WATER
            if GRID_OVERWORLD[posTileY][posTileX] == WATER_0:                
                return True
            if GRID_OVERWORLD[posTileY][posTileX] == WATER_1:
                return True
            if GRID_OVERWORLD[posTileY][posTileX] == WATER_2:
                return True

            # CHECK IF THE TILE IS A CORNER OF GRASS NEXT TO WATER
            if GRID_OVERWORLD[posTileY+1][posTileX] == GRASS_1 and GRID_OVERWORLD[posTileY][posTileX+1] == GRASS_4 and GRID_OVERWORLD[posTileY][posTileX+2] == GRASS_3 and GRID_OVERWORLD[posTileY][posTileX-1] != DIRT_1:
                return 2
            if GRID_OVERWORLD[posTileY][posTileX] == GRASS_3:
                return True
            if GRID_OVERWORLD[posTileY][posTileX] == GRASS_4:
                return True
        except IndexError:
            return True
    else:
        try:
            # CHECK IF THE TILE IS WATER
            if GRID_TEMPLE[posTileY][posTileX] == WATER_0:
                return True
            if GRID_TEMPLE[posTileY][posTileX] == WATER_1:
                return True
            if GRID_TEMPLE[posTileY][posTileX] == WATER_2:
                return True
            
            # CHECK IF THE TILE IS A CORNER OF GRASS NEXT TO WATER
            if GRID_TEMPLE[posTileY+1][posTileX] == GRASS_1 and GRID_OVERWORLD[posTileY][posTileX+1] == GRASS_4 and GRID_OVERWORLD[posTileY][posTileX+2] == GRASS_3 and GRID_OVERWORLD[posTileY][posTileX-1] != DIRT_1:
                return 2
            if GRID_TEMPLE[posTileY][posTileX] == GRASS_3:
                return True
            if GRID_TEMPLE[posTileY][posTileX] == GRASS_4:
                return True
        except IndexError:
            return True


# INSTANCES OF GAME OBJECTS
PLAYER = heroes.LINK(5, 5, 75, 75)
key_events = KeyEvents(PLAYER)
WAND = items.WAND()
GOLD = items.GOLD()
SWORD = items.SWORD()
SHIELD = items.SHIELD()
BOW = items.BOW()
GANON = enemies.GANON()
PORTAL = enemies.PORTAL()
TEMPLE = TEMPLE()
CHEST = CHEST()
KEY = items.KEY()
tree = Tree()
btnstart = BTNStart()
btnquit = BTNQuit()
btnoptions = BTNOptions()
btnrestart = BTNRestart()

# GROUPINGS OF RELATED GAME OBJECTS
GAME_ITEMS = [SWORD, SHIELD, KEY]
GAME_WEAPONS = [WAND, BOW]
PUZZLE = [CHEST]
PUZZLE_KEY = []
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
# HAVE KEY OR NOT
haveKey = False

# CLASS TO CHANGE THE STATE
class gameState():
    def __init__(self) -> None:
        self.state = 'menu'

    def main_game(self, tree, TEMPLE, KEY):
        # SFX
        gunSFX = pygame.mixer.Sound("./Sounds/gun.wav")
        playerHurtSFX = pygame.mixer.Sound("./Sounds/smallAugh.mp3")

        GANON_VULNERABLE_IF = [beast for beast in BEAST_LIST if beast.APPEAR == True]
        global haveKey
        zone = 'overworld'
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
        PLAYER.hitbox = (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE, 50, 65)    
        pygame.draw.rect(DISPLAYSURFACE, (0,   0,   0), PLAYER.hitbox, -1)

        # RENDER TEMPLE
        DISPLAYSURFACE.blit(TEMPLE.SPRITE, (TEMPLE.X_POS*TILESIZE, TEMPLE.Y_POS*TILESIZE))
        pygame.draw.rect(DISPLAYSURFACE, (255,   0,   0), TEMPLE, -1)

        # Left side of the temple rect for collider
        templeLeftRect = pygame.rect.Rect(170, 30, 150, 200)
        pygame.draw.rect(DISPLAYSURFACE, (0, 255, 0), templeLeftRect, -1)

        # Right side of the temple rect for collider
        templeRightRect = pygame.rect.Rect(382, 30, 150, 200)
        pygame.draw.rect(DISPLAYSURFACE, (0, 0, 255), templeRightRect, -1)

        # Top temple rect collider
        templeTopRect = pygame.rect.Rect(250, 30, 200, 40)
        pygame.draw.rect(DISPLAYSURFACE, (0, 0, 255), templeTopRect, -1)

        # RENDERING ARMED ITEMS WITH PLAYER SPRITE
        if PLAYER.WEAPON:
            DISPLAYSURFACE.blit(PLAYER.WEAPON.IMAGE_ARMED, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

        # RENDER BEASTS AND PORTAL
        # beasts spawn at a fixed position
        for beast in BEAST_LIST:
            if beast.PORTAL_APPEAR:
                DISPLAYSURFACE.blit(pygame.image.load(portal_images[beast.PORTAL.FRAME]), (beast.PORTAL.POS[0]*TILESIZE, beast.PORTAL.POS[1]*TILESIZE))
            if beast.APPEAR:
                DISPLAYSURFACE.blit(beast.SPRITE, (beast.POS[0]*TILESIZE, beast.POS[1]*TILESIZE))
                pygame.draw.rect(DISPLAYSURFACE, (255,   0,   0),
                                beast.rect, -1)

        # RENDER ITEMS ON THE GROUND
        for item in GAME_ITEMS:
            if item.PLACED == True:
                DISPLAYSURFACE.blit(item.IMAGE, (item.POS[0]*TILESIZE, item.POS[1]*TILESIZE))
            # IF THE ITEM IS A KEY, ADD IT TO THE LIST OF KEYS HELD BY THE PLAYER
            if item == KEY:
                PUZZLE_KEY.append(KEY)
        

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
            pygame.draw.rect(DISPLAYSURFACE, (255,   0,   0), tree, -1)
        
        for tree in sorted(trees2, key=lambda t: t.Y_POS):
            DISPLAYSURFACE.blit(tree.SPRITE, (tree.X_POS, tree.Y_POS))
            pygame.draw.rect(DISPLAYSURFACE, (255,   0,   0), tree, -1)
        
        for tree in sorted(trees3, key=lambda t: t.Y_POS):
            DISPLAYSURFACE.blit(tree.SPRITE, (tree.X_POS, tree.Y_POS))
            pygame.draw.rect(DISPLAYSURFACE, (255,   0,   0), tree, -1)
            

        if TEMPLE.rect.colliderect(PLAYER.rect):
            self.state = 'puzzle_room'
            TEMPLE.rect = None
            pygame.display.flip()

        # KEY FOR CHEST PUZZLE
        for KEY in PUZZLE_KEY:

            # KEY COLLISION
            colKey = KEY.rect.colliderect(PLAYER.rect)
            
            # WHEN THE PLAYER COLLIDES WITH A KEY, HE IS ABLE TO USE IT
            if colKey:
                haveKey = True

        # RENDER CHEST PUZZLE
        for CHEST in PUZZLE:
            
            # DISPLAY CHEST ON THE OVERWORLD
            DISPLAYSURFACE.blit(CHEST.SPRITE, (CHEST.X_POS*TILESIZE, CHEST.Y_POS*TILESIZE))
            
            pygame.draw.rect(DISPLAYSURFACE, (255,   0,   0), CHEST, -1)
            
            # CHECK IF THE CHEST COLLIDES WITH THE PLAYER
            colChest = CHEST.rect.colliderect(PLAYER.rect)
            
            # THE SOUND OF THE CHEST OPENING
            chestSFX = pygame.mixer.Sound("./Sounds/chest.wav")

            # OPEN THE CHEST IF THE PLAYER HAS THE KEY AND THE CHEST IS COLLIDING WITH THE PLAYER
            if colChest and haveKey:
                
                # CHEST IS REMOVED AND WAND APPEARS IN ITS PLACE
                PUZZLE.remove(CHEST)
                GAME_ITEMS.append(WAND)
                
                # KEY HAS BEEN USED AND CANNOT OPEN ANOTHER CHEST
                haveKey = False

                # CONGRATULATIONS! YOU HAVE OPENED A CHEST AND A SOUND HAS PLAYED TO LET YOU KNOW
                pygame.mixer.Sound.play(chestSFX)

        # GAME EVENTS
        for event in pygame.event.get():

            keys = pygame.key.get_pressed()
            key_events.global_events()
        
            if event.type == QUIT:
                key_events.quit()
        
            if keys[K_w] and keys[K_t]:
                key_events.key_w()

            colBeast = False
            colEnvironment = False

            PLAYER.rect = pygame.rect.Rect(PLAYER.hitbox) 

            '''
            damageTimer = 1000
            run = False

            def takeDamage(damageTimer):
                pygame.time.set_timer(USEREVENT, 1000)
                
                run = True
                while run:
                    if damageTimer > 0:
                        damageTimer -= 1
                        print("Timer " + str(damageTimer))
                    else:
                        PLAYER.HEALTH -= 10
                        damageTimer = 1000
                        run = False
            '''

            # Check if we make contact with an ennemy and if so we put the ennemy's rect in beastCoord, which is used later
            for beast in BEAST_LIST:
                if PLAYER.rect.colliderect(beast.rect):                         
                    colBeast = True 
                    playerHurtSFX.play()  
                    #takeDamage(damageTimer)
                    PLAYER.HEALTH -= 4
                    print("Sante " + str(PLAYER.HEALTH)) 
                    beastCoord = beast.rect 

            # Check if we make contact with an obstacle and if so we put the tree or temple's rect in environmentCoord, which is used later
            if PLAYER.rect.colliderect(templeLeftRect) or PLAYER.rect.colliderect(tree.rect) or PLAYER.rect.colliderect(templeRightRect) or PLAYER.rect.colliderect(templeTopRect):
                colEnvironment = True
                if PLAYER.rect.colliderect(tree.rect):
                    environmentCoord = tree.rect 
                elif PLAYER.rect.colliderect(templeRightRect):
                    environmentCoord = templeRightRect 
                elif PLAYER.rect.colliderect(templeLeftRect):
                    environmentCoord = templeLeftRect
                elif PLAYER.rect.colliderect(templeTopRect):
                    environmentCoord = templeTopRect
                       

            # This function takes as a parameter the coordinates of the beast or environment established with one of the previous 2 non-functions
            # We check if the contact is made with the player's rectangle's bottom, top, right or left and return it as a string
            def checkContact(coord):   
                if PLAYER.rect.bottom >= coord.top and (coord.bottom - PLAYER.rect.top) > 100 and (coord.bottom - PLAYER.rect.top) <= (PLAYER.rect[3] + coord[3]) and PLAYER.rect[1] <= coord.top :
                    contactPoint = "bottom"                      
                elif PLAYER.rect.right >= coord.left and (coord.right - PLAYER.rect.left) > 100 and (coord.right - PLAYER.rect.left) <= (PLAYER.rect[2] + coord[2]) and PLAYER.rect[0] <= coord.left:
                    contactPoint = "right"                                               
                elif PLAYER.rect.top <= coord.bottom and (PLAYER.rect.bottom - coord.top) <= (PLAYER.rect[3] + coord[3]) and PLAYER.rect.bottom >= coord.bottom: 
                    contactPoint = "top"                    
                elif PLAYER.rect.left <= coord.right and (PLAYER.rect.right - coord.left) <= (PLAYER.rect[2] + coord[2]) and PLAYER.rect[0] <= coord.right:
                    contactPoint = "left"               
                return contactPoint
            
            # This function pushes the player back, if there's space on the screen, in the direction opposite of the contact point (more or less: a few discrepancies remain)
            def bounce(contact):
                if contact == "bottom":
                    if PLAYER.PLAYER_POS[1] > 0 :
                        PLAYER.PLAYER_POS[1] -= 0.25
                    else:
                        print("Pas de place")
                elif contact == "right":
                    if PLAYER.PLAYER_POS[0] > 0:
                        PLAYER.PLAYER_POS[0] -= 0.25
                    else:
                        print("Pas de place")
                elif contact == "top":
                    if PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1:
                        PLAYER.PLAYER_POS[1] += 0.25
                    else:
                        print("Pas de place")
                elif contact == "left":
                    if PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
                        PLAYER.PLAYER_POS[0] += 0.25
                    else:
                        print("Pas de place")


            # This part launches the functions checkContact() and bounce() if there's been a contact
            if colBeast:
                contactPoint = checkContact(beastCoord)                
                bounce(contactPoint)
            elif colEnvironment:
                contactPoint = checkContact(environmentCoord)                
                bounce(contactPoint)


            # This section moves the player and checks if it collides with a obstacle tile

            # MOVE RIGHT
            if (keys[K_RIGHT]) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0] + 1), int(PLAYER.PLAYER_POS[1]), zone) == 2:
                    key_events.key_right()                
                elif CheckIfObstacles(int(PLAYER.PLAYER_POS[0] + 1), int(PLAYER.PLAYER_POS[1]), zone) == True:              # or col == True      
                    col = False
                    pass
                else:
                    key_events.key_right()
        
            # MOVE LEFT
            if (keys[K_LEFT]) and PLAYER.PLAYER_POS[0] > 0:                
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0] - 1), int(PLAYER.PLAYER_POS[1]),zone) == True: # or col == True
                    col = False
                    pass
                else:
                    key_events.key_left() 
        
            # MOVE UP
            if (keys[K_UP]) and PLAYER.PLAYER_POS[1] > 0:                
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0]), int(PLAYER.PLAYER_POS[1] - 0.25), zone) == True: # or col == True
                    col = False
                    pass
                else:
                    key_events.key_up()
        
            # MOVE DOWN
            if (keys[K_DOWN]) and PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1:                
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0]), int(PLAYER.PLAYER_POS[1] + 0.25),zone) == True or CheckIfObstacles(int(PLAYER.PLAYER_POS[0]), int(PLAYER.PLAYER_POS[1] + 0.25), zone) == 2: # or col == True
                    col = False
                    pass
                else:
                    key_events.key_down()
        
            # PLACING DOWN ITEMS
            
            if (keys[K_SPACE]):                
                key_events.key_space()
        
            # FIRE ORB FROM WAND
            if (keys[K_f]):
                if PLAYER.WEAPON == WAND:
                    gunSFX.play(maxtime=350)
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
                    # Make sure Ganon stays on map
                    ganonRandPOSx = GANON.GANON_POS[0]+random.randint(-1,1)
                    ganonRandPOSy = GANON.GANON_POS[1]+random.randint(-1,1)
                    if (GANON.GANON_POS[0] < 0 and GANON.GANON_POS[0] > 10) or (GANON.GANON_POS[1] < 0 and GANON.GANON_POS[1] > 10):
                        if GANON.GANON_POS[0] < -3:
                            GANON.GANON_POS[0]+=10
                        elif GANON.GANON_POS[1] > 13:
                            GANON.GANON_POS[1] -=10
                        else:
                            ganonRandPOSx+=1
                            ganonRandPOSy+=1
                    else:
                        pass
                    GANON.GANON_POS = [ganonRandPOSx, ganonRandPOSy]
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
            
            # BEASTS MOVEMENTS HUNT PLAYER
            elif (event.type == USEREVENT + 3):
                for beast in BEAST_LIST:
                    if beast.APPEAR:
                        if PLAYER.PLAYER_POS == beast.POS:
                            PLAYER.HEALTH -= 0

                        for coordinate in range(len(beast.POS)):
                            beast.rect = pygame.rect.Rect(beast.rect.left, beast.rect.top, 75, 75)
                            col = tree.rect.colliderect(beast.rect) or TEMPLE.rect.colliderect(beast.rect) or PLAYER.rect.colliderect(beast.rect)
                            if PLAYER.PLAYER_POS[coordinate] > beast.POS[coordinate]:
                                if col == True:
                                    beast.POS[coordinate]-=0.1 * 2
                                    beast.rect.update(beast.POS[0] * TILESIZE, beast.POS[1] * TILESIZE, 75, 75)
                                else:
                                    beast.POS[coordinate] += 0.5
                                    beast.rect.update(beast.POS[0] * TILESIZE, beast.POS[1] * TILESIZE, 75, 75)
                            else:
                                if col == True:
                                    beast.POS[coordinate]+=0.1 * 2
                                    beast.rect.update(beast.POS[0] * TILESIZE, beast.POS[1] * TILESIZE, 75, 75)
                                else:
                                    beast.POS[coordinate] -= 0.5
                                    beast.rect.update(beast.POS[0] * TILESIZE, beast.POS[1] * TILESIZE, 75, 75)

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
            itemSFX = pygame.mixer.Sound("./Sounds/pickup.wav")
            # FOR EACH ITEM THAT IS ON THE GROUND AND ALSO COLLIDES WITH THE PLAYER, SAID ITEM IS PICKED UP
            for item in GAME_ITEMS:
                if PLAYER.rect.colliderect(item.rect) and item.PLACED:
                    PLAYER.PLAYER_INV.append(item)
                    item.PLACED = False
                    # A SOUND PLAYS WHEN AN ITEM IS PICKED UP
                    pygame.mixer.Sound.play(itemSFX)
                    # CONFIRMS IF THE ITEM WAS A WEAPON
                    if item in GAME_WEAPONS:
                        PLAYER.WEAPON = item
        
        # UPDATE THE FRAMES OF THE GAME
        pygame.display.update()

        if GANON.HEALTH <= 0:
            GAME_OVER = True
            self.state = 'end_game'
        
        if PLAYER.HEALTH <= 0:
            GAME_OVER = True
            self.state = 'end_game'    

    # Create the puzzle room when you enter the cave
    def puzzle_room(self):
        # this line was put to remove the bug while pressing f in the temple
        gunSFX = pygame.mixer.Sound("./Sounds/gun.wav")
        #Control in the temple
        pygame.display.update()
        zone = 'temple_overworld'
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

            # MOVE RIGHT
            if (keys[K_RIGHT]) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0] + 1), int(PLAYER.PLAYER_POS[1]), zone) == 2:
                    key_events.key_right()
                elif CheckIfObstacles(int(PLAYER.PLAYER_POS[0] + 1), int(PLAYER.PLAYER_POS[1]), zone) == True or col == True:
                    PLAYER.PLAYER_POS[0] -= 0.25
                    col = False
                    pass
                else:
                    key_events.key_right()
        
            # MOVE LEFT
            if (keys[K_LEFT]) and PLAYER.PLAYER_POS[0] > 0:
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0] - 1), int(PLAYER.PLAYER_POS[1]), zone) == True or col == True:
                    PLAYER.PLAYER_POS[0] += 0.25
                    col = False
                    pass
                else:
                    key_events.key_left() 
        
            # MOVE UP
            if (keys[K_UP]) and PLAYER.PLAYER_POS[1] > 0:
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0]), int(PLAYER.PLAYER_POS[1] - 0.25),zone) == True or col == True:
                    PLAYER.PLAYER_POS[1] += 0.25
                    col = False
                    pass
                else:
                    key_events.key_up()
        
            # MOVE DOWN
            if (keys[K_DOWN]) and PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1:
                if CheckIfObstacles(int(PLAYER.PLAYER_POS[0]), int(PLAYER.PLAYER_POS[1] + 0.25),zone) == True or CheckIfObstacles(int(PLAYER.PLAYER_POS[0]), int(PLAYER.PLAYER_POS[1] + 0.25), zone) == 2 or col == True:
                    PLAYER.PLAYER_POS[1] -= 0.25
                    col = False
                    pass
                else:
                    key_events.key_down()
        
            # PLACING DOWN ITEMS
            
            if (keys[K_SPACE]):
                
                key_events.key_space()
        
            # FIRE ORB FROM WAND
            if (keys[K_f]):
                if PLAYER.WEAPON == WAND:
                    gunSFX.play()
                    orbs_list.append(heroes.ORB(math.ceil(PLAYER.PLAYER_POS[0]), math.ceil(PLAYER.PLAYER_POS[1]), PLAYER.DIRECTION))
            
            if (event.type == USEREVENT):
                if PORTAL.FRAME < 5:
                    PORTAL.FRAME += 1
                else:
                    x = random.randint(1, 9)
                    y = random.randint(1, 9)
                    PORTAL.POS = [x, y]
                    # Make sure Ganon stays on map
                    ganonRandPOSx = GANON.GANON_POS[0]+random.randint(-1,1)
                    ganonRandPOSy = GANON.GANON_POS[1]+random.randint(-1,1)
                    if (GANON.GANON_POS[0] < 1 and GANON.GANON_POS[0] > 9) or (GANON.GANON_POS[1] < 1 and GANON.GANON_POS[1] > 9):
                        if GANON.GANON_POS[0] < -1:
                            GANON.GANON_POS[0]+=3
                        elif GANON.GANON_POS[0] > 10:
                            GANON.GANON_POS[0]-=3
                        elif GANON.GANON_POS[1] > 13:
                            GANON.GANON_POS[1] -=10
                        elif GANON.GANON_POS[1] < -1:
                            GANON.GANON_POS[1] +=3
                        else:
                            ganonRandPOSx+=1
                            ganonRandPOSy+=1
                    else:
                        pass
                    GANON.GANON_POS = [ganonRandPOSx, ganonRandPOSy]
                    PORTAL.FRAME = 1
 
        pygame.display.flip()
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            key_events.global_events()
        
            if event.type == QUIT:
                key_events.quit()
        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURFACE.blit(TEXTURES[GRID_TEMPLE[row][column]], (column*TILESIZE, row*TILESIZE))

        # Player spawns in the temple
        DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))
        PLAYER.hitbox = (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE, 50, 50)    
        pygame.draw.rect(DISPLAYSURFACE, (255,   0,   0), PLAYER.hitbox, -1)

        # RENDER GANON AND PORTAL
        DISPLAYSURFACE.blit(pygame.image.load(portal_images[PORTAL.FRAME]), (GANON.GANON_POS[0]*TILESIZE, GANON.GANON_POS[1]*TILESIZE))
        # Hide Ganon for this map
        DISPLAYSURFACE.blit(GANON.GANON, (GANON.GANON_POS[0]*TILESIZE, GANON.GANON_POS[1]*TILESIZE))

        if GANON.HEALTH <= 0:
            GAME_OVER = True
            self.state = 'end_game'
        
        if PLAYER.HEALTH <= 0:
            GAME_OVER = True
            self.state = 'end_game' 

    # CREATE THE GAME MENU SCREEN
    def menu(self):        
        bgMenu = pygame.image.load('textures/boutons/bg_menu.png')
        bgMenu = pygame.transform.scale(bgMenu, (1000, 500))
        BACKGROUNDCOLOR = (60,179,113)
        DISPLAYSURFACE.fill(BACKGROUNDCOLOR)
        DISPLAYSURFACE.blit(bgMenu, (0,0))

        # RENDER PLAY GAME TEXT
        PLAY_GAME_TEXT = HEALTHFONT.render('PLAY GAME', True, GREEN, BLACK)
        DISPLAYSURFACE.blit(PLAY_GAME_TEXT, (pygame.display.get_window_size()[0] / 2 - PLAY_GAME_TEXT.get_size()[0] / 2, 50))

        # RENDER BUTTONS
        width = DISPLAYSURFACE.get_width()
        height = DISPLAYSURFACE.get_height()

        # BUTTON IMAGES 
        START_BUTTON_IMG = btnstart.SPRITE
        QUIT_BUTTON_IMG = btnquit.SPRITE

        # DRAW BUTTONS
        pygame.draw.rect(DISPLAYSURFACE, (0,255,0), btnstart, -1)
        pygame.draw.rect(DISPLAYSURFACE, (0,255,0), btnquit, -1)

        # SET THE BUTTON IMAGES
        DISPLAYSURFACE.blit(START_BUTTON_IMG, (btnstart.X_POS, btnstart.Y_POS))
        DISPLAYSURFACE.blit(QUIT_BUTTON_IMG, (btnquit.X_POS, btnquit.Y_POS))

        # Updates the frames of the game
        pygame.display.update()

        # INITIATING running AS TRUE
        running = True

        # WHILE LOOP 
        while running:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    running = False
                # MAKE THE BUTTON CLICKABLE
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if btnstart.rect.collidepoint(mouse[0], mouse[1]):
                        PLAYER.HEALTH = 100
                        BEAST_LIST.clear()
                        self.state = 'main_game'
                        running = False

                    if btnquit.rect.collidepoint(mouse[0], mouse[1]):
                        key_events.quit()

            # INITIATE THE MOUSE VARIABLE AND WE GET ITS POSITION
            mouse = pygame.mouse.get_pos()

            # LOAD AUDIO FILE        
            pygame.mixer.music.load("./Sounds/ZeldaMenuSong.mp3")
            # PLAY THE MUSIC
            pygame.mixer.music.play(-1)
            
            # Updates the frames of the game
            pygame.display.update()

    # CREATE THE GAME OVER SCREEN
    def End(self):
        # Stop the music when the end screen
        pygame.mixer.music.stop()        
        BACKGROUNDCOLOR = (60,179,113)
        DISPLAYSURFACE.fill(BACKGROUNDCOLOR)

        # RENDER GAME OVER TEXT
        GAME_OVER_TEXT = HEALTHFONT.render('GAME OVER', True, GREEN, BLACK)
        DISPLAYSURFACE.blit(GAME_OVER_TEXT, (pygame.display.get_window_size()[0] / 2 - GAME_OVER_TEXT.get_size()[0] / 2, 50))

        # RENDER BUTTONS
        width = DISPLAYSURFACE.get_width()
        height = DISPLAYSURFACE.get_height()

        # BUTTON IMAGES 
        RESTART_BUTTON_IMG = btnrestart.SPRITE
        QUIT_BUTTON_IMG = btnquit.SPRITE

        # DRAW BUTTONS
        pygame.draw.rect(DISPLAYSURFACE, (0,255,0), btnrestart, 4)
        pygame.draw.rect(DISPLAYSURFACE, (0,255,0), btnquit, 4)

        # SET THE BUTTON IMAGES
        BUTTON_RESTART_IMAGE = DISPLAYSURFACE.blit(RESTART_BUTTON_IMG, (btnstart.X_POS, btnstart.Y_POS))
        BUTTON_QUIT_IMAGE = DISPLAYSURFACE.blit(QUIT_BUTTON_IMG, (btnquit.X_POS, btnquit.Y_POS))

        # updates the frames of the game
        pygame.display.update()

        # INITIATING running AS TRUE
        running = True

        # WHILE LOOP
        while running:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    running = False
                # MAKE THE BUTTON CLICKABLE
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # IF WE CLICK ON THE RESTART BUTTON IT BRINGS US BACK TO THE MENU
                    if btnrestart.rect.collidepoint(mouse[0], mouse[1]):
                        self.state = 'menu'
                        running = False

                    if btnquit.rect.collidepoint(mouse[0], mouse[1]):
                        key_events.quit()

            # INITIATING MOUSE VARIABLE AND WE GET ITS POSITION
            mouse = pygame.mouse.get_pos()

            # Updates the frames of the game
            pygame.display.update()

    # Function to switch windows during the game
    def state_manager(self):
        if self.state == 'menu':
            self.menu()
        elif self.state == 'main_game':
            self.main_game(Tree, TEMPLE, KEY)
        elif self.state == 'puzzle_room':
            self.puzzle_room()
        elif self.state == 'end_game':
            self.End()

# GAME VARIABLE               
GAME_OVER = False
GAME_STATE = gameState()

# Draw the canvas of the map
# RENDER GAME GRID
pygame.display.init()
window = (MAPWIDTH, MAPHEIGHT) 
background = pygame.Surface(window)

# Populate the surface with objects to be displayed
pygame.draw.rect(background,(0,255,255),(20,20,40,40))
pygame.draw.rect(background,(255,0,255),(120,120,50,50))

# GAME LOOP
while not GAME_OVER:
    # The function to call to start the game at the first window
    GAME_STATE.state_manager()

# END OF GAME LOOP