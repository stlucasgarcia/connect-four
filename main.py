import pygame as pg

from init_screen import InitScreen
from main_screen import MainScreen
from settings import Settings

pg.init()

config = Settings()

width: int = config.width
height: int = config.height

size: tuple = (width, height)

screen: pg.Surface = pg.display.set_mode((size), pg.FULLSCREEN)

pg.display.set_caption("Connect Four")

icon: pg.Surface = pg.image.load("data\images\icon.png")

pg.display.set_icon(icon)

pg.mouse.set_visible(0)

pg.mouse.set_pos(963, 63)

is_controller: bool = False

try:
    joystick = pg.joystick.Joystick(0)
    is_controller = True

except pg.error:
    pass

InitScreen_object: object = InitScreen(screen)
InitScreen_object.starter_screen()

MainScreen_object: object = MainScreen(screen, is_controller)
MainScreen_object.main_screen()
