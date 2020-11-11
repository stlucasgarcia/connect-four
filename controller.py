import pygame as pg

pg.init()
pg.joystick.init()


class Controller:
    def __init__(self) -> None:
        self.x_axis = 270  # TODO Full HD
        if pg.joystick.get_count() > 1:
            joystick_1 = pg.joystick.Joystick(0)
            joystick_2 = pg.joystick.Joystick(1)
            joystick_1.init()
            joystick_2.init()

        else:
            joystick = pg.joystick.Joystick(0)
            joystick.init()

    def controllerStick(self, axisX):
        if (
            self.x_axis >= 280 and self.x_axis <= 912
        ):  # Joystick to move it horizontally
            if axisX > 0.5:
                self.x_axis += 10

            elif axisX < -0.5:
                self.x_axis -= 10

            elif self.x_axis == 270:
                if axisX > 0.5:
                    self.x_axis += 10

            elif self.x_axis == 922:
                if axisX < -0.5:
                    self.x_axis -= 10

    def controllerDpad(self):
        if self.x_axis >= 270 and self.x_axis < 380:
            if dpad == (-1, 0):
                self.x_axis = 270

            elif dpad == (1, 0):
                self.x_axis = 380

        elif self.x_axis >= 380 and self.x_axis < 490:
            if dpad == (1, 0):
                self.x_axis = 490

            elif dpad == (-1, 0):
                self.x_axis = 270

        elif self.x_axis >= 490 and self.x_axis < 595:
            if dpad == (-1, 0):
                self.x_axis = 380

            elif dpad == (1, 0):
                self.x_axis = 595

        elif self.x_axis >= 595 and self.x_axis < 705:
            if dpad == (-1, 0):
                self.x_axis = 490

            elif dpad == (1, 0):
                self.x_axis = 705

        elif self.x_axis >= 705 and self.x_axis < 812:
            if dpad == (-1, 0):
                self.x_axis = 595

            elif dpad == (1, 0):
                self.x_axis = 812

        elif self.x_axis >= 812 and self.x_axis < 922:
            if dpad == (-1, 0):
                self.x_axis = 705

            elif dpad == (1, 0):
                self.x_axis = 922

        elif self.x_axis == 922:
            if dpad == (-1, 0):
                self.x_axis = 812

    # def pressButtons(self):
    #     if joystick.get_button(0) or right_trigger > 0.5:  # A or Right Trigger
    #         print(f"A or Right Trigger: {joystick.get_button(0)}, {right_trigger}")

    #     if joystick.get_button(1) or joystick.get_button(7):  # B or start
    #         print(f"Botão B or Start: {joystick.get_button(1)}, {joystick.get_button(7)}")

    def joystickRun(self):
        # joystickType = self.joystick.get_name()

        c = Controller()

        close = True
        while close:

            for event in pg.event.get():  # User did something.
                pass

            joystick = pg.joystick.Joystick(0)
            joystick.init()

            dpad = joystick.get_hat(0)
            axisX = joystick.get_axis(0)  # Horizontal Axis of left joystick

            # right_trigger = joystick.get_axis(5)

            c.controllerDpad(dpad)
            c.controllerStick(axisX)
            print(dpad)
            print(axisX)
            # Controller.pressButtons()


Controller().joystickRun()