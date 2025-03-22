import sys
import os
import pytest

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from core.tuples import Point, Vector, Tuple

@pytest.fixture
def setup():
    p1 = Point(3, -2, 5)
    p2 = Vector(-2, 3, 1)
    p3 = Point(3, 2, 1)
    p4 = Point(5, 6, 7)
    return p1, p2, p3, p4

def test_tuple_add(setup):
    p1, p2, p3, p4 = setup
    # Test 1: Normal add 
    assert p1.add(p2) == Point(1, 1, 6)

def test_tuple_subtract(setup):
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
    p1, p2, p3, p4 = setup
    # Test 1: Negate a point
    assert p1.negate() == Point(-3, 2, -5)

    # Test 2: Negate a vector
    assert p2.negate() == Vector(2, -3, -1)

def test_tuple_multiply(setup):
    p1 = Tuple(1, -2, 3, -4)
    # Test 1: Multiply a tuple
    assert p1.multiply(3.5) == Tuple(3.5, -7, 10.5, -14)

    # Test 2: Multiplying a tuple by a fraction
    assert p1.multiply(0.5) == Tuple(0.5, -1, 1.5, -2)

def test_tuple_divide(setup):
    p1 = Tuple(1, -2, 3, -4)
    # Test 1: Divide a tuple
    assert p1.divide(2) == Tuple(0.5, -1, 1.5, -2)

def test_tuple_magnitude(setup):
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
    p1 = Vector(4, 0, 0)
    p2 = Vector(1, 2, 3)
    # Test 1: Normalize x-axis unit vector
    assert p1.normalize() == Vector(1, 0, 0)

    # Test 2: Normalize vector
    assert p2.normalize() == Vector(1/14**0.5, 2/14**0.5, 3/14**0.5)

def test_tuple_dot(setup):
    p1 = Vector(1, 2, 3)
    p2 = Vector(2, 3, 4)
    # Test 1: Dot product of two vectors
    assert p1.dot(p2) == 20

if __name__=="__main__":
    pytest.main()