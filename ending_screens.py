import os
import pygame_gui
import pygame as pg
from sys import exit

from typing import Any
from settings import Settings
from database import ScoreboardData


class EndingScreen:
    def __init__(self, screen: Any, data: dict, **kwargs):
        self.screen = screen
        self.data = data
        self.score_1, self.score_2 = data.values()
        self.name_1, self.name_2 = data.keys()
        self.st = Settings()
        self.size = self.st.size
        self.width = self.st.width

        self._createUI(kwargs)

        self.sb = ScoreboardData(data)
        self.sb.updateTable()
        self.sb.winnerUpdate()

    def _createUI(self, kwargs):
        # pg.display.set_mode(kwargs["res"], pg.FULLSCREEN)
        self.manager = pygame_gui.UIManager(
            kwargs["res"], "data/styles/winner_menu.json"
        )

        self.play_again = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect(*kwargs["pg_res"]),
            text="Play Again",
            manager=self.manager,
            object_id="#Button",
        )

        self.starter_menu = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect(*kwargs["sm_res"]),
            text="Starter Menu",
            manager=self.manager,
            object_id="#Button",
        )

        self.leaderboard = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect(*kwargs["lb_res"]),
            text="Leaderboard",
            manager=self.manager,
            object_id="#Button",
        )

        self.quit = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect(*kwargs["quit_res"]),
            text="Quit",
            manager=self.manager,
            object_id="#Button",
        )

    def scores(self) -> bool:
        snd_win = pg.mixer.Sound("data/sounds/win_effect.mp3")
        pg.mixer.Sound.play(snd_win)
        pg.mixer.Sound.set_volume(snd_win, 0.1)
        pg.time.wait(1000)

        snd = pg.mixer.Sound("data/soundtracks/score.mp3")
        pg.mixer.Sound.play(snd, -1)
        pg.mixer.Sound.set_volume(snd, 0.05)

        pg.mouse.set_visible(True)

        a = self.screen.get_width() // 2
        b = self.screen.get_height()

        GREY = (37, 41, 46)

        FONT = pg.font.Font(f"{os.getcwd()}\data\\fonts\classic.ttf", 125)

        clock = pg.time.Clock()

        bg_image = pg.image.load(f"data\images\menu\score_screen.png")

        ending = True
        while ending:
            pg.mixer.music.fadeout(1000)

            text = FONT.render("SCORE SCREEN", True, (GREY))
            text_rec = text.get_rect().width // 2

            players = FONT.render(
                f"{str(self.name_1)}  X  {str(self.name_2)}", True, (GREY)
            )
            score1 = FONT.render(f"{str(self.score_1)}", True, (GREY))
            score2 = FONT.render(f"{str(self.score_2)}", True, (GREY))
            players_rec = players.get_rect().width // 2

            time_delta = clock.tick(60) / 1000.0

            for event in pg.event.get():
                self.manager.process_events(event)

                if self.play_again.check_pressed():
                    pg.mixer.Sound.stop(snd)
                    return True

                if self.starter_menu.check_pressed():
                    pg.mixer.Sound.stop(snd)
                    return False

                if self.leaderboard.check_pressed():
                    pg.mixer.Sound.stop(snd)
                    self.leaderboard.disable()
                    LeaderBoard(
                        self.sb,
                        self.screen,
                        self.size,
                        (
                            self.st.lb_back,
                            self.st.lb_player,
                            self.st.lb_score,
                            self.st.lb_mult,
                        ),
                    ).run()
                    self.leaderboard.enable()
                    pg.mixer.Sound.play(snd, -1)

                if self.quit.check_pressed():
                    exit()

            self.screen.blit(bg_image, (0, 0))
            self.screen.blit(text, [a - text_rec, 20])
            self.screen.blit(players, [a - players_rec, b // 3])
            self.screen.blit(score1, [a - players_rec + players_rec // 3, b // 3 + 150])
            self.screen.blit(score2, [a + players_rec - players_rec // 2, b // 3 + 150])

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)

            pg.display.update()

        pg.mouse.set_visible(False)

        return False


class LeaderBoard:
    def __init__(self, sb, screen, size, lb_res):
        self.screen = screen
        self.res = size
        self.style = "data/styles/winner_menu.json"

        self.lb_back, self.lb_player, self.lb_score, self.lb_mult = lb_res
        self.object_id = "#Text" if size[0] == 1920 else "#Text2"

        self.sb = sb
        self.scores = self._get_scores()
        self._show_lb()

    def _get_scores(self):
        return self.sb.getData(9)

    def _show_lb(self):
        self.manager = pygame_gui.UIManager(self.res, self.style)

        self.back = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect(*self.lb_back),
            text="Back",
            manager=self.manager,
            object_id="#Button",
        )

        for i in range(len(self.scores)):
            add = self.lb_mult * i
            cont_p = list(
                elem + add if self.lb_player.index(elem) == 1 else elem
                for elem in self.lb_player
            )
            cont_s = list(
                elem + add if self.lb_score.index(elem) == 1 else elem
                for elem in self.lb_score
            )

            pygame_gui.elements.UILabel(
                pg.Rect(cont_p),
                text=self.scores[i][0],
                manager=self.manager,
                object_id=self.object_id,
            )

            pygame_gui.elements.UILabel(
                pg.Rect(cont_s),
                text=str(self.scores[i][1]),
                manager=self.manager,
                object_id=self.object_id,
            )

    def run(self):
        snd = pg.mixer.Sound(f"data/soundtracks/leaderboard.mp3")
        pg.mixer.Sound.play(snd, -1)
        pg.mixer.Sound.set_volume(snd, 0.05)

        is_running = True
        clock = pg.time.Clock()

        img = pg.image.load("data/images/menu/leaderboard.png")

        if self.res == (1280, 720):
            img = pg.transform.scale(img, self.res)

        while is_running:
            time_delta = clock.tick(60) / 1000.0

            for event in pg.event.get():
                self.manager.process_events(event)

                if event.type == pg.USEREVENT and self.back.check_pressed():
                    is_running = False

            self.manager.update(time_delta)
            self.screen.blit(img, (0, 0))
            self.manager.draw_ui(self.screen)

            pg.display.update()
