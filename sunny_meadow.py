'''
Rohan Shah

Animation of flower growing on a field
grows 175 flowers
'''

import random
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('sunny meadow animation')
font = pygame.font.Font('freesansbold.ttf', 12)
clock = pygame.time.Clock()

def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )

def draw_flower(x, y, size, color):
    pygame.draw.line(screen, (60, 179, 113), (x, y), (x, y+2 * size))
    pygame.draw.circle(screen, color, (x, y), (size))

    if color == (255, 255, 0): # yellow
        inner = (205, 133, 63) # peru 
    elif color  == (224, 255, 255): # light cyan
        inner = (135, 206, 235) # sky blue
    elif color  == (255, 255, 255): # white
        inner = (255, 192, 203) # pink

    pygame.draw.circle(screen, inner, (x, y), size // 2)

pygame.draw.rect(screen, (135, 206, 250), (0, 0, 400, 400))

msg = font.render('Flower Count:', True, (0, 0, 0))
msg_r = msg.get_rect()
msg_r.midright = (340, 20)
screen.blit(msg, msg_r)

 # sun and grass
pygame.draw.circle(screen, (255, 255, 0), (0, 0), 55)
gradientRect(screen, (154, 205, 50), (34, 139, 34), pygame.Rect(0, 150, 400, 250))

msg_rect = pygame.Rect(0, 0, 0, 0)
FLOWER_COUNT = 0
while True:
    
    pygame.draw.rect(screen, (135, 206, 250), msg_rect)
    msg = font.render(str(FLOWER_COUNT), True, (0, 0, 0))
    msg_rect = msg.get_rect()
    msg_rect.midleft = (340, 20)
    screen.blit(msg, msg_rect)

    # As long as there aren't too many flowers, make another.
    if FLOWER_COUNT < 175:
        # Get the random position of the flower. It can't be higher than the
        # grass and the lowest point it can be is a y value of 390.
        flower_x = random.randint(0, 400)
        flower_y = random.randint(150, 391)

        # Makes the flower size bigger the lower it is on the canvas.
        size = 2 * flower_y // 100

        # Randomly define pickColor to a value between 0 and 100 (excluding
        # 100). If it is less than 60, set the color to yellow, if it is
        # between 60 and 80 set it to lightCyan, and white otherwise.
        pickcolor = random.randint(0, 100)
        if pickcolor < 60:
            color = (255, 255, 0)
        elif pickcolor < 80:
            color = (224, 255, 255)
        else:
            color =  (255, 255, 255)

        draw_flower(flower_x, flower_y, size, color)
        FLOWER_COUNT += 1
    
    

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
    clock.tick(30)
    pygame.display.update()