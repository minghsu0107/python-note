import numpy as np

A = np.array([
    [2, -3, -4, 0],
    [-3, 1, -1, 5],
    [4, 0, -6, -7]
])
k = -4
print(k * A)

C = np.array([
    [4, -3, 2],
    [0, 1, -1],
    [5, 4, 0]
])
D = np.array([
    [2, 2, -5],
    [3, 1, 0],
    [-1, 1, 4]
])
print(C.dot(D))