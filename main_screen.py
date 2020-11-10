import sys
import pygame as pg
import numpy as np
import math


ROW_AMOUNT: int = 6
COLUMN_AMOUNT: int = 7


def create_matrix() -> list:
    matrix = np.zeros((ROW_AMOUNT, COLUMN_AMOUNT))
    return matrix


def drop_piece(matrix: list, row: int, column: int, piece: int) -> None:
    matrix[row][column] = piece


def is_available(matrix: list, column: int) -> bool:
    return matrix[ROW_AMOUNT - 1][column] == 0


def location_X(matrix: list, click_loc: int) -> None:
    # First location (X)
    if click_loc > 357 and click_loc < 551:
        print("Loc 1")
        return 1
    elif click_loc > 551 and click_loc < 714:
        print("loc 2")
        return 2
    elif click_loc > 714 and click_loc < 879:
        print("loc 3")
        return 3
    elif click_loc > 879 and click_loc < 1038:
        print("loc 4")
        return 4
    elif click_loc > 1038 and click_loc < 1203:
        print("loc 5")
        return 5
    elif click_loc > 1203 and click_loc < 1362:
        print("loc 6")
        return 6
    elif click_loc > 1362 and click_loc < 1423:
        print("loc 7")
        return 7
    else:
        return 0


# [[1, 2, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0]]


def draw_board(matrix: list, screen) -> None:
    screen.blit(background_image, (0, 0))

    for column in range(COLUMN_AMOUNT):
        for row in range(ROW_AMOUNT):
            if matrix[row][column] == 1:
                X_CONST = 140
                Y_CONST = 128.5

                x = 403 + ((X_CONST * column) + (23 * (column)))  # CERTO

                y = 924 - (Y_CONST * (row) + (17 * (row)))

                screen.blit(
                    chip_1,
                    (x, y),
                )
                # python -u "c:\Users\lukep\Documents\Projects\Connect Four\Connect-Four\main_screen.py"
            elif matrix[row][column] == 2:
                X_CONST = 140
                Y_CONST = 128.5

                x = 403 + ((X_CONST * column) + (23 * (column)))  # CERTO

                y = 924 - (Y_CONST * (row) + (17 * (row)))

                screen.blit(
                    chip_2,
                    (x, y),
                )


def get_next_open_row(matrix: list, column: int) -> int:
    for row in range(ROW_AMOUNT):
        if matrix[row][column] == 0:
            return row


def is_victory(matrix: list, chip: int) -> bool:
    # Check horizontal
    for column in range(COLUMN_AMOUNT - 3):
        for row in range(ROW_AMOUNT):
            if (
                matrix[row][column] == chip
                and matrix[row][column + 1] == chip
                and matrix[row][column + 2] == chip
                and matrix[row][column + 3] == chip
            ):
                return True

    # Check Vertical
    for column in range(COLUMN_AMOUNT):
        for row in range(ROW_AMOUNT - 3):
            if (
                matrix[row][column] == chip
                and matrix[row + 1][column] == chip
                and matrix[row + 2][column] == chip
                and matrix[row + 3][column] == chip
            ):
                return True

    # Main diagonal
    for column in range(COLUMN_AMOUNT - 3):
        for row in range(ROW_AMOUNT - 3):
            if (
                matrix[row][column] == chip
                and matrix[row + 1][column + 1] == chip
                and matrix[row + 2][column + 2] == chip
                and matrix[row + 3][column + 3] == chip
            ):
                return True

    # MainC diagonal
    for column in range(COLUMN_AMOUNT - 3):
        for row in range(3, ROW_AMOUNT):
            if (
                matrix[row][column] == chip
                and matrix[row - 1][column + 1] == chip
                and matrix[row - 2][column + 2] == chip
                and matrix[row - 3][column + 3] == chip
            ):
                return True


background_image = pg.image.load("images/game_screens/halloween/game_screen.png")

chip_1 = pg.image.load("images/game_screens/halloween/chip_1.png")

chip_2 = pg.image.load("images/game_screens/halloween/chip_2.png")

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

pg.mouse.set_visible(1)

pg.display.set_caption("Connect Four")

while not close_game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            close_game = True
            sys.exit()

        if event.type == pg.MOUSEMOTION:
            x = event.pos[0]
            y = event.pos[1]

        draw_board(matrix, screen)
        screen.blit(chip, (x, y))
        pg.display.update()

        if event.type == pg.MOUSEBUTTONDOWN:
            print(pg.mouse.get_pos())
            if turn == 0:
                # Ask player 1 input
                column = location_X(None, pg.mouse.get_pos()[0])
                if column != 0:
                    column -= 1
                    if is_available(matrix, column):
                        row = get_next_open_row(matrix, column)
                        drop_piece(matrix, row, column, 1)

            else:
                # Ask player 2 input
                column = location_X(None, pg.mouse.get_pos()[0])

                if column != 0:
                    column -= 1
                    if is_available(matrix, column):
                        row = get_next_open_row(matrix, column)
                        drop_piece(matrix, row, column, 2)

            turn += 1
            turn %= 2

            # draw_board(matrix, screen)
            pg.display.flip()

            if turn == 0:
                chip = chip_1
            else:
                chip = chip_2
