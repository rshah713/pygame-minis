"""
Rohan
Move the mouse to watch three other balls copy
"""

import pygame
import numpy
import math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)

def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(surf, color, start, end, width)

dot1 = (100, 100)
dot2 = (300, 100)
dot3 = (100, 300)
dot4 = (300, 300)

while True:
    screen.fill((30, 144, 255))

    pygame.draw.circle(screen, (220, 20, 60), dot1, 10)
    pygame.draw.circle(screen, (220, 20, 60), dot2, 10)
    pygame.draw.circle(screen, (220, 20, 60), dot3, 10)
    pygame.draw.circle(screen, (220, 20, 60), dot4, 10)

    draw_dashed_line(screen, (0,0,0), (0, 200), (400, 200), dash_length=5)
    draw_dashed_line(screen, (0,0,0), (200, 400), (200, 0), dash_length=5)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            """
            dot 1 follows mouse
            dot 2 reflects horizontally
            dot 3 reflects vertically
            dot 4 reflects both horiz/vert"""
            dot1 = pos
            dot2 = (400-pos[0], pos[1])
            dot3 = (pos[0], 400-pos[1])
            dot4 = (400-pos[0], 400-pos[1])

    pygame.display.update()