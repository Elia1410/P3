import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.toggle import Toggle
from fish import Flock

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pygame.font.init()
font = pygame.font.SysFont('Arial', 18)


flock = None

def newFlock():
    global flock
    del flock
    numberOfFish =getNumberOfFish()
    cohesion = getCohesion()
    seperation = getSeperation()
    alignment = getAlignment()
    speed = getSpeed()
    drawTail = getDrawTails()
    flock = Flock(screen, numberOfFish, cohesion, seperation, alignment, speed, drawTail)

# GUI
btnNewFlock = Button(screen, 45, 40, 100, 30, onClick=newFlock, text="Reset boids")
sldCohesion = Slider(screen, 200, 30, 120, 10) 
sldSeperation = Slider(screen, 200, 60, 120, 10) 
sldAlignment = Slider(screen, 200, 90, 120, 10) 
sldNumberOfFish = Slider(screen, 200, 120, 120, 10)
sldSpeed = Slider(screen, 200, 150, 120, 10)
tglDrawTail = Toggle(screen, 50, 105, 22, 17)

def getCohesion():
    return round(sldCohesion.value/100+0.5, 2)

def getSeperation():
    return round(sldSeperation.value/100+0.5, 2)

def getAlignment():
    return round(sldAlignment.value/100+0.5, 2)

def getNumberOfFish():
    return int(sldNumberOfFish.value*2)

def getSpeed():
    return round(sldSpeed.value*0.1, 2)

def getDrawTails():
    return tglDrawTail.value

def blitText(text: str, pos: tuple):
    textRendered = font.render(text, True, (0, 0, 0))
    screen.blit(textRendered, pos)

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill("beige")
    
    if type(flock) == Flock:
        flock.update()

    blitText("Cohesion", (330, 20))
    blitText("Seperation", (330, 50))
    blitText("Alignment", (330, 80))
    blitText("NumberOfFish", (330, 110))
    blitText("Speed", (330, 140))
    blitText("Tails", (90, 100))

    blitText(str(getCohesion()), (460, 20))
    blitText(str(getSeperation()), (460, 50))
    blitText(str(getAlignment()), (460, 80))
    blitText(str(getNumberOfFish()), (460, 110))
    blitText(str(getSpeed()), (460, 140))

    pygame_widgets.update(events)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
