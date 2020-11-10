import sys
import pygame as pg
import numpy as np
import math


ROW_AMOUNT: int = 6
COLUMN_AMOUNT: int = 7


def create_matrix() -> list:
    matrix = np.zeros((ROW_AMOUNT, COLUMN_AMOUNT))
    return matrix


def drop_piece(matrix: list, row: int, column: int, piece: int):
    matrix[row][column] = piece


def is_available(matrix: list, column: int) -> bool:
    return matrix[ROW_AMOUNT - 1][column] == 0


def location_X(matrix: list, click_loc: int):
    # First location (X)
    if click_loc >= 355 and click_loc <= 535:
        print("Loc 1")
        return 1, x
    elif click_loc >= 535 and click_loc <= 705:
        print("loc 2")
        return 2, x
    elif click_loc >= 705 and click_loc <= 877:
        print("loc 3")
        return 3, x
    elif click_loc >= 877 and click_loc <= 1043:
        print("loc 4")
        return 4, x
    elif click_loc >= 1043 and click_loc <= 1210:
        print("loc 5")
        return 5, x
    elif click_loc >= 1210 and click_loc <= 1380:
        print("loc 6")
        return 6, x
    elif click_loc >= 1380 and click_loc <= 1556:
        print("loc 7")
        return 7, x


def draw_board(matrix: list, screen):
    screen.blit(background_image, (0, 0))

    for column in range(COLUMN_AMOUNT):
        for row in range(ROW_AMOUNT):
            if matrix[row][column] == 1:
                screen.blit(chip_1, (x, y))

            elif matrix[row][column] == 2:
                screen.blit(chip_2, (x, y))


background_image = pg.image.load("images/game_screens/vaporwave/game_screen.png")

chip_1 = pg.image.load("images/game_screens/vaporwave/chip_1.png")

chip_2 = pg.image.load("images/game_screens/vaporwave/chip_2.png")

pg.init()

width: int = 1920
height: int = 1080

size: tuple = (width, height)

screen = pg.display.set_mode((size), pg.FULLSCREEN)

screen.blit(background_image, (0, 0))

close_game: bool = False

clock = pg.time.Clock()

matrix = create_matrix()

turn: int = 0

ADD_CONSTANT: int = 147  # Starts at 194

x: int = 963
y: int = 63

chip = chip_1

screen.blit(chip, (x, y))

pg.mouse.set_pos(963, 63)

pg.mouse.set_visible(0)

pg.display.set_caption("Connect Four")

while not close_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            close_game = True
            sys.exit()

        if event.type == pg.MOUSEMOTION:
            x = event.pos[0]

            y = event.pos[1]

        pg.transform.scale(chip, (x, y))
        # screen.blit(chip, (x, y))
        pg.display.update()

        if event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())
            # if turn == 0:
            # Ask player 1 input
            location_X(None, pg.mouse.get_pos()[0])
            screen.blit(chip, (402, 194))  # 194 * Y
            # if is_available(matrix, column):
            #     row = get_next_open_row(matrix, column)
            #     drop_piece(matrix, row, column, 1)
            #     if winning_move(matrix, 1):
            #         label = myFont.render("Player 1 Wins!", 1, RED)
            #         screen.blit(label, (40, 10))
            #         close_game = True

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

            turn += 1
            turn %= 2

            pg.display.flip()

            if turn == 0:
                chip = chip_1
            else:
                chip = chip_2

            screen.blit(background_image, (0, 0))
