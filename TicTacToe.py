import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# color
RED = (255, 0, 0)
BG_COLOR = (28, 170, 160)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (240, 240, 222)
CROSS_COLOR = (66, 66, 66)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)
# main looop

# BOARD
board = np.zeros((BOARD_ROWS, BOARD_COLS))
# print(board)

# draw X and O
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(
                    screen,
                    CIRCLE_COLOR,
                    (int(col * 200 + 100), int(row * 200 + 100)),
                    CIRCLE_RADIUS,
                    CIRCLE_WIDTH,
                )
            elif board[row][col] == 2:
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * 200 + SPACE, row * 200 + 200 - SPACE),
                    (col * 200 + 200 - SPACE, row * 200 + SPACE),
                    CROSS_WIDTH,
                )
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * 200 + SPACE, row * 200 + SPACE),
                    (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE),
                    CROSS_WIDTH,
                )


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
# print(is_board_full())
# marking all squares
"""
for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
        mark_square(row, col, 1)
"""

# board is full --True
# print(is_board_full())

# DRAW # LINE
def draw_lines():
    # 1 horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # 2 horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # 1 vertical line
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # 2 vertical line
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


draw_lines()

player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # checking which screen we click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]  # x
            mouseY = event.pos[1]  # y

            """print(mouseX)
            print(mouseY)"""

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            """print(clicked_row)
            print(clicked_col)"""

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    player = 1

                draw_figures()
                print(board)

    pygame.display.update()
