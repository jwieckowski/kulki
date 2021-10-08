import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# --------------------------------------- SCREEN ------------------------------------------
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 0, 0))

# # Create a surface and pass in a tuple containing its length and width
# surf = pygame.Surface((50, 50))

# # Give the surface a color to separate it from the background
# surf.fill((0, 0, 0))
# rect = surf.get_rect()

# # Put the center of surf at the center of the display
# surf_center = (
#     (SCREEN_WIDTH-surf.get_width())/2,
#     (SCREEN_HEIGHT-surf.get_height())/2
# )

# # Draw surf at the new coordinates
# screen.blit(surf, surf_center)
# pygame.display.flip()

# ----------------------- OBJECTS CLASSESS ---------------------------------------------------
# Define a UserBoard object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'user_board'


class GameBoard(pygame.sprite.Sprite):
    def __init__(self):
        super(GameBoard, self).__init__()
        self.surf = pygame.Surface((SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50))
        self.surf.fill((255, 255, 255))
        self.position = (
            (SCREEN_WIDTH-self.surf.get_width())/2,
            (SCREEN_HEIGHT-self.surf.get_height())/2
        )
        self.rect = self.surf.get_rect()


class UserBoard(pygame.sprite.Sprite):
    def __init__(self):
        super(UserBoard, self).__init__()
        self.surf = pygame.Surface((500, 300))
        self.surf.fill((169, 169, 169))
        self.position = (
            (SCREEN_WIDTH-self.surf.get_width())/2,
            (SCREEN_HEIGHT-self.surf.get_height())/2
        )
        self.rect = self.surf.get_rect()

        self.circles = []

    def add_circle(self, circle):
        self.circles.append(circle)

class Circle(pygame.sprite.Sprite):
    def __init__(self, color, x, y, radius):
        super(Circle, self).__init__()
        self.color = color
        self.position = ((x, y))
        self.radius = radius

CIRCLES_COLORS = [
    (255, 0, 0), # red
    (0, 255, 0), # green
    (0, 0, 255), # blue
    (255, 255, 0), # yellow
    (128, 0, 128), # purple
    (0, 0, 0) # black
]

CIRCLE_RADIUS = 30


game_board = GameBoard()
# Draw the player on the screen
screen.blit(game_board.surf, game_board.position)

user_board = UserBoard()
# Draw the player on the screen
screen.blit(user_board.surf, user_board.position)

# TEXT - TOTAL POINTS
total = 'TOTAL POINTS: '
font = pygame.font.SysFont('Comic Sans MS', 15)
total_text = font.render(total, True, CIRCLES_COLORS[5])
screen.blit(total_text, (320, 70))

total = '50'
font = pygame.font.SysFont('Comic Sans MS', 15)
total_text = font.render(total, True, CIRCLES_COLORS[5])
screen.blit(total_text, (460, 70))

# TEXT - NUMBER FOR EACH COLUMN
labels = [str(i+1) for i in range(5)]
font = pygame.font.SysFont('Comic Sans MS', 30)
for index, label in enumerate(labels):
    text = font.render(label, True, CIRCLES_COLORS[5])
    screen.blit(text, (190 + index * 100, 100))

circle = Circle(CIRCLES_COLORS[0], 200, 200, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)
circle = Circle(CIRCLES_COLORS[0], 200, 300, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)
circle = Circle(CIRCLES_COLORS[0], 200, 400, CIRCLE_RADIUS)
# user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)

circle = Circle(CIRCLES_COLORS[1], 300, 200, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)
circle = Circle(CIRCLES_COLORS[1], 300, 300, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)
circle = Circle(CIRCLES_COLORS[1], 300, 400, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)

circle = Circle(CIRCLES_COLORS[2], 400, 200, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)
circle = Circle(CIRCLES_COLORS[2], 400, 300, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)
circle = Circle(CIRCLES_COLORS[2], 400, 400, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)

circle = Circle(CIRCLES_COLORS[3], 500, 200, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)
circle = Circle(CIRCLES_COLORS[3], 500, 300, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)
circle = Circle(CIRCLES_COLORS[3], 500, 400, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)

circle = Circle(CIRCLES_COLORS[4], 600, 200, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)
circle = Circle(CIRCLES_COLORS[4], 600, 300, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)
circle = Circle(CIRCLES_COLORS[4], 600, 400, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)
# print(user_board.circles)


# ADDITIONAL CIRCLES
circle = Circle(CIRCLES_COLORS[5], 400, 520, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)

# NEXT COLOR
circle = Circle(CIRCLES_COLORS[5], 700, 520, CIRCLE_RADIUS)
user_board.add_circle(circle)
pygame.draw.circle(screen, circle.color, circle.position, circle.radius)


# Update the display
pygame.display.flip()







# ---------------------- GAME ----------------------------------------------------------------
# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
