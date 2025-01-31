import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from vector import Vector2d
from random import randint, random, seed
from fish import Pray, Flock

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pygame.font.init()
font = pygame.font.SysFont('Arial', 22)


seed()

flock = Flock(screen, 50, 1, 1, 1, 2, True)

def newFlock(numberOfFish, cohesion, seperation, alignment, speed, drawTail):
    global flock
    del flock
    flock = Flock(screen, numberOfFish, cohesion, seperation, alignment, speed, drawTail)

# GUI
btnNewFlock = Button(screen, 50, 20, 100, 30, onClick=lambda: print("clicked!"), text="Reset boids")
sldCohesion = Slider(screen, 200, 30, 120, 10) 
sldSeperation = Slider(screen, 200, 60, 120, 10) 
sldAlignment = Slider(screen, 200, 90, 120, 10) 
sldNumberOfFish = Slider(screen, 200, 120, 120, 10)

def getCohesion():
    return round(sldCohesion.value/100+0.5, 2)

def getSeperation():
    return round(sldSeperation.value/100+0.5, 2)

def getAlignment():
    return round(sldAlignment.value/100+0.5, 2)

def getNumberOfFish():
    return int(sldNumberOfFish.value*2)

def blitText(text: str, pos: tuple):
    textRendered = font.render(text, True, (0, 0, 0))
    screen.blit(textRendered, pos)




while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill("beige")

    flock.update()

    blitText("Cohesion", (330, 20))
    blitText("Seperation", (330, 50))
    blitText("Alignment", (330, 80))
    blitText("NumberOfFish", (330, 110))

    blitText(str(getCohesion()), (460, 20))
    blitText(str(getSeperation()), (460, 50))
    blitText(str(getAlignment()), (460, 80))
    blitText(str(getNumberOfFish()), (460, 110))

    pygame_widgets.update(events)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
