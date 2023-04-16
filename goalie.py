
"""
Rohan Shah
Goalie-defender game using mouse movement
"""

import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
clock = pygame.time.Clock()
pygame.display.set_caption('goalie!')

WHITE = (255,255,255)
ROSYBROWN = (188,143,143)
PEACHPUFF = (255,218,185)
MEDIUMSEAGREEN = (60,179,113)

SHOT_WAS_MADE = False

while True:
    # background
    screen.fill(MEDIUMSEAGREEN)
    pygame.draw.line(screen, WHITE, (0, 30), (100, 30), 4)
    pygame.draw.line(screen, WHITE, (300, 30), (400, 30), 4)
    pygame.draw.line(screen, WHITE, (0, 320), (400, 320), 3)
    pygame.draw.rect(screen, WHITE, (40, 30, 320, 90), 2)
    pygame.draw.circle(screen, ROSYBROWN, (200, 200), 12)
    pygame.draw.ellipse(screen, WHITE, (50, 280, 400-100, 80), 1)
    pygame.draw.rect(screen, MEDIUMSEAGREEN, (0, 275, 400, 45))

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(*pos)
    pygame.display.update()
    clock.tick(100)