from vector import Vector2d
import pygame
from random import choice, random
from math import cos, sin, pi

class Fish:
    def __init__(self, pos: Vector2d, velo: Vector2d, color: tuple[float, float, float], drawTail: bool):
        self.velo = velo
        self.pos = pos
        self.speed = velo.getLen()
        self.color = color
        self.__trail = []
        self.nearbyFish = []
        self.maxDist = 50
        self.drawTail = drawTail

    def draw(self, screen: pygame.Surface):
        # tegn en trekant der peger i retningen af fiskens fartvektor
        arrowWidth = 8
        arrowLength = 14
        polygonVectors = [
            Vector2d.add2(self.pos, self.velo.perpendicular().normalized(arrowWidth/2)),
            Vector2d.add2(self.pos, self.velo.perpendicular().normalized(arrowWidth/2).negated()),
            Vector2d.add2(self.pos, self.velo.normalized(arrowLength))
        ]
        polygonPoints = [(v.getX(), v.getY()) for v in polygonVectors]
        pygame.draw.polygon(screen, [int(i*255) for i in self.color], polygonPoints)
        
        if self.drawTail:
            # tegn hale lavet af linjer mellem fiskens 10 seneste positioner
            self.__trail.append((self.pos.getX(), self.pos.getY()))
            if len(self.__trail) > 8:
                self.__trail.pop(0)
            if len(self.__trail) > 1:
                pygame.draw.lines(screen, [int(i*255) for i in self.color], False, self.__trail, 3)

    def update(self, group: list, screen: pygame.Surface):
        self.nearbyFish = self.getNearbyFish(group, self.maxDist)
        self.pos.add(self.velo)

        # bouce on edge
        if self.pos.getX() > screen.get_width() and self.velo.getX() > 0:
            self.velo.setX(self.velo.getX() * -1)

        if self.pos.getY() > screen.get_height() and self.velo.getY() > 0:
            self.velo.setY(self.velo.getY() * -1)

        if self.pos.getX() < 0 and self.velo.getX() < 0:
            self.velo.setX(self.velo.getX() * -1)

        if self.pos.getY() < 0 and self.velo.getY() < 0:
            self.velo.setY(self.velo.getY() * -1)
    
    def getNearbyFish(self, group: list, maxDist: float):
        nearby = []
        for other in group:
            if other != self:
                distVector = Vector2d()
                distVector.setX(other.pos.getX()-self.pos.getX())
                distVector.setY(other.pos.getY()-self.pos.getY())
                dist = distVector.getLen()
                if dist <= maxDist:
                    nearby.append(other)
        return nearby


class Pray(Fish):
    def __init__(self, pos, velo, color, cohesion, seperation, alignment, drawTail):
        super().__init__(pos, velo, color, drawTail)
        self.cohesionMult = cohesion
        self.seperationMult = seperation
        self.alignmentMult = alignment

    def update(self, group: list, screen: pygame.Surface):
        super().update(group, screen)
        
        behaviourForce = Vector2d()
        behaviourForce.add(self.seperation().multiplied(self.seperationMult))
        behaviourForce.add(self.alignment().multiplied(self.alignmentMult))
        behaviourForce.add(self.cohesion().multiplied(self.cohesionMult))

        self.velo.add(behaviourForce)
        self.velo.normalize(self.speed)

    def seperation(self):
        force = Vector2d()
        for f in self.nearbyFish:
            diffVector = Vector2d(self.pos.getX() - f.pos.getX(), self.pos.getY() - f.pos.getY())
            dist = diffVector.getLen()
            if dist > 0:
                force.add(diffVector.multiplied(1/dist**2))
        return force.normalized()

    def alignment(self):
        force = Vector2d()
        for f in self.nearbyFish:
            force.add(f.velo.multiplied(1/len(self.nearbyFish)))
        return Vector2d(force.getX()-self.velo.getX(), force.getY()-self.velo.getY()).normalized()

    def cohesion(self):
        force = Vector2d()
        if len(self.nearbyFish) > 0:
            for f in self.nearbyFish:
                force.add(f.pos.multiplied(1/len(self.nearbyFish)))
            return Vector2d(force.getX()-self.pos.getX(), force.getY()-self.pos.getY()).normalized()
        else:
            return force


class Flock:
    def __init__(self, 
                 screen: pygame.Surface, 
                 numberOfFish: int,
                 cohesion: float,
                 seperation: float,
                 alignment: float,
                 speed: float,
                 drawTail: bool):
    
        self.screen = screen
        self.flock = [Pray(self.__randomVector(), self.__randomVelo(speed), (1, 0, 0), cohesion, seperation, alignment, drawTail) for _ in range(numberOfFish)]
    
    def __randomVector(self):
        return Vector2d(random() * self.screen.get_width(), random() * self.screen.get_height())
    
    def __randomVelo(self, speed):
        angle = random() * 2 * pi
        xVelo = sin(angle) * speed
        yVelo = cos(angle) * speed
        return Vector2d(xVelo, yVelo)
    
    def update(self):
        for f in self.flock:
            f.update(self.flock, self.screen)
            f.draw(self.screen)
