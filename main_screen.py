import sys
from numpy.matrixlib.defmatrix import matrix
import pygame as pg
import numpy as np
import math


ROW_AMOUNT: int = 6
COLUMN_AMOUNT: int = 7


def create_matrix() -> list:
    matrix = np.zeros((ROW_AMOUNT, COLUMN_AMOUNT))
    return matrix


def drop_piece(board: list, row: int, column: int, piece: int):
    board[row][column] = piece


background_image = pg.image.load(
    "images/game_screens/halloween/game_screen_Halloween.png"
)

piece1 = pg.image.load("images/game_screens/halloween/piece_2.png")

piece2 = pg.image.load("images/game_screens/halloween/piece_1.png")

pg.init()

width: int = 1920
height: int = 1080

size: tuple = (width, height)

screen = pg.display.set_mode((size), pg.FULLSCREEN)

screen.blit(background_image, (0, 0))

close_game: bool = False
clock = pg.time.Clock()

turn: int = 0
x = 963
y = 63

screen.blit(piece1, (x, y))
pg.mouse.set_pos(963, 63)
pg.mouse.set_visible(0)

pg.display.set_caption("Connect 4")

while not close_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            close_game = True
            sys.exit()

        if event.type == pg.MOUSEMOTION:
            x = pg.mouse.get_pos()[0]
            y = pg.mouse.get_pos()[1]

        screen.blit(background_image, (0, 0))
        screen.blit(piece1, (x, y))
        pg.display.flip()
        clock.tick(60)

        if event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())

            # if turn == 0:
            #     # Ask player 1 input
            #     posx = event.pos[0]
            #     column = int(math.floor(posx / SQUARE_SIZE))

            #     if is_valid_location(matrix, column):
            #         row = get_next_open_row(matrix, column)
            #         drop_piece(matrix, row, column, 1)
            #         if winning_move(matrix, 1):
            #             label = myFont.render("Player 1 Wins!", 1, RED)
            #             screen.blit(label, (40, 10))
            #             close_game = True

            # else:
            #     # Ask player 2 input
            #     posx = event.pos[0]
            #     column = int(math.floor(posx / SQUARE_SIZE))

            #     if is_valid_location(board, column):
            #         row = get_next_open_row(board, column)
            #         drop_piece(board, row, column, 2)

            #         if winning_move(board, 2):
            #             label = myFont.render("Player 2 Wins!", 1, YELLOW)
            #             screen.blit(label, (40, 10))
            #             close_game = True

            # turn += 1
            # turn %= 2
