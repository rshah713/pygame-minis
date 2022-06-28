"""
Rohan Shah

Proper atari game, move the mouse to move paddle
"""


import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('atari breakout')
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 50)
FPS = 50


COLORS = {
    'red': (255, 0, 0),
    'lemonChiffon': (255, 250, 205),
    'steelBlue': (70, 130, 180),
    'cornflowerBlue' : (100, 149, 237),
    'skyBlue' : (135, 206, 235),
    'lightBlue': (173, 216, 230),
    'lightCyan': (224, 255, 255)
}
# [ [rect, color], [rect, color]..]
BLOCKS = []
BLOCK_COUNT = 0
ROW_COLOR = 'red'

paddle = pygame.Rect(160, 380, 80, 20)
paddle_prevx = 160

ball = [200, 370]
ball_dx = 3
ball_dy = -6

def set_row_color(row):
    global ROW_COLOR
    if row == 0:
        ROW_COLOR = 'steelBlue'
    elif row == 1:
        ROW_COLOR = 'cornflowerBlue'
    elif row == 2:
        ROW_COLOR = 'skyBlue'
    elif row == 3:
        ROW_COLOR = 'lightBlue'
    else:
        ROW_COLOR = 'lightCyan'

def make_row(row):
    global BLOCKS, BLOCK_COUNT
    # For the given row, add 5 blocks and increase the blockCount.
    for col in range(5):
        r = pygame.Rect(col * 80, row * 30, 80, 30)
        BLOCKS.append([r, ROW_COLOR])
        BLOCK_COUNT += 1

def make_blocks():
    for row in range(5):
        # For each row, set the row color and make the row.
        set_row_color(row)
        make_row(row)
        
def isectRectCircle(rect, circle_cpt, circle_rad):

    if rect.collidepoint(*circle_cpt):
        return True

    centerPt = pygame.math.Vector2(*circle_cpt)
    cornerPts = [rect.bottomleft, rect.bottomright, rect.topleft, rect.topright]
    if [p for p in cornerPts if pygame.math.Vector2(*p).distance_to(centerPt) <= circle_rad]:
        return True

    return False

make_blocks()

while True:
    screen.fill((0, 0, 0))

    # paddle! 
    pygame.draw.rect(screen, COLORS['lemonChiffon'], paddle)

    # ball
    pygame.draw.circle(screen, COLORS['lemonChiffon'], tuple(ball), 10)

    # blocks
    for row in BLOCKS:
        rect, color = row
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 3)

    if BLOCK_COUNT == 0:
        msg = font.render('You Win!', True, (255, 255, 255))
        msg_rect = msg.get_rect()
        msg_rect.center = (200, 200)
        screen.blit(msg, msg_rect)
        pygame.display.update()
        break



    ball[0] += ball_dx
    ball[1] += ball_dy
    # Checks if the ball has gone out of range and bounce it if it hits a wall.
    ball_left = ball[0] - 5
    ball_right = ball[0] + 5
    ball_top = ball[1] - 5
    ball_bottom = ball[1] + 5

    if ball_left <= 0 or ball_right >= 400:
        ball_dx *= -1
    if ball_top <= 0:
        ball_dy = 6
    elif ball_bottom >= 400:
        msg = font.render('You Lose!', True, (255, 255, 255))
        msg_rect = msg.get_rect()
        msg_rect.center = (200, 200)
        screen.blit(msg, msg_rect)
        pygame.display.update()
        break

    # Checks if the paddle intersected the ball.
    if isectRectCircle(paddle, ball, 10):
        ball_dy = -6

        # If player moved the paddle left to right, moves the ball right.
        if paddle.centerx - paddle_prevx > 0:
            ball_dx = 6
        # If player moved the paddle right to left, moves the ball left.
        elif paddle.centerx - paddle_prevx < 0:
            ball_dx = -6
        else:
            ball_dx = 0

        
    # Check if the ball has hit any blocks in the group blocks.
    # If it has, remove that block, reverse the direction of the ball,
    # and decrease the block count.

    for row in BLOCKS:
        block = row[0]
        if isectRectCircle(block, ball, 10):
            BLOCKS.remove(row)
            ball_dy *= -1
            BLOCK_COUNT -= 1

    
            
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            paddle_prevx = paddle.centerx
            paddle.centerx = pos[0]
            

    clock.tick(FPS)
    pygame.display.update()

    