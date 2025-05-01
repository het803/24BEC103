class matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Matrix must be 3x3.")
        self.data = [list(row) for row in data]

    def __add__(self, other):
        return matrix([
            [self.data[i][j] + other.data[i][j] for j in range(3)]
            for i in range(3)
        ])

    def __mul__(self, other):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                result[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(3))
        return matrix(result)

    def transpose(self):
        return matrix([[self.data[j][i] for j in range(3)] for i in range(3)])

    def __repr__(self):
        return '\n'.join(str(row) for row in self.data)

A = matrix([[1,2,3],[4,5,6],[7,8,9]])
B = matrix([[9,8,7],[6,5,4],[3,2,1]])
print("A + B:\n", A + B)
print("A * B:\n", A * B)
print("Transpose of A:\n", A.transpose())
