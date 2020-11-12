import pygame as pg
import os

from itertools import cycle


class InitScreen:
    def __init__(self, screen) -> None:
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

    def starter_screen(self):
        background = pg.image.load("data\images\starter\classic\starter_screen.png")

        FONT = pg.font.Font(f"{os.getcwd()}\data\\fonts\classic.ttf", 125)

        Clock = pg.time.Clock()

        intro = True
        while intro == True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    intro = False

            self.screen.blit(background, (0, 0))

            text = FONT.render("Press any key to start", True, (0, 0, 0))

            self.screen.blit(text, [580, 800])

            pg.display.update()

            Clock.tick(60)
