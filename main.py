import pygame as pg

from starter_screen import InitScreen
from main_screen import MainScreen
from settings import Settings
from menu import StarterMenu

pg.init()

config = Settings()

width: int = config.width
height: int = config.height

size: tuple = (width, height)

screen: pg.Surface = pg.display.set_mode(size, pg.FULLSCREEN)

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

StarterMenu(
    res=config.size,
    sm_res=[
        config.sm_title,
        config.sm_mode_txt,
        config.sm_mode,
        config.sm_theme_text,
        config.sm_theme,
        config.sm_res_text,
        config.sm_res,
        config.sm_next,
        config.sm_quit,
    ],
    screen=screen,
).run()

MainScreen_object: object = MainScreen(screen, is_controller)
MainScreen_object.main_screen()
