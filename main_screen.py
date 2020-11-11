import sys
import pygame as pg

from utilities import UtilitiesMain


class MainScreen:
    def __init__(self, screen, background_image=None, chip_1=None, chip_2=None) -> None:
        self.screen: pg.Surface = screen
        self.background_image: pg.Surface = pg.image.load(
            "data/images/game_screens/classic/game_screen.png"
        )
        self.chip_1: pg.Surface = pg.image.load(
            "data/images/game_screens/classic/chip_1.png"
        )
        self.chip_2: pg.Surface = pg.image.load(
            "data/images/game_screens/classic/chip_2.png"
        )

    def main_screen(self) -> list:
        utilities: object = UtilitiesMain()

        matrix: list = utilities.create_matrix()

        turn: int = 0

        chip: pg.Surface = self.chip_1

        close_game: bool = False

        x, y = 0, 0

        while not close_game:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    close_game = True
                    sys.exit()

                if event.type == pg.MOUSEMOTION:
                    x = event.pos[0]

                    y = event.pos[1]

                utilities.draw_board(matrix, self.screen)

                self.screen.blit(chip, (x, y))

                pg.display.update()

                if event.type == pg.MOUSEBUTTONDOWN:
                    print(pg.mouse.get_pos())
                    if turn == 0:
                        # Player 1 input
                        column = utilities.location_X(None, pg.mouse.get_pos()[0])

                        if column != 0:
                            column -= 1

                            if utilities.is_available(matrix, column):
                                row = utilities.get_open_row(matrix, column)

                                utilities.drop_piece(matrix, row, column, 1)

                                if utilities.is_victory(matrix, 1):
                                    # Insert winning_screen here

                                    print("Won")
                                    sys.exit()

                    else:
                        # Player 2 input
                        column = utilities.location_X(None, pg.mouse.get_pos()[0])

                        if column != 0:
                            column -= 1

                            if utilities.is_available(matrix, column):
                                row = utilities.get_open_row(matrix, column)

                                utilities.drop_piece(matrix, row, column, 2)

                                if utilities.is_victory(matrix, 2):
                                    # Insert winning_screen here

                                    print("Won")
                                    sys.exit()

                    pg.display.update()

                    if utilities.location_X(None, pg.mouse.get_pos()[0]) != 0:
                        turn += 1

                        turn %= 2

                        if turn == 0:
                            chip = self.chip_1

                        else:
                            chip = self.chip_2
