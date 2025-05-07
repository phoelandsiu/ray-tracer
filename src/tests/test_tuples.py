import sys
import os
import pytest

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from core.tuples import Point, Vector, Tuple, Projectile, Environment, Color

@pytest.fixture
def setup():
    """
    Fixture to set up test data for the tests.
    Returns:
        A tuple containing two points, a vector, and another point.
    """
    p1 = Point(3, -2, 5)
    p2 = Vector(-2, 3, 1)
    p3 = Point(3, 2, 1)
    p4 = Point(5, 6, 7)
    return p1, p2, p3, p4

def test_tuple_add(setup):
    """Test the addition of tuples."""
    p1, p2, p3, p4 = setup
    # Test 1: Normal add 
    assert p1.add(p2) == Point(1, 1, 6)

def test_tuple_subtract(setup):
    """Test the subtraction of tuples."""
    p1, p2, p3, p4 = setup
    # Test 1: Subtract two points
    assert p3.subtract(p4) == Vector(-2, -4, -6)

    # Test 2: Subtract vector from point
    p5 = Vector(5, 6, 7)
    assert p3.subtract(p5) == Point(-2, -4, -6)

    # Test 3: Subtracting two vectors
    p6 = Vector(3, 2, 1)
    assert p6.subtract(p5) == Vector(-2, -4, -6)

    # Test 4: Subtract point from vector
    with pytest.raises(TypeError, match="Cannot subtract a Point from a Vector"):
        p2.subtract(p1)

def test_tuple_negate(setup):
    """Test the negation of tuples."""
    p1, p2, p3, p4 = setup
    # Test 1: Negate a point
    assert p1.negate() == Point(-3, 2, -5)

    # Test 2: Negate a vector
    assert p2.negate() == Vector(2, -3, -1)

def test_tuple_multiply(setup):
    """Test the multiplication of tuples."""
    p1 = Tuple(1, -2, 3, -4)
    # Test 1: Multiply a tuple
    assert p1.multiply(3.5) == Tuple(3.5, -7, 10.5, -14)

    # Test 2: Multiplying a tuple by a fraction
    assert p1.multiply(0.5) == Tuple(0.5, -1, 1.5, -2)

def test_tuple_divide(setup):
    """Test the division of tuples."""
    p1 = Tuple(1, -2, 3, -4)
    # Test 1: Divide a tuple
    assert p1.divide(2) == Tuple(0.5, -1, 1.5, -2)

def test_tuple_magnitude(setup):
    """Test the magnitude of tuples."""
    p1 = Vector(1, 0, 0)
    p2 = Vector(0, 1, 0)
    p3 = Vector(0, 0, 1)
    p4 = Vector(1, 2, 3)
    p5 = Vector(-1, -2, -3)
    # Test 1: Magnitude of x-axis unit vector
    assert p1.magnitude() == 1

    # Test 2: Magnitude of y-axis unit vector
    assert p2.magnitude() == 1

    # Test 3: Magnitude of z-axis unit vector
    assert p3.magnitude() == 1

    # Test 4: Magnitude of a positive vector
    assert p4.magnitude() == 14**0.5

    # Test 5: Magnitude of a negative vector
    assert p5.magnitude() == 14**0.5

def test_tuple_normalize(setup):
    """Test the normalization of tuples."""
    p1 = Vector(4, 0, 0)
    p2 = Vector(1, 2, 3)
    # Test 1: Normalize x-axis unit vector
    assert p1.normalize() == Vector(1, 0, 0)

    # Test 2: Normalize vector
    assert p2.normalize() == Vector(1/14**0.5, 2/14**0.5, 3/14**0.5)

def test_tuple_dot(setup):
    """Test the dot product of tuples."""
    p1 = Vector(1, 2, 3)
    p2 = Vector(2, 3, 4)
    # Test 1: Dot product of two vectors
    assert p1.dot(p2) == 20

def test_tuple_cross(setup):
    """Test the cross product of tuples."""
    p1 = Vector(1, 2, 3)
    p2 = Vector(2, 3, 4)
    # Test 1: Cross product of two vertices
    assert p1.cross(p2) == Vector(-1, 2, -1)
    assert p2.cross(p1) == Vector(1, -2, 1)

def test_tuple_tick(setup):
    """Test the tick function of tuples."""
    projectile = Projectile(Point(0,1,0), Vector(1,1,0).normalize())
    environment = Environment(Vector(0,-0.1,0), Vector(-0.01,0,0))
    tick = Tuple.tick(environment, projectile)
    print(tick.position)

def test_color_tuple():
    """Test the color tuple."""
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    # Test 1: Add two colors
    assert c1.add(c2) == Color(1.6, 0.7, 1.0)
    # Test 2: Subtract two colors
    assert c1.subtract(c2) == Color(0.2, 0.5, 0.5)
    # Test 3: Multiply a color by a scalar
    assert c1.multiply(2) == Color(1.8, 1.2, 1.5)
    # Test 4: Multiply two colors
    assert c1.multiply_color(c2) == Color(0.63, 0.06, 0.1875)

if __name__=="__main__":
    pytest.main()