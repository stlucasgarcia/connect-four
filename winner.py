import pygame as pg


class EndingScreen:
    def __init__(self, screen, data: list, font) -> None:
        screen = self.screen
        self.score_1 = data[0]
        self.name_1 = data[1]
        self.score_2 = data[2]
        self.name_2 = data[2]
        self.font = font
        
    

    def scores(self):
        
