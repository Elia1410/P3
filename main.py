import pygame
from vector import Vector2d
from random import randint, random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

vectors = []
startPoints = []
for i in range(10_000):
    vectors.append(Vector2d(randint(-15, 15), randint(-15, 15), (random(), random(), random()), 2))
    startPoints.append((randint(0, 1280), randint(0, 720)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for i, v in enumerate(vectors):
        v.draw(screen, startPoints[i][0], startPoints[i][1])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()