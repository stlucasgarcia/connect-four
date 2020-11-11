from sys import exit
import pygame as pg
import pygame_gui

from typing import Any


class OptionsMenu:
    def __init__(self, **attr):
        self.res = attr["res"]
        self.manager: Any
        self.label: Any
        self.resume: Any
        self.starter_menu: Any
        self.quit: Any

        self.style: str = attr["style"]
        self.label_res = attr["label"]
        self.resume_res = attr["resume"]
        self.starter_res = attr["st_menu"]
        self.quit_res = attr["quit"]

        pg.init()
        pg.display.set_mode(self.res, pg.FULLSCREEN)
        self.img = pg.image.load("pb.png")
        self.img.set_alpha(100)

        self._setup()

    def _setup(self):
        self.manager = pygame_gui.UIManager(self.res, self.style)

        self.label = pygame_gui.elements.UILabel(
            relative_rect=pg.Rect(*self.label_res),
            text="Menu",
            manager=self.manager,
            object_id="#Menu",
        )

        self.resume = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect(*self.resume_res),
            text="Resume",
            manager=self.manager,
            object_id="#Options",
        )

        self.starter_menu = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect(*self.starter_res),
            text="Starter Menu",
            manager=self.manager,
            object_id="#Options",
        )

        self.quit = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect(*self.quit_res),
            text="Quit",
            manager=self.manager,
            object_id="#Options",
        )

    def run(self, screen, clock):
        options = True

        while options:
            for event in pg.event.get():
                self.manager.process_events(event)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        options = False

                if self.resume.check_pressed():
                    options = False

                if self.starter_menu.check_pressed():
                    pass

                if self.quit.check_pressed():
                    exit()

            time_delta = clock.tick(60) / 1000.0

            screen.blit(self.img, (0, 0))
            # pg.display.flip()

            self.manager.update(time_delta)
            self.manager.draw_ui(screen)

            pg.display.update()
