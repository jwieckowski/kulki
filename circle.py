import pygame

class Circle(pygame.sprite.Sprite):
    def __init__(self, color, x, y, radius):
        super(Circle, self).__init__()
        self.color = color
        self.position = ((x, y))
        self.radius = radius
