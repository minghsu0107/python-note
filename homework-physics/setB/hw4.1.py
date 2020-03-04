import numpy as np
A = np.array([
    [1/2, -1/2, 1],
    [-1/2, 1/2 + 1/3 + 1/5, 0],
    [1, 0, 0]
])
B = np.array([
    [0],
    [0],
    [5]
])
print(np.around(np.linalg.inv(A).dot(B), decimals=2))
