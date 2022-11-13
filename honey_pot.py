"""
Rohan Shah
11/13/22
Click the mouse to draw honey from pot
automatically adjusts width of honey depending on click
"""

import pygame, sys
from pygame.locals import *
import math
import numpy

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('honey jar!')
font = pygame.font.Font('freesansbold.ttf', 25)

GOLDENROD = (218,165,32)
PERU = (205,133,63)
SADDLEBROWN = (139,69,19)
MEDIUMSEAGREEN = (60,179,113)
GREEN = (0,128,0)
CHOCOLATE = (210,105,30)
SIENNA = (160,82,45)
BURLYWOOD = (222,184,135)
MAROON = (128,0,0)
WHITE = (255,255,255)
LIGHTSKYBLUE = (135,206,250)
LIGHTCYAN = (224,255,255)

def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )  


def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=5):
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

sticky_honey_y2 = 200
sticky_honey_linewidth = 40
dipper_stick = [200, 100]
dipper_top = [200, 180]
    
while True:
    gradientRect(screen, LIGHTSKYBLUE, LIGHTCYAN, pygame.Rect(0, 0, 400, 400))

    #flower and tree
    pygame.draw.rect(screen, PERU, (375, 200, 25, 200))
    pygame.draw.circle(screen, GREEN, (325, 200), 50)
    pygame.draw.circle(screen, GREEN, (400, 200), 50)
    pygame.draw.circle(screen, GREEN, (350, 150), 50)
    pygame.draw.circle(screen, GREEN, (375, 100), 50)
    pygame.draw.circle(screen, GREEN, (400, 50), 50)


    # honey stick, dipper stick
    pygame.draw.line(screen, GOLDENROD, (200, 275), (200, sticky_honey_y2), sticky_honey_linewidth)
    pygame.draw.line(screen, SIENNA, (200, dipper_stick[0]), (400, dipper_stick[1]), 20)
    draw_dashed_line(screen, GOLDENROD, (200, dipper_top[0]), (240, dipper_top[1]), width=40)

    # honey pot
    pygame.draw.polygon(screen, CHOCOLATE, ((125, 265), (140, 275), (125, 300), (125, 375), (140, 400), (260, 400), (275, 375), (275, 300), (260, 275), (275, 265)))
    pygame.draw.polygon(screen, GOLDENROD, ((125, 265), (140, 275), (125, 300), (125, 375), (140, 400), (260, 400), (275, 375), (275, 300), (260, 275), (275, 265)), 2)

    # label
    pygame.draw.rect(screen, GOLDENROD, (200-50, 340-25, 100, 50))
    msg = font.render('HONEY', True, WHITE)
    msg_r = msg.get_rect()
    msg_r.center = (200, 340)
    screen.blit(msg, msg_r)
    
    
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            sticky_honey_y2 = pos[1]

            # This changes the lineWidth and position of the honey.
            sticky_honey_linewidth = int(pos[1] / 5) + 1

            # Change the y1 and y2 values of the dipperStick to move to the
            # location of click.
            dipper_stick = [pos[1], pos[1] - 100]

            # Change the y1 and y2 values of dipperTop.
            dipper_top = [pos[1], pos[1]-20]
    pygame.display.update()