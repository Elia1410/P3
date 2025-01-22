import pygame
from vector import Vector2d
from random import randint, random
from fish import Fish

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

fish = []
for i in range(1):
    fish.append(Fish(Vector2d(screen.get_width()/2, screen.get_height()/2), Vector2d(1, 1), (0.8, 0, 0)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("beige")

    for f in fish:
        f.update(fish)
        f.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()