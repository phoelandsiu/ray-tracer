import sys
import os
import pytest

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from core.matrices import Matrix
from core.tuples import Tuple

@pytest.fixture
def setup_matrix():
    """Fixture to set up a matrix for testing."""
    rows = 4
    cols = 4
    matrix = Matrix(rows, cols)
    return matrix

def test_4x4_matrix(setup_matrix):
    """Test the initialization of a matrix."""
    m = setup_matrix
    assert m.rows == 4
    assert m.cols == 4
    assert m[0][0] == 0

    m.set_values([[1, 2, 3, 4],
                    [5.5, 6.5, 7.5, 8.5],
                    [9, 10, 11, 12],
                    [13.5, 14.5, 15.5, 16.5]])

    assert m[0][0] == 1
    assert m[0][3] == 4
    assert m[1][0] == 5.5
    assert m[1][2] == 7.5
    assert m[2][0] == 9
    assert m[2][2] == 11
    assert m[3][0] == 13.5
    assert m[3][2] == 15.5

def test_3x3_matrix():
    """Tests the initialization of a 3x3 matrix."""
    m = Matrix(3, 3)
    assert m.rows == 3
    assert m.cols == 3
    assert m[0][0] == 0
    assert m[1][1] == 0
    assert m[2][2] == 0

    m.set_values([[-3, 5, 0],
                [1, -2, 0],
                [0, 0, 1]])

    assert m[0][0] == -3
    assert m[1][1] == -2
    assert m[2][2] == 1

def test_2x2_matrix():
    """Tests the initialization of a 3x3 matrix."""
    m = Matrix(2,2)
    assert m.rows == 2
    assert m.cols == 2
    assert m[0][0] == 0
    assert m[1][1] == 0

    m.set_values([[-3, 5],
                [1, -2]])

    assert m[0][0] == -3
    assert m[0][1] == 5
    assert m[1][0] == 1
    assert m[1][1] == -2

def test_matrix_equality():
    """Tests the equality of two matrices."""
    m1 = Matrix(4, 4)
    m2 = Matrix(4, 4)

    m1.set_values([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 8, 7, 6],
                    [5, 4, 3, 2]])
    
    m2.set_values([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 8, 7, 6],
                    [5, 4, 3, 2]])
    
    assert m1.compare(m2) == True
    assert m2.compare(m1) == True

def test_matrix_multiply():
    """Tests the multiplication of two matrices."""
    m1 = Matrix(4, 4)
    m2 = Matrix(4, 4)
    m3 = Matrix(4, 4)

    m1.set_values([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 8, 7, 6],
                    [5, 4, 3, 2]])
    
    m2.set_values([[-2, 1, 2, 3],
                    [3, 2, 1, -1],
                    [4, 3, 6, 5],
                    [1, 2, 7, 8]])
    
    m3.set_values([[20, 22, 50, 48],
                    [44, 54, 114, 108],
                    [40, 58, 110, 102],
                    [16, 26, 46, 42]])
    
    result = m1.multiply(m2)
    assert result.compare(m3) == True

def test_matrix_tuple_multiply():
    """Tests the multiplication of a matrix by a tuple."""
    m = Matrix(4, 4)
    t = Tuple(1,2,3,1)
    m.set_values([[1, 2, 3, 4],
                    [2, 4, 4, 2],
                    [8, 6, 4, 1],
                    [0, 0, 0, 1]])
    
    result = m.tuple_multiply(t)
    
    m2 = Matrix(4, 1)
    m2.set_values([[18],
                    [24],
                    [33],
                    [1]])
    
    assert result.compare(m2) == True

def test_identity_matrix():
    """Tests the creation of an identity matrix."""
    m = Matrix.identity(4)
    assert m.rows == 4
    assert m.cols == 4
    assert m[0][0] == 1
    assert m[1][1] == 1
    assert m[2][2] == 1
    assert m[3][3] == 1

    # Check non-diagonal elements
    assert m[0][1] == 0
    assert m[1][0] == 0
    assert m[2][3] == 0
    assert m[3][2] == 0