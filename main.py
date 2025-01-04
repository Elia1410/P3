class Vector:
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
    
    def add2(v1, v2):
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


v1 = Vector(10, 5, name="My Vector")
v2 = Vector(2, 2)
v3 = Vector.add2(v1, v2)

print(f"v1: [{v1.getX()}, {v1.getY()}]")
print(f"v2: [{v2.getX()}, {v2.getY()}]")
print(f"v3: [{v3.getX()}, {v3.getY()}]")