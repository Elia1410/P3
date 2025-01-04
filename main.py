class Vector:
    '''
    Vector
    ======

    setX(float): sæt værdien af vektorens x-koordinat

    setY(float): sæt værdien af vektorens y-koordinat
    
    getX(): returner x-værdien

    getY(): returner y-værdien 

    setColor(3-tuple): sæt farven på vektoren
    
    setWidth(float): sæt bredden på vektoren

    setName(string): sæt navnet på vektoren

    add(v1): adder en vektor til vektoren

    add2(v1, v2): returner vektorsummen af 2 vektorer

    '''
    def __init__(self, x=0.0, y=0.0, color=(0, 0, 0), width=5, name="Vector"):
        self.setX(x)
        self.setY(y)
        self.setColor(color)
        self.setWidth(width)

        self.setName(name)

    def getX(self):
        return self.__x__
    
    def getY(self):
        return self.__y__

    def setX(self, newX: float):
        self.__x__ = newX

    def setY(self, newY: float):
        self.__y__ = newY

    def setColor(self, newColor: tuple):
        self.__color__ = newColor

    def setWidth(self, newWidth: float):
        self.__width__ = newWidth
    
    def setName(self, newName: str):
        self.__name__ = newName

    def add(self, v2):
        self.setX(self.getX()+v2.getX())
        self.setX(self.getY()+v2.getY())
    
    def add2(self, v1, v2):
        return Vector(x=v1.getX()+v2.getX(), y=v1.getY()+v2.getY())
    
    def dot(self, v1, v2):
        return v1.getX() * v2.getX() + v1.getY() * v2.getY()
    
    def det(self, v1, v2):
        return v1.getX() * v2.getY() - v1.getY() * v2.getX()
    
    def getLen(self):
        return (self.getX()**2 + self.getY()**2)**0.5
    
    def normalize(self, len=1.0):
        self.setX(self.getX()/self.getLen()*len)
        self.setY(self.getY()/self.getLen()*len)
    