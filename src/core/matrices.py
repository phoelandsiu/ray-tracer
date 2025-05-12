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

    def compare(self, other):
        """Compares two matrices for equality."""
        if (self.rows != other.rows or self.cols != other.cols):
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if (self.data[i][j] != other.data[i][j]):
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