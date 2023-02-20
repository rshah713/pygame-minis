"""
Rohan Shah
Small animation cycling thru RGB vals
"""
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
clock = pygame.time.Clock()
pygame.display.set_caption('Reds')

REDS = [255, 220, 200, 150, 125, 100, 90, 75, 50, 10]
Y = 0

def draw_rect_row():
    x = 0
    for red in REDS:
        pygame.draw.rect(screen, (red, 0, 0), (x, Y, 40, 25))
        x += 40

pygame.draw.rect(screen, (0, 0, 0), (0, 0, 400, 400))
while True:
    if Y <= 400:
        draw_rect_row()
        REDS.insert(0, REDS.pop())
        Y += 25
        
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(5)
    pygame.display.update()
