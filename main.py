import sys
import pygame
import numpy as np
import math
from init_screen import init_screen

ROW_AMOUNT: int = 6
COLUMN_AMOUNT: int = 7

BLUE: tuple = (0, 0, 255)
BLACK: tuple = (0, 0, 0)
RED: tuple = (255, 0, 0)
YELLOW: tuple = (255, 255, 0)


def create_board() -> list:
    board = np.zeros((ROW_AMOUNT, COLUMN_AMOUNT))
    return board


def drop_piece(board: list, row: int, column: int, piece: int):
    board[row][column] = piece


def is_valid_location(board: list, column: int) -> bool:
    return board[ROW_AMOUNT - 1][column] == 0


def get_next_open_row(board: list, column: int) -> list:
    for row in range(ROW_AMOUNT):
        if board[row][column] == 0:
            return row


def print_board(board: list):
    print(np.flip(board, 0))


def winning_move(board: list, piece: int) -> bool:

    # Check horizontal
    for column in range(COLUMN_AMOUNT - 3):
        for row in range(ROW_AMOUNT):
            if (
                board[row][column] == piece
                and board[row][column + 1] == piece
                and board[row][column + 2] == piece
                and board[row][column + 3] == piece
            ):
                return True

    # Check Vertical
    for column in range(COLUMN_AMOUNT):
        for row in range(ROW_AMOUNT - 3):
            if (
                board[row][column] == piece
                and board[row + 1][column] == piece
                and board[row + 2][column] == piece
                and board[row + 3][column] == piece
            ):
                return True

    # Main diagonal
    for column in range(COLUMN_AMOUNT - 3):
        for row in range(ROW_AMOUNT - 3):
            if (
                board[row][column] == piece
                and board[row + 1][column + 1] == piece
                and board[row + 2][column + 2] == piece
                and board[row + 3][column + 3] == piece
            ):
                return True

    # MainC diagonal
    for column in range(COLUMN_AMOUNT - 3):
        for row in range(3, ROW_AMOUNT):
            if (
                board[row][column] == piece
                and board[row - 1][column + 1] == piece
                and board[row - 2][column + 2] == piece
                and board[row - 3][column + 3] == piece
            ):
                return True


def draw_board(board: list):
    for column in range(COLUMN_AMOUNT):
        for row in range(ROW_AMOUNT):
            pygame.draw.rect(
                screen,
                BLUE,
                (
                    column * SQUARE_SIZE,
                    row * SQUARE_SIZE + SQUARE_SIZE,
                    SQUARE_SIZE,
                    SQUARE_SIZE,
                ),
            )
            pygame.draw.circle(
                screen,
                BLACK,
                (
                    int(column * SQUARE_SIZE + SQUARE_SIZE / 2),
                    int(row * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2),
                ),
                RADIUS,
            )

        for column in range(COLUMN_AMOUNT):
            for row in range(ROW_AMOUNT):
                if board[row][column] == 1:
                    pygame.draw.circle(
                        screen,
                        RED,
                        (
                            int(column * SQUARE_SIZE + SQUARE_SIZE / 2),
                            height - int(row * SQUARE_SIZE + SQUARE_SIZE / 2),
                        ),
                        RADIUS,
                    )

                elif board[row][column] == 2:
                    pygame.draw.circle(
                        screen,
                        YELLOW,
                        (
                            int(column * SQUARE_SIZE + SQUARE_SIZE / 2),
                            height - int(row * SQUARE_SIZE + SQUARE_SIZE / 2),
                        ),
                        RADIUS,
                    )
    pygame.display.update()


board = create_board()
close_game: bool = False
turn: int = 0
SQUARE_SIZE: int = 100

width = 1920
height = 1080

size: tuple = (width, height)

RADIUS: int = int(SQUARE_SIZE / 2 - 5)

pygame.init()

myFont = pygame.font.SysFont("monospace", 75)

screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
draw_board(board)
pygame.display.update()
# Put image
# background_image = pygame.image.load("images/background/game_screen.png")
# screen.blit(background_image, (0, 0))
# pygame.display.flip()

while not close_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        starterscreen = True
        while starterscreen:
            starterscreen = init_screen(screen=screen).starter_screen()
            if not starterscreen:
                break

        if event.type == pygame.MOUSEMOTION:
            pygame.display.update()

            pygame.mouse.set_visible(0)

            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))

            posx = event.pos[0]

            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARE_SIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE / 2)), RADIUS)

            pygame.display.update()

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARE_SIZE))
            
            if turn == 0:
                # Ask player 1 input
                posx = event.pos[0]
                column = int(math.floor(posx / SQUARE_SIZE))

                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 1)
                    if winning_move(board, 1):
                        label = myFont.render("Player 1 Wins!", 1, RED)
                        screen.blit(label, (40, 10))
                        close_game = True

            else:
                # Ask player 2 input
                posx = event.pos[0]
                column = int(math.floor(posx / SQUARE_SIZE))

                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 2)

                    if winning_move(board, 2):
                        label = myFont.render("Player 2 Wins!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        close_game = True

            turn += 1
            turn %= 2

            draw_board(board)

            if close_game:
                pygame.time.wait(3000)
