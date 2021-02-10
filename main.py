import pygame as pg

from screens.starter_screen import InitScreen
from screens.main_screen import MainScreen
from utils.settings import Settings
from screens.menu import StarterMenu

from os import sep
scores = [0, 0]

"""
Main file, it's used to create the main loop and call other function, as well as initialize classes and initial settings/menus.
"""
# Pygame exit to stop initial loop
def game_run():
    pg.init()

    config = Settings()

    width: int = config.width
    height: int = config.height

    size: tuple = (width, height)

    screen: pg.Surface = pg.display.set_mode(size)

    pg.display.set_caption("Connect Four")

    icon: pg.Surface = pg.image.load("data\images\icon.png")

    pg.display.set_icon(icon)

    pg.mouse.set_visible(0)

    pg.mouse.set_pos(963, 63)

    is_controller: bool = False

    changes_res = False

    isRunning = True

    InitScreen_object = InitScreen(screen)
    InitScreen_object.starter_screen()

    play_again = False
    name1, name2 = None, None

    while isRunning:
        pg.mouse.set_visible(False)

        try:
            joystick = pg.joystick.Joystick(0)
            is_controller = True

        except pg.error:
            pass

        if not play_again:
            name1, name2, changes_res = StarterMenu(
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
                    config.sm_p1,
                    config.sm_p2,
                    config.sm_p1_1,
                ],
                screen=screen,
            ).run()
            config = Settings()

        if changes_res:
            pg.quit()
            re_exec()
            break

        pg.mouse.set_visible(False)

        MainScreen_object = MainScreen(screen, is_controller, config.option)
        play_again = MainScreen_object.main_screen(scores, usernames=[name1, name2])


def re_exec():
    import os, sys, subprocess

    subprocess.call(
        [
            f"{sys.path[0]}{sep}venv{sep}bin{sep}python.exe",
            os.path.join(sys.path[0], __file__),
        ]
        + sys.argv[1:]
    )


if __name__ == "__main__":
    game_run()
