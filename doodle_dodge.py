import pygame
from pygame.locals import *

FPS = 30

class Doodle(object):
    def __init__(self):
        self.key_inputs = {
            K_LEFT: -10,
            K_RIGHT: 10
        }
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


pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('doodle dodge')
CLOCK = pygame.time.Clock()
screen.fill((255, 255, 255))

doodle = Doodle()


while True:
    CLOCK.tick(FPS)
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), doodle.get_rect())
    
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        doodle.handle_key_input(K_LEFT)
    elif keys[K_RIGHT]:
        doodle.handle_key_input(K_RIGHT)
        

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.display.update()