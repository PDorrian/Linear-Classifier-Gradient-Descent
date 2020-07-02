import Perceptron
import sys
import pygame

import Point

# Surface setup
pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

# Colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

# Create points
points = []
for i in range(100):
    points.append(Point.Point.auto(screen, size))

# Create perceptron
brain = Perceptron.Perceptron()


def f(x):
    # y = mx + c
    return 3*x + 2


# Pygame game loop
pygame.display.update()
while 1:
    # Draw background and separating line
    screen.fill(white)

    p1 = Point.Point(screen, size, -1, f(-1))
    p2 = Point.Point(screen, size, 1, f(1))
    pygame.draw.line(screen, black, (p1.pixel_x(), p1.pixel_y()), (p2.pixel_x(), p2.pixel_y()))

    # Draw points on screen
    for point in points:
        point.draw()

    for point in points:
        # Colour points depending on guess accuracy
        inputs = [point.x, point.y]
        guess = brain.guess(inputs)
        if guess == point.label:
            pygame.draw.circle(screen, green, (point.pixel_x(), point.pixel_y()), 5)
        else:
            pygame.draw.circle(screen, red, (point.pixel_x(), point.pixel_y()), 5)

    # Update screen
    pygame.display.update()

    for event in pygame.event.get():
        # Stop on window close
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            # Train perceptron when mouse is clicked
            for point in points:
                inputs = [point.x, point.y]
                brain.train(inputs, point.label)
