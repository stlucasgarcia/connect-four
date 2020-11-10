import os
import pygame as pg

from typing import Tuple, Any


class Settings:
    def __init__(
        self,
        scale: str = "FULLHD",
        theme: str = "classic",
    ):
        self.scale = "_full_hd" if scale == "FULLHD" else "_hd"
        self.theme = theme

        self.height: int
        self.width: int
        self.size: Tuple[int, int]
        self.font: Any
        self.style: str = "styles/"
        self.op_label = Tuple[int, int, int, int]
        self.op_resume = Tuple[Tuple[int, int], Tuple[int, int]]
        self.op_start_menu = Tuple[Tuple[int, int], Tuple[int, int]]
        self.op_quit = Tuple[Tuple[int, int], Tuple[int, int]]

        pg.init()

        getattr(self, self.scale)()
        self._config_theme()
        self._config_font()

    def _full_hd(self):
        self.width = 1920
        self.height = 1080
        self.size = (1920, 1080)
        self.op_label = (840, 260, 250, 160)
        self.op_resume = ((880, 440), (160, 80))
        self.op_start_menu = ((830, 540), (260, 80))
        self.op_quit = ((910, 640), (100, 80))

    def _hd(self):
        self.width = 1280
        self.height = 720
        self.size = (1280, 720)
        self.op_label = (520, 100, 250, 160)
        self.op_resume = ((560, 280), (160, 80))
        self.op_start_menu = ((510, 380), (260, 80))
        self.op_quit = ((590, 480), (100, 80))

    def _config_font(self):
        if self.theme == "classic":
            self.font = pg.font.Font(f"{os.getcwd()}\\fonts\JustMyType-KePl.ttf", 75)
            self.style += "options_menu_classic.json"
        elif self.theme == "halloween":
            self.font = pg.font.Font(f"{os.getcwd()}\\fonts\Halloween Night.otf", 75)
            self.style += "options_menu_halloween.json"
        elif self.theme == "old_west":
            self.font = pg.font.Font(f"{os.getcwd()}\\fonts\Western Bang Bang.otf", 75)
            self.style += "options_menu_old_west.json"
        elif self.theme == "vaporwave":
            self.font = pg.font.Font(f"{os.getcwd()}\\fonts\VaporfuturismCond.otf", 75)
            self.style += "options_menu_vaporwave.json"
        elif self.theme == "christmas":
            self.font = pg.font.Font(
                f"{os.getcwd()}\\fonts\Christmas Time Personal Use.ttf", 75
            )
            self.style += "options_menu_christmas.json"

    def _config_theme(self):
        self.bg_image = pg.image.load(
            f"images/game_screens/{self.theme}/game_screen.png"
        )

        self.chip_1 = pg.image.load(f"images/game_screens/{self.theme}/chip_1.png")

        self.chip_2 = pg.image.load(f"images/game_screens/{self.theme}/chip_2.png")
