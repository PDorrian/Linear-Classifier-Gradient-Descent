import pygame
import random


class Point:
    def __init__(self, size):
        # Give point random position
        self.x = random.randrange(size[0])
        self.y = random.randrange(size[1])

        # Label depending on which side of line it is
        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1

    # Draw point
    def show(self, screen):
        if self.label == 1:
            color = (0, 255, 255)
        else:
            color = (0, 0, 255)
        pygame.draw.circle(screen, color, (self.x, self.y), 10, 1)