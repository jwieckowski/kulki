import pygame
import random

from game_board import GameBoard
from user_board import UserBoard
from game import Game
from constants import *

# GAME VARIANTS
# 0 - rewards - smile
# 1 - rewards - lighter background
# 2 - penalties - sad
# 3 - penalties - sound
game_variant = 3


START_IMAGE = 'assets/smile.png' if game_variant == 0 else 'assets/sad.png'
pygame.init()


active_color = CIRCLES_COLORS[random.randint(0, 4)]
next_color = CIRCLES_COLORS[random.randint(0, 4)]

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 0, 0))

game_board = GameBoard(SCREEN_WIDTH, SCREEN_HEIGHT, START_IMAGE)
screen.blit(game_board.surf, game_board.position)

user_board = UserBoard(SCREEN_WIDTH, SCREEN_HEIGHT,
                       BOARD_WIDTH, BOARD_HEIGHT, active_color, next_color)
screen.blit(user_board.surf, user_board.position)

game_board.add_board_labels(screen, TOTAL, POINTS,
                            COLUMNS_NUMBER, CIRCLES_COLORS[5])
game_board.add_board_circles(
    screen, active_color, next_color, CIRCLE_RADIUS)

Game.run(screen, user_board, game_board, game_variant)
