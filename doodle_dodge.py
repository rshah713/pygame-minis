import pygame
from pygame.locals import *
import random



"""
Objects fall randomly
use left/right key to avoid them
player turns red when you crash
"""

FPS = 30
OBSTACLES = []

class Doodle(object):
    def __init__(self):
        self.key_inputs = {
            K_LEFT: -10,
            K_RIGHT: 10
        }
        self.fill = (0, 0, 0)
        self.draw()

    def handle_key_input(self, key):
        # Get the input from the key and attempt to move the doodle using it.
        dx = self.key_inputs.get(key)
        if dx is None:
            return
        was_moved = self.attempt_move(dx)

    def attempt_move(self, dx):
        # Make sure moving the ship keeps it on the canvas

        newX = self.drawing.centerx + dx
        if newX < 0 or newX > 400:
            return False

        self.move(dx)
        return True
    
    def move(self, dx):
        self.drawing.centerx += dx

    def draw(self):
        self.drawing = pygame.Rect(183, 305, 35, 70)

    def get_rect(self):
        return self.drawing

    def get_fill(self):
        return self.fill

    def _check_collision(self):
        
        # Check if the ship hits any of the obstacles
        for center in OBSTACLES:
            if self._isectRectCircle(center, 10):
                self.fill = (255, 0, 0)
                

    def _isectRectCircle(self,circle_cpt, circle_rad):

        rect = self.drawing
        if rect.collidepoint(*circle_cpt):
            return True
    
        centerPt = pygame.math.Vector2(*circle_cpt)
        cornerPts = [rect.bottomleft, rect.bottomright, rect.topleft, rect.topright]
        if [p for p in cornerPts if pygame.math.Vector2(*p).distance_to(centerPt) <= circle_rad]:
            return True
    
        return False


pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('doodle dodge')
CLOCK = pygame.time.Clock()
screen.fill((255, 255, 255))

doodle = Doodle()

cnt = 0
while True:
    cnt += 1
    CLOCK.tick(FPS)
    screen.fill((255, 255, 255))
    
        
    
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        doodle.handle_key_input(K_LEFT)
        # pygame.time.wait(100000*100)
    elif keys[K_RIGHT]:
        doodle.handle_key_input(K_RIGHT)


    for center in OBSTACLES:
        center[1] += 3
        if center[1] > 400:
            OBSTACLES.remove(center)

    if cnt % 15 == 0:
        randX = random.randint(0, 400)
        randY = random.randint(-100, 0)
        OBSTACLES.append([randX, randY])


    for center in OBSTACLES:
        pygame.draw.circle(screen, (0, 0, 0), center, 10)

    doodle._check_collision()

    pygame.draw.rect(screen, doodle.get_fill(), doodle.get_rect())

    if doodle.get_fill() == (255, 0, 0):
        pygame.display.update()
        pygame.time.wait(100000*100)
        

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.display.update()
