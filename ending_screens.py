import os
import pygame_gui
import pygame as pg
from sys import exit

from typing import Any
from settings import Settings

# from database import ScoreboardData


class EndingScreen:
    def __init__(self, screen: Any, data: dict, **kwargs):
        self.screen = screen
        self.score_1, self.score_2 = data.values()
        self.name_1, self.name_2 = data.keys()
        self.width = Settings().width

        pg.display.set_mode(kwargs["res"], pg.FULLSCREEN)
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
        pg.mouse.set_visible(True)

        a = self.screen.get_width() // 2
        b = self.screen.get_height()

        # WHITE = (255, 255, 255)
        GREY = (37, 41, 46)  # 2529

        FONT = pg.font.Font(f"{os.getcwd()}\data\\fonts\classic.ttf", 125)

        clock = pg.time.Clock()

        bg_image = pg.image.load(f"data\images\menu\score_screen.png")
        self.screen.blit(bg_image, (0, 0))

        ending = True
        while ending:
            pg.mixer.music.fadeout(1000)

            # bg_music = pg.mixer.Sound(f"data/soundtracks/classic.mp3")
            # pg.mixer.music.play(loops=-1)
            # pg.mixer.music.set_volume(1)

            text = FONT.render("SCORE SCREEN", True, (GREY))
            text_rec = text.get_rect().width // 2

            self.screen.blit(text, [a - text_rec, 20])

            players = FONT.render(
                f"{str(self.name_1)}  X  {str(self.name_2)}", True, (GREY)
            )
            score1 = FONT.render(f"{str(self.score_1)}", True, (GREY))
            score2 = FONT.render(f"{str(self.score_2)}", True, (GREY))
            players_rec = players.get_rect().width // 2

            self.screen.blit(players, [a - players_rec, b // 3])
            self.screen.blit(score1, [a - players_rec + players_rec // 3, b // 3 + 150])
            self.screen.blit(score2, [a + players_rec - players_rec // 2, b // 3 + 150])

            time_delta = clock.tick(60) / 1000.0

            self.manager.update(time_delta)
            self.manager.draw_ui(self.screen)

            for event in pg.event.get():
                self.manager.process_events(event)

                if self.play_again.check_pressed():
                    return True

                if self.starter_menu.check_pressed():
                    return False

                if self.leaderboard.check_pressed():
                    LeaderBoard()

                if self.quit.check_pressed():
                    exit()

            pg.display.update()

        pg.mouse.set_visible(0)

        return False


class LeaderBoard:
    def __init__(self):
        pass

    def _get_scores(self):
        # ScoreboardData()
        pass


# st = Settings()

# pg.init()

# # Pega as config que ta no user_settings.json (TA EM FULLHD E CLASSIC)
# width = st.width
# height = st.height

# size = st.size
# screen = pg.display.set_mode(size, pg.FULLSCREEN)


# data = {"Guilherme": 10, "Leonardo": 5}
# ac = EndingScreen(
#     screen,
#     data,
#     res=size,
#     pg_res=st.win_pg,
#     sm_res=st.win_sm,
#     quit_res=st.win_quit,
# )
# ac.scores()
