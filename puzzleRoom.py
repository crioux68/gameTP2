import pygame, sys
from pygame.locals import *
from lib import enemies, heroes, items
from grid import *
import random
from key_events import KeyEvents
import math

#Room smaller than the map
roomWidht = 10
roomHeigth = 10

class Room:
    # Class to hold info about rooms/levels

    def __init__(self):
        pygame.init
        pygame.display.set_mode(roomWidht * TILESIZE, roomHeigth *TILESIZE)
        window = (roomWidht, roomHeigth) 
        background = pygame.Surface(window)
        #### Populate the surface with objects to be displayed ####
        pygame.draw.rect(background,(0,255,255),(20,20,40,40))
        pygame.draw.rect(background,(255,0,255),(120,120,50,50))
        # self.wall_list = self.goal_list = self.enemy_list = self.victory_sprite = None
        # self.collectedCoins = 0
        # self.numCoins = 0
        
        # Voir quoi mettre dans cette fonction
        print('dequoi')

# On definit la piece 1
def setup_room_1():
    room = Room()
    #TODO code pour tester une piece
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))

    #TODO code a faire pour dessiner la piece

    # room.wall_list = arcade.SpriteList(use_spatial_hash=True)
    # room.enemy_list = arcade.SpriteList()
    # room.goal_list = arcade.SpriteList(use_spatial_hash=True)
    # room.victory_sprite = arcade.SpriteList(use_spatial_hash=True)

    # # Draw platforms and ground
    # for x in range(0, roomWidht, tileSize):
    #     wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)

    #     wall.bottom = 0
    #     wall.left = x
    #     room.wall_list.append(wall)

    # for x in range(SPRITE_SIZE * 3, SPRITE_SIZE * 8, SPRITE_SIZE):
    #     wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)

    #     wall.bottom = SPRITE_SIZE * 3
    #     wall.left = x
    #     room.wall_list.append(wall)

    # # Draw the crates
    # for x in range(0, SCREEN_WIDTH, SPRITE_SIZE * 5):
    #     wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)

    #     wall.bottom = SPRITE_SIZE
    #     wall.left = x
    #     room.wall_list.append(wall)

    # # Draw an enemy 1
    # enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

    # enemy.bottom = SPRITE_SIZE
    # enemy.left = SPRITE_SIZE * 2

    # enemy.change_x = 2
    # room.enemy_list.append(enemy)

    # # -- Draw enemy2 on the platform
    # enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

    # enemy.bottom = SPRITE_SIZE * 4
    # enemy.left = SPRITE_SIZE * 4

    # # Set boundaries for enemy
    # enemy.boundary_right = SPRITE_SIZE * 8
    # enemy.boundary_left = SPRITE_SIZE * 3
    # enemy.change_x = 2
    # room.enemy_list.append(enemy)

    # # Set up coins
    # for pos in [[128, 96], [418, 300], [670, 150]]:
    #     goal = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING)
    #     goal.center_x = pos[0]
    #     goal.center_y = pos[1]
    #     room.goal_list.append(goal)
    #     room.numCoins += 1

    # # Set up checkpoint/level clear
    # flag = arcade.Sprite(":resources:images/tiles/signExit.png", SPRITE_SCALING)
    # flag.center_x = 770
    # flag.center_y = 96
    # room.victory_sprite.append(flag)

    # # Load the background image for this level.
    # room.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

    return room

# On definit la piece 2
# def setup_room_2():
#     room = Room()
#     room.wall_list = arcade.SpriteList(use_spatial_hash=True)
#     room.enemy_list = arcade.SpriteList()
#     room.goal_list = arcade.SpriteList(use_spatial_hash=True)
#     room.victory_sprite = arcade.SpriteList(use_spatial_hash=True)

#     # Set up walls
#     for y in range(0, 800, 200):
#         for x in range(100, 700, 64):
#             wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
#             wall.center_x = x
#             wall.center_y = y
#             room.wall_list.append(wall)

#     for pos in [[35, 40], [765, 80], [35, 280], [765, 480]]:
#         wall = arcade.Sprite(":resources:images/tiles/grassHalf.png", SPRITE_SCALING)
#         wall.center_x = pos[0]
#         wall.center_y = pos[1]
#         room.wall_list.append(wall)

#     # Create the coins
#     for i in range(50):

#         # Create the coin instance
#         # Coin image from kenney.nl
#         goal = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

#         # Boolean variable if we successfully placed the coin
#         coin_placed_successfully = False

#         # Keep trying until success
#         while not coin_placed_successfully:
#             # Position the coin
#             goal.center_x = random.randrange(100, 700)
#             goal.center_y = random.randrange(SCREEN_HEIGHT)

#             # See if the coin is hitting a wall
#             wall_hit_list = arcade.check_for_collision_with_list(goal, room.wall_list)

#             # See if the coin is hitting another coin
#             coin_hit_list = arcade.check_for_collision_with_list(goal, room.goal_list)

#             if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
#                 coin_placed_successfully = True

#         # Add the coin to the lists
#         room.goal_list.append(goal)
#         room.numCoins += 1

#     # Draw an enemy1
#     enemy = arcade.Sprite(":resources:images/enemies/fly.png", SPRITE_SCALING_COIN)

#     enemy.bottom = SPRITE_SIZE
#     enemy.left = SPRITE_SIZE * 2

#     enemy.boundary_right = SPRITE_SIZE * 8 + 60
#     enemy.boundary_left = SPRITE_SIZE * 1 + 60
#     enemy.change_x = 3
#     room.enemy_list.append(enemy)

#     # Draw a enemy2
#     enemy = arcade.Sprite(":resources:images/enemies/fly.png", SPRITE_SCALING_COIN)

#     enemy.bottom = SPRITE_SIZE * 4
#     enemy.left = SPRITE_SIZE * 4

#     enemy.boundary_right = SPRITE_SIZE * 8
#     enemy.boundary_left = SPRITE_SIZE * 3
#     enemy.change_x = 4
#     room.enemy_list.append(enemy)

#     # Draw a enemy3
#     enemy = arcade.Sprite(":resources:images/enemies/fly.png", SPRITE_SCALING_COIN)

#     enemy.bottom = SPRITE_SIZE * 7.2
#     enemy.left = SPRITE_SIZE * 4

#     enemy.boundary_right = SPRITE_SIZE * 8 + 80
#     enemy.boundary_left = SPRITE_SIZE * 3
#     enemy.change_x = 4.8
#     room.enemy_list.append(enemy)

#     # Draw victory point
#     flag = arcade.Sprite(":resources:images/tiles/signExit.png", SPRITE_SCALING)
#     flag.center_x = 765
#     flag.center_y = 545
#     room.victory_sprite.append(flag)

#     # Load the background image for this level.
#     room.background = arcade.load_texture(":resources:images/backgrounds/abstract_1.jpg")

#     return room