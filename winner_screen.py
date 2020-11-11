import os
import pygame_gui
import pygame as pg
from sys import exit

from itertools import cycle


class EndingScreen:
    def __init__(self, screen, data: list, res) -> None:
        self.screen = screen
        self.score_1 = data[0]
        self.name_1 = data[1]
        self.score_2 = data[2]
        self.name_2 = data[3]

        pg.init()
        pg.display.set_mode(res, pg.FULLSCREEN)
        self.manager = pygame_gui.UIManager(res, "data/styles/winner_menu.json")

        self.play_again = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect((530, 700), (200, 80)),
            text="Play Again",
            manager=self.manager,
            object_id="#PlayAgain",
        )

        self.starter_menu = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect((835, 700), (250, 80)),
            text="Starter Menu",
            manager=self.manager,
            object_id="#StarterMenu",
        )

        self.quit = pygame_gui.elements.UIButton(
            relative_rect=pg.Rect((1185, 700), (150, 80)),
            text="Quit",
            manager=self.manager,
            object_id="#Quit",
        )

    def scores(self) -> bool:
        a = screen.get_width() // 2
        b = screen.get_height()
        WHITE = (255, 255, 255)
        background = pg.image.load("data\images\\background\\black.jpg")
        FONT = pg.font.Font(f"{os.getcwd()}\data\\fonts\classic.ttf", 125)
        clock = pg.time.Clock()

        ending = True
        while ending:

            self.screen.blit(background, (0, 0))

            text = FONT.render("SCORE SCREEN", True, (WHITE))
            text_rec = text.get_rect().width // 2

            self.screen.blit(text, [a - text_rec, 20])

            players = FONT.render(
                f"{str(self.name_1)}  X  {str(self.name_2)}", True, (WHITE)
            )
            score1 = FONT.render(f"{str(self.score_1)}", True, (WHITE))
            score2 = FONT.render(f"{str(self.score_2)}", True, (WHITE))
            players_rec = players.get_rect().width // 2
            # score1_rec = score1.get_rect().width//2
            # score2_rec = score2.get_rect().width//2

            print(a, b)
            self.screen.blit(players, [a - players_rec, b // 3])
            self.screen.blit(score1, [a - players_rec + players_rec // 3, b // 3 + 150])
            self.screen.blit(score2, [a + players_rec - players_rec // 2, b // 3 + 150])

            time_delta = clock.tick(60) / 1000.0

            self.manager.update(time_delta)
            self.manager.draw_ui(screen)

            for event in pg.event.get():
                self.manager.process_events(event)

                if event.type == pg.KEYDOWN:
                    ending = False
                    return False

                if self.play_again.check_pressed():
                    pass

                if self.starter_menu.check_pressed():
                    pass

                if self.quit.check_pressed():
                    exit()

            pg.display.update()

        return False


pg.init()

width: int = 1920
height: int = 1080

size: tuple = (width, height)
screen = pg.display.set_mode(size, pg.FULLSCREEN)


data = [10, "Guilherme", 5, "Leonardo"]
ac = EndingScreen(screen, data, size)
ac.scores()
