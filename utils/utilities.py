import random
from datetime import timedelta

import math
import numpy as np
import pygame as pg

from multiplayer import Server, Client
from screens import EndingScreen
from utils.settings import Settings


class UtilitiesMain:
    """Utilities class used to organize the main screen loop"""

    def __init__(self, screen: pg.Surface, server: Server, client: Client):
        self.config = Settings()
        self.screen = screen
        self.server = server
        self.client = client

        self.COLUMN_AMOUNT = 7
        self.ROW_AMOUNT = 6
        self.WINDOWS_LENGHT = 4

        self.background_image = self.config.bg_image
        self.chip_1 = self.config.chip_1
        self.chip_2 = self.config.chip_2
        self.width = self.config.width
        self.font = self.config.font
        self.zero = 0
        self.player_chip = 1
        self.ai_chip = 2

    def create_matrix(self) -> np.ndarray:
        """Creates and returns the matrix"""

        matrix = np.zeros((self.ROW_AMOUNT, self.COLUMN_AMOUNT))
        return matrix

    def drop_piece(self, matrix: np.ndarray, row: int, column: int, piece: int, ignore_move: bool = False) -> None:
        """Drops the piece on the matrix"""

        if self.client:
            piece = 1 if self.client.is_player_one else 2
            if ignore_move:
                piece = 1 if piece == 2 else 2
            print(f"has client, {ignore_move=} and {piece=}")

        matrix[row][column] = piece

    def is_available(self, matrix: np.ndarray, column: int) -> bool:
        """Check if the chips position is available on the matrix"""

        return matrix[self.ROW_AMOUNT - 1][column] == 0

    def location_X(self, click_loc: int) -> int:
        """'Hit Box of the chip' this function is used to defines the place in which the chip will be placed by the
        player"""

        # First location (X)
        if self.width == 1280:
            if 240 < click_loc < 364:
                return 1

            elif 364 < click_loc < 473:
                return 2

            elif 473 < click_loc < 582:
                return 3

            elif 582 < click_loc < 688:
                return 4

            elif 688 < click_loc < 798:
                return 5

            elif 798 < click_loc < 907:
                return 6

            elif 907 < click_loc < 1040:
                return 7

            else:
                return 0

        else:
            if 357 < click_loc < 551:
                return 1

            elif 551 < click_loc < 714:
                return 2

            elif 714 < click_loc < 879:
                return 3

            elif 879 < click_loc < 1038:
                return 4

            elif 1038 < click_loc < 1203:
                return 5

            elif 1203 < click_loc < 1362:
                return 6

            elif 1362 < click_loc < 1423:
                return 7

            else:
                return 0

    def draw_board(self, matrix: np.ndarray, start_time, usernames) -> None:
        """Print the board on the screen with all features"""

        self.screen.blit(self.background_image, (0, 0))

        self.timer(start_time)
        self.print_names(usernames)
        for column in range(self.COLUMN_AMOUNT):
            for row in range(self.ROW_AMOUNT):

                if matrix[row][column] != 0:
                    if self.width == 1280:
                        X_CONST = 21
                        Y_CONST = 10

                        x = 269 + ((X_CONST * column) + (87.75 * (column)))
                        y = 616 - (Y_CONST * (row) + (87.5 * (row)))

                    else:
                        X_CONST = 140
                        Y_CONST = 128.5

                        x = 402.25 + ((X_CONST * column) + (22.78 * (column)))
                        y = 923.75 - (Y_CONST * (row) + (17.43 * (row)))

                    if matrix[row][column] == 1:
                        self.screen.blit(self.chip_1, (x, y))

                    elif matrix[row][column] == 2:
                        self.screen.blit(self.chip_2, (x, y))

    def get_open_row(self, matrix: np.ndarray, column: int) -> int:
        """gets the open row on the matrix"""

        for row in range(self.ROW_AMOUNT):
            if matrix[row][column] == 0:
                return row

    def get_available_list(self, matrix):
        """Creates a list with all the available positions on the list"""

        available_slots = []

        for column in range(self.COLUMN_AMOUNT):
            if self.is_available(matrix, column):
                available_slots.append(column)

        return available_slots

    def is_victory(self, matrix: np.ndarray, chip: int) -> bool:
        """Check if the player won using the matrix"""

        # Check horizontal
        for column in range(self.COLUMN_AMOUNT - 3):
            for row in range(self.ROW_AMOUNT):
                if (
                        matrix[row][column] == chip
                        and matrix[row][column + 1] == chip
                        and matrix[row][column + 2] == chip
                        and matrix[row][column + 3] == chip
                ):
                    return True

        # Check Vertical
        for column in range(self.COLUMN_AMOUNT):
            for row in range(self.ROW_AMOUNT - 3):
                if (
                        matrix[row][column] == chip
                        and matrix[row + 1][column] == chip
                        and matrix[row + 2][column] == chip
                        and matrix[row + 3][column] == chip
                ):
                    return True

        # Main diagonal
        for column in range(self.COLUMN_AMOUNT - 3):
            for row in range(self.ROW_AMOUNT - 3):
                if (
                        matrix[row][column] == chip
                        and matrix[row + 1][column + 1] == chip
                        and matrix[row + 2][column + 2] == chip
                        and matrix[row + 3][column + 3] == chip
                ):
                    return True

        # MainC diagonal
        for column in range(self.COLUMN_AMOUNT - 3):
            for row in range(3, self.ROW_AMOUNT):
                if (
                        matrix[row][column] == chip
                        and matrix[row - 1][column + 1] == chip
                        and matrix[row - 2][column + 2] == chip
                        and matrix[row - 3][column + 3] == chip
                ):
                    return True

    def is_tie(self, matrix: np.ndarray):
        """Check if it's a tie to end the game on PlayersTurn function"""

        return (matrix[:][:] != 0).all()

    def is_valid(
            self,
            column: int,
            is_position_available: bool,
            turn: int,
            sound_chip_1,
            sound_chip_2,
            option,
    ):
        """Verify if the desired position is available in the matrix"""

        chip = None
        if column != 0 and is_position_available:
            turn += 1

            if turn % 2 == 0:
                chip = self.chip_2 if option == "Player vs AI" else self.chip_1

                turn = 2

                sound_chip_1.play()

                return turn, chip

            elif turn % 2 == 1:
                chip = self.chip_1 if option == "Player vs AI" else self.chip_2

                turn = 1

                sound_chip_2.play()

                return turn, chip

    def is_terminal(self, matrix):
        """Check if the position will end the game, is used on the AI"""

        return (
                self.is_victory(matrix, self.player_chip)
                or self.is_victory(matrix, self.ai_chip)
                or len(self.get_available_list(matrix)) == 0  # TODO self.is_tie()
        )

    def timer(self, start_time) -> None:
        """Creates a timer that's shown on the screen"""

        hour, minutes, seconds = str(
            timedelta(milliseconds=pg.time.get_ticks() - start_time)
        ).split(":")
        seconds = seconds.split(".")[0]

        time = f"{minutes} : {seconds}"

        y = 41 if self.width != 1280 else 27

        text_time = self.font.render(time, True, (255, 255, 255))

        self.screen.blit(text_time, (self.width // 2 - 80, y))

    def playersTurn(
            self,
            column: int,
            matrix,
            player_turn,
            sound_chip_1,
            sound_chip_2,
            usernames,
            start_time,
            scores,
            option,
            ignore_move=False,
    ):
        """Main function of utilities, it makes the players turn and call other function to create the difference
        between turns and check for win"""

        turn = player_turn
        play_again = None
        chip = None
        column -= 1

        is_pos_available = self.is_available(matrix, column)

        if is_pos_available:
            turn, chip = self.is_valid(
                column + 1, is_pos_available, turn, sound_chip_1, sound_chip_2, option
            )

            row = self.get_open_row(matrix, column)

            if option == "Multiplayer" and not ignore_move:
                self.client.move(column)

            self.drop_piece(matrix, row, column, turn, ignore_move)

            print(matrix)

            if self.is_victory(matrix, turn) or self.is_tie(matrix):
                scores[0] += 1 if turn % 2 == 0 else scores[0]
                scores[1] += 1 if turn % 2 == 1 else scores[1]

                self.draw_board(matrix, start_time, usernames)

                pg.display.update()

                pg.time.wait(1500)

                data = {usernames[0]: scores[0], usernames[1]: scores[1]}

                ending = EndingScreen(
                    self.screen,
                    data,
                    res=self.config.size,
                    pg_res=self.config.win_pg,
                    sm_res=self.config.win_sm,
                    quit_res=self.config.win_quit,
                    lb_res=self.config.win_ld,
                )

                play_again = ending.scores()

        return play_again, turn, chip, scores, column, matrix, sound_chip_1, sound_chip_2, usernames, start_time, option

    def evaluate_window(self, window, chip) -> int:
        """Evaluate the window and returns the score, it's used by the AI"""

        score = 0
        opp_chip = self.player_chip

        if chip == self.player_chip:
            opp_chip = self.ai_chip

        if window.count(chip) == 4:
            score += 100

        elif window.count(chip) == 3 and window.count(self.zero) == 1:
            score += 5

        elif window.count(chip) == 2 and window.count(self.zero) == 2:
            score += 2

        if window.count(opp_chip) == 3 and window.count(self.zero) == 1:
            score -= 4

        return score

    def score_position(self, matrix, chip) -> int:
        """Check the windows and return the scores"""

        score = 0

        ## Score center column
        center_array = [int(i) for i in list(matrix[:, self.COLUMN_AMOUNT // 2])]
        center_count = center_array.count(chip)
        score += center_count * 3

        ## Score Horizontal
        for r in range(self.ROW_AMOUNT):
            row_array = [int(i) for i in list(matrix[r, :])]
            for c in range(self.COLUMN_AMOUNT - 3):
                window = row_array[c: c + self.WINDOWS_LENGHT]
                score += self.evaluate_window(window, chip)

        ## Score Vertical
        for c in range(self.COLUMN_AMOUNT):
            col_array = [int(i) for i in list(matrix[:, c])]
            for r in range(self.ROW_AMOUNT - 3):
                window = col_array[r: r + self.WINDOWS_LENGHT]
                score += self.evaluate_window(window, chip)

        ## Score positive sloped diagonal
        for r in range(self.ROW_AMOUNT - 3):
            for c in range(self.COLUMN_AMOUNT - 3):
                window = [matrix[r + i][c + i] for i in range(self.WINDOWS_LENGHT)]
                score += self.evaluate_window(window, chip)

        for r in range(self.ROW_AMOUNT - 3):
            for c in range(self.COLUMN_AMOUNT - 3):
                window = [matrix[r + 3 - i][c + i] for i in range(self.WINDOWS_LENGHT)]
                score += self.evaluate_window(window, chip)

        return score

    def minimaxTree(self, matrix, depth, alpha, beta, maximizingPlayer):
        """Main function of the AI, it calls the other AI functions to create a move"""

        valid_locations = self.get_available_list(matrix)

        is_terminal = self.is_terminal(matrix)

        if depth == 0 or is_terminal:
            if is_terminal:
                if self.is_victory(matrix, self.ai_chip):
                    return (None, 100000000000000)
                elif self.is_victory(matrix, self.player_chip):
                    return (None, -10000000000000)
                else:  # Game is over, no more valid moves
                    return (None, 0)
            else:  # Depth is zero
                return (None, self.score_position(matrix, self.ai_chip))

        if maximizingPlayer:
            value = -math.inf

            column = random.choice(valid_locations)

            for col in valid_locations:
                row = self.get_open_row(matrix, col)
                b_copy = matrix.copy()

                self.drop_piece(b_copy, row, col, self.ai_chip)

                new_score = self.minimaxTree(b_copy, depth - 1, alpha, beta, False)[1]

                if new_score > value:
                    value = new_score
                    column = col

                alpha = max(alpha, value)

                if alpha >= beta:
                    break

            return column, value

        else:  # Minimizing player
            value = math.inf

            column = random.choice(valid_locations)

            for col in valid_locations:
                row = self.get_open_row(matrix, col)

                b_copy = matrix.copy()

                self.drop_piece(b_copy, row, col, self.player_chip)

                new_score = self.minimaxTree(b_copy, depth - 1, alpha, beta, True)[1]

                if new_score < value:
                    value = new_score
                    column = col

                beta = min(beta, value)

                if alpha >= beta:
                    break

            return column, value

    def print_names(self, usernames) -> None:
        """Print the names of the user's on the screen"""

        name_1 = usernames[0]
        name_2 = "AI" if len(usernames) == 1 else usernames[1]

        name_1 = name_1[:10] if len(name_1) > 10 else name_1
        name_2 = name_2[:10] if len(name_2) > 10 else name_2

        x_2 = 1610 if self.width != 1280 else 1000
        y = 41 if self.width != 1280 else 30

        name_text_1 = self.font.render(name_1, True, (255, 255, 255))
        name_text_2 = self.font.render(name_2, True, (255, 255, 255))

        self.screen.blit(name_text_1, (43, y))
        self.screen.blit(name_text_2, (x_2, y))
