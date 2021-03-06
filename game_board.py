import pygame

from circle import Circle
from constants import *


class GameBoard(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, image):
        super(GameBoard, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50))
        self.surf.fill((255, 255, 255))
        self.position = (
            (SCREEN_WIDTH-self.surf.get_width())/2,
            (SCREEN_HEIGHT-self.surf.get_height())/2
        )
        self.rect = self.surf.get_rect()
        self.active_image = image

    def add_board_labels(self, screen, total, points, columns_number, color):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        self.total_text = font.render(total, True, color)
        screen.blit(self.total_text, (920, 70))

        font = pygame.font.SysFont('Comic Sans MS', 30, bold=True)
        self.points_text = font.render(points, True, color)
        screen.blit(self.points_text, (1200, 70))

        # TEXT - NUMBER FOR EACH COLUMN
        labels = [str(i+1) for i in range(columns_number)]
        labels[-1] = '0'
        font = pygame.font.SysFont('Comic Sans MS', 30)
        for index, label in enumerate(labels):
            text = font.render(label, True, color)
            screen.blit(text, (300 + index * 150, 120))

    def update_points_label(self, screen, points, color):

        font = pygame.font.SysFont('Comic Sans MS', 30, bold=True)
        self.points_text = font.render(
            str(points), True, color)
        screen.blit(self.points_text, (1200, 70))

    def add_board_circles(self, screen, first_color, next_color, radius):
        # CURRENT CIRCLE COLOR
        self.active_circle = Circle(first_color, 1000, 1040, radius)
        pygame.draw.circle(screen, self.active_circle.color,
                           self.active_circle.position, self.active_circle.radius)

        # NEXT CIRCLE COLOR
        self.next_circle = Circle(next_color, 1800, 1040, radius)
        pygame.draw.circle(screen, self.next_circle.color,
                           self.next_circle.position, self.next_circle.radius)

    def update_board_circles(self, screen, first_color, next_color):
        self.active_circle.color = first_color
        pygame.draw.circle(screen, self.active_circle.color,
                           self.active_circle.position, self.active_circle.radius)

        self.next_circle.color = next_color
        pygame.draw.circle(screen, self.next_circle.color,
                           self.next_circle.position, self.next_circle.radius)
        pygame.display.update()

    def add_image(self, screen, image, position):
        self.active_image = image
        faceImg = pygame.image.load(self.active_image)
        faceImg = pygame.transform.scale(faceImg, (100, 100))
        screen.blit(faceImg, position)
