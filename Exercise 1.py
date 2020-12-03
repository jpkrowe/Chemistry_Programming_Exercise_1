import numpy as np


def eigenvalues(matrix):
    evals, evecs = np.linalg.eig(matrix)
    return evals


def degeneracies(evals): ### creates a matrix where the ijth element is 1 if i and j are degenerate eigenavalues
    degeneracy = np.zeros((len(evals), len(evals)))
    for i in range(len(evals)):
        for j in range(len(evals)):
            if abs(evals[i]-evals[j]) < 0.00001:
                degeneracy[i][j] = 1
            else:
                degeneracy[i][j] = 0
    return degeneracy


class Matrix: ###Creates a matrix class in which the matrix built is dependent on the option and length chosen
    def __init__(self, length, option):
        self.matrix = np.zeros((length, length))
        a = -np.ones(length - 1)
        np.fill_diagonal(self.matrix[1:], a)
        np.fill_diagonal(self.matrix[:, 1:], a)
        if option == 2:
            self.matrix[length - 1][0] = - 1
            self.matrix[0][length - 1] = - 1
        self.evals = eigenvalues(self.matrix)


length = int(input("State length of polyene:"))
option = int(input("Choose an option: (1 for linear, 2 for cyclic)"))
matrix = Matrix(length, option)
evals = matrix.evals
evals.sort()
degeneracy = degeneracies(evals)
checked = np.zeros(len(evals))
for i in range(len(evals)):
    if checked[i] == 0:
        degen = 0
        for j in range(len(evals)):
            degen = degen + degeneracy[i][j]
            if degeneracy[i][j] == 1:
                checked[j] = 1
        print("Eigenvalue = " + str(evals[i]) + " Degeneracy = " + str(degen))