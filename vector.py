from math import sqrt, pow
import pygame

class Vector2d:
    """
    Vector2d
    --------

    Vector2d klassen indeholder metoderne relevante til at arbejde med vektorer i to dimensioner.

    """
    def __init__(self, x=0.0, y=0.0, color=(0.0, 0.0, 0.0), width=5, name="Vector"):
        """
        Instantieres en vektor uden argumenter, vil en nulvektor med \n
        predefineret navn, farve og bredde oprettes.
        """
        self.__x = x
        self.__y = y
        self.__color = color
        self.__width = width
        self.__name = name

    def getX(self):
        """
        Returnerer x-værdien for vektoren.
        """
        return self.__x
    
    def getY(self):
        """
        Returnerer y-værdien for vektoren.
        """
        return self.__y
    
    def getColor(self):
        """
        Returnerer vektorens farve.
        """
        return self.__color
    
    def getWidth(self):
        """
        Returnerer vektorens bredde.
        """
        return self.__width
    
    def getName(self):
        """
        Returnerer vektorens navn.
        """
        return self.__name

    def setX(self, newX: float):
        """
        Sætter x-værdien for vektoren.
        """
        self.__x = newX

    def setY(self, newY: float):
        """
        Sætter y-værdien for vektoren.
        """
        self.__y = newY

    def setColor(self, newColor: tuple):
        """
        Sætter farven på vektoren. Relevant når man vil tegne vektoren på skærmen.
        """
        self.__color = newColor

    def setWidth(self, newWidth: int):
        """
        Sætter bredden på vektoren. Relevant når man vil tegne vektoren på skærmen.
        """
        self.__width = newWidth
    
    def setName(self, newName: str):
        """
        Sætter navnet på vektoren. Relevant når man vil tegne vektoren på skærmen.
        """
        self.__name = newName

    def copy(self):
        """
        Returnerer en kopi af vektoren, med ens x- og y-koordinater, farve, bredde og navn.
        """
        return Vector2d(self.__x, self.__y, self.__color, self.__width, self.__name)

    def add(self, v):
        """
        Lægger x- og y-koordinaterne af vectoren v til vektoren.
        """
        self.setX(self.getX()+v.getX())
        self.setY(self.getY()+v.getY())
    
    def add2(v1, v2):
        """
        Returnerer en vektor der svarer til vektorsummen af vektorene v1 og v2.
        """
        return Vector2d(x=v1.getX()+v2.getX(), y=v1.getY()+v2.getY())
    
    def multiply(self, mult):
        """
        Ganger vektorens x- og y-koordinater med værdien 'mult'.
        """
        self.setX(self.getX()*mult)
        self.setY(self.getY()*mult)

    def multiplied(self, mult):
        """
        Returnerer en ny vektor tilsvarende til den originale vektor ganget med mult.
        """
        copy = self.copy()
        copy.multiply(mult)
        return copy

    
    def dot(self, v1, v2):
        """
        Returnerer prikproduktet (skalarproduktet) af vektorerne v1 og v2.
        """
        return v1.getX() * v2.getX() + v1.getY() * v2.getY()
    
    def det(self, v1, v2):
        """
        Returnerer determinanten af vektorerne v1 og v2.
        """
        return v1.getX() * v2.getY() - v1.getY() * v2.getX()
    
    def getLen(self):
        """
        Returnerer den eksakte længde af vektoren.
        """
        return sqrt(pow(self.getX(), 2) + pow(self.getY(), 2))
    
    def getLenApprox(self):
        """
        Returnerer den tilnærmede længde af vektoren (Manhattan afstand). \n
        Denne metode til at finde afstanden er hurtigere en getLen, men giver en forholdsvis upræcis afstand. \n
        Manhattanafstanden har dog fordelen af stadig at være sammenlignelig.
        """
        return abs(self.getX()) + abs(self.getY())
    
    def normalize(self, len=1.0):
        """
        Normaliserer vektoren til længden 'len'. Standard værdien for 'len' er 1.
        """
        if self.getLen() != 0:
            self.multiply(len/self.getLen())

    def normalized(self, len=1.0):
        """
        Returnerer den normaliseret vektor med længden 'len'. \n
        Ændrer ikke på den originale vektor.
        """
        copy = self.copy()
        copy.normalize(len)
        return copy
    
    def negate(self):
        """
        Modsætter retningen af vektoren.
        """
        self.multiply(-1)

    def negated(self):
        """
        Returnerer den modsatte vektor uden at ændre den originale vektor.
        """
        copy = self.copy()
        copy.negate()
        return copy
    
    def isEqual(self, v):
        """
        Returnerer om vektoren har samme koordinater som vektoren v.
        """
        return self.getX() == v.getX() and self.getY() == v.getY()

    def isParallel(self, v):
        """
        Returnerer om vektoren er parallel med vektor v eller ej.
        """
        return self.normalized().isEqual(v.normalized())
    
    def isPerpendicular(self, v):
        """
        Returnerer om vektoren er vinkelret på vektor v eller ej.
        """
        return self.dot(self, v) == 0
    
    def perpendicular(self):
        """
        Returnerer den vinkelrette vektor til vektoren.
        """
        return Vector2d(-self.getY(), self.getX())
        
    
    def isOpposite(self, v):
        """
        Returnerer om vektoren har modsat retning til vektor v eller ej.
        """
        return self.negated().normalized().isEqual(v.normalized())

    def toString(self):
        """
        Returnerer en streng indeholdende vektorens koordinater.
        """
        return f"[{self.getX()}, {self.getY()}]"

    def draw(self, surface, X, Y):
        """
        Tegner vektoren med startpunkt i (X, Y)
        """
        color255 = (int(self.getColor()[0]*255), int(self.getColor()[1]*255), int(self.getColor()[2]*255))
        pygame.draw.line(surface, color255, (X, Y), (X+self.getX(), Y+self.getY()), self.getWidth())

