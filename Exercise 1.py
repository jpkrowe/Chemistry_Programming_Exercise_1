import numpy as np


def degeneracies(evals):  # creates a matrix where the ijth element is 1 if i and j are degenerate eigenvalues
    degeneracy = np.zeros((len(evals), len(evals)))
    for i in range(len(evals)):
        for j in range(len(evals)):
            if abs(evals[i] - evals[j]) < 0.00001:
                degeneracy[i][j] = 1
            else:
                degeneracy[i][j] = 0
    return degeneracy


def eigenvalues(length,
                option):  # generates the eigenvalues for a matrix in which the matrix built is dependent on the option and length chosen
    connections = []
    matrix = np.zeros((length, length))
    a = -np.ones(length - 1)
    np.fill_diagonal(matrix[1:], a)
    np.fill_diagonal(matrix[:, 1:], a)
    if option == 2:  # cyclic polyene
        connections = [[1, length]]
    elif option == 3:  # tetrahedron
        connections = [[1, 3], [1, 4], [2, 4]]
    elif option == 4:  # cube
        connections = [[1, 4], [1, 6], [2, 7], [3, 8], [5, 8]]
    elif option == 5:  # dodecahedron
        connections = [[1, 5], [1, 8], [2, 10], [3, 12], [4, 14], [6, 15], [7, 20], [9, 19], [11, 18], [13, 17], [20, 16]]
    elif option == 6:  # buckminster fullerene
        connections = [[1, 9], [2, 12], [3, 15], [4, 18], [5, 1], [6, 20], [7, 22], [8, 25], [10, 26], [11, 29],
                       [13, 30], [14, 33]
            , [16, 34], [17, 37], [19, 38], [21, 40], [23, 42], [24, 44], [27, 45], [28, 47], [31, 48], [32, 50],
                       [35, 51],
                       [36, 53], [39, 54], [41, 55], [43, 57], [46, 58], [49, 59] , [52, 60], [56, 60]]
    for i in connections:
        matrix[i[0] - 1, i[1] - 1] = -1
        matrix[i[1] - 1, i[0] - 1] = -1
    evals, evecs = np.linalg.eig(matrix)
    return evals



option = int(input("Choose an option: (1 for linear, 2 for cyclic, 3 for tetrahedron, 4 for cube, 5 for dodecahedron and 6 for buckminster fullerene) "))
if option == 1 or option == 2:
    length = int(input("State length of polyene: "))
elif option == 3:
    length = 4
elif option == 4:
    length = 8
elif option == 5:
    length = 50
elif option == 6:
    length = 60
else:
    print("Please choose an option from those listed")
    exit()

evals = eigenvalues(length, option)
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
        print("Eigenvalue = \u03B1 + " + str(np.round(evals[i], 4)) + "\u03B2 Degeneracy = " + str(np.round(degen)))
