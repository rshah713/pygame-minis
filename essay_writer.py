import pygame
from pygame.locals import *
from _dashes import draw_dashed_line

print("DIRECTIONS")
print("type on ur keyboard to write the essay")

pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption("essay writer")
font = pygame.font.Font('freesansbold.ttf', 20)

essay = 40
pageNumber = 1

while True:
    screen.fill((25, 25, 112))

    pygame.draw.rect(screen, (255, 255, 255), (50, 10, 300, 380))

    draw_dashed_line(screen, (0,0,0), (200, 20), (200, essay), width=250)

    message_text = font.render(str(pageNumber), True, (0,0,0))
    message_rect = message_text.get_rect()
    message_rect.center = (335, 375)
    screen.blit(message_text, message_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            essay += 20
            if essay > 380:
                essay = 40
                pageNumber += 1

    pygame.display.update()
