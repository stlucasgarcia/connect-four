import pygame as pg
import sys
import time

from itertools import cycle
from utils import Path, Settings, sep

class InitScreen:
    """Starter loop which emulates a gif"""

    def __init__(self, screen) -> None:
        self.config = Settings()
        self.screen = screen
        self.resources_images = Path.images() + "starter" + sep

        self.bg_classic = pg.image.load(
            f"{self.resources_images}classic{sep}starter_screen{Path.IMAGE_SUFFIX}"
        )
        self.bg_halloween = pg.image.load(
            f"{self.resources_images}halloween{sep}starter_screen{Path.IMAGE_SUFFIX}"
        )
        self.bg_vaporwave = pg.image.load(
            f"{self.resources_images}vaporwave{sep}starter_screen{Path.IMAGE_SUFFIX}"
        )
        self.bg_christmas = pg.image.load(
            f"{self.resources_images}christmas{sep}starter_screen{Path.IMAGE_SUFFIX}"
        )
        self.bg_old_west = pg.image.load(
            f"{self.resources_images}old_west{sep}starter_screen{Path.IMAGE_SUFFIX}"
        )
        self.size = self.config.size

        if self.size == (1280, 720):
            self.bg_classic = pg.transform.scale(self.bg_classic, (1280, 720))
            self.bg_halloween = pg.transform.scale(self.bg_halloween, (1280, 720))
            self.bg_vaporwave = pg.transform.scale(self.bg_vaporwave, (1280, 720))
            self.bg_christmas = pg.transform.scale(self.bg_christmas, (1280, 720))
            self.bg_old_west = pg.transform.scale(self.bg_old_west, (1280, 720))

    def starter_screen(self):
        """Starter screen loop"""

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

        startGame = True
        while startGame == True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        sys.exit()

                    startGame = False
                    return

            self.screen.blit(next(backgrounds), (0, 0))

            pg.display.update()

            time.sleep(1.5)

            Clock.tick(60)
