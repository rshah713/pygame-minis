"""
Rohan Shah
Use arrow keys to move painter
Spacebar to place color
Use key (below) to change color
Press 's' to save drawing
Press 'o' to open existing drawing
"""

import pygame, time
from helper import blit_text
from pygame.locals import *

print("DIRECTIONS\n")
print("Use arrow keys to move around -> space bar to place pixel")
print("\nUse 's' to save drawing,'o' to open\n ")
print("""
      # Change the cursor's fill depending on key. Use the following matches.
    # 'r' -> 'red'
    # 'g' -> 'green'
    # 'b' -> 'blue'
    # 'k' -> 'black'
    # 'w' -> 'white'""")
pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('pixel art')
font = pygame.font.Font('freesansbold.ttf', 20)

cursor = pygame.Rect(20, 20, 20, 20)
pygame.draw.rect(screen, (255, 0, 0), cursor)


def move_cursor(key):
    if key == K_UP:
        return 0, -20
    elif key == K_DOWN:
        return 0, 20
    elif key == K_LEFT:
        return -20, 0
    elif key == K_RIGHT:
        return 20, 0
    return False

def change_color(key):
    global fill
    if key == K_r:
        fill = (255, 0, 0)
    elif key == K_g:
        fill = (0, 255, 0)
    elif key == K_b:
        fill = (0, 0, 255)
    elif key == K_k:
        fill = (0, 0, 0)
    elif key == K_w:
        fill = (255, 255, 255)

def save_seq():
    message_text = font.render("Saved Drawing!", True, (255,255,255))
    message_rect = message_text.get_rect()
    message_rect.center = (200, 200)

    pygame.draw.rect(screen, (0, 0, 0), (100, 150, 200, 100))
    screen.blit(message_text, message_rect)
    pygame.display.update()
    time.sleep(1)
    
def open_seq():
    SavedDrawings = open("saved_drawings.txt", "r")
    readlines = SavedDrawings.readlines()
    SavedDrawings.close()
    msg = ""
    for num in range(len(readlines)):
        msg += "Drawing " + str(num) + "\n"

    blit_text(screen, msg, (150, 150), font)
    pygame.display.update()
    num = input("\n\nENTER NUMBER CHOICE HERE: ")
    return int(num)
        
    
    
pos = (0, 0)
colors_and_pos = {}
fill = (255, 0, 0)
while True:
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), cursor, 1)
    pygame.draw.circle(screen, fill, (cursor.left+10, cursor.top+10), 2)
    for pos in colors_and_pos:
        pygame.draw.rect(screen, colors_and_pos[pos], (pos[0], pos[1], 20, 20))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_s:
                save_seq()
                with open("saved_drawings.txt", "a") as SavedDrawings:
                    SavedDrawings.write(str(colors_and_pos) + "\n")

            if event.key == K_o:
                open_draw_num = open_seq()
                SavedDrawings = open("saved_drawings.txt", "r")
                readlines = SavedDrawings.readlines()
                colors_and_pos = eval(readlines[open_draw_num].strip())
                SavedDrawings.close()
                
            pos = move_cursor(event.key)
            change_color(event.key)
            if pos != False:
                cursor.move_ip(pos)
                
            if event.key == K_SPACE:
                # if space -- save current color & pos to be redrawn
                colors_and_pos[(cursor.left, cursor.top)] = fill

    pygame.display.update()