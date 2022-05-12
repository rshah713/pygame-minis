"""
Rohan Shah
Click the cookie to eat the cookie
"""

import pygame
from pygame.locals import *

print("\n\nDIRECTIONS:")
print('click screen to eat cookie')

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
screen.fill((176, 196, 222))

# brown - 139, 69, 19
# peru - 205, 133, 63

# cookie
pygame.draw.circle(screen, (139, 69, 19), (205, 205), 155 )
pygame.draw.circle(screen, (205, 133, 63), (200, 200), 150)

def draw_choco_chips(x, y):
    pygame.draw.circle(screen, (90, 35, 15), (x,y), 10)


draw_choco_chips(140, 90)
draw_choco_chips(215, 150)
draw_choco_chips(275, 100)
draw_choco_chips(315, 200)
draw_choco_chips(270, 300)
draw_choco_chips(230, 240)
draw_choco_chips(150, 315)
draw_choco_chips(150, 245)
draw_choco_chips(80, 220)
draw_choco_chips(120, 155)
draw_choco_chips(190, 200)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (176, 196, 222), pos, 40)

    pygame.display.update()