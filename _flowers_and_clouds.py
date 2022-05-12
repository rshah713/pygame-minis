import pygame

def draw_cloud(screen, x, y, color):
    print(color)
    "draw cloud centered at (x, y)"
    pygame.draw.ellipse(screen, color, (x-50, y-45//2, 100, 45))
    pygame.draw.circle(screen, color, (x+40, y-10), 20)
    pygame.draw.circle(screen, color, (x+10, y-20), 20)
    pygame.draw.circle(screen, color, (x-15, y-20), 20)
    pygame.draw.circle(screen, color, (x-30, y), 20)


def draw_flower(screen, x, y):
    "draw a flower centered at (x, y-10)"
    pygame.draw.ellipse(screen, (255, 20, 147), (x-5, (y-10) - 10, 10, 20))
    pygame.draw.circle(screen, (255, 255, 0), (x, y-10), 2)