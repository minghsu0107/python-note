import numpy as np

J = np.array([
    [12, 23, 14],
    [20, 29, 38],
    [3, 6, 10],
    [15, 15, 2]
])
F = np.array([
    [13, 33, 22],
    [10, 19, 8],
    [30, 0, 20],
    [0, 0, 0]
])
print(J)
print(F)
print(np.array_equal(J + F, F + J))
print(np.array_equal(J - F, F - J))

a, b, c, d = F
print(a) # [13 33 22]
print(b) # [10 19 8]
print(c) # [30 0 20] 
print(d) # [0 0 0]