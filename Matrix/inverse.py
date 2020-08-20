import numpy as np

A = np.array([
    [4, -7],
    [2, -3]
])
A_inv = np.linalg.inv(A)
print(A.dot(A_inv))

B = np.array([
    [8, 2],
    [12, 3]
])
try:
    B_inv = np.linalg.inv(B)
except np.linalg.LinAlgError:
    print('矩陣 B 是不可逆矩陣')
