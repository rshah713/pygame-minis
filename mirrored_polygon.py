"""
Rohan Shah

Click (at least 3 times) on the left canvas to create a polygon that will be mirrored

continue clicking to expand polygon
"""


import math
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('mirrored polygons')


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


green_polygon = []
pink_polygon = []

while True:
    screen.fill((100, 149, 237))
    draw_dashed_line(screen, (255, 255,255), (200, 0), (200, 400))
    
    if len(green_polygon) > 2:
        pygame.draw.polygon(screen, (144, 238, 144), tuple(green_polygon))
        pygame.draw.polygon(screen, (0, 0, 0), tuple(green_polygon), 2)
        pygame.draw.polygon(screen, (255, 192, 203), tuple(pink_polygon))
        pygame.draw.polygon(screen, (0, 0, 0), tuple(pink_polygon), 2)
        
   # draw_dashed_line(screen, (192, 192, 192), (0, 200), (200, 400), dash_length=5)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[0] < 200:
                green_polygon.append((pos))
                pink_polygon.append((400-pos[0], pos[1]))
    pygame.display.update()