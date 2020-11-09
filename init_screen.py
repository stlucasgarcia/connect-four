import pygame
import os

from itertools import cycle


class init_screen:
    def __init__(self, screen) -> None:
        self.screen = screen

    def starter_screen(self):
        background = pygame.image.load("images\starter\starterclassic.png")

        FONT = pygame.font.Font(f"{os.getcwd()}\\fonts\JustMyType-KePl.ttf", 95)

        intro = True
        while intro == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    intro = False
                    return False

            print("Saiu 1")
            self.screen.blit(background, (0, 0))

            text = FONT.render("Press any key to start", True, (0, 0, 0))

            self.screen.blit(text, [580, 800])

            pygame.display.update()

            if not intro:
                break

        return False
