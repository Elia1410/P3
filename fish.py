from vector import Vector2d
import pygame

class Fish:
    def __init__(self, x: float, y: float, color: tuple[int, int, int]):
        self.velo = Vector2d(0, 0)
        self.pos = Vector2d(x, y)
        self.color = color
        self.__trail = []

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
        pygame.draw.polygon(screen, self.color, polygonPoints)

        # tegn hale lavet af linjer mellem 10 fiskens seneste positioner
        self.__trail.append((self.pos.getX(), self.pos.getY()))
        if len(self.__trail) > 10:
            self.__trail.pop(0)
        if len(self.__trail) > 1:
            pygame.draw.lines(screen, self.color, False, self.__trail, 3)

        
        

    def update(self):

        # temp kode til at følge musen
        mousePos = pygame.mouse.get_pos()
        self.velo.setX(self.pos.getX()-mousePos[0])
        self.velo.setY(self.pos.getY()-mousePos[1])
        self.velo.normalize(5)
        self.velo.negate()

        self.pos.add(self.velo)