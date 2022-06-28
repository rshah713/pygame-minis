"""
Rohan Shah

Type to draw letters, space moves cursor, automatically wraps line
"""

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('caption the worm')
font = pygame.font.Font('freesansbold.ttf', 40)

screen.fill((102, 205, 170))

def draw_oval(centerX, centerY, width, height, color):
    pygame.draw.ellipse(screen, color, (centerX - width//2, centerY - height//2, width, height))

# apple
draw_oval(200, 70, 20, 50, (34, 139, 34))
draw_oval(175, 145, 100, 150, (178, 34, 34))
draw_oval(225, 145, 100, 150, (178, 34, 34))
draw_oval(150, 140, 40, 100, (255, 255, 255))
draw_oval(155, 140, 40, 100, (178, 34, 34))

# worm
pygame.draw.circle(screen,(102, 205, 170), (260, 140), 30)
draw_oval(235, 140, 10, 20, (60, 179, 113))
draw_oval(245, 145, 10, 20, (144, 238, 144))
draw_oval(255, 140, 10, 20, (60, 179, 113))
draw_oval(265, 145, 10, 20, (144, 238, 144))
draw_oval(275, 140, 10, 20, (60, 179, 113))
pygame.draw.line(screen, (238, 232, 170), (285, 125), (280, 115))
pygame.draw.line(screen, (238, 232, 170), (280, 115), (275, 120))
pygame.draw.line(screen, (238, 232, 170), (295, 125), (300, 115))
pygame.draw.line(screen, (238, 232, 170), (300, 115), (305, 120))
pygame.draw.circle(screen, (34, 139, 34), (290, 130), 10)
pygame.draw.circle(screen, (0, 0, 0), (285, 125), 2)
pygame.draw.circle(screen, (0, 0, 0), (295, 125), 2)
pygame.draw.circle(screen, (0, 0, 0), (290, 133), 3)

cursor_centerX = 20
cursor_centerY = 260


while True:

    cursor = font.render('|', True, (255, 255, 255))
    cursor_rect = cursor.get_rect()
    cursor_rect.center = (cursor_centerX, cursor_centerY)
    
    screen.blit(cursor, cursor_rect)
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            pygame.draw.rect(screen,(102, 205, 170), cursor_rect )
            if event.key != K_SPACE:
                msg = font.render(event.unicode, True, (255, 255, 255))
                msg_rect = msg.get_rect()
                msg_rect.center = (cursor_centerX, cursor_centerY)
                screen.blit(msg, msg_rect)
            
            cursor_centerX += 30
            if cursor_centerX > 380:
                cursor_centerY += 40
                cursor_centerX = 20
                
    pygame.display.update()
