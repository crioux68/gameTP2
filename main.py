import pygame, sys
from pygame.locals import *
from lib import enemies, heroes, items
from grid import *
import random
from key_events import KeyEvents
import math

# INSTANCES OF GAME OBJECTS
PLAYER = heroes.LINK()
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

# GROUPINGS OF RELATED GAME OBJECTS
GAME_ITEMS = [WAND, SWORD, SHIELD]
GAME_WEAPONS = [WAND, BOW]
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
pygame.time.set_timer(USEREVENT, 400)
# SPAWN BEAST
pygame.time.set_timer(USEREVENT + 1, 7500)
# INCREMENT BEAST PORTAL FRAMES
pygame.time.set_timer(USEREVENT + 2, 400)
# MOVE BEASTS
pygame.time.set_timer(USEREVENT + 3, 1000)
# ORB TRAVEL ON PATH
pygame.time.set_timer(USEREVENT + 4, 100)

def menu():
    # CREATE THE GAME MENU SCREEN
    BACKGROUNDCOLOR = (36,110,7)
    DISPLAYSURFACE.fill(BACKGROUNDCOLOR)

    # RENDER PLAY GAME TEXT
    PLAY_GAME_TEXT = HEALTHFONT.render('PLAY GAME', True, GREEN, BLACK)
    DISPLAYSURFACE.blit(PLAY_GAME_TEXT, (pygame.display.get_window_size()[0] / 2 - PLAY_GAME_TEXT.get_size()[0] / 2, 50))

    # TODO RENDER BUTTONS
    width = DISPLAYSURFACE.get_width()
    height = DISPLAYSURFACE.get_height()

    # light shade of the button
    color_light = (170,170,170)
    
    # dark shade of the button
    color_dark = (100,100,100)

    BUTTON_QUIT_TEXT = HEALTHFONT.render('PLAY', True, BLACK)
    BUTTON_PLAY_TEXT = HEALTHFONT.render('QUIT', True, BLACK)

    # updates the frames of the game
    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False
            #RENDRE LE BOUTON CLIQUABLE
            if event.type == pygame.MOUSEBUTTONDOWN:

                if width/2 <= mouse[0] <= width/2+140 and height/2-100 <= mouse[1] <= height/2-60:
                    main()
                    print(mouse[1])
                    running = False

                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                    key_events.quit()

        mouse = pygame.mouse.get_pos()

        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            pygame.draw.rect(DISPLAYSURFACE,color_light,[width/2,height/2,140,40])
            
        else:
            pygame.draw.rect(DISPLAYSURFACE,color_dark,[width/2,height/2,140,40])

        if width/2 <= mouse[0] <= width/2+140 and height/2-100 <= mouse[1] <= height/2-60:
            pygame.draw.rect(DISPLAYSURFACE,color_light,[width/2,height/2-100,140,40])

        else:
            pygame.draw.rect(DISPLAYSURFACE,color_dark,[width/2,height/2-100,140,40])
        
        # superimposing the text onto our button
        DISPLAYSURFACE.blit(BUTTON_PLAY_TEXT , (width/2+50,height/2))        
        DISPLAYSURFACE.blit(BUTTON_QUIT_TEXT , (width/2+10,height/2-100))
        
        
        # updates the frames of the game
        pygame.display.update()
 

def main():

    PLAYER = heroes.LINK()
    key_events = KeyEvents(PLAYER)
    WAND = items.WAND()
    GOLD = items.GOLD()
    SWORD = items.SWORD()
    SHIELD = items.SHIELD()
    BOW = items.BOW()
    GANON = enemies.GANON()
    PORTAL = enemies.PORTAL()
    MIDNA = heroes.MIDNA()

    # GROUPINGS OF RELATED GAME OBJECTS
    GAME_ITEMS = [WAND, SWORD, SHIELD]
    GAME_WEAPONS = [WAND, BOW]
    BEAST_LIST = []
    orbs_list = []

    GAME_OVER = False
    # GAME LOOP
    while not GAME_OVER:

        GANON_VULNERABLE_IF = [beast for beast in BEAST_LIST if beast.APPEAR == True]

        if len(GANON_VULNERABLE_IF) < 1:
            GANON.VULNERABLE = True
        else:
            GANON.VULNERABLE = False

        for event in pygame.event.get():

            keys = pygame.key.get_pressed()
            key_events.global_events()
        
            if event.type == QUIT:
                key_events.quit()
        
            if keys[K_w] and keys[K_t]:
                key_events.key_w()

            # MOVE RIGHT
            if (keys[K_RIGHT]) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
                key_events.key_right() 
        
            # MOVE LEFT
            if (keys[K_LEFT]) and PLAYER.PLAYER_POS[0] > 0:
                key_events.key_left() 
        
            # MOVE UP
            if (keys[K_UP]) and PLAYER.PLAYER_POS[1] > 0:
                key_events.key_up()
        
            # MOVE DOWN
            if (keys[K_DOWN]) and PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1:
                key_events.key_down()
        
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
                    GANON.GANON_POS = [x, y]
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
            
            # BEASTS MOVEMENTS HUNT PLAYER
            elif (event.type == USEREVENT + 3):
                for beast in BEAST_LIST:
                    if beast.APPEAR:
                        if PLAYER.PLAYER_POS == beast.POS:
                            PLAYER.HEALTH -= 10
                        for coordinate in range(len(beast.POS)):
                            if PLAYER.PLAYER_POS[coordinate] > beast.POS[coordinate]:
                                beast.POS[coordinate] += 1 
                            else:
                                beast.POS[coordinate] -= 1
            
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

        """
        RENDERING GRID, SPRITES, AND VIEWS
        """

        # RENDER GAME GRID
        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))

        # RENDER LINK
        if PLAYER.TRANSFORM:
            DISPLAYSURFACE.blit(PLAYER.WOLF, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))
        else:
            DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

        # RENDER TEMPLE
        DISPLAYSURFACE.blit(TEMPLE.SPRITE, (TEMPLE.X_POS*TILESIZE, TEMPLE.Y_POS*TILESIZE))

        # RENDER MIDNA
        MIDNA.APPEARED = True
        if MIDNA.APPEARED:
            if PLAYER.TRANSFORM:
                DISPLAYSURFACE.blit(MIDNA.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE + 20, PLAYER.PLAYER_POS[1] * TILESIZE + 35))
            else:
                DISPLAYSURFACE.blit(MIDNA.SPRITE_POS, (TEMPLE.X_POS*TILESIZE, TEMPLE.Y_POS*TILESIZE))

        # RENDERING ARMED ITEMS WITH PLAYER SPRITE
        if PLAYER.WEAPON:
            DISPLAYSURFACE.blit(PLAYER.WEAPON.IMAGE_ARMED, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

        # RENDER BEASTS AND PORTAL
        for beast in BEAST_LIST:
            if beast.PORTAL_APPEAR:
                DISPLAYSURFACE.blit(pygame.image.load(portal_images[beast.PORTAL.FRAME]), (beast.PORTAL.POS[0]*TILESIZE, beast.PORTAL.POS[1]*TILESIZE))
            if beast.APPEAR:
                DISPLAYSURFACE.blit(beast.BEAST, (beast.POS[0]*TILESIZE, beast.POS[1]*TILESIZE))

        # RENDER ITEMS
        for item in GAME_ITEMS:
                if item.PLACED == True:
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

    # END OF GAME LOOP
    End()

def End():
    # CREATE THE GAME OVER SCREEN
    #pygame.init()
    #screen = pygame.display.set_mode((800, 600))
    BACKGROUNDCOLOR = (36,110,7)
    DISPLAYSURFACE.fill(BACKGROUNDCOLOR)

    # RENDER GAME OVER TEXT
    GAME_OVER_TEXT = HEALTHFONT.render('GAME OVER', True, GREEN, BLACK)
    DISPLAYSURFACE.blit(GAME_OVER_TEXT, (pygame.display.get_window_size()[0] / 2 - GAME_OVER_TEXT.get_size()[0] / 2, 50))

    # TODO RENDER BUTTONS
    width = DISPLAYSURFACE.get_width()
    height = DISPLAYSURFACE.get_height()

    # light shade of the button
    color_light = (170,170,170)
    
    # dark shade of the button
    color_dark = (100,100,100)

    BUTTON_QUIT_TEXT = HEALTHFONT.render('QUIT', True, BLACK)
    BUTTON_RESTART_TEXT = HEALTHFONT.render('RESTART', True, BLACK)

    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                running = False
            #RENDRE LE BOUTON CLIQUABLE
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                    key_events.quit()
                if width/2 <= mouse[0] <= width/2+140 and height/2-100 <= mouse[1] <= height/2-60:
                    running = False
                    main()
                    print(mouse[1])

        mouse = pygame.mouse.get_pos()
        
        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
            pygame.draw.rect(DISPLAYSURFACE,color_light,[width/2,height/2,140,40])
            
        else:
            pygame.draw.rect(DISPLAYSURFACE,color_dark,[width/2,height/2,140,40])

        if width/2 <= mouse[0] <= width/2+140 and height/2-100 <= mouse[1] <= height/2-60:
            pygame.draw.rect(DISPLAYSURFACE,color_light,[width/2,height/2-100,140,40])

        else:
            pygame.draw.rect(DISPLAYSURFACE,color_dark,[width/2,height/2-100,140,40])
        
        # superimposing the text onto our button
        DISPLAYSURFACE.blit(BUTTON_QUIT_TEXT , (width/2+50,height/2))
        DISPLAYSURFACE.blit(BUTTON_RESTART_TEXT , (width/2+10,height/2-100))
        
        # updates the frames of the game
        pygame.display.update()

menu()
#End()
