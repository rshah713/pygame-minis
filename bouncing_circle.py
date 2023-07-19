'''
Rohan Shah
Small animation of circle bouncing
'''

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('changing directions!')
clock = pygame.time.Clock()

TURQUOISE = (64,224,208)
ORANGERED = (255,69,0)
bouncing_circle_speedx = 5
bouncing_circle = [200, 200]

while True:
    pygame.draw.rect(screen, TURQUOISE, (0, 0, 400, 400))
    pygame.draw.ellipse(screen, ORANGERED, (200-300//2, 200-150//2, 300, 150))
    pygame.draw.circle(screen, TURQUOISE, bouncing_circle, 25)

    if bouncing_circle[0] > 300:
        bouncing_circle_speedx = -12
    elif bouncing_circle[0] < 100:
        bouncing_circle_speedx = 5

    bouncing_circle[0] += bouncing_circle_speedx
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    clock.tick(30)
    pygame.display.update()