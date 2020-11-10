import pygame as pg
import os

from itertools import cycle


class EndingScreen:
    def __init__(self, screen, data: list) -> None:
        self.screen = screen
        self.score_1 = data[0]
        self.name_1 = data[1]
        self.score_2 = data[2]
        self.name_2 = data[3]

    def scores(self):
        a = screen.get_width()//2
        b = screen.get_height()
        WHITE = (255,255,255)
        background = pg.image.load("images\\background\\black.jpg")
        FONT = pg.font.Font(f"{os.getcwd()}\\fonts\JustMyType-KePl.ttf", 125)

        ending = True
        while ending:

            self.screen.blit(background, (0, 0))

            text = FONT.render("SCORE SCREEN", True, (WHITE))
            text_rec = text.get_rect().width//2
          

            self.screen.blit(text, [a - text_rec, 20])

            players = FONT.render(
                f"{str(self.name_1)}  X  {str(self.name_2)}", True, (WHITE)
            )
            score1 = FONT.render(
                f"{str(self.score_1)}", True, (WHITE)
            )
            score2 = FONT.render(
                f"{str(self.score_2)}", True, (WHITE)
            )
            players_rec = players.get_rect().width//2
            # score1_rec = score1.get_rect().width//2
            # score2_rec = score2.get_rect().width//2

            print(a, b)
            self.screen.blit(
                players, [a - players_rec, b // 3]
            )
            self.screen.blit(
                score1, [a - players_rec + players_rec//3, b // 3 + 150]
            )
            self.screen.blit(
                score2, [a + players_rec - players_rec//2 , b // 3 + 150]
            )

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    ending = False
                    return False
        return False


pg.init()

width: int = 1280
height: int = 720

size: tuple = (width, height)
screen = pg.display.set_mode((size), pg.FULLSCREEN)


data = [10, "Guilherme", 5, "Leonardo"]
ac = EndingScreen(screen, data)
ac.scores()
