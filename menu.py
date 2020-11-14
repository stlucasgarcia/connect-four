import pygame_gui
import pygame as pg

from sys import exit
from json import dump
from typing import Any, Tuple

from controller import Controller


class OptionsMenu:
    """ Creates a menu when esc is pressed during the game, it has 3 options, resume, starter menu and quit"""

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
        control = Controller()
        options = True

        while options:
            pg.mouse.set_visible(True)
            for event in pg.event.get():
                self.manager.process_events(event)

                if control.isControllerEscEvent(event):
                    options = False
                    return True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        options = False
                        return True

                if self.resume.check_pressed():
                    options = False
                    return True

                if self.starter_menu.check_pressed():
                    return False

                if self.quit.check_pressed():
                    exit()

            time_delta = clock.tick(60) / 1000.0

            screen.blit(self.img, (0, 0))

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
            self.sm_p1,
            self.sm_p2,
            self.sm_p1_1,
        ) = attr["sm_res"]
        self.data: dict = {}
        self.selected = True

        self.style: str = "data/styles/select_menu.json"
        self.screen = attr["screen"]
        self.window = "select"
        self.plrs = (False, False)
        self.name1: str = "AI"
        self.name2: str = "AI"

        self.last_mode: str = ""
        self.last_theme: str = ""
        self.last_res: str = ""

        self.clock = pg.time.Clock()
        self._read_json()
        self._create_first_UI()

    def _read_json(self):
        with open("user_settings.json", "r") as user:
            data = user.readlines()

            if self.res == (1920, 1080):
                prep = "1920x1080 - "
            else:
                prep = "1280x720 - "

            self.last_mode = data[1].split('"')[-2]
            self.last_theme = data[2].split('"')[-2].capitalize()
            self.last_res = prep + data[3].split('"')[-2]

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
            self.last_mode,
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
            self.last_theme,
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
            self.last_res,
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
                pg.Rect(*self.sm_p1),
                self.manager,
                object_id="#PlayerName",
            )

            self.p2 = pygame_gui.elements.UITextEntryLine(
                pg.Rect(*self.sm_p2),
                self.manager,
                object_id="#PlayerName",
            )

        elif self.plrs == (True, False):
            self.p1 = pygame_gui.elements.UITextEntryLine(
                pg.Rect(*self.sm_p1_1),
                self.manager,
                object_id="#PlayerName",
            )

        self.next.disable()

    def _check_next(self, enter):
        if self.window == "select" and (self.next.check_pressed() or enter):
            self.data = {
                "mode": self.mode.selected_option,
                "theme": self.theme_selector.selected_option.lower(),
                "resolution": self.res_selector.selected_option.split()[-1],
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
                self.selected = False

            self.mode.kill()
            self.res_selector.kill()
            self.theme_selector.kill()

            self._ver()
            self.window = "player"

        elif self.window == "player" and (self.next.check_pressed() or enter):
            self.selected = False

            if self.plrs == (True, True):
                if self.p1.get_text() and self.p2.get_text():
                    self.name1 = self.p1.get_text()
                    self.name2 = self.p2.get_text()

            elif self.plrs == (True, False):
                if self.p1.get_text():
                    self.name1 = self.p1.get_text()

        elif self.window == "player":
            if self.p1.get_text() and self.plrs == (True, False):
                self.next.enable()

            elif (self.p1.get_text() and self.p2.get_text()) and self.plrs == (
                True,
                True,
            ):
                self.next.enable()
                self.next.enable()

            else:
                self.next.disable()

    def run(self):
        pg.mixer.music.stop()
        snd = pg.mixer.Sound("data/soundtracks/select_menu.mp3")
        pg.mixer.Sound.play(snd, -1)
        pg.mixer.Sound.set_volume(snd, 0.35)

        self.next.disable()

        img = pg.image.load("data/images/menu/select_menu.png")

        if self.res == (1280, 720):
            img = pg.transform.scale(img, self.res)

        while self.selected:
            enter = False
            pg.mouse.set_visible(True)
            time_delta = self.clock.tick(60) / 1000.0

            for event in pg.event.get():
                self.manager.process_events(event)

                if (
                    self.mode.selected_option
                    and self.theme_selector.selected_option
                    and self.res_selector.selected_option
                ):
                    self.next.enable()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        enter = True

                self._check_next(enter)

                if self.quit.check_pressed():
                    exit()

            self.manager.update(time_delta)
            self.screen.blit(img, (0, 0))
            self.manager.draw_ui(self.screen)

            pg.mouse.set_visible(False)

            pg.display.update()

        pg.mixer.Sound.stop(snd)

        change_res = StarterMenu._export(self.data)
        return self.name1, self.name2, change_res

    @staticmethod
    def _export(data: dict):
        change_res = False

        res = open("user_settings.json", "r+").readlines()
        if res:
            change_res = True if data["resolution"] != res[3].split('"')[-2] else False

        with open("user_settings.json", "w+") as user:
            dump(data, user, indent=4)

        return change_res
