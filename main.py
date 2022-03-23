from _thread import start_new_thread

import pygame as pg

from multiplayer import Server, Client
from screens import MainScreen, StarterMenu, InitScreen
from utils import Settings, Path, sep

scores = [0, 0]

"""
Main file, it's used to create the main loop and call other function, as well as initialize classes and initial 
settings/menus.
"""


# Pygame exit to stop initial loop
def game_run():
    server, client = init_multiplayer()

    # return

    pg.init()

    config = Settings()

    width: int = config.width
    height: int = config.height

    size: tuple = (width, height)

    screen: pg.Surface = pg.display.set_mode(size)

    pg.display.set_caption("Connect Four")

    icon: pg.Surface = pg.image.load(f"{Path.images()}icon{Path.IMAGE_SUFFIX}")

    pg.display.set_icon(icon)

    pg.mouse.set_visible(False)

    pg.mouse.set_pos(963, 63)

    is_controller: bool = False

    changes_res = False

    is_running = True

    init_screen_object = InitScreen(screen)
    init_screen_object.starter_screen()

    play_again = False
    name1, name2 = None, None

    while is_running:
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

        main_screen_object = MainScreen(screen, is_controller, config.option, server, client)
        play_again = main_screen_object.main_screen(scores, usernames=[name1, name2])


def init_multiplayer() -> tuple[Server, Client]:
    server = Server()

    try:
        server.post_init()
        start_new_thread(server.listen, ())
    except OSError:
        print('Servidor já está inicializado')

    client = Client()
    start_new_thread(client.listen, ())

    return server, client


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

    while True:
        pass
