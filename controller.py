import pygame
from pygame.locals import *

pygame.init()
display = pygame.display.set_mode((600, 600))


class Controller:
    def __init__(self):

        self.joysticks = []
        self.type = []
        self.x_hd = 596  # initial position of the chip

        for i in range(pygame.joystick.get_count()):
            self.joysticks.append(pygame.joystick.Joystick(i))
            self.joysticks[-1].init()
            self.type.append(self.joysticks[i].get_name())

            axes = self.joysticks[i].get_numaxes()
            print(axes)

        print(self.joysticks)

    def checkController(self):
        if self.joysticks:
            return True
        else:
            return False

    def isControllerEvent(self, event):
        return (
            event.type == JOYBUTTONDOWN
            or event.type == JOYAXISMOTION
            or event.type == JOYHATMOTION
        )

    def isControllerDropEvent(self, event):
        if len(self.type) > 0:
            if self.type[0] == "PS4 Controller":
                if event.type == JOYBUTTONDOWN:
                    return event.button == 12 or event.button == 0
                if event.type == JOYAXISMOTION:
                    return abs(event.axis) == 5 and event.value == 1

            else:
                if event.type == JOYBUTTONDOWN:
                    return event.button == 0
                if event.type == JOYHATMOTION:
                    return event.value[1] == -1
                if event.type == JOYAXISMOTION:
                    return abs(event.axis) == 5 and event.value == 1
    def isControllerEscEvent(self, event):
        if len(self.type) > 0:
            if self.type[0] == "PS4 Controller":
                if event.type == JOYBUTTONDOWN:
                    return event.button == 1 or event.button == 6
                if event.type == JOYAXISMOTION:
                    return abs(event.axis) == 4 and event.value == 1

            else:
                if event.type == JOYBUTTONDOWN:
                    return event.button == 1 or event.button == 7
                if event.type == JOYAXISMOTION:
                    return abs(event.axis) == 2 and event.value == 1

    def get_x_pos(self, event):
        px_diff_hd = 109  # how much the  chip will move each time
        max_px_hd = 931  # max x position of the chip
        min_px_hd = 269  # min x position of the chip

        if self.type[0] == "PS4 Controller":
            if event.type == JOYBUTTONDOWN:
                if event.button == 13 or event.button == 9:
                    print("Move left")
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )

                if event.button == 14 or event.button == 10:
                    print("Move right")
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0

            if event.type == JOYAXISMOTION:
                if abs(event.axis) == 0:
                    if event.value > 0.7:
                        print("Move Right")
                        self.x_hd += 5 if self.x_hd + 5 < max_px_hd else 0

                    if event.value < -0.7:
                        print("Move Left")
                        self.x_hd -= 5 if self.x_hd - 5 >= min_px_hd else 0

        else:
            if event.type == JOYBUTTONDOWN:
                if event.button == 4:
                    print("Move left")
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )

                if event.button == 5:
                    print("Move right")
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0

            if event.type == JOYHATMOTION:
                if event.value[0] == 1:
                    print("Move right")
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0

                if event.value[0] == -1:
                    print("Move left")
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )

            if event.type == JOYAXISMOTION:
                if abs(event.axis) == 0:
                    if event.value > 0.7:
                        print("Move Right")
                        self.x_hd += 5 if self.x_hd + 5 < max_px_hd else 0

                    if event.value < -0.7:
                        print("Move Left")
                        self.x_hd -= 5 if self.x_hd - 5 >= min_px_hd else 0

        return self.x_hd

    def check_event(self, event):
        px_diff_hd = 109  # how much the  chip will move each time
        max_px_hd = 931  # max x position of the chip
        min_px_hd = 269  # min x position of the chip

        if self.type[0] == "PS4 Controller":

            # Press Buttons
            if event.type == JOYBUTTONDOWN:
                if event.button == 13 or event.button == 9:
                    print("Move left")
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )
                    return self.x_hd

                if event.button == 14 or event.button == 10:
                    print("Move right")
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0
                    return self.x_hd

            # Sticks   PS4
            if event.type == JOYAXISMOTION:
                if abs(event.axis) == 0:
                    if event.value > 0.7:
                        print("Move Right")

                        self.x_hd += 1 if self.x_hd + 1 < max_px_hd else 0
                        return self.x_hd

                    if event.value < -0.7:
                        print("Move Left")

                        self.x_hd -= 1 if self.x_hd - 1 >= min_px_hd else 0
                        return self.x_hd

        # Xbox and other
        else:

            # Press buttons
            if event.type == JOYBUTTONDOWN:

                if event.button == 4:
                    print("Move left")
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )
                    return self.x_hd

                if event.button == 5:
                    print("Move right")
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0
                    return self.x_hd

            # D-pad Xbox
            if event.type == JOYHATMOTION:
                if event.value[0] == 1:
                    print("Move right")
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0
                    return self.x_hd

                if event.value[0] == -1:
                    print("Move left")
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )
                    return self.x_hd

            if event.type == JOYAXISMOTION:
                if abs(event.axis) == 0:
                    if event.value > 0.7:
                        print("Move Right")
                        self.x_hd += 1 if self.x_hd + 1 < max_px_hd else 0
                        return self.x_hd

                    if event.value < -0.7:
                        print("Move Left")
                        self.x_hd -= 1 if self.x_hd - 1 >= min_px_hd else 0
                        return self.x_hd
