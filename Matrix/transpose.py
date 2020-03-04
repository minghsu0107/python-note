import numpy as np

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])
C = (A + B).T
D = A.T + B.T
print(np.array_equal(C, D)) # True

A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
B = np.array([
    [1, 0, 2],
    [4, 5, 6]
])
C = (A.dot(B)).T
D = (B.T).dot(A.T)
print(np.array_equal(C, D)) # True

tp1 = (1,2,3,4,5,6) 
tp2 = (2,2,3,4,5,6) 
arr1 = np.array(tp1,dtype=float) 
arr2 = np.array(tp2,dtype=float) 
d = np.sqrt(np.sum(np.square(arr1-arr2)))#求两个数组之间的距离 
print(type(arr1))#查看arr1的数据类型 
print(arr1)
print(d)
