"""
Rohan Shah

arrow keys to move the cursor, space to clear the sketch
"""

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('etch-a-sketch')
font = pygame.font.Font('freesansbold.ttf', 30)
dir_fnt = pygame.font.Font('freesansbold.ttf', 15)

BEIGE = (245,245,220)
WHITE = (255,255,255)
DARKGREY = (169,169,169)
RED = (255,0,0)

screen.fill(RED)

msg = font.render('Etch-a-Sketch', True, BEIGE)
msg_r = msg.get_rect()
msg_r.center = (200, 30)
screen.blit(msg, msg_r)

msg = dir_fnt.render('Use the arrow keys to draw!', True, BEIGE)
msg_r = msg.get_rect()
msg_r.center = (200, 360)
screen.blit(msg, msg_r)

msg = dir_fnt.render('Use the space key to clear the screen!', True, BEIGE)
msg_r = msg.get_rect()
msg_r.center = (200, 60)
screen.blit(msg, msg_r)

pygame.draw.circle(screen, WHITE, (45, 360), 25)
pygame.draw.circle(screen, WHITE, (355, 360), 25)

pygame.draw.circle(screen, DARKGREY, (30, 85), 10)
pygame.draw.circle(screen, DARKGREY, (370, 85), 10)
pygame.draw.circle(screen, DARKGREY, (30, 305), 10)
pygame.draw.circle(screen, DARKGREY, (370, 305), 10)

pygame.draw.line(screen, DARKGREY, (30, 85), (370, 85), 20)
pygame.draw.line(screen, DARKGREY, (30, 85), (30, 305), 20)
pygame.draw.line(screen, DARKGREY, (370, 85), (370, 305), 20)
pygame.draw.line(screen, DARKGREY, (30, 305), (370, 305), 20)

sketch = pygame.Rect(30, 85, 340, 225)
pygame.draw.rect(screen, DARKGREY, sketch)
cursor = pygame.Rect(200, 200, 4, 4)
pygame.draw.rect(screen, (0, 0, 0), cursor)

cursor_newX = 200
cursor_newY = 200


while True:
    

    if sketch.collidepoint(cursor_newX, cursor_newY):
        pygame.draw.line(screen, (0, 0, 0), cursor.center, (cursor_newX, cursor_newY))
        pygame.draw.rect(screen, DARKGREY, cursor)
        cursor.center = (cursor_newX, cursor_newY)
            

    #pygame.draw.rect(screen, DARKGREY, cursor)
    pygame.draw.rect(screen, (0, 0, 0), cursor)

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            cursor_newX, cursor_newY = cursor.center
            if event.key == K_UP:
                cursor_newY -= 15
            elif event.key == K_DOWN:
                cursor_newY += 15
            elif event.key == K_LEFT:
                cursor_newX -= 15
            elif event.key == K_RIGHT:
                cursor_newX += 15
            elif event.key == K_SPACE:
                pygame.draw.rect(screen, DARKGREY, sketch)
                pygame.draw.rect(screen, (0, 0, 0), cursor)

    
    pygame.display.update()
