import pygame
from pygame.locals import *


class Controller:
    """Class created to manage all the controllers features """

    def __init__(self):
        self.joysticks = []
        self.type = []
        self.x_hd = 596  # initial position of the chip

        for i in range(pygame.joystick.get_count()):
            self.joysticks.append(pygame.joystick.Joystick(i))
            self.joysticks[-1].init()
            self.type.append(self.joysticks[i].get_name())

            axes = self.joysticks[i].get_numaxes()

    def check_controller(self):
        """Check if there's a connected controller"""
        if self.joysticks:
            return True
        else:
            return False

    @staticmethod
    def is_controller_event(event):
        """Used later to manage controller events"""
        return (
                event.type == JOYBUTTONDOWN
                or event.type == JOYAXISMOTION
                or event.type == JOYHATMOTION
        )

    def is_controller_drop_event(self, event):
        """Drop piece using the controllers available option"""
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

    def is_controller_esc_event(self, event):
        """Check for the esc menu event for controller"""
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
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )

                if event.button == 14 or event.button == 10:
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0

            if event.type == JOYAXISMOTION:
                if abs(event.axis) == 0:
                    if event.value > 0.7:
                        self.x_hd += 5 if self.x_hd + 5 < max_px_hd else 0

                    if event.value < -0.7:
                        self.x_hd -= 5 if self.x_hd - 5 >= min_px_hd else 0

        else:
            if event.type == JOYBUTTONDOWN:
                if event.button == 4:
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )

                if event.button == 5:
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0

            if event.type == JOYHATMOTION:
                if event.value[0] == 1:
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0

                if event.value[0] == -1:
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )

            if event.type == JOYAXISMOTION:
                if abs(event.axis) == 0:
                    if event.value > 0.7:
                        self.x_hd += 5 if self.x_hd + 5 < max_px_hd else 0

                    if event.value < -0.7:
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
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )
                    return self.x_hd

                if event.button == 14 or event.button == 10:
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0
                    return self.x_hd

            # Sticks   PS4
            if event.type == JOYAXISMOTION:
                if abs(event.axis) == 0:
                    if event.value > 0.7:
                        self.x_hd += 1 if self.x_hd + 1 < max_px_hd else 0
                        return self.x_hd

                    if event.value < -0.7:
                        self.x_hd -= 1 if self.x_hd - 1 >= min_px_hd else 0
                        return self.x_hd

        # Xbox and other
        else:

            # Press buttons
            if event.type == JOYBUTTONDOWN:

                if event.button == 4:
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )
                    return self.x_hd

                if event.button == 5:
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0
                    return self.x_hd

            # D-pad Xbox
            if event.type == JOYHATMOTION:
                if event.value[0] == 1:
                    self.x_hd += px_diff_hd if self.x_hd + px_diff_hd < max_px_hd else 0
                    return self.x_hd

                if event.value[0] == -1:
                    self.x_hd -= (
                        px_diff_hd if self.x_hd - px_diff_hd >= min_px_hd else 0
                    )
                    return self.x_hd

            if event.type == JOYAXISMOTION:
                if abs(event.axis) == 0:
                    if event.value > 0.7:
                        self.x_hd += 1 if self.x_hd + 1 < max_px_hd else 0
                        return self.x_hd

                    if event.value < -0.7:
                        self.x_hd -= 1 if self.x_hd - 1 >= min_px_hd else 0
                        return self.x_hd
