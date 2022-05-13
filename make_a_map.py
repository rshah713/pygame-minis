"""
Rohan Shah
Click to place pushpin on map
"""

import pygame
from pygame.locals import *

print("\n\nDIRECTIONS")
print("Click to place pushpin")

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)

def draw_road(startX, startY, endX, endY):
    pygame.draw.line(screen, (142, 137, 131), (startX, startY), (endX, endY), 4)

def draw_river(centerX, centerY, width, height):
    pygame.draw.ellipse(screen, (65, 105, 225), (centerX - width//2, centerY - height//2, width, height))
    pygame.draw.ellipse(screen,(144, 238, 144), (centerX - (width-30)//2, centerY - (height-30)//2, width-30, height-30))



screen.fill((144, 238, 144))

pygame.draw.ellipse(screen, (65, 105, 225), (10-50, 300-150//2, 100, 150))

draw_river(400, 0, 450, 320)
draw_river(400, 400, 350, 350)


draw_road(35, 110, 100, 110)
draw_road(100, 110, 100, 265)
draw_road(100, 110, 155, 170)
draw_road(155, 170, 345, 170)
draw_road(345, 170, 405, 205)
draw_road(35, 110, 35, 35)
draw_road(0, 35, 220, 35)
draw_road(220, 35, 255, -5)
draw_road(-5, 180, 185, 335)
draw_road(185, 335, 405, 335)
draw_road(100, 265, 60, 360)
draw_road(60, 360, 60, 405)
draw_road(295, 405, 295, 80)
draw_road(295, 80, 220, 35)
draw_road(295, 80, 405, 80)


while True:
    
    # royal blue 65, 105, 225


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0,0,0), pos, 2)
            pygame.draw.line(screen, (0,0,0), pos, (pos[0], pos[1]-20))
            pygame.draw.circle(screen, (220, 20, 60), (pos[0], pos[1]-20), 5)


    pygame.display.update()

    




