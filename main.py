import pygame as pg

from init_screen import InitScreen
from main_screen import MainScreen

pg.init()

width: int = 1920
height: int = 1080

size: tuple = (width, height)

screen: pg.Surface = pg.display.set_mode((size), pg.FULLSCREEN)

pg.display.set_caption("Connect Four")

icon: pg.Surface = pg.image.load("data\images\icon.png")

pg.display.set_icon(icon)

pg.mouse.set_visible(0)

pg.mouse.set_pos(963, 63)

InitScreen_object: object = InitScreen(screen)
InitScreen_object.starter_screen()

MainScreen_object: object = MainScreen(screen)
MainScreen_object.main_screen()


# close_game: bool = False
# while not close_game:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.exit()
#             sys.exit()

#     screen.fill((255, 255, 255))

#     pg.display.update()
