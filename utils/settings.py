import os
import json
import pygame as pg

from typing import Tuple, Any
from os import sep

T = Tuple[int, int, int, int]
S = Tuple[Tuple[int, int], Tuple[int, int]]


class Settings:
    """Class created to organize the different options and variables"""

    def __init__(self):
        kwargs = json.load(open("user_settings.json", "r"))
        self.res = "_full_hd" if kwargs["resolution"] == "FULLHD" else "_hd"
        self.theme = kwargs["theme"]
        self.option = kwargs["mode"]
        self.resources = "resources" + sep
        self.resources_images = self.resources + f"images{sep}"
        self.resources_sounds = self.resources + f"sounds{sep}"
        self.resources_soundtracks = self.resources + f"soundtracks{sep}"

        self.height: int
        self.width: int
        self.size: Tuple[int, int]
        self.font: Any
        self.style: str = f"resources{sep}styles{sep}"
        self.volume: float

        self.sm_title = T
        self.sm_mode_txt = T
        self.sm_mode = S
        self.sm_theme_text = T
        self.sm_theme = S
        self.sm_res_text = T
        self.sm_res = S
        self.sm_next = S
        self.sm_quit = S

        self.op_label = T
        self.op_resume = S
        self.op_start_menu = S
        self.op_quit = S

        pg.mixer.init(44100, -16, 2, 64)

        getattr(self, self.res)()
        self._config_theme()
        self._config_font()
        self._config_sound()
        self._config_start_menu()

    def _full_hd(self) -> None:
        """Full hd settings and pixels locations which are used around the code"""

        self.width = 1920
        self.height = 1080
        self.size = (1920, 1080)
        self.win_pg = ((530, 700), (200, 80))
        self.win_sm = ((835, 700), (250, 80))
        self.win_quit = ((1185, 700), (150, 80))
        self.win_ld = ((835, 900), (250, 80))
        self.lb_back = ((885, 985), (150, 70))
        self.lb_player = [550, 65, 400, 200]
        self.lb_score = [975, 65, 400, 200]
        self.lb_mult = 94.8
        self.fullhd = True

    def _hd(self) -> None:
        """Hd settings and pixels locations which are used around the code"""

        self.width = 1280
        self.height = 720
        self.size = (1280, 720)
        self.win_pg = ((230, 550), (200, 80))
        self.win_sm = ((515, 550), (250, 80))
        self.win_quit = ((850, 550), (150, 80))
        self.win_ld = ((515, 640), (250, 80))
        self.lb_back = ((565, 645), (150, 70))
        self.lb_player = [300, 8.55, 400, 200]
        self.lb_score = [590, 8.55, 400, 200]
        self.lb_mult = 63.35
        self.fullhd = False

    def _config_font(self) -> None:
        """Gets the respective theme's font"""

        if self.theme == "classic":
            self.font = pg.font.Font(f"{os.getcwd()}{sep}resources{sep}fonts{sep}classic.ttf", 75)
            self.style += "options_menu_classic.json"
            self.volume = 0.25

            self.op_label = (
                (840, 260, 250, 160) if self.fullhd else (520, 100, 250, 160)
            )
            self.op_resume = (
                ((880, 440), (160, 80)) if self.fullhd else ((560, 280), (160, 80))
            )
            self.op_start_menu = (
                ((830, 540), (260, 80)) if self.fullhd else ((510, 380), (260, 80))
            )
            self.op_quit = (
                ((910, 640), (100, 80)) if self.fullhd else ((590, 480), (100, 80))
            )

        elif self.theme == "halloween":
            self.font = pg.font.Font(
                f"{os.getcwd()}{sep}resources{sep}fonts{sep}halloween.otf", 75
            )
            self.style += "options_menu_halloween.json"
            self.volume = 0.35

            self.op_label = (
                (840, 260, 270, 160) if self.fullhd else (500, 100, 280, 160)
            )
            self.op_resume = (
                ((880, 440), (160, 80)) if self.fullhd else ((560, 280), (160, 80))
            )
            self.op_start_menu = (
                ((830, 540), (260, 80)) if self.fullhd else ((510, 380), (260, 80))
            )
            self.op_quit = (
                ((910, 640), (100, 80)) if self.fullhd else ((590, 480), (100, 80))
            )

        elif self.theme == "old_west":
            self.font = pg.font.Font(
                f"{os.getcwd()}{sep}resources{sep}fonts{sep}old_west.otf", 75
            )
            self.style += "options_menu_old_west.json"
            self.volume = 0.30

            self.op_label = (
                (820, 260, 270, 160) if self.fullhd else (515, 100, 250, 160)
            )
            self.op_resume = (
                ((880, 440), (160, 80)) if self.fullhd else ((560, 280), (160, 80))
            )
            self.op_start_menu = (
                ((830, 540), (260, 80)) if self.fullhd else ((510, 380), (260, 80))
            )
            self.op_quit = (
                ((910, 640), (100, 80)) if self.fullhd else ((590, 480), (100, 80))
            )

        elif self.theme == "vaporwave":
            self.font = pg.font.Font(
                f"{os.getcwd()}{sep}resources{sep}fonts{sep}vaporwave.otf", 75
            )
            self.style += "options_menu_vaporwave.json"
            self.volume = 0.35

            self.op_label = (
                (840, 260, 290, 160) if self.fullhd else (500, 100, 290, 160)
            )
            self.op_resume = (
                ((880, 440), (170, 80)) if self.fullhd else ((550, 280), (180, 80))
            )
            self.op_start_menu = (
                ((830, 540), (270, 80)) if self.fullhd else ((500, 380), (290, 80))
            )
            self.op_quit = (
                ((910, 640), (110, 80)) if self.fullhd else ((590, 480), (100, 80))
            )

        elif self.theme == "christmas":
            self.font = pg.font.Font(
                f"{os.getcwd()}{sep}resources{sep}fonts{sep}christmas.ttf", 75
            )
            self.style += "options_menu_christmas.json"
            self.volume = 0.10

            self.op_label = (740, 220, 470, 210) if self.fullhd else (445, 60, 400, 210)
            self.op_resume = (
                ((880, 440), (180, 80)) if self.fullhd else ((555, 280), (180, 80))
            )
            self.op_start_menu = (
                ((810, 540), (320, 80)) if self.fullhd else ((495, 380), (300, 80))
            )
            self.op_quit = (
                ((910, 640), (110, 80)) if self.fullhd else ((585, 480), (110, 80))
            )

    def _config_theme(self) -> None:
        """Gets the respective theme's images, like the board and each chips, it also resizes them for HD"""

        self.bg_image = pg.image.load(
            f"{self.resources_images}game_screens{sep}{self.theme}{sep}game_screen.png"
        )
        self.chip_1 = pg.image.load(
            f"{self.resources_images}game_screens{sep}{self.theme}{sep}chip_1.png"
        )
        self.chip_2 = pg.image.load(
            f"{self.resources_images}game_screens{sep}{self.theme}{sep}chip_2.png"
        )

        if self.size == (1280, 720):
            self.bg_image = pg.transform.scale(self.bg_image, (1280, 720))
            self.chip_1 = pg.transform.scale(self.chip_1, (86, 86))
            self.chip_2 = pg.transform.scale(self.chip_2, (86, 86))

    def _config_sound(self) -> None:
        """Gets the respective theme's sounds for the chips and background song"""

        pg.mixer.music.load(f"{self.resources_soundtracks}{self.theme}.mp3")
        self.sound_chip_1 = pg.mixer.Sound(
            f"{self.resources_sounds}{self.theme}{sep}chip_1.mp3"
        )
        self.sound_chip_2 = pg.mixer.Sound(
            f"{self.resources_sounds}{self.theme}{sep}chip_2.mp3"
        )

    def _config_start_menu(self):
        """Configures the start{sep}select menu for both resolutions"""

        self.sm_title = (660, 20, 600, 300) if self.fullhd else (340, 40, 600, 150)
        self.sm_mode_txt = (460, 260, 200, 300) if self.fullhd else (140, 150, 200, 300)
        self.sm_mode = (
            ((470, 460), (200, 40)) if self.fullhd else ((150, 350), (200, 40))
        )
        self.sm_theme_text = (
            (860, 260, 200, 300) if self.fullhd else (540, 150, 200, 300)
        )
        self.sm_theme = (
            ((870, 460), (200, 40)) if self.fullhd else ((550, 350), (200, 40))
        )
        self.sm_res_text = (
            (1260, 260, 250, 300) if self.fullhd else (940, 150, 250, 300)
        )
        self.sm_res = (
            ((1240, 460), (290, 40)) if self.fullhd else ((930, 350), (290, 40))
        )
        self.sm_next = (
            ((875, 600), (170, 70)) if self.fullhd else ((555, 500), (170, 70))
        )
        self.sm_quit = (
            ((885, 850), (150, 70)) if self.fullhd else ((565, 630), (150, 70))
        )

        self.sm_p1 = (
            ((430, 460), (250, 150)) if self.fullhd else ((110, 350), (250, 150))
        )
        self.sm_p2 = (
            ((1260, 460), (250, 150)) if self.fullhd else ((940, 350), (250, 150))
        )
        self.sm_p1_1 = (
            ((845, 460), (250, 150)) if self.fullhd else ((515, 350), (250, 150))
        )
