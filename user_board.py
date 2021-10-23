import pygame
import numpy as np
import random

from constants import *


class UserBoard(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_WIDTH, BOARD_HEIGHT, active_color, next_color):
        super(UserBoard, self).__init__()
        self.surf = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))
        self.surf.fill((180, 180, 180))
        self.position = (
            (SCREEN_WIDTH-self.surf.get_width())/2,
            (SCREEN_HEIGHT-self.surf.get_height())/2
        )
        self.rect = self.surf.get_rect()

        self.circles = np.zeros(
            (ROWS, COLUMNS), dtype='object')
        self.active_color = active_color
        self.next_color = next_color

    def get_row_position(self, column):
        try:
            return list(self.circles[:, column]).index(0)
        except Exception as e:
            return -1

    def add_circle(self, circle, column, row):
        try:
            self.circles[row][column] = circle
            return
        except Exception as e:
            pass

    def set_new_color(self):
        self.active_color = self.next_color
        self.next_color = CIRCLES_COLORS[random.randint(0, 4)]

    def is_board_filled(self):
        return np.any((self.circles == 0))

    def clear_board(self):
        self.circles = np.zeros(
            (ROWS, COLUMNS), dtype='object')

    def calculate_points(self, screen, game_board, current_points, game_variant):
        rows, columns = self.circles.shape
        total_points = 0
        active_points = 1

        # calculate points in rows
        for r in range(rows):
            row = self.circles[r, :]
            for i in range(len(row)-1):
                if row[i] != 0 and row[i+1] != 0:
                    if row[i].color == row[i+1].color:
                        total_points += active_points
                        active_points += 1
                    else:
                        active_points = 1
                else:
                    active_points = 1

            active_points = 1

        # calculate points in columns
        for c in range(columns):
            column = self.circles[:, c]
            for i in range(len(column)-1):
                if column[i] != 0 and column[i+1] != 0:
                    if column[i].color == column[i+1].color:
                        total_points += active_points
                        active_points += 1
                    else:
                        active_points = 1
                else:
                    active_points = 1
            active_points = 1

        # update extra points and set rewards and penalties
        if total_points == current_points:
            if game_variant == 0:
                game_board.active_image = 'assets/empty.png'
            elif game_variant == 2:
                game_board.active_image = 'assets/sad.png'
            elif game_variant == 3:
                errorSound = pygame.mixer.Sound('assets/error.wav')
                errorSound.play()
            elif game_variant == 1:
                self.surf.fill((100, 100, 100))

            # smaller circles
            # for circles in self.circles:
            #     for circle in circles:
            #         if circle != 0:
            #             pygame.draw.circle(screen, circle.color,
            #                                circle.position, CIRCLE_RADIUS)

        else:
            if game_variant == 0:
                game_board.active_image = 'assets/smile.png'
            if game_variant == 2:
                game_board.active_image = 'assets/empty.png'
            elif game_variant == 1:
                self.surf.fill((180, 180, 180))

            # enlarge circles
            # for circles in self.circles:
            #     for circle in circles:
            #         if circle != 0:
            #             pygame.draw.circle(screen, circle.color,
            #                                circle.position, BIGGER_CIRCLE_RADIUS)

        return total_points
