import sys
import pygame as pg

from utilities import UtilitiesMain
from settings import Settings
from menu import OptionsMenu


class MainScreen:
    def __init__(self, screen, background_image=None, chip_1=None, chip_2=None) -> None:
        self.screen: pg.Surface = screen
        self.background_image: pg.Surface = pg.image.load(
            "data/images/game_screens/vaporwave/game_screen.png"
        )
        self.chip_1: pg.Surface = pg.image.load(
            "data/images/game_screens/vaporwave/chip_1.png"
        )
        self.chip_2: pg.Surface = pg.image.load(
            "data/images/game_screens/vaporwave/chip_2.png"
        )

    def main_screen(self):
        utilities = UtilitiesMain()
        config = Settings()

        attr = {
            "res": config.size,
            "style": config.style,
            "label": config.op_label,
            "resume": config.op_resume,
            "st_menu": config.op_start_menu,
            "quit": config.op_quit,
        }
        menu = OptionsMenu(**attr)

        clock = pg.time.Clock()

        matrix = utilities.create_matrix()

        turn: int = 0

        chip: pg.Surface = self.chip_1

        close_game: bool = False

        x, y = 0, 0

        # try:
        #     joystick_count = pg.joystick.get_count()

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

                if event.type == pg.MOUSEBUTTONDOWN:
                    if turn == 0:
                        # Player 1 input
                        column = utilities.location_X(pg.mouse.get_pos()[0])

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
                        column = utilities.location_X(pg.mouse.get_pos()[0])

                        if column != 0:
                            column -= 1

                            if utilities.is_available(matrix, column):
                                row = utilities.get_open_row(matrix, column)

                                utilities.drop_piece(matrix, row, column, 2)

                                if utilities.is_victory(matrix, 2):
                                    # Insert winning_screen here

                                    print("Won")
                                    sys.exit()

                    if utilities.location_X(pg.mouse.get_pos()[0]) != 0:
                        turn += 1

                        turn %= 2

                        if turn == 0:
                            chip = self.chip_1
                        else:
                            chip = self.chip_2

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        menu.run(self.screen, clock)

            pg.display.update()

            clock.tick(60)
