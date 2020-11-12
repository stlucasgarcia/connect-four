import pygame as pg
import os
import time

from itertools import cycle
from settings import Settings


class InitScreen:
    def __init__(self, screen) -> None:
        self.config = Settings()
        self.screen = screen
        self.bg_classic = pg.image.load(
            "data\images\starter\classic\starter_screen.png"
        )
        self.bg_halloween = pg.image.load(
            "data\images\starter\halloween\starter_screen.png"
        )
        self.bg_vaporwave = pg.image.load(
            "data\images\starter\\vaporwave\starter_screen.png"
        )
        self.bg_christmas = pg.image.load(
            "data\images\starter\christmas\starter_screen.png"
        )
        self.bg_old_west = pg.image.load(
            "data\images\starter\old_west\starter_screen.png"
        )
        self.size = self.config.size

        if self.size == (1280, 720):
            self.bg_classic = pg.transform.scale(self.bg_classic, (1280, 720))
            self.bg_halloween = pg.transform.scale(self.bg_halloween, (1280, 720))
            self.bg_vaporwave = pg.transform.scale(self.bg_vaporwave, (1280, 720))
            self.bg_christmas = pg.transform.scale(self.bg_christmas, (1280, 720))
            self.bg_old_west = pg.transform.scale(self.bg_old_west, (1280, 720))

    def starter_screen(self):
        Clock = pg.time.Clock()

        backgrounds = cycle(
            [
                self.bg_classic,
                self.bg_halloween,
                self.bg_vaporwave,
                self.bg_old_west,
                self.bg_christmas,
            ]
        )

        intro = True
        while intro == True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    intro = False
                    return

            self.screen.blit(next(backgrounds), (0, 0))

            pg.display.update()

            time.sleep(1)

            Clock.tick(60)
