import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3


BG_COLOR = (28, 170, 160)
LINE_COLOR = (23, 145, 135)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)
# main looop

# BOARD
board = np.zeros((BOARD_ROWS, BOARD_COLS))
# print(board)

# mark the square
def mark_square(row, col, player):
    board[row][col] = player


"""mark_square(0, 0, 2)
mark_square(1, 2, 1)
print(board)"""

# check the square is available
def available_square(row, col):
    return board[row][col] == 0


# check all the square are full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


# false
print(is_board_full())
# marking all squares
for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
        mark_square(row, col, 1)
# board is full --True
print(is_board_full())

# DRAW # LINE
def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


draw_lines()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
