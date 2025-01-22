from vector import Vector2d
import pygame
from random import choice

class Fish:
    def __init__(self, pos: Vector2d, velo: Vector2d, color: tuple[float, float, float]):
        self.velo = velo
        self.pos = pos
        self.speed = velo.getLen()
        self.color = color
        self.__trail = []
        self.__nearbyFish = []
        self.maxDist = 150

    def draw(self, screen: pygame.Surface):
        # tegn en trekant der peger i retningen af fiskens fartvektor
        arrowWidth = 12
        arrowLength = 18
        polygonVectors = [
            Vector2d.add2(self.pos, self.velo.perpendicular().normalized(arrowWidth/2)),
            Vector2d.add2(self.pos, self.velo.perpendicular().normalized(arrowWidth/2).negated()),
            Vector2d.add2(self.pos, self.velo.normalized(arrowLength))
        ]
        polygonPoints = [(v.getX(), v.getY()) for v in polygonVectors]
        pygame.draw.polygon(screen, [int(i*255) for i in self.color], polygonPoints)

        # tegn hale lavet af linjer mellem fiskens 10 seneste positioner
        self.__trail.append((self.pos.getX(), self.pos.getY()))
        if len(self.__trail) > 10:
            self.__trail.pop(0)
        if len(self.__trail) > 1:
            pygame.draw.lines(screen, [int(i*255) for i in self.color], False, self.__trail, 3)

    def update(self, group: list):
        self.__nearbyFish = self.getNearbyFish(group, self.maxDist)
        self.pos.add(self.velo)
    
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