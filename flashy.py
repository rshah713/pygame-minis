"""
Rohan Shah

3/17/23
Flashing circles animation that randomly appear and change
"""

import pygame, sys
from pygame.locals import *

import random

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('flashy!')
clock = pygame.time.Clock()

LIGHTCORAL = (240,128,128)
PALEGREEN = (152,251,152)
LAVENDER = (230,230,250)

# Creates the lists of x and y coordinates for the circles.
listX = []
listY = []
list_colors = [LIGHTCORAL, PALEGREEN, LAVENDER]

def add_circle():
    centerX = random.randint(0, 400)
    centerY = random.randint(0, 400)
    listX.append(centerX)
    listY.append(centerY)

def remove_circle():
    if len(listX) > 10:
        remove_ind = random.randint(0, len(listX)-1)
        listX.pop(remove_ind)
        listY.pop(remove_ind)

def draw_circles():
    # Clears the canvas and redraws the background.
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 400))

    # Loops over all the coordinates and draws 2 circles with random
    # radius and color.
    for index, centerX in enumerate(listX):
        centerY = listY[index]
        radius = random.randint(5, 25)

        color = random.choice(list_colors)

        pygame.draw.circle(screen, color, (centerX, centerY), radius, 1)
        pygame.draw.circle(screen, color, (centerX, centerY), radius+5, 3)    

while True:
    add_circle()
    remove_circle()
    draw_circles()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.display.update()
    clock.tick(10)