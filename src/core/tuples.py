class Tuple:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def add(self, other):
        if not isinstance(other, Tuple):
            raise TypeError("Can only add another Tuple")
        result = Tuple(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
        if result.w == 1.0 or result.w == 2.0:
            return Point(result.x, result.y, result.z)
        elif result.w == 0.0:
            return Vector(result.x, result.y, result.z)
        else:
            return result

    def subtract(self, other):
        if not isinstance(other, Tuple):
            raise TypeError("Can only subtract another Tuple")
        if self.is_vector() and other.is_point():
            raise TypeError("Cannot subtract a Point from a Vector")
        if self.w == 0.0 and other.w == 0.0:
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        if self.w == 1.0 and other.w == 0.0:
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        if self.w == 1.0 and other.w == 1.0:
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        if self.w == 0.0 and other.w == 1.0:
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        
    def negate(self):
        if self.is_point():
            return Point(-self.x, -self.y, -self.z)
        elif self.is_vector():
            return Vector(-self.x, -self.y, -self.z)
        else:
            return Tuple(-self.x, -self.y, -self.z, -self.w)

    def is_point(self):
        return self.w == 1.0
    
    def is_vector(self):
        return self.w == 0.0

    def __eq__(self, other):
        if not isinstance(other, Tuple):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

class Point(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1.0)

class Vector(Tuple):
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0.0)