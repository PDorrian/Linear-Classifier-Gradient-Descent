import pygame
import random
from utility import translate


class Point:
    def __init__(self, screen, size, x, y):
        # Give point random position
        self.x = x
        self.y = y
        self.screen = screen
        self.width = size[0]
        self.height = size[1]

        # Label depending on which side of line it is
        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1

    # Create point with random coordinates
    @classmethod
    def auto(cls, screen, size):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        return cls(screen, size, x, y)

    def pixel_x(self):
        return int(translate(self.x, -1, 1, 0, self.width))

    def pixel_y(self):
        return int(translate(self.y, -1, 1, self.height, 0))

    # Draw point
    def draw(self):
        if self.label == 1:
            color = (0, 0, 0)
        else:
            color = (200, 200, 200)

        px = self.pixel_x()
        py = self.pixel_y()

        pygame.draw.circle(self.screen, color, (px, py), 10)