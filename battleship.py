"""
Rohan Shah
battleship vs computer
"""
import random
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 400), 0, 32)
pygame.display.set_caption('battleship')
font = pygame.font.Font('freesansbold.ttf', 25)
inst_fnt = pygame.font.Font('freesansbold.ttf', 17)
win_fnt = pygame.font.Font('freesansbold.ttf', 30)

GAME_STATE = 'setup'

pygame.draw.polygon(screen, (60, 179, 113), ((0, 80), (50, 50), (150, 50), (200, 80), (250, 50), (350, 50), (400, 80), (400, 320), (350, 350), (250, 350), (200, 320), (150, 350), (50, 350),( 0, 320)))

pygame.draw.polygon(screen, (50, 205, 50), ((0, 80), (50, 50), (150, 50), (200, 80), (250, 50), (350, 50), (400, 80), (400, 320), (350, 350), (250, 350), (200, 320), (150, 350), (50, 350),( 0, 320)), 6)

message_text = font.render('PLAYER', True, (0,0,0))
message_rect = message_text.get_rect()
message_rect.center = (100, 330)
screen.blit(message_text, message_rect)

message_text = font.render('ENEMY', True, (0,0,0))
message_rect = message_text.get_rect()
message_rect.center = (300, 330)
screen.blit(message_text, message_rect)

message_text = inst_fnt.render('Click to place four ships of size 2', True, (0,0,0))
message_rect = message_text.get_rect()
message_rect.center = (200, 94)
screen.blit(message_text, message_rect)

def make_board(startX, startY):
    rows = 8
    cols = 8
    gridSize = 24
    board = [[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
    for row in range(rows):
        for col in range(cols):
            #### START OF BLOCK MAKE_BOARD ####
            # Draw a rectangular cell for this row and column.
            x0 = startX + col * gridSize
            y0 = startY + row * gridSize
            # {rect pos, status, row, col}
            cell = [pygame.Rect(x0, y0, gridSize, gridSize), 'ocean', row, col]

            #### END OF BLOCK ####

            # Sets the cell properties and add it to the board.
            board[row][col] = cell

    for row in board:
        for item in row:

            pygame.draw.rect(screen, (0, 0, 205), item[0])
            pygame.draw.rect(screen, (255, 255, 255), item[0], 1)
    print(board)
    return board

            
PLAYER_BOARD = make_board(3, 110)
ENEMY_BOARD = make_board(205, 110)
SHIPS_PLACED = 0
LAST_CLICKED = None

def find_cell(x, y, board):
    # Find the cell that the point (x, y) lies in.
     for row in range(8):
        for col in range(8):
            cell = board[row][col]
            cell_rect = cell[0]
            if (cell_rect.collidepoint(x, y)):
                return cell

def is_adjacent(cell, cellClicked):
    global LAST_CLICKED
    # cellclicked -- the entire board item
    # check if 2 cells r adjacent
    clickedRow = cellClicked[2]
    clickedCol = cellClicked[3]
    cellRow = cell[2]
    cellCol = cell[3]

    # If either the rows are equal and the columns are within 1, or
    # the columns are equal and the rows are within 1, they are adjacent.

    return (((cellRow == clickedRow) and (abs(cellCol - clickedCol) == 1)) or ((cellCol == clickedCol) and (abs(cellRow - clickedRow) == 1)))


def is_legal_ship(cell, board, numParts):
    # If the location is not an ocean, it is not legal.
    global LAST_CLICKED
    if cell == None or cell[1] != 'ocean':
        return False

    if numParts % 2 == 0: # every ship has length 2 (new ship = legal)
        LAST_CLICKED = cell
        return True
    else:
        # we placed first part, make sure second is next to it
        if is_adjacent(cell, LAST_CLICKED):
            return True
        return False

def place_player(mouseX, mouseY):
    # Place a player ship in the cell if it will be a legal move.
    global SHIPS_PLACED
    cell = find_cell(mouseX, mouseY, PLAYER_BOARD)
    # Place a player ship in the cell if it will be a legal move.
    if is_legal_ship(cell, PLAYER_BOARD, SHIPS_PLACED):
        cell[1] = 'hiddenShip'
        SHIPS_PLACED += 1

        pygame.draw.rect(screen, (128, 128, 128), cell[0])


def place_enemies():
    # Randomly places enemy ships until there are 4 ships of size 2 on the board.
    global ENEMY_BOARD
    num_ships = 0
    while num_ships < 8:
        rand_row = random.randint(0, 7)
        rand_col = random.randint(0, 7)
        random_cell = ENEMY_BOARD[rand_row][rand_col]
        if is_legal_ship(random_cell, ENEMY_BOARD, num_ships):
            random_cell[1] = 'hiddenShip'
            num_ships += 1
            
def play_turn(mouseX, mouseY):
    # On each turn, see if the cell clicked was valid.
    global GAME_STATE
    # fire at enemy
    cell = find_cell(mouseX, mouseY, ENEMY_BOARD)
    if sink_or_miss(cell):
        enemy_turn()

    # check if game ends
    if check_win(ENEMY_BOARD):
        pygame.draw.rect(screen, (0, 128, 0), (0, 160, 400, 90))
        msg = win_fnt.render('YOU WON!', True, (255, 255, 255))
        msg_rect = msg.get_rect()
        msg_rect.center = (200, 200)
        screen.blit(msg, msg_rect)
        GAME_STATE = 'over'
        return True
        
def enemy_turn():
    global PLAYER_BOARD, GAME_STATE
    # On an enemy turn, randomly pick a new cell to attack.

    new_spot = False
    while not new_spot:
        # Pick a random cell by choosing a row and column.
        randomRow = random.randint(0, 7)
        randomCol = random.randint(0, 7)
        randomCell = PLAYER_BOARD[randomRow][randomCol]

        # If the cell has not been attacked yet, end the loop.
        if ((randomCell[1] == 'ocean') or
            (randomCell[1] == 'hiddenShip')):
            new_spot = True

    # Checks if the attacked cell is a ship then check if the game ends.
    sink_or_miss(randomCell)
    if check_win(PLAYER_BOARD):
        # draw game lost screen
        pygame.draw.rect(screen, (255, 0, 0), (0, 160, 400, 90))
        msg = win_fnt.render('YOU LOST!', True, (255, 255,255))
        msg_rect = msg.get_rect()
        msg_rect.center = (200, 200)
        screen.blit(msg, msg_rect)
        GAME_STATE = 'over'
    
def sink_or_miss(cell):
    print('sink or miss')
    if cell is not None:
        # if cell has no ship, draw ripple
        if cell[1] == 'ocean':
            cell[1] = 'missed'
            draw_ripple(cell)
            return True
        elif cell[1] == 'hiddenShip':
            cell[1] = 'hit'
            draw_hit(cell)
            return True

        return False
        


def draw_ripple(cell):
    radiusList = [ 11, 7, 3 ]

    for radius in radiusList:
        pygame.draw.circle(screen, (0, 255, 255), (cell[0].center[0], cell[0].center[1]), radius)
        pygame.draw.circle(screen, (0, 0, 255), (cell[0].center[0], cell[0].center[1]), radius, 1)

def draw_hit(cell):
    pygame.draw.circle(screen, (255, 0, 0), cell[0].center, 6)

def check_win(opp_board):
    # If any cell still has a hidden ship, return False.
    for row in range(8):
        for col in range(8):
            cell = opp_board[row][col]
            if cell[1] == 'hiddenShip':
                return False
    return True

    
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            # If on the start screen, place ship parts until the player has
            # 4 ships. Then creates 4 enemy ships.
            if GAME_STATE == 'setup':
                pos = pygame.mouse.get_pos()
                place_player(*pos)
                
                if SHIPS_PLACED == 8:
                    pygame.draw.rect(screen, (60, 179, 113), message_rect)
                
                    msg = inst_fnt.render('Guess the location of the enemy ships',True, (0,0,0) )
                    screen.blit(msg, message_rect)
                    place_enemies()
                
                    GAME_STATE = 'play'
            elif GAME_STATE == 'play':
                pos = pygame.mouse.get_pos()
                play_turn(*pos)
            

    pygame.display.update()