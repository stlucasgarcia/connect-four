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
        background_image=None,
        chip_1=None,
        chip_2=None,
        volume=None,
    ) -> None:
        self.config = Settings()

        self.screen: pg.Surface = screen
        self.background_image: pg.Surface = self.config.bg_image
        self.chip_1: pg.Surface = self.config.chip_1
        self.chip_2: pg.Surface = self.config.chip_2
        self.is_controller = is_controller
        # self.soundtrack = pg.mixer.music.load("data/soundtracks/classic.mp3")
        self.sound_chip_1 = self.config.sound_chip_1
        self.sound_chip_2 = self.config.sound_chip_2
        # self.sound_chip_2 = pg.mixer.Sound("data/sounds/classic/chip_2.mp3")
        self.volume = self.config.volume

    def main_screen(self):
        utilities = UtilitiesMain()

        attr = {
            "res": self.config.size,
            "style": self.config.style,
            "label": self.config.op_label,
            "resume": self.config.op_resume,
            "st_menu": self.config.op_start_menu,
            "quit": self.config.op_quit,
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
        pg.mixer.music.set_volume(
            self.volume
        )  # 0.25 for classic, 0.35 for halloween, 0.30 for old west, 0.35 for vaporwave, 0.10 for christmas
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

                            if utilities.is_available(matrix, column):
                                self.sound_chip_1.play()
                                row = utilities.get_open_row(matrix, column)

                                utilities.drop_piece(matrix, row, column, 1)

                                if utilities.is_victory(matrix, 1):
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

                            if utilities.is_available(matrix, column):
                                self.sound_chip_2.play()

                                row = utilities.get_open_row(matrix, column)

                                utilities.drop_piece(matrix, row, column, 2)

                                if utilities.is_victory(matrix, 2):
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

                    if utilities.location_X(
                        pg.mouse.get_pos()[0]
                    ) != 0 and utilities.is_available(matrix, column):
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
