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

def test_transpose(setup_matrix):
    """Tests the transposition of a matrix."""
    m = setup_matrix
    m.set_values([[0, 9, 3, 0],
                    [9, 8, 0, 8],
                    [1, 8, 5, 3],
                    [0, 0, 5, 8]])
    t = m.transpose()
    t1 = Matrix(4, 4)
    t1.set_values([[0, 9, 1, 0],
                    [9, 8, 8, 0],
                    [3, 0, 5, 5],
                    [0, 8, 3, 8]])
    assert t.compare(t1) == True
    assert m.compare(t.transpose()) == True

def test_transpose_identity():
    """Tests the transposition of an identity matrix."""
    m = Matrix.identity(4)
    assert m.transpose().compare(m) == True

def test_determinant_2x2():
    """Tests the determinant of a 2x2 matrix."""
    m = Matrix(2, 2)
    m.set_values([[1, 5],
                    [-3, 2]])
    assert m.determinant() == 17

    m.set_values([[1, 2],
                    [3, 4]])
    assert m.determinant() == -2

def test_submatrix(setup_matrix):
    """Tests the creation of a submatrix."""
    m = Matrix(3, 3)
    m.set_values([[1, 5, 0],
                    [-3, 2, 7],
                    [0, 6, -3]])
    sub = m.submatrix(0, 2)
    sub1 = Matrix(2, 2)
    sub1.set_values([[-3, 2],
                    [0, 6]])
    assert sub.compare(sub1) == True

    m = setup_matrix
    m.set_values([[-6, 1, 1, 6],
                  [-8, 5, 8, 6],
                  [-1, 0, 8, 2],
                  [-7, 1, -1, 1]])
    sub = m.submatrix(2, 1)
    sub1 = Matrix(3, 3)
    sub1.set_values([[-6, 1, 6],
                    [-8, 8, 6],
                    [-7, -1, 1]])
    assert sub.compare(sub1) == True

def test_minor():
    """Tests the calculation of the minor of a matrix."""
    m = Matrix(3, 3)
    m.set_values([[3, 5, 0], 
                 [2, -1, -7],
                 [6, -1, 5]])
    assert m.minor(1, 0) == 25

def test_cofactor():
    """Tests the calculation of the cofactor of a matrix."""
    m = Matrix(3, 3)
    m.set_values([[3, 5, 0], 
                 [2, -1, -7],
                 [6, -1, 5]])
    assert m.cofactor(0, 0) == -12
    assert m.cofactor(1, 0) == -25

def test_determinant_general(setup_matrix):
    """Tests the calculation of the determinant of a matrix."""
    m = Matrix(3, 3)
    m.set_values([[1, 2, 6], 
                  [-5, 8, -4], 
                  [2, 6, 4]])
    assert m.determinant() == -196

    m = setup_matrix
    m = Matrix(4, 4)
    m.set_values([[-2, -8, 3, 5],
                  [-3, 1, 7, 3],
                  [1, 2, -9, 6],
                  [-6, 7, 7, -9]])
    assert m.determinant() == -4071

def test_invertible():
    m = Matrix(4, 4)
    m.set_values([[-4, 2, -2, -3], 
                  [9, 6, 2, 6],
                  [0, -5, 1, -5],
                  [0, 0, 0, 0]])
    assert m.determinant() == 0
    with pytest.raises(ValueError):
        m.inverse()

    m.set_values([[6, 4, 4, 4], 
                  [5, 5, 7, 6],
                  [4, -9, 3, -7],
                  [9, 1, 7, -6]])
    assert m.determinant() == -2120
    assert m.inverse().determinant() == -1/2120

def test_inverse(setup_matrix):
    """Tests the calculation of the inverse of a matrix."""
    m = setup_matrix
    m.set_values([[-5, 2, 6, -8],
                  [1, -5, 1, 8],
                  [7, 7, -6, -7],
                  [1, -3, 7, 4]])
    n = m.inverse()
    n1 = Matrix(4, 4)
    n1.set_values([[0.21805, 0.45113, 0.24060, -0.04511],
                    [-0.80827, -1.45677, -0.44361, 0.52068],
                    [-0.07895, -0.22368, -0.05263, 0.19737],
                    [-0.52256, -0.81391, -0.30075, 0.30639]])
    assert m.determinant() == 532
    assert m.cofactor(2, 3) == -160
    assert n[3][2] == -160 / 532
    assert m.cofactor(3, 2) == 105 
    assert n[2][3] == 105 / 532
    assert n.compare(n1) == True

    m.set_values([[8, -5, 9, 2],
                  [7, 5, 6, 1],
                  [-6, 0, 9, 6],
                  [-3, 0, -9, -4]])
    n = m.inverse()
    n1.set_values([[-0.15385, -0.15385, -0.28205, -0.53846],
                    [-0.07692, 0.12308, 0.02564, 0.03077],
                    [0.35897, 0.35897, 0.43590, 0.92308],
                    [-0.69231, -0.69231, -0.76923, -1.92308]])
    assert n.compare(n1) == True

    m.set_values([[9, 3, 0, 9],
                    [-5, -2, -6, -3],
                    [-4, 9, 6, 4],
                    [-7, 6, 6, 2]])
    n = m.inverse()
    n1.set_values([[-0.04074, -0.07778, 0.14444, -0.22222],
                    [-0.07778, 0.03333, 0.36667, -0.33333],
                    [-0.02901, -0.14630, -0.10926, 0.12963],
                    [0.17778, 0.06667, -0.26667, 0.33333]])
    assert n.compare(n1) == True

def test_inverse_equality():
    """Tests the transitive property of matrix inversion."""
    m = Matrix(4, 4)
    m.set_values([[3, -9, 7, 3],
                    [3, -8, 2, -9],
                    [-4, 4, 4, 1],
                    [-6, 5, -1, 1]])
    n = Matrix(4, 4)
    n.set_values([[8, 2, 2, 2],
                    [3, -1, 7, 0],
                    [7, 0, 5, 4],
                    [6, -2, 0, 5]])
    assert m.compare(m.multiply(n).multiply(n.inverse())) == True
    