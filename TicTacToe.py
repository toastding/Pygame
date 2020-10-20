import pygame, sys

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15

BG_COLOR = (28, 170, 160)
LINE_COLOR = (23, 145, 135)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BG_COLOR)
# main looop


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
