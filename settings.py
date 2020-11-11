import pygame as pg
import json
import os

from typing import Tuple, Any


class Settings:
    def __init__(self):
        kwargs = json.load(open("user_settings.json", "r"))
        self.res = "_full_hd" if kwargs["resolution"] == "FULLHD" else "_hd"
        self.theme = kwargs["theme"]

        self.height: int
        self.width: int
        self.size: Tuple[int, int]
        self.font: Any
        self.style: str = "data/styles/"
        self.volume: float
        self.op_label = Tuple[int, int, int, int]
        self.op_resume = Tuple[Tuple[int, int], Tuple[int, int]]
        self.op_start_menu = Tuple[Tuple[int, int], Tuple[int, int]]
        self.op_quit = Tuple[Tuple[int, int], Tuple[int, int]]

        pg.init()

        getattr(self, self.res)()
        self._config_theme()
        self._config_font()
        self._config_sound()

    def _full_hd(self):
        self.width = 1920
        self.height = 1080
        self.size = (1920, 1080)
        self.win_pg = ((530, 700), (200, 80))
        self.win_sm = ((835, 700), (250, 80))
        self.win_quit = ((1185, 700), (150, 80))
        self.fullhd = True

    def _hd(self):
        self.width = 1280
        self.height = 720
        self.size = (1280, 720)
        self.win_pg = ((230, 550), (200, 80))
        self.win_sm = ((515, 550), (250, 80))
        self.win_quit = ((850, 550), (150, 80))
        self.fullhd = False

    def _config_font(self):
        if self.theme == "classic":
            self.font = pg.font.Font(f"{os.getcwd()}\data\\fonts\classic.ttf", 75)
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
            self.font = pg.font.Font(f"{os.getcwd()}\data\\fonts\halloween.otf", 75)
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
            self.font = pg.font.Font(f"{os.getcwd()}\data\\fonts\old_west.otf", 75)
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
            self.font = pg.font.Font(f"{os.getcwd()}\data\\fonts\\vaporwave.otf", 75)
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
            self.font = pg.font.Font(f"{os.getcwd()}\data\\fonts\christmas.ttf", 75)
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

    def _config_theme(self):
        self.bg_image = pg.image.load(
            f"data/images/game_screens/{self.theme}/game_screen.png"
        )
        self.chip_1 = pg.image.load(f"data/images/game_screens/{self.theme}/chip_1.png")
        self.chip_2 = pg.image.load(f"data/images/game_screens/{self.theme}/chip_2.png")

    def _config_sound(self):
        pg.mixer.music.load(f"data/soundtracks/{self.theme}.mp3")
        # self.sound_chip_1 = pg.mixer.Sound(f"data/sounds/{self.theme}/chip_1.mp3")
        # self.sound_chip_2 = pg.mixer.Sound(f"data/sounds/{self.theme}/chip_2.mp3")
