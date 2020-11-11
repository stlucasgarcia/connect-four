import pygame as pg
import time

pg.init()
pg.joystick.init()

# controller_x_axis_fullHD =
x_axis_HD = 270

joystick_count = pg.joystick.get_count()


def controllerMovementPlayer1StickHD(x_axis_HD, axisX):

    if (
        x_axis_HD >= 280 and x_axis_HD <= 912
    ):  # Usando o analógico para mexer a peça horizontalmente
        if axisX > 0.5:
            x_axis_HD += 10

        elif axisX < -0.5:
            x_axis_HD -= 10

        elif x_axis_HD == 270:
            if axisX > 0.5:
                x_axis_HD += 10

        elif x_axis_HD == 922:
            if axisX < -0.5:
                x_axis_HD -= 10


def controllerMovementPlayer1DpadHD(x_axis_HD, dpad):
    if x_axis_HD >= 270 and x_axis_HD < 380:
        if dpad == (-1, 0):
            x_axis_HD = 270

        elif dpad == (1, 0):
            x_axis_HD = 380

    elif x_axis_HD >= 380 and x_axis_HD < 490:
        if dpad == (1, 0):
            x_axis_HD = 490

        elif dpad == (-1, 0):
            x_axis_HD = 270

    elif x_axis_HD >= 490 and x_axis_HD < 595:
        if dpad == (-1, 0):
            x_axis_HD = 380

        elif dpad == (1, 0):
            x_axis_HD = 595

    elif x_axis_HD >= 595 and x_axis_HD < 705:
        if dpad == (-1, 0):
            x_axis_HD = 490

        elif dpad == (1, 0):
            x_axis_HD = 705

    elif x_axis_HD >= 705 and x_axis_HD < 812:
        if dpad == (-1, 0):
            x_axis_HD = 595

        elif dpad == (1, 0):
            x_axis_HD = 812

    elif x_axis_HD >= 812 and x_axis_HD < 922:
        if dpad == (-1, 0):
            x_axis_HD = 705

        elif dpad == (1, 0):
            x_axis_HD = 922

    elif x_axis_HD == 922:
        if dpad == (-1, 0):
            x_axis_HD = 812


def pressButtons():
    if joystick.get_button(0) or right_trigger > 0.5:  # A or Right Trigger
        print(f"A or Right Trigger: {joystick.get_button(0)}, {right_trigger}")

    if joystick.get_button(1) or joystick.get_button(7):  # B or start
        print(f"Botão B or Start: {joystick.get_button(1)}, {joystick.get_button(7)}")


flag = True

while flag:
    for event in pg.event.get():  # User did something.
        if event.type == pg.QUIT:  # If user clicked close.
            done = True  # Flag that we are done so we exit this loop.

        elif event.type == pg.JOYBUTTONDOWN:
            print("Joystick button pressed.")

        elif event.type == pg.JOYBUTTONUP:
            print("Joystick button released.")

    time.sleep(1)

    joystick = pg.joystick.Joystick(0)
    joystick.init()
    dpad = joystick.get_hat(0)
    axisX = joystick.get_axis(0)  # Horizontal Axis of left joystick
    right_trigger = joystick.get_axis(5)

    controllerMovementPlayer1DpadHD(x_axis_HD, dpad)
    controllerMovementPlayer1StickHD(x_axis_HD, axisX)
    pressButtons()
