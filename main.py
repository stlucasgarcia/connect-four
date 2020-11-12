import pygame as pg

from starter_screen import InitScreen
from main_screen import MainScreen
from settings import Settings
from menu import StarterMenu

# Pygame exit to stop initial loop
def game_run():
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

    isRunning = True
    InitScreen_object = InitScreen(screen)
    InitScreen_object.starter_screen()
    play_again = False
    name1, name2 = None, None
    while isRunning:
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

        pg.mouse.set_visible(0)

        MainScreen_object = MainScreen(screen, is_controller)
        play_again = MainScreen_object.main_screen(usernames=[name1, name2])


if __name__ == "__main__":
    game_run()
