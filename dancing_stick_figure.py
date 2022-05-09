import pygame
from pygame.locals import *

print("""
      DIRECTIONS:
      PRESS LEFT ARROW AND RIGHT ARROW TO DANCE
      """)

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('dancing stick figure')

left_arm_y2 = 175
right_arm_y2 = 175

def toggleLeftArm():
    global left_arm_y2
    # Move the left arm down if it is currently up, and up if it is currently down.
    if (left_arm_y2 == 125):
        left_arm_y2 = 175
    else:
        left_arm_y2 = 125

def toggleRightArm():
    global right_arm_y2
    # Move the right arm down if it is currently up, and up if it is currently down.
    if (right_arm_y2 == 125):
        right_arm_y2 = 175
    else:
        right_arm_y2 = 125


while True:

    screen.fill((173, 216, 230))
    
    # face and body
    pygame.draw.circle(screen, (0, 0, 0), (200, 135), 25)
    pygame.draw.line(screen, (0, 0, 0), (200, 160), (200, 240))

    # upper arms
    pygame.draw.line(screen, (0, 0, 0), (200, 185), (150, left_arm_y2))
    pygame.draw.line(screen, (0, 0, 0), (200, 185), (250, right_arm_y2))

    # legs
    pygame.draw.line(screen, (0, 0, 0), (200, 240), (230, 300))
    pygame.draw.line(screen, (0, 0, 0), (200, 240), (170, 300))

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                toggleLeftArm()
            elif event.key == K_RIGHT:
                toggleRightArm()

    pygame.display.update()

