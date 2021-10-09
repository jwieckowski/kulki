import pygame

from game_board import GameBoard
from user_board import UserBoard
from circle import Circle
from constants import *

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

moves = {
    K_1: 200,
    K_2: 300,
    K_3: 400,
    K_4: 500,
    K_5: 600,
}


class Game():
    @staticmethod
    def refresh_screen(screen, game_board, user_board, POINTS):
        screen.fill((0, 0, 0))

        screen.blit(game_board.surf, game_board.position)
        screen.blit(user_board.surf, user_board.position)

        game_board.add_board_labels(screen, TOTAL, str(POINTS),
                                    COLUMNS_NUMBER, CIRCLES_COLORS[5])
        game_board.add_board_circles(
            screen, user_board.active_color, user_board.next_color, CIRCLE_RADIUS)

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
                        200 + row * 100, CIRCLE_RADIUS)
        user_board.add_circle(circle, list(moves.keys()).index(key), row)
        pygame.draw.circle(screen, circle.color,
                           circle.position, circle.radius)
        user_board.set_new_color()

    @staticmethod
    def run(screen, user_board, game_board):
        running = True
        points = 0

        # Main loop
        while running:
            Game.refresh_screen(screen, game_board, user_board, points)
            # Look at every event in the queue
            for event in pygame.event.get():
                # Did the user hit a key?
                if event.type == KEYDOWN:

                    # check if the pressed key was correct to add a circle
                    if event.key in moves.keys():
                        Game.user_move(screen, user_board, event.key)
                        game_board.update_board_circles(screen,
                                                        user_board.active_color, user_board.next_color)
                        points = user_board.calculate_points()
                        game_board.update_points_label(
                            screen, points, CIRCLES_COLORS[5])

                    # Was it the Escape key? If so, stop the loop.
                    if event.key == K_ESCAPE:
                        running = False

                # Did the user click the window close button? If so, stop the loop.
                elif event.type == QUIT:
                    running = False

                # Update the display
                pygame.display.flip()
