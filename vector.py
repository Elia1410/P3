from math import sqrt, pow

class Vector2d:
    """
    Vector2d
    ======

    Vector2d klassen indeholder metoderne relevante til at arbejde med vektorer i to dimensioner.
    
    """
    def __init__(self, x=0.0, y=0.0, color=(0, 0, 0), width=5, name="Vector"):
        """
        Instantieres en vektor uden argumenter, vil en nulvektor med \n
        predefineret navn farve og bredde oprettes.
        """
        self.setX(x)
        self.setY(y)
        self.setColor(color)
        self.setWidth(width)
        self.setName(name)

    def getX(self):
        """
        Returnerer x-værdien for vektoren.
        """
        return self.__x__
    
    def getY(self):
        """
        Returnerer y-værdien for vektoren.
        """
        return self.__y__
    
    def getColor(self):
        """
        Returnerer vektorens farve.
        """
        return self.__color__
    
    def getWidth(self):
        """
        Returnerer vektorens bredde.
        """
        return self.__width__
    
    def getName(self):
        """
        Returnerer vektorens navn.
        """
        return self.__name__

    def setX(self, newX: float):
        """
        Sætter x-værdien for vektoren.
        """
        self.__x__ = newX

    def setY(self, newY: float):
        """
        Sætter y-værdien for vektoren.
        """
        self.__y__ = newY

    def setColor(self, newColor: tuple):
        """
        Sætter farven på vektoren. Relevant når man vil tegne vektoren på skærmen.
        """
        self.__color__ = newColor

    def setWidth(self, newWidth: float):
        """
        Sætter bredden på vektoren. Relevant når man vil tegne vektoren på skærmen.
        """
        self.__width__ = newWidth
    
    def setName(self, newName: str):
        """
        Sætter navnet på vektoren. Relevant når man vil tegne vektoren på skærmen.
        """
        self.__name__ = newName

    def copy(self):
        return Vector2d(self.__x__, self.__y__, self.__color__, self.__width__, self.__name__)

    def add(self, v):
        """
        Lægger x- og y-koordinaterne til vektoren.
        """
        self.setX(self.getX()+v.getX())
        self.setX(self.getY()+v.getY())
    
    def add2(v1, v2):
        """
        Returnerer en vektor der svarer til vektorsummen af vektorene v1 og v2.
        """
        return Vector2d(x=v1.getX()+v2.getX(), y=v1.getY()+v2.getY())
    
    def multiply(self, mult):
        self.setX(self.getX()*mult)
        self.setY(self.getY()*mult)
    
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
        Afstanden er dog sammenlignelig.
        """
        return abs(self.getX()) + abs(self.getY())
    
    def normalize(self, len=1.0):
        """
        Normaliserer vektoren til længden 'len'. Standard værdien for 'len' er 1.
        """
        self.setX(self.getX()/self.getLen()*len)
        self.setY(self.getY()/self.getLen()*len)

    def normalized(self, len=1.0):
        """
        Returnerer den normaliseret vektor med længden 'len'. \n
        Ændrer ikke på den originale vektor.
        """
        return self.copy().normalize(len)

    def isParallel(self, v):
        """
        Returnerer om vektoren er parallel med vektor v eller ej.
        """
        return self.det(self, v) == 0
    
    def isPerpendicular(self, v):
        """
        Returnerer om vektoren er vinkelret på vektor v eller ej.
        """
        return self.dot(self, v) == 0
    
    def isOpposite(self, v):
        """
        Returnerer om vektoren har modsat retning til vektor v eller ej
        """
        vNorm = v.normalized()
        selfNorm = self.normalized()
        return (vNorm.getX() - selfNorm.getX()*-1) + (vNorm.getY() - selfNorm.getY()*-1) == 0


if __name__ == "__main__":
    v1 = Vector2d(10, 5, name="My Vector")
    v2 = Vector2d(2, 2)
    v3 = Vector2d.add2(v1, v2)

    print(f"v1: [{v1.getX()}, {v1.getY()}] \t '{v1.getName()}'")
    print(f"v2: [{v2.getX()}, {v2.getY()}] \t '{v2.getName()}'")
    print(f"v3: [{v3.getX()}, {v3.getY()}] \t '{v3.getName()}'")
