import pygame as pg
import sys

from pygame.image import save

from ending_screens import EndingScreen
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
        self.chip_2 = self.config.chip_2

    def main_screen(self, usernames: list):
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

        turn: int = 0

        chip = self.chip_2

        close_loop: bool = False

        x, y = 0, 0

        seconds, minutes = 0, 0

        player_turn = 1
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

                utilities.draw_board(matrix)

                self.screen.blit(chip, (x, y))

                if event.type == pg.MOUSEBUTTONDOWN:
                    save_chip = chip
                    print(x, y)
                    column = utilities.location_X(pg.mouse.get_pos()[0])
                    if column != 0:
                        play_again, player_turn, chip = utilities.playerTurn(
                            column,
                            matrix,
                            player_turn,
                            self.sound_chip_1,
                            self.sound_chip_2,
                            usernames,
                        )

                        print(play_again)
                        if play_again != None:
                            return play_again

                        if chip == None:
                            chip = save_chip

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        play_again = menu.run(self.screen, clock)
                        if not play_again:
                            return play_again

            # utilities.timer(self.screen, start_time, clock) #TODO FIX THIS

            pg.display.update()

            clock.tick(60)
