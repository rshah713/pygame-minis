"""
Rohan Shah

move the mouse to move the player
speed increases every barrier you pass
"""

import pygame, random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 400), 0, 32)
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 30)
score_fnt = pygame.font.Font('freesansbold.ttf', 18)
direction_fnt = pygame.font.Font('freesansbold.ttf', 12)
game_over_fnt= pygame.font.Font('freesansbold.ttf', 48)

FPS = 30
GAP_WIDTH = 90# change this to make gap bigger/smaller
MEDIUMSLATEBLUE = (123,104,238)
WHITE = (255,255,255)
ALICEBLUE = (240,248,255)
ORANGERED = (255,69,0)
ORANGE = (255,165,0)
RED = (255,0,0)
DARKBLUE = (0,0,139)


score = 0
gameover_visible = False
barrier1 = pygame.Rect(-400, 0, 425, 25)
barrier2 = pygame.Rect(100, 0, 400, 25)
player = pygame.Rect(0, 0, 50, 50)
player.center = (200, 300)
barrier_dy = 6
barrier_maxdy = 12


def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 0,1 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 1,0 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )  

def next_barrier():
    # keep 75 px opening
    global barrier1, barrier2
    barrier1.bottom, barrier2.bottom = 0, 0
    barrier1.right = random.randint(50, 400-GAP_WIDTH)
    barrier2.left = barrier1.right + GAP_WIDTH

def move_barrier():
    global score, barrier_dy, barrier1, barrier2
    barrier1.top += barrier_dy
    barrier2.top += barrier_dy

    if barrier1.top >= 400:
        score += 1
        # If we wraparound, increases speed until we reach max speed.
        if barrier_dy < barrier_maxdy:
            barrier_dy += 1
        next_barrier()
    
while True:
    gradientRect(screen, MEDIUMSLATEBLUE,DARKBLUE, pygame.Rect(0, 0, 400, 400) )

    # draw barrier and player

    gradientRect(screen, ORANGE, RED, barrier1)
    gradientRect(screen, ORANGE, RED, barrier2)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, MEDIUMSLATEBLUE, player, 2)

    author = font.render('Barriers!', True, WHITE)
    author_r = author.get_rect()
    author_r.midright = (390, 20)
    screen.blit(author, author_r)

    msg = score_fnt.render('Score: ', True, WHITE)
    msg_r = msg.get_rect()
    msg_r.center = (340, 45)
    screen.blit(msg, msg_r)

    msg = score_fnt.render(str(score), True, WHITE)
    msg_r = msg.get_rect()
    msg_r.center = (380, 45)
    screen.blit(msg, msg_r)

    msg = direction_fnt.render('Move the mouse to avoid barriers', True, WHITE)
    msg_r = msg.get_rect()
    msg_r.midleft = (20, 20)
    screen.blit(msg, msg_r)

    if gameover_visible:
        rect = pygame.Rect(200, 200, 300, 125)
        rect.center = (200, 200)
        pygame.draw.rect(screen, (198, 201, 240), rect)
        
        msg = game_over_fnt.render('Game Over', True, ORANGERED)
        msg_r = msg.get_rect()
        msg_r.center = (200, 175)
        screen.blit(msg, msg_r)

        msg = score_fnt.render('Press any key to restart', True, ORANGERED)
        msg_r = msg.get_rect()
        msg_r.center = (200, 225)
        screen.blit(msg, msg_r)

    else:
        # If the game is not over, move the barrier.
        move_barrier()
        # End the game if the player hits the barrier.
        if player.colliderect(barrier1) or player.colliderect(barrier2):
            gameover_visible = True


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if not gameover_visible:
                player.center = pos
        if event.type == KEYDOWN:
            if gameover_visible:
                gameover_visible = False
                score = 0
                next_barrier()
                barrier_dy = 6
                
    clock.tick(FPS)
    pygame.display.update()