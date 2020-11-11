import pygame as pg
import os

from itertools import cycle


class initScreen:
    def __init__(self, screen) -> None:
        self.screen = screen

    def starter_screen(self):
        background = pg.image.load("data\images\starter\starterclassic.png")

        FONT = pg.font.Font(f"{os.getcwd()}\data\\fonts\classic.ttf", 125)

        intro = True
        while intro == True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    intro = False

            self.screen.blit(background, (0, 0))

            pg.display.update()

            text = FONT.render("Press any key to start", True, (0, 0, 0))

            self.screen.blit(text, [580, 800])

            pg.display.update()
