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
    return p1, p2

def test_tuple_add(setup):
    p1, p2 = setup
    # Test 1: Normal add 
    assert p1.add(p2) == Point(1, 1, 6)

def test_tuple_subtract(setup):
    p1, p2 = setup
    # Test 2: Illegal subtract
    with pytest.raises(TypeError, match="Cannot subtract a Point from a Vector"):
        p2.subtract(p1)

def test_tuple_negate(setup):
    p1, p2 = setup
    # Test 3: Negate
    assert p1.negate() == Point(-3, 2, -5)

if __name__=="__main__":
    pytest.main()