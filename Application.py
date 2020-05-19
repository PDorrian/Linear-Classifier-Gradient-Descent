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
    points.append(Point.Point(size))

# Create perceptron
brain = Perceptron.Perceptron()

# Pygame game loop
pygame.display.update()
while 1:
    # Draw background and separating line
    screen.fill(white)
    pygame.draw.line(screen, black, (0, 0), size)

    # Draw points on screen
    for point in points:
        point.show(screen)

    for point in points:
        # Colour points depending on guess accuracy
        inputs = [point.x, point.y]
        guess = brain.guess(inputs)
        if guess == point.label:
            pygame.draw.circle(screen, green, (point.x, point.y), 5)
        else:
            pygame.draw.circle(screen, red, (point.x, point.y), 5)

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
