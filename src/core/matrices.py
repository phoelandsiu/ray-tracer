import math
from core.tuples import Tuple, Point, Vector

class Matrix:
    def __init__(self, rows, cols):
        """Initializes a matrix with the given number of rows and columns."""
        if rows <= 0 or cols <= 0:
            raise ValueError("Matrix dimensions must be positive integers")
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __getitem__(self, index):
        """Returns the row at the given index."""
        return self.data[index]
    
    def __setitem__(self, index, value):
        """Sets the row at the given index."""
        if (len(value) != self.cols):
            raise ValueError("Row length must match the number of columns")
        self.data[index] = value

    def set_values(self, values):
        """Set matrix values from a 2D list of the same dimensions."""
        if len(values) != self.rows or any(len(row) != self.cols for row in values):
            raise ValueError("Input dimensions do not match the matrix size")
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = values[i][j]

    def compare(self, other, epsilon=1e-5):
        """Compares two matrices for equality."""
        if (self.rows != other.rows or self.cols != other.cols):
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if not math.isclose(self.data[i][j], other.data[i][j], abs_tol=epsilon):
                    return False
        return True

    def multiply(self, other):
        """Multiplies two matrices."""
        if (self.cols != other.rows):
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result[i][j] = sum(self[i][k] * other[k][j] for k in range(self.cols))
        return result
    
    def tuple_multiply(self, tuple):
        """Multiplies a matrix by a tuple."""
        if (self.cols != tuple.__len__()):
            raise ValueError("Number of columns in the matrix must match the length of the tuple")
        result = Matrix(self.rows, 1)
        for i in range(self.rows):
            result[i][0] = sum(self[i][j] * tuple[j] for j in range(self.cols))
        return result
    
    @classmethod
    def identity(cls, size = 4):
        """Creates an identity matrix of the given size."""
        if size <= 0:
            raise ValueError("Size must be a positive integer")
        identity_matrix = Matrix(size, size)
        for i in range(size):
            identity_matrix[i][i] = 1
        return identity_matrix

    def transpose(self):
        """Transposes the matrix."""
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed[j][i] = self[i][j]
        return transposed
    
    def determinant(self):
        """Calculates the determinant of a matrix."""
        if self.rows < 2 or self.cols < 2:
            raise ValueError("Determinant is only defined for 2x2 matrices")
        if (self.rows == 2 and self.cols == 2):
            return self[0][0] * self[1][1] - self[0][1] * self[1][0]
        det = 0
        for c in range(self.cols):
            det += self[0][c] * self.cofactor(0, c)
        return det
    
    def submatrix(self, row, col):
        """Returns the submatrix obtained by removing the specified row and column."""
        if row < 0 or row > self.rows or col < 0 or col > self.cols:
            raise ValueError("Row and column indices must be within the matrix dimensions")
        submatrix = Matrix(self.rows - 1, self.cols - 1)
        for i in range(self.rows):
            for j in range(self.cols):
                if i != row and j != col:
                    submatrix[i - (i > row)][j - (j > col)] = self[i][j]
        return submatrix
    
    def minor(self, row, col):
        """Calculates the minor of the matrix at the specified row and column."""
        return self.submatrix(row, col).determinant()
    
    def cofactor(self, row, col):
        """Calculates the cofactor of the matrix at the specified row and column."""
        return (-1) ** (row + col) * self.minor(row, col)
    
    def inverse(self):
        """Calculates the inverse of the matrix."""
        if self.rows != self.cols:
            raise ValueError("Inverse is only defined for square matrices")
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is not invertible")
        inverse_matrix = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                # Calculate the cofactor, transpose it, and divide by the determinant
                inverse_matrix[j][i] = self.cofactor(i, j) / det
        return inverse_matrix
    
    @classmethod
    def translation_matrix(cls, x, y, z):
        """Create a translation matrix."""
        translation_matrix = Matrix.identity(4)
        translation_matrix[0][3] = x
        translation_matrix[1][3] = y
        translation_matrix[2][3] = z
        return translation_matrix

    def __mul__(self, tuple):
        """Multiplies a matrix by a tuple and returns a tuple.
        [ 1  0  0  tx ]   [ x ]     [ x + tx ]
        [ 0  1  0  ty ] × [ y ]  =  [ y + ty ]
        [ 0  0  1  tz ]   [ z ]     [ z + tz ]
        [ 0  0  0   1 ]   [ 1 ]     [   1    ]
        """
        if (self.cols != len(tuple)):
            raise ValueError("Number of columns in the matrix must match the length of the tuple")
        x = (self[0][0] * tuple.x + self[0][1] * tuple.y + self[0][2] * tuple.z + self[0][3] * tuple.w)
        y = (self[1][0] * tuple.x + self[1][1] * tuple.y + self[1][2] * tuple.z + self[1][3] * tuple.w)
        z = (self[2][0] * tuple.x + self[2][1] * tuple.y + self[2][2] * tuple.z + self[2][3] * tuple.w)
        w = (self[3][0] * tuple.x + self[3][1] * tuple.y + self[3][2] * tuple.z + self[3][3] * tuple.w)

        if (math.isclose(w, 0.0)):
            return Vector(x, y, z)
        elif math.isclose(w, 1.0):
            return Point(x, y, z)
        else:
            return Tuple(x, y, z, w)
        
    @classmethod
    def scaled_matrix(cls, x, y, z):
        """Creates a scaling matrix."""
        scaled_matrix = Matrix.identity(4)
        scaled_matrix[0][0] = x
        scaled_matrix[1][1] = y
        scaled_matrix[2][2] = z
        return scaled_matrix

    def scale(self, tuple):
        """Scales a tuple using the matrix."""
        if (self.cols != len(tuple)):
            raise ValueError("Number of columns in the matrix must match the length of the tuple")
        x = (self[0][0] * tuple.x + self[0][1] * tuple.y + self[0][2] * tuple.z + self[0][3] * tuple.w)
        y = (self[1][0] * tuple.x + self[1][1] * tuple.y + self[1][2] * tuple.z + self[1][3] * tuple.w)
        z = (self[2][0] * tuple.x + self[2][1] * tuple.y + self[2][2] * tuple.z + self[2][3] * tuple.w)
        w = (self[3][0] * tuple.x + self[3][1] * tuple.y + self[3][2] * tuple.z + self[3][3] * tuple.w)

        if (math.isclose(w, 0.0)):
            return Vector(x, y, z)
        elif math.isclose(w, 1.0):
            return Point(x, y, z)
        else:
            return Tuple(x, y, z, w)

    @classmethod
    def rotation_matrix_x(self, angle):
        """Creates a rotation matrix around the x-axis."""
        rotation_matrix = Matrix.identity(4)
        rotation_matrix[1][1] = math.cos(angle)
        rotation_matrix[2][2] = math.cos(angle)
        rotation_matrix[1][2] = -math.sin(angle)
        rotation_matrix[2][1] = math.sin(angle)
        return rotation_matrix
    
    @classmethod
    def rotation_matrix_y(self, angle):
        """Creates a rotation matrix around the y-axis."""
        rotation_matrix = Matrix.identity(4)
        rotation_matrix[0][0] = math.cos(angle)
        rotation_matrix[2][2] = math.cos(angle)
        rotation_matrix[0][2] = math.sin(angle)
        rotation_matrix[2][0] = -math.sin(angle)
        return rotation_matrix

    @classmethod
    def rotation_matrix_z(self, angle):
        """Creates a rotation matrix around the z-axis."""
        rotation_matrix = Matrix.identity(4)
        rotation_matrix[0][0] = math.cos(angle)
        rotation_matrix[1][1] = math.cos(angle)
        rotation_matrix[0][1] = -math.sin(angle)
        rotation_matrix[1][0] = math.sin(angle)
        return rotation_matrix

    @classmethod
    def shearing_matrix(self, xy=0, xz=0, yx=0, yz=0, zx=0, zy=0):
        """Creates a shear matrix."""
        shear_matrix = Matrix.identity(4)
        shear_matrix[0][1] = xy
        shear_matrix[0][2] = xz
        shear_matrix[1][0] = yx
        shear_matrix[1][2] = yz
        shear_matrix[2][0] = zx
        shear_matrix[2][1] = zy
        return shear_matrix
         
    def __repr__(self):
        """Returns a string representation of the matrix."""
        return "\n".join([" ".join([str(self.data[i][j]) for j in range(self.cols)]) for i in range(self.rows)])