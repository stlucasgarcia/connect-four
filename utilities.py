import numpy as np
import random
import math
import time

import pygame as pg
from settings import Settings
from ending_screens import EndingScreen


class UtilitiesMain:
    def __init__(self, screen: pg.Surface):
        self.config = Settings()
        self.screen = screen

        self.COLUMN_AMOUNT = 7
        self.ROW_AMOUNT = 6
        self.WINDOWS_LENGHT = 4

        self.background_image = self.config.bg_image
        self.chip_1 = self.config.chip_1
        self.chip_2 = self.config.chip_2
        self.width = self.config.width
        self.width = self.config.width
        self.font = self.config.font
        self.zero = 0
        self.player_chip = 1
        self.ai_chip = 2

    def create_matrix(self) -> np.ndarray:
        matrix = np.zeros((self.ROW_AMOUNT, self.COLUMN_AMOUNT))
        return matrix

    def drop_piece(self, matrix: np.ndarray, row: int, column: int, piece: int) -> None:
        matrix[row][column] = piece

    def is_available(self, matrix: np.ndarray, column: int) -> bool:
        return matrix[self.ROW_AMOUNT - 1][column] == 0

    def location_X(self, click_loc: int) -> int:
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

    def draw_board(self, matrix: np.ndarray, start_time, clock) -> None:
        self.screen.blit(self.background_image, (0, 0))

        start_time = self.timer(start_time, clock)

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

        return start_time

    def get_open_row(self, matrix: np.ndarray, column: int) -> int:
        for row in range(self.ROW_AMOUNT):
            if matrix[row][column] == 0:
                return row

    def get_available_list(self, matrix):
        available_slots = []

        for column in range(self.COLUMN_AMOUNT):
            if self.is_available(matrix, column):
                available_slots.append(column)

        return available_slots

    def is_victory(self, matrix: np.ndarray, chip: int) -> bool:
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
        return (matrix[:][:] != 0).all()

    def is_valid(
        self,
        column: int,
        is_position_available: bool,
        turn: int,
        sound_chip_1,
        sound_chip_2,
    ):

        chip = None
        if column != 0 and is_position_available:
            turn += 1

            if turn % 2 == 0:
                chip = self.chip_1

                turn = 2

                sound_chip_1.play()

                return turn, chip

            elif turn % 2 == 1:
                chip = self.chip_2

                turn = 1

                sound_chip_2.play()

                return turn, chip

    def is_terminal(self, matrix):
        return (
            self.is_victory(matrix, self.player_chip)
            or self.is_victory(matrix, self.ai_chip)
            or len(self.get_available_list(matrix)) == 0  # TODO self.is_tie()
        )

    def timer(self, start_time, clock):
        seconds = pg.time.get_ticks() - start_time
        minutes = 0

        if seconds >= 59900 and seconds <= 60100:
            start_time *= pg.time.get_ticks()
            seconds = 0
            minutes += 1

        timeF = f"{seconds // 1000}"

        if minutes > 0:
            timeF = f"{minutes} : {seconds // 1000}"
        else:
            pass

        textTime = self.font.render(timeF, True, (255, 255, 255))

        self.screen.blit(textTime, (self.width // 2, 15 - 15))

        return start_time

    def playersTurn(
        self,
        column: int,
        matrix: np.ndarray,
        player_turn,
        sound_chip_1,
        sound_chip_2,
        usernames,
        start_time,
        clock,
        option="AI",
    ):
        turn = player_turn
        play_again = None
        chip = None
        column -= 1

        is_pos_available = self.is_available(matrix, column)

        if is_pos_available:
            turn, chip = self.is_valid(
                column + 1, is_pos_available, turn, sound_chip_1, sound_chip_2
            )

            row = self.get_open_row(matrix, column)

            self.drop_piece(matrix, row, column, turn)

            if self.is_victory(matrix, turn) or self.is_tie(matrix):

                self.draw_board(matrix, start_time, clock)

                pg.time.wait(500)

                data = {usernames[0]: 10, usernames[1]: 5}

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

        return play_again, turn, chip

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = self.player_chip

        if piece == self.player_chip:
            opp_piece = self.ai_chip

        if window.count(piece) == 4:
            score += 100

        elif window.count(piece) == 3 and window.count(self.zero) == 1:
            score += 5

        elif window.count(piece) == 2 and window.count(self.zero) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(self.zero) == 1:
            score -= 4

        return score

    def score_position(self, board, piece):
        score = 0

        ## Score center column
        center_array = [int(i) for i in list(board[:, self.COLUMN_AMOUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        ## Score Horizontal
        for r in range(self.ROW_AMOUNT):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(self.COLUMN_AMOUNT - 3):
                window = row_array[c : c + self.WINDOWS_LENGHT]
                score += self.evaluate_window(window, piece)

        ## Score Vertical
        for c in range(self.COLUMN_AMOUNT):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(self.ROW_AMOUNT - 3):
                window = col_array[r : r + self.WINDOWS_LENGHT]
                score += self.evaluate_window(window, piece)

        ## Score positive sloped diagonal
        for r in range(self.ROW_AMOUNT - 3):
            for c in range(self.COLUMN_AMOUNT - 3):
                window = [board[r + i][c + i] for i in range(self.WINDOWS_LENGHT)]
                score += self.evaluate_window(window, piece)

        for r in range(self.ROW_AMOUNT - 3):
            for c in range(self.COLUMN_AMOUNT - 3):
                window = [board[r + 3 - i][c + i] for i in range(self.WINDOWS_LENGHT)]
                score += self.evaluate_window(window, piece)

        return score

    def minimaxTree(self, matrix, depth, alpha, beta, maximizingPlayer):
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
