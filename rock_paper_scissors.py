"""
Rohan Shah
10/17/22

Rock Paper Scissors using keydown inputs
Automatically displaying winner
"""

import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Rock Paper Scissors!')
font = pygame.font.Font('freesansbold.ttf', 25)
directions_fnt = pygame.font.Font('freesansbold.ttf', 14)
winner_fnt = pygame.font.Font('freesansbold.ttf', 60)

STEELBLUE = (70,130,180)
LIGHTSTEELBLUE = (176,196,222)
GOLD = (255,215,0)
BLACK = (0, 0, 0)

def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )  

def draw_fingers(x1, y1, x2, y2):
    pygame.draw.line(screen, GOLD, (x1, y1), (x2, y2), 20)
    pygame.draw.circle(screen, GOLD, (x1, y1), 10)

def drawLeftHand():
    pygame.draw.circle(screen, GOLD, (100, 200), 50)
    if leftThrow != 'Rock':
        draw_fingers(85, 90, 85, 200)
        draw_fingers(60, 100, 60, 200)
    if leftThrow == 'Paper':
        draw_fingers(110, 90, 110, 200)
        draw_fingers(135, 100, 135, 200)
        draw_fingers(160, 170, 125, 230)


def drawRightHand():
    pygame.draw.circle(screen, GOLD, (300, 200), 50)
    if rightThrow != 'Rock':
        draw_fingers(285, 90, 285, 200)
        draw_fingers(260, 100, 260, 200)
    if rightThrow == 'Paper':
        draw_fingers(310, 90, 310, 200)
        draw_fingers(335, 100, 335, 200)
        draw_fingers(360, 170, 325, 230)


def drawWinner(leftMove, rightMove):
    # Check leftMove and rightMove and draw == , > , < accordingly.
    if (leftMove == rightMove):
        msg = winner_fnt.render('==', True, BLACK)
    elif (((leftMove == 'Rock') and (rightMove == 'Scissors')) or
          ((leftMove == 'Paper') and (rightMove == 'Rock')) or
          ((leftMove == 'Scissors') and (rightMove == 'Paper'))):
        msg = winner_fnt.render('>', True, BLACK)
    else:
        msg = winner_fnt.render('<', True, BLACK)

    msg_r = msg.get_rect()
    msg_r.center = (200, 200)
    screen.blit(msg, msg_r)

    

        
def throwdown():
    # Draw over the old hand and redraw the hands.
    gradientRect(screen, STEELBLUE, LIGHTSTEELBLUE, pygame.Rect(0, 0, 400, 400) )

    # update left/right choice labels
    msg = font.render(leftThrow, True, BLACK)
    msg_r = msg.get_rect()
    msg_r.center = (100, 275)
    screen.blit(msg, msg_r)

    msg = font.render(rightThrow, True, BLACK)
    msg_r = msg.get_rect()
    msg_r.center = (300, 275)
    screen.blit(msg, msg_r)

    # bring directions to front
    msg = directions_fnt.render('Use s, d, f key to control left', True, BLACK)
    msg_r = msg.get_rect()
    msg_r.center = (200, 375)
    screen.blit(msg, msg_r)

    msg = directions_fnt.render('Use j, k, l key to control right', True, BLACK)
    msg_r = msg.get_rect()
    msg_r.center = (200, 390)
    screen.blit(msg, msg_r)
    
    drawLeftHand()
    drawRightHand()
    drawWinner(leftThrow, rightThrow)

leftThrow = 'Rock'
rightThrow = 'Rock'

throwdown()

while True:

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the left/right choice
            if event.key == K_s:
                leftThrow = 'Rock'
            elif event.key == K_d:
                leftThrow = 'Paper'
            elif event.key == K_f:
                leftThrow = 'Scissors'
            elif event.key == K_l:
                rightThrow = 'Rock'
            elif event.key == K_k:
                rightThrow = 'Paper'
            elif event.key == K_j:
                rightThrow = 'Scissors'
            throwdown()
            
    pygame.display.update()