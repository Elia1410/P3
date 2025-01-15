import pygame
from vector import Vector2d
from random import randint, random
from fish import Fish

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

fish = Fish(screen.get_width()/2, screen.get_height()/2, (255, 0, 0))
fish.velo.setX(4)
fish.velo.setY(2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("beige")

    fish.update()
    fish.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()