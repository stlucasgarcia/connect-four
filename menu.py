import pygame_gui
import pygame as pg
from json import dump

from sys import exit
from typing import Any, Tuple


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
        self.img = pg.image.load(
            f"data\images\\background\\{attr['theme']}\esc_image.png"
        )
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
            pg.mouse.set_visible(True)
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

            pg.mouse.set_visible(False)

            pg.display.update()


class StarterMenu:
    def __init__(self, **attr):
        self.res: Tuple[int, int] = attr["res"]
        (
            self.sm_title,
            self.sm_mode_txt,
            self.sm_mode,
            self.sm_theme_text,
            self.sm_theme,
            self.sm_res_text,
            self.sm_res,
            self.sm_next,
            self.sm_quit,
        ) = attr["sm_res"]

        self.style: str = "data/styles/select_menu.json"
        self.screen = attr["screen"]
        self.window = "select"
        self.plrs = (False, False)
        self.name1: str = "AI"
        self.name2: str = "AI"

        pg.init()
        pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        self._create_first_UI()

    def _create_first_UI(self):
        self.manager = pygame_gui.UIManager(self.res, self.style)

        self.title = pygame_gui.elements.UILabel(
            pg.Rect(self.sm_title),
            text="Select Menu",
            manager=self.manager,
            object_id="#Title",
        )

        self.mode_text = pygame_gui.elements.UILabel(
            pg.Rect(self.sm_mode_txt),
            text="Mode",
            manager=self.manager,
            object_id="#Text",
        )

        self.mode = pygame_gui.elements.UIDropDownMenu(
            ["Player vs AI", "Player vs Player", "AI vs AI"],
            "",
            pg.Rect(*self.sm_mode),
            manager=self.manager,
            object_id="#Mode",
        )

        self.theme_text = pygame_gui.elements.UILabel(
            pg.Rect(self.sm_theme_text),
            text="Theme",
            manager=self.manager,
            object_id="#Text",
        )

        self.theme_selector = pygame_gui.elements.UIDropDownMenu(
            ["Classic", "Halloween", "Old_West", "VaporWave", "Christmas"],
            "",
            pg.Rect(*self.sm_theme),
            manager=self.manager,
            object_id="#Mode",
        )

        self.res_text = pygame_gui.elements.UILabel(
            pg.Rect(self.sm_res_text),
            text="Resolution",
            manager=self.manager,
            object_id="#Text",
        )

        self.res_selector = pygame_gui.elements.UIDropDownMenu(
            ["1280x720 - HD", "1920x1080 - FULLHD"],
            "",
            pg.Rect(*self.sm_res),
            manager=self.manager,
            object_id="#Mode",
        )

        self.next = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect(*self.sm_next),
            text="Continue",
            manager=self.manager,
            object_id="#Quit",
        )

        self.quit = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect(*self.sm_quit),
            text="Quit",
            manager=self.manager,
            object_id="#Quit",
        )

    def _ver(self):
        if self.plrs == (True, True):
            self.p1 = pygame_gui.elements.UITextEntryLine(
                pg.Rect((430, 460), (250, 150)),
                self.manager,
                object_id="#PlayerName",
            )

            self.p2 = pygame_gui.elements.UITextEntryLine(
                pg.Rect((1260, 460), (250, 150)),
                self.manager,
                object_id="#PlayerName",
            )

        elif self.plrs == (True, False):
            self.p1 = pygame_gui.elements.UITextEntryLine(
                pg.Rect((845, 460), (250, 150)),
                self.manager,
                object_id="#PlayerName",
            )

        self.next.disable()

    def run(self):
        selected = True
        data: dict = {}
        self.next.disable()

        while selected:
            pg.mouse.set_visible(True)
            time_delta = self.clock.tick(60) / 1000.0

            for event in pg.event.get():
                self.manager.process_events(event)

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        selected = False

                if self.window == "select":
                    if (
                        self.mode.selected_option
                        and self.theme_selector.selected_option
                        and self.res_selector.selected_option
                    ):
                        self.next.enable()

                    if self.next.check_pressed():

                        data = {
                            "resolution": self.res_selector.selected_option.split()[-1],
                            "theme": self.theme_selector.selected_option.lower(),
                        }

                        if self.mode.selected_option == "Player vs AI":
                            self.mode_text.kill()
                            self.res_text.kill()
                            self.theme_text.set_text("Name")
                            self.theme_text.set_dimensions((220, 300))
                            self.plrs = (True, False)

                        elif self.mode.selected_option == "Player vs Player":
                            self.theme_text.kill()
                            self.mode_text.set_text("Player 1")
                            self.res_text.set_text("Player 2")
                            self.plrs = (True, True)

                        else:
                            selected = False

                        self.mode.kill()
                        self.res_selector.kill()
                        self.theme_selector.kill()

                        self._ver()
                        self.window = "player"

                else:
                    if self.next.check_pressed():
                        selected = False

                    if self.plrs == (True, True):
                        if self.p1.get_text() and self.p2.get_text():
                            self.name1 = self.p1.get_text()
                            self.name2 = self.p2.get_text()
                            self.next.enable()

                    elif self.plrs == (True, False):
                        if self.p1.get_text():
                            self.name1 = self.p1.get_text()
                            self.next.enable()

                if self.quit.check_pressed():
                    exit()

            self.screen.fill((255, 255, 255))

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)

            pg.mouse.set_visible(False)

            pg.display.update()

        StarterMenu._export(data)
        return self.name1, self.name2

    @staticmethod
    def _export(data: dict):
        with open("user_settings.json", "w") as user:
            dump(data, user, indent=4)


# pg.init()
# screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
#
# from settings import Settings
#
# st = Settings()
#
# StarterMenu(
#     res=st.size,
#     sm_res=[
#         st.sm_title,
#         st.sm_mode_txt,
#         st.sm_mode,
#         st.sm_theme_text,
#         st.sm_theme,
#         st.sm_res_text,
#         st.sm_res,
#         st.sm_next,
#         st.sm_quit,
#     ],
#     screen=screen,
# ).run()
