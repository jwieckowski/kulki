import pygame

from game_board import GameBoard
from user_board import UserBoard
from circle import Circle
from constants import *
from statistics import save_move_to_file

import csv
import secrets
from datetime import datetime


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_7,
    K_8,
    K_9,
    K_0,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

moves = {
    K_1: 310,
    K_2: 460,
    K_3: 610,
    K_4: 760,
    K_5: 910,
    K_6: 1060,
    K_7: 1210,
    K_8: 1360,
    K_9: 1510,
    K_0: 1660,
}

# Generowanie losowego ID
userID = secrets.token_urlsafe(6)


class Game():
    @staticmethod
    def refresh_screen(screen, game_board, user_board, POINTS, game_variant):
        screen.fill((0, 0, 0))

        screen.blit(game_board.surf, game_board.position)
        screen.blit(user_board.surf, user_board.position)

        game_board.add_board_labels(screen, TOTAL, str(POINTS),
                                    COLUMNS_NUMBER, CIRCLES_COLORS[5])
        game_board.add_board_circles(
            screen, user_board.active_color, user_board.next_color, CIRCLE_RADIUS)
        if game_variant == 0 or game_variant == 2:
            game_board.add_image(screen, game_board.active_image, IMG_POSITION)

        # refresh circles
        for circles in user_board.circles:
            for circle in circles:
                if circle != 0:
                    pygame.draw.circle(screen, circle.color,
                                       circle.position, circle.radius)

    @staticmethod
    def user_move(screen, user_board, key):
        row = user_board.get_row_position(list(moves.keys()).index(key))
        if row < 0:
            return

        circle = Circle(user_board.active_color, moves[key],
                        300 + row * 100, CIRCLE_RADIUS)
        user_board.add_circle(circle, list(moves.keys()).index(key), row)
        pygame.draw.circle(screen, circle.color,
                           circle.position, circle.radius)
        user_board.set_new_color()

        return row

    @staticmethod
    def run(screen, user_board, game_board, game_variant):
        running = True
        all_points = 0
        current_points = 0

        # count game time
        start_time = pygame.time.get_ticks()
        current_time = 0

        # Ustawiewnie timestampa odniesienia (początku gry)
        timestamp = datetime.now().timestamp()

        # Main loop
        while running:
            Game.refresh_screen(screen, game_board,
                                user_board, all_points + current_points, game_variant)

            if user_board.is_board_filled() == False:
                user_board.clear_board()
                all_points = current_points + all_points
                current_points = 0

            # Look at every event in the queue
            for event in pygame.event.get():
                # Did the user hit a key?
                if event.type == KEYDOWN:

                    # check if the pressed key was correct to add a circle
                    if event.key in moves.keys():
                        row = Game.user_move(screen, user_board, event.key)
                        game_board.update_board_circles(screen,
                                                        user_board.active_color, user_board.next_color)
                        current_points = user_board.calculate_points(screen,
                                                                     game_board, current_points, game_variant)
                        game_board.update_points_label(
                            screen, current_points + all_points, CIRCLES_COLORS[5])

                        save_move_to_file(userID, timestamp,
                                          current_points + all_points, game_variant, row)

                    # Was it the Escape key? If so, stop the loop.
                    if event.key == K_ESCAPE:
                        running = False

                # Did the user click the window close button? If so, stop the loop.
                elif event.type == QUIT:
                    running = False

                # Update the display
                pygame.display.flip()

            # count time
            current_time = pygame.time.get_ticks()
            if (current_time-start_time) / (1000 * 60) >= GAME_TIME:
                running = False
                print('Koniec gry')
