# Importing the pygame module
import pygame
from pygame.locals import *
 
# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()
 
# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((600, 600))
 
# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()
 
 
# Creating a new rect for first object
player_rect = Rect(200, 500, 50, 50)
 
# Creating a new rect for second object
player_rect2 = Rect(200, 0, 50, 50)
 
 
# Creating a boolean variable that
# we will use to run the while loop
run = True
 
# Speed for the objects
speed_a = 8
speed_b = -7
 
# Creating an infinite loop
# to run our game
while run:
 
    # Setting the framerate to 60fps
    clock.tick(60)
 
    # Adding speed in player rects
    player_rect.bottom += speed_a
    player_rect2.top += speed_b
 
    # Checking if player is colliding
    # with platform or not using the
    # colliderect() method.
    # It will return a boolean value
    collide = pygame.Rect.colliderect(player_rect,
                                      player_rect2)
 
    # If the objects are colliding
    # then changing the speed direction
    if collide:
        speed_a *= -1
        speed_b *= -1
 
    # Changing the direction if the objects
    # goes outside the window
    if player_rect.top<0 or player_rect.bottom > 600:
        speed_a *= -1
    if player_rect2.bottom > 600 or player_rect2.top<0:
        speed_b *= -1
     
    # Drawing player rect
    pygame.draw.rect(window, (0,   255,   0),
                     player_rect)
    # Drawing player rect2
    pygame.draw.rect(window, (0,   0,   255),
                     player_rect2)
 
    # Updating the display surface
    pygame.display.update()
 
    # Filling the window with white color
    window.fill((255, 255, 255))