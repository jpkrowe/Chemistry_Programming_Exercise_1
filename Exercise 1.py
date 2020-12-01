import numpy as np

def eigenvalues(matrix):
    evals, evecs = np.linalg.eig(matrix)
    return evals

class Matrix: ###creates a matrix class in which the
    def __init__(self, length, option):
        self.matrix = np.zeros((length, length))
        if option == 1:
            a = -np.ones(length - 1)
            np.fill_diagonal(self.matrix[1:], a)
            np.fill_diagonal(self.matrix[:, 1:], a)
        elif option == 2:
            for i in range(length):
                if 0 < i < length - 1:
                    self.matrix[i, i + 1] = -1
                    self.matrix[i, i - 1] = - 1
                elif i > 0:
                    self.matrix[i, i - 1] = - 1
                else:
                    self.matrix[i, i + 1] = - 1
        self.evals = eigenvalues(self.matrix)


length = int(input("State length of linear polyene"))
matrix  = Matrix(length, 1)
evals = matrix.evals
print(evals)
print(matrix.matrix)