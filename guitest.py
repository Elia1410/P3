import pygame
import thorpy as tp

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

tp.init(screen, tp.theme_classic)

button = tp.Button("button")
button.set_center(screen.get_width()/3, screen.get_height()/2)
button.set_font_color([10, 10, 10])
button.set_font_size(18)

dropdownLauncher = tp.Button("dropdown button")
dropdownLauncher.set_center(screen.get_width()/3*2, screen.get_height()/2)
dropdownLauncher.set_font_color([10, 10, 10])
dropdownLauncher.set_font_size(18)
dropdown = tp.DropDownList(dropdownLauncher, ["A", "B", "C"])

uiElements = tp.Group([dropdown, dropdownLauncher, button])
updater = uiElements.get_updater()

while running:
    clock.tick(60)
    events = pygame.event.get()
    mouseRel = pygame.mouse.get_rel()
    for event in events:
        if event == pygame.QUIT:
            running = False

    screen.fill("beige")

    updater.update(events=events, mouse_rel=mouseRel)
    
    pygame.display.flip()
    
pygame.quit()