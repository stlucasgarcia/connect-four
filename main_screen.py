import pygame as pg
import math
import sys

from ending_screens import EndingScreen
from utilities import UtilitiesMain

from controller import Controller
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
        self.chip_2 = self.config.chip_2
        self.ai_chip = 2

    def main_screen(self, usernames: list, option="AI"):
        control = Controller()
        utilities = UtilitiesMain(self.screen)

        start_time = pg.time.get_ticks()

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

        chip = self.chip_1

        close_loop: bool = False

        x, y = 950, 15

        seconds, minutes = 0, 0

        player_turn: int = 1  # if not option else option
        # try:
        #     joystick_count = pg.joystick.get_count()

        pg.mixer.music.play(loops=-1)
        pg.mixer.music.set_volume(self.volume)
        while not close_loop:
            start_time = utilities.draw_board(matrix, start_time, clock)
            self.screen.blit(chip, (x, y))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    close_loop = True
                    sys.exit()

                if self.is_controller:
                    if control.checkController():
                        x = control.x_hd
                        y = 8

                if event.type == pg.MOUSEMOTION:
                    x = event.pos[0]
                    y = event.pos[1]

                if event.type == pg.MOUSEBUTTONDOWN:
                    save_chip = chip

                    column = utilities.location_X(pg.mouse.get_pos()[0])
                    if column != 0:
                        play_again, player_turn, chip = utilities.playersTurn(
                            column,
                            matrix,
                            player_turn,
                            self.sound_chip_1,
                            self.sound_chip_2,
                            usernames,
                            start_time,
                            clock,
                            option,
                        )

                        if play_again != None:
                            return play_again

                        if chip == None:
                            chip = save_chip
                if self.is_controller:
                    if control.isControllerDropEvent(event):
                        save_chip = chip

                        column = utilities.location_X(control.get_x_pos(event))
                        if column != 0:
                            play_again, player_turn, chip = utilities.playersTurn(
                                column,
                                matrix,
                                player_turn,
                                self.sound_chip_1,
                                self.sound_chip_2,
                                usernames,
                                start_time,
                                clock,
                                option,
                            )

                            if play_again != None:
                                return play_again

                            if chip == None:
                                chip = save_chip

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        play_again = menu.run(self.screen, clock)
                        if not play_again:
                            return play_again

                if control.isControllerEvent(event):
                    screen = self.screen
                    control.check_event(event, menu, screen, clock)

            if option == "AI" and player_turn % 2 == 1:
                column, minimax_score = utilities.minimaxTree(
                    matrix, 5, -math.inf, math.inf, True
                )

                if utilities.is_available(matrix, column):
                    row = utilities.get_open_row(matrix, column)
                    utilities.drop_piece(matrix, row, column, self.ai_chip)

                    if utilities.is_victory(matrix, self.ai_chip):
                        utilities.draw_board(matrix, start_time, clock)

                        pg.time.wait(500)

                        data = {usernames[0]: 10, usernames[1]: 5}

                        ending = EndingScreen(
                            self.screen,
                            data,
                            res=self.config.size,
                            pg_res=self.config.win_pg,
                            sm_res=self.config.win_sm,
                            quit_res=self.config.win_quit,
                            lb_res=self.config.win_ld,
                        )

                        play_again = ending.scores()

                        return play_again

                    player_turn += 1
                    player_turn = player_turn % 2

            pg.display.update()

            clock.tick(75)
