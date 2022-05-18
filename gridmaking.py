"""
Rohan Shah
Small animated grid that expands
"""

import pygame
from pygame.locals import *
from _dashes import draw_dashed_line

pygame.init()

screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('grid making')
clock = pygame.time.Clock()

lWidth = 2
while True:

    draw_dashed_line(screen, (211, 211, 211), (0, 200), (400, 200), width=lWidth)

    draw_dashed_line(screen, (70, 130, 180), (200, 0), (200, 400), width=lWidth)

    pygame.draw.line(screen, (192, 192, 192), (15, 0), (15, 400), 30)
    pygame.draw.line(screen, (192, 192, 192), (385, 0), (385, 400), 30)
    pygame.draw.line(screen, (192, 192, 192), (0, 15), (400, 15), 30)
    pygame.draw.line(screen, (192, 192, 192), (0, 385), (400, 385), 30)

    lWidth += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    clock.tick(30)
    pygame.display.update()