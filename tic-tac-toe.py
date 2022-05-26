"""
Rohan Shah
GUI Tic-Tac-Toe
"""
import random
import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('REAL TIC TAC TOES')

font = pygame.font.Font('freesansbold.ttf', 90)
player_font = pygame.font.Font('freesansbold.ttf', 15)
gm_over_fnt = pygame.font.Font('freesansbold.ttf', 20)
new_game_fnt = pygame.font.Font('freesansbold.ttf', 30)
win_fnt = pygame.font.Font('freesansbold.ttf', 50)

ROWS = 3
COLS = 3
BOARD_GUI = []
APP_BOARD = [[None, None, None], [None, None, None], [None, None, None]]
APP_BOARD_VALUES = [['', '', ''], ['', '', ''], ['', '', '']]
player = ''
isGamePlaying = False
new_game = True # visibility for new game screen
first_time = False

CURR_PLAYER_FONT = player_font.render('Current Player: ', True, (255, 255, 255))
CURR_PLAYER_FONT_rect = CURR_PLAYER_FONT.get_rect()
CURR_PLAYER_FONT_rect.center = (190, 20)

CURR_PLAYER = player_font.render(player, True, (255, 255, 255))
CURR_PLAYER_rect = CURR_PLAYER.get_rect()
CURR_PLAYER_rect.center = (250, 20)

def initGame():
    cellSize = 400 / ROWS
    for row in range(ROWS):
        for col in range(COLS):
            # calculate x and y to add to gui
            x = col * cellSize
            y = row * cellSize
            BOARD_GUI.append(pygame.Rect(x, y, cellSize, cellSize))

            # Calculate the center of each cell and add a label there.
            # we can then edit label when they make a move
            cx = x + cellSize / 2
            cy = y + cellSize / 2
            message_text = font.render(APP_BOARD_VALUES[row][col], True, (255,255,255))
            message_rect = message_text.get_rect()
            message_rect.center = (cx, cy)
            APP_BOARD[row][col] = {message_text: message_rect}
            # might need to save label/rect into board-gui??
            
            

    for rect in BOARD_GUI:
        pygame.draw.rect(screen, (135, 206, 235), rect)
        pygame.draw.rect(screen, (224, 255, 255), rect, 5)

    for row in APP_BOARD:
        for item in row:
            label, rect = list(item.keys())[0], list(item.values())[0]
            screen.blit(label, rect)

            
    global player
    player = 'O'

def update_labels():
    global APP_BOARD
    """any changes to app_board_values updates the label value and blits"""

    print(APP_BOARD)
    print("\n\n")
    for row in range(ROWS):
        for col in range(COLS):
            # only change label keep same rect positioning
            message_text = font.render(APP_BOARD_VALUES[row][col], True, (70, 130, 180) if APP_BOARD_VALUES[row][col] == 'O' else (255, 255, 255))
            rect = list(APP_BOARD[row][col].values())[0]
            new_rect = message_text.get_rect()
            new_rect.center = rect.center
            APP_BOARD[row][col] = {message_text:new_rect}
            
            
    print(APP_BOARD)
    for row in APP_BOARD:
        for item in row:
            label, rect = list(item.keys())[0], list(item.values())[0]
            screen.blit(label, rect)
            

def is_valid_move(row, col):
    return APP_BOARD_VALUES[row][col] == ''

def make_move(row, col):
    global APP_BOARD_VALUES
    APP_BOARD_VALUES[row][col] = player
    update_labels()


def find_cell(mouseX, mouseY):
    size = 400 / ROWS
    for row in range(ROWS):
        for col in range(COLS):
            x = col * size
            y = row * size

             # If the mouseX, mouseY is between the boundaries of a cell,
            # returns the coordinates of that cell.

            if (x <= mouseX and mouseX <= x + size) and (y <= mouseY and mouseY <= y + size):
                return [row, col]
                

def check_tie():
    for row in APP_BOARD_VALUES:
        if '' in row:
            return False
    return True

def check_win(row):
    count = 0
    for val in row:
        if val == player:
            count += 1

    return count == ROWS

def check_game_win():
    for row in APP_BOARD_VALUES:
        if check_win(row):
            return True

    for i in range(COLS):
        col = [APP_BOARD_VALUES[0][i], APP_BOARD_VALUES[1][i], APP_BOARD_VALUES[2][i]]
        if check_win(col):
            return True

    diagonalLeftToRight = [ APP_BOARD_VALUES[0][0], APP_BOARD_VALUES[1][1], APP_BOARD_VALUES[2][2] ]

    # Gets the top-right to bottom-left diagonal.
    diagonalRightToLeft = [ APP_BOARD_VALUES[0][2], APP_BOARD_VALUES[1][1], APP_BOARD_VALUES[2][0] ]


    return check_win(diagonalLeftToRight) or check_win(diagonalRightToLeft)
    

def display_gameover(win):
    # True means someone won
    # False means tie
    pygame.draw.rect(screen, (240, 248, 255), (0, 0, 400, 400))
    restart_label = gm_over_fnt.render('Press "r" to restart', True, (255, 140, 0))
    restart_rect = restart_label.get_rect()
    restart_rect.center = (200, 250)
    if win:
        win_label = win_fnt.render('Winner: ' + player + ' !', True, (255, 140, 0))
    else:
        win_label = win_fnt.render('Tie!', True, (255, 140, 0))

    win_rect = win_label.get_rect()
    win_rect.center = (200, 200)

    screen.blit(restart_label, restart_rect)
    screen.blit(win_label, win_rect)

initGame()   

while True:

    CURR_PLAYER = player_font.render(player, True, (255, 255, 255))

    pygame.draw.rect(screen, (255, 105, 180), (120, 5, 160, 30))
    screen.blit(CURR_PLAYER_FONT, CURR_PLAYER_FONT_rect)
    screen.blit(CURR_PLAYER, CURR_PLAYER_rect)

    if new_game:
        pygame.draw.rect(screen, (240, 248, 255), (0, 100, 400, 200))
        ng = new_game_fnt.render('Welcome to Tic-Tac-Toes', True, (255, 140, 0))
        ng_rect = ng.get_rect()
        ng_rect.center = (200, 190)
        screen.blit(ng, ng_rect)

        ng = player_font.render('press space to start a new game', True, (255, 140, 0))
        ng_rect = ng.get_rect()
        ng_rect.center = (200, 220)
        screen.blit(ng, ng_rect)

    if first_time:
        initGame()
        first_time = False

    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not isGamePlaying:
                    new_game = False
                    isGamePlaying = True
                    first_time = True

            if event.key == K_r:
                BOARD_GUI = []
                APP_BOARD = [[None, None, None], [None, None, None], [None, None, None]]
                APP_BOARD_VALUES = [['', '', ''], ['', '', ''], ['', '', '']]
                isGamePlaying = True
                first_time = True     
                
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(isGamePlaying)
            if isGamePlaying:
                row, col = find_cell(*pos)
                if is_valid_move(row, col):
                    make_move(row, col)
                    if check_tie():
                        display_gameover(False)
                        isGamePlaying = False
                    elif check_game_win():
                        display_gameover(True)
                        isGamePlaying = False
                        
                    player = 'X' if player == 'O' else 'O'
        
    pygame.display.update()