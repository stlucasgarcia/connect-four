import pygame as pg
import sys

from winner_screen import EndingScreen
from utilities import UtilitiesMain

# from controller import Controller
from settings import Settings
from menu import OptionsMenu


class MainScreen:
    def __init__(
        self,
        screen,
        is_controller,
    ) -> None:
        self.config = Settings()

        self.screen: pg.Surface = screen
        self.background_image: pg.Surface = self.config.bg_image
        self.is_controller = is_controller
        self.sound_chip_1 = self.config.sound_chip_1
        self.sound_chip_2 = self.config.sound_chip_2
        self.volume = self.config.volume
        self.chip_1 = self.config.chip_1

    def main_screen(self):
        utilities = UtilitiesMain()

        attr = {
            "res": self.config.size,
            "style": self.config.style,
            "label": self.config.op_label,
            "resume": self.config.op_resume,
            "st_menu": self.config.op_start_menu,
            "quit": self.config.op_quit,
            "theme": self.config.theme,
        }
        menu = OptionsMenu(**attr)

        clock = pg.time.Clock()

        matrix = utilities.create_matrix()

        turn: int = 0

        chip: pg.Surface = self.chip_1

        close_loop: bool = False

        x, y = 0, 0

        # try:
        #     joystick_count = pg.joystick.get_count()

        pg.mixer.music.play(loops=-1)
        pg.mixer.music.set_volume(self.volume)
        while not close_loop:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    close_loop = True
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

                            is_pos_available = utilities.is_available(matrix, column)

                            if is_pos_available:
                                self.sound_chip_1.play()

                                row = utilities.get_open_row(matrix, column)

                                try:
                                    turn, chip = utilities.is_valid(
                                        column + 1, is_pos_available, turn
                                    )
                                except TypeError:
                                    pass

                                utilities.drop_piece(matrix, row, column, 1)

                                if utilities.is_victory(matrix, 1) or utilities.is_tie(
                                    matrix
                                ):
                                    utilities.draw_board(matrix, self.screen)
                                    # pg.mixer.music.fadeout(5000)

                                    data = {"Guilherme": 10, "Leonardo": 5}

                                    ending = EndingScreen(
                                        self.screen,
                                        data,
                                        res=self.config.size,
                                        pg_res=self.config.win_pg,
                                        sm_res=self.config.win_sm,
                                        quit_res=self.config.win_quit,
                                    )

                                    close_loop = True

                                    ending.scores()

                    else:
                        # Player 2 input
                        column = utilities.location_X(pg.mouse.get_pos()[0])

                        if column != 0:
                            column -= 1

                            is_pos_available = utilities.is_available(matrix, column)

                            if utilities.is_available(matrix, column):
                                self.sound_chip_2.play()

                                row = utilities.get_open_row(matrix, column)

                                try:
                                    turn, chip = utilities.is_valid(
                                        column + 1, is_pos_available, turn
                                    )
                                except TypeError:
                                    pass

                                utilities.drop_piece(matrix, row, column, 2)

                                if utilities.is_victory(matrix, 2) or utilities.is_tie(
                                    matrix
                                ):
                                    utilities.draw_board(matrix, self.screen)

                                    # pg.mixer.music.fadeout(5000)

                                    data = {"Guilherme": 10, "Leonardo": 5}

                                    ending = EndingScreen(
                                        self.screen,
                                        data,
                                        res=self.config.size,
                                        pg_res=self.config.win_pg,
                                        sm_res=self.config.win_sm,
                                        quit_res=self.config.win_quit,
                                    )
                                    close_loop = True
                                    ending.scores()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        menu.run(self.screen, clock)

            pg.display.update()

            clock.tick(60)
