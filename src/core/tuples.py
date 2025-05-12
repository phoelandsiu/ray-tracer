class Tuple:
    def __init__(self, x, y, z, w):
        """
        Initializes a Tuple object with x, y, z coordinates and a w component.
        Args:
            x: The x coordinate.
            y: The y coordinate.
            z: The z coordinate.
            w: The w component (1.0 for points, 0.0 for vectors).
        """
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def add(self, other):
        """
        Returns a new Tuple representing the sum of two Tuples.
        If the Tuple is a Point, it returns a Point with the sum of coordinates.
        If the Tuple is a Vector, it returns a Vector with the sum of coordinates.
        If the Tuple is a generic Tuple, it returns a new Tuple with the sum of coordinates.
        Args:
            other: Another Tuple object to add to this Tuple.
        Returns:
            A new Tuple with the sum of coordinates.
        Raises:
            TypeError: If the other object is not a Tuple."""
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
        """
        Returns a new Tuple representing the difference between two Tuples.
        If the Tuple is a Point, it returns a Point with the difference of coordinates.
        If the Tuple is a Vector, it returns a Vector with the difference of coordinates.
        If the Tuple is a generic Tuple, it returns a new Tuple with the difference of coordinates.
        Args:
            other: Another Tuple object to subtract from this Tuple.
        Returns:
            A new Tuple with the difference of coordinates.
        Raises:
            TypeError: If the other object is not a Tuple.
        """
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
        """
        Returns a new Tuple with each component negated.
        If the Tuple is a Point, it returns a Point with negated coordinates.
        If the Tuple is a Vector, it returns a Vector with negated coordinates.
        If the Tuple is a generic Tuple, it returns a new Tuple with negated coordinates."""
        if self.is_point():
            return Point(-self.x, -self.y, -self.z)
        elif self.is_vector():
            return Vector(-self.x, -self.y, -self.z)
        else:
            return Tuple(-self.x, -self.y, -self.z, -self.w)
        
    def multiply(self, scalar):
        """
        Returns a new Tuple with each component multiplied by the scalar.
        Args:
            scalar: A float to multiply each component of the Tuple.
        Returns:
            A new Tuple with each component multiplied by the scalar.
        """
        return Tuple(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)
    
    def divide(self, scalar):
        """
        Returns a new Tuple with each component divided by the scalar.
        Args:
            scalar: A float to divide each component of the Tuple.
        Returns:
            A new Tuple with each component divided by the scalar.
        """
        return Tuple(self.x / scalar, self.y / scalar, self.z / scalar, self.w / scalar)
    
    def magnitude(self):
        """
        Returns the magnitude (length) of the vector.
        The magnitude is calculated as the square root of the sum of the squares of its components.
        """
        return (self.x**2 + self.y**2 + self.z**2 + self.w**2)**0.5

    def normalize(self):
        """
        Returns a normalized version of the vector.
        Normalization means converting the vector to a unit vector (length of 1).
        """
        mag = self.magnitude()
        return Tuple(self.x / mag, self.y / mag, self.z / mag, self.w / mag)

    def dot(self, other):
        """
        Returns the dot product of two vectors.
        Args:
            other: Another Vector object.
        Returns:
            A float representing the dot product.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w
    
    def cross(self, other):
        """
        Returns the cross product of two vectors.
        Args:
            other: Another Vector object.
        Returns:
            A new Vector object representing the cross product.
        """
        return Vector(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y - self.y*other.x)
    
    def is_point(self):
        """
        Returns True if the Tuple is a point (w = 1.0), False otherwise.
        """
        return self.w == 1.0
    
    def is_vector(self):
        """
        Returns True if the Tuple is a vector (w = 0.0), False otherwise.
        """
        return self.w == 0.0

    def __eq__(self, other):
        """
        Compares two Tuple objects for equality.
        Args:
            other: Another Tuple object to compare with.
        Returns:
            True if the Tuples are equal, False otherwise.
        """ 
        if not isinstance(other, Tuple):
            return False
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w
    
    def __len__(self):
        """
        Returns the number of components in the Tuple.
        """
        return 4
    
    def __getitem__(self, index):
        """
        Returns the component at the given index.
        Args:
            index: An integer index (0, 1, 2, or 3).
        Returns:
            The component at the given index.
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= 4:
            raise IndexError("Index out of range")
        return [self.x, self.y, self.z, self.w][index]
    
    def __setitem__(self, index, value):
        """
        Sets the component at the given index.
        Args:
            index: An integer index (0, 1, 2, or 3).
            value: The value to set at the given index.
        Raises:
            IndexError: If the index is out of range.
        """
        if index < 0 or index >= 4:
            raise IndexError("Index out of range")
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        elif index == 3:
            self.w = value

class Point(Tuple):
    """
    Represents a point in 3D space.
    Inherits from the Tuple class.
    """
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1.0)

class Vector(Tuple):
    """
    Represents a vector in 3D space.
    Inherits from the Tuple class.
    """
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0.0)

class Projectile():
    """
    Represents a projectile in motion.
    Contains position and velocity vectors.
    """
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def tick(self, env, proj):
        """
        Updates the position and velocity of a projectile after one time step, 
        given the environmental forces of gravity and wind.
        Args:
            env: An object with gravity and wind vectors.
            proj: A Projectile object with position and velocity vectors.
        Returns:
            A new Projectile with updated position and velocity.
        """
        position = Point(proj.position.x + proj.velocity.x, proj.position.y + proj.velocity.y, proj.position.z + proj.velocity.z)
        velocity = Vector(proj.velocity.x + env.wind.x, proj.velocity.y + env.gravity.y, proj.velocity.z + env.gravity.z)
        return Projectile(position, velocity)

class Environment():
    """
    Represents the environment in which a projectile moves.
    Contains gravitational and wind forces.
    """
    def __init__(self, gravity, wind):
        self.gravity = gravity
        self.wind = wind

class Color(Tuple):
    """
    Represents a color in RGB space.
    Contains red, green, and blue components.
    """
    def __init__(self, red, green, blue):
        super().__init__(red, green, blue, 0.0)

    def add(self, other):
        """
        Returns a new Color representing the sum of two Colors.
        Args:
            other: Another Color object to add to this Color.
        Returns:
            A new Color with the sum of components.
        """
        return Color(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def subtract(self, other):
        """
        Returns a new Color representing the difference between two Colors.
        Args:
            other: Another Color object to subtract from this Color.
        Returns:
            A new Color with the difference of components.
        """
        return Color(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def multiply(self, scalar):
        """
        Returns a new Color with each component multiplied by the scalar.
        Args:
            scalar: A float to multiply each component of the Color.
        Returns:
            A new Color with each component multiplied by the scalar.
        """
        return Color(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def multiply_color(self, other):
        """
        Returns a new Color representing the product of two Colors.
        This is called the Hadamard (or Schur) product.
        Args:
            other: Another Color object to multiply with this Color.
        Returns:
            A new Color with the product of components.
        """
        return Color(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def __eq__(self, other):
        """
        Compares two Color objects for equality.
        Args:
            other: Another Color object to compare with.
        Returns:
            True if the Colors are equal, False otherwise.
        """ 
        if not isinstance(other, Color):
            return False
        return (self.x - other.x < 1e-5) and (self.y - other.y < 1e-5) and (self.z - other.z < 1e-5) and (self.w - other.w < 1e-5)
    