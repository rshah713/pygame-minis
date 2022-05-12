"""
Rohan Shah
Move the mouse to start the UFO chase
"""

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption("UFO Chase")

trail1start = (0, 0)
trail2start = (0, 0)
trail3start = (0, 0)

trail1end = (0, 0)
trail2end = (0, 0)
trail3end = (0, 0)

fighter1 = (-10, -10)
fighter2 = (-10, -10)
fighter3 = (-10, -10)



while True:
    screen.fill((0,0,0))

    # moon
    pygame.draw.circle(screen, (128, 128, 128), (50, 100), 30)
    pygame.draw.circle(screen, (50, 50, 50), (40, 80), 3)
    pygame.draw.circle(screen, (85, 85, 85), (65, 85), 4)
    pygame.draw.circle(screen, (85, 85, 85), (40, 115), 4)
    pygame.draw.circle(screen, (55, 55, 55), (45, 95), 4)

    # trails
    pygame.draw.line(screen, (0, 0, 255), trail1start, trail1end, 5)
    pygame.draw.line(screen, (0, 255, 0), trail2start, trail2end, 5)
    pygame.draw.line(screen, (255, 0, 0), trail3start, trail3end, 5)

    # fighters
    pygame.draw.circle(screen, (128, 128, 128), fighter1, 5)
    pygame.draw.circle(screen, (128, 128, 128), fighter2, 5)
    pygame.draw.circle(screen, (128, 128, 128), fighter3, 5)
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            fighter1 = pos
            fighter2 = trail1start
            fighter3 = trail2start

            trail1start = trail1end
            trail1end = fighter1

            trail2start = trail2end
            trail2end = fighter2

            trail3start = trail3end
            trail3end = fighter3
            

    pygame.display.update()