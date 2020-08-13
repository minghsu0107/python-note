import numpy as np

a = np.array([1, 2, 3, 4])  # 建立array

print("a:", a)
print("type:", type(a))    # 型別為ndarray
print("ndim:", a.ndim)     # 維度

a = [3, 4, 5, 6]
a = np.asarray(a)  # convert a list into 1D array

# arange
a = np.arange(10)
print(type(a))
print(a)
print(np.arange(3, 6, 0.4))  # in [3, 6)

# linspace
print(np.linspace(4, 6, 5))

b = np.array([[1, 2, 3, 4], [4, 3, 2, 1], [1, 3, 5, 7]])
print(b)
print("ndim:", b.ndim)
print("shape:", b.shape)  # (3, 4)
print("dtype:", b.dtype)  # int64
print("size:", b.size)  # 12
print("transpose:", b.T, sep="\n")

c = np.zeros((2, 3, 4))  # 建立全為0的陣列
print(c)
c = np.zeros(5)  # [ 0.  0.  0.  0.  0.]
c = np.zeros((5,))  # [ 0.  0.  0.  0.  0.]

d = np.ones((2, 3))  # 建立全為1的陣列
print(d)
print("ndim:", d.ndim)
print("shape:", d.shape)  # (2, 3)
print("dtype:", d.dtype)  # float64

# 改變儲存的type
d = d.astype('int32')
print(d)
print(d.dtype)  # int32
print(type(d[0, 0]))  # <class 'numpy.int32'>

# 改變形狀
e = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
f = e.reshape((2, 6))
g = e.reshape((2, 2, 3))
print(f)
print()
print(g)

h = np.array([[1, 2, 3], [4, 5, 6]])
l = h.reshape((3, -1))  # 會自動計算-1那個位子應該是多少
print(l)

# 一維陣列
o = np.array([0, 1, 2, 3, 4, 5])
print(o[1])
print(o[1:5])  # [1 2 3 4]
print(o[::-1])  # [5 4 3 2 1 0]
# 二維陣列
p = np.array(range(12))
p = p.reshape((3, -1))
print(p)
print(p[0])
print(p[2, 0])

# 更多切片
q = np.array(range(30)).reshape((5, -1))
p = q[1:4, ::2]
r1 = q[1:4, :]
r2 = q[1:4]  # == r1
s = q[(0, 1, 4), (1, 3, 5)]
t = q[3:, (0, 4, 2)]
x = q[0:2, 3]
y = q[q % 4 == 0]
print("q", q, sep="\n")
print("p", p, sep="\n")
print("r1", r1, sep="\n")
print("r2", r2, sep="\n")
print("s", s, sep="\n")
print("t", t, sep="\n")
print("x", x, sep="\n")
print("y", y, sep="\n")

'''
q
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]
 [24 25 26 27 28 29]]
p
[[ 6  8 10]
 [12 14 16]
 [18 20 22]]

r1
[[ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
r2
[[ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
s
[ 1  9 29]
t
[[18 22 20]
 [24 28 26]]
x
[3, 9]
y
[ 0  4  8 12 16 20 24 28]
'''
# copy
u = np.array([1, 2, 3, 4, 5, 6])
v = u
v[0] = 87
print("u:", u)
print("v:", v)

w = np.array([[1, 2, 3], [4, 5, 6]])
x = w.copy()
x[0, 0] = 87
print("w:", w)
print("x:", x)

# replacement
E = np.array([[-1, 2, 3, -2], [3, -9, 5, -3]])
E[E < 0] = 0
print(E)
'''
[[0 2 3 0]
 [3 0 5 0]]
 '''

F = np.array([[1, 2], [3, 4]])
print(F.sum())  # 10
print(F.max())
print(F.min())
print(F.mean())

a = np.array([1, 0, 0, 1, 1])
print((a == 0).sum())  # 2 (number of elements that = 0)

# visit all elements
z = np.arange(12).reshape((3, -1))
for i in z:
    for j in i:
        print(j, end=' ')


for i in range(z.shape[0]):
    for j in range(z.shape[1]):
        print(z[i, j], end=' ')


A = np.arange(5)
B = np.array([1, 2, 3, 0, 1])
print(A)
print(A+3)  # 每個元素都+3
print(A*2)  # 每個元素都*2
print(A**2)  # 每個元素都平方
print(A+B)  # A, B相加
print(A*B)  # A, B相同位置相乘
print(A.dot(B))  # 內積


# 矩陣乘法
C = np.array([[1, 2], [3, 4]])
D = np.array([[2, 8], [5, 1]])
print(np.matmul(C, D))

a = np.arange(6).reshape(2, 3) + 10
print(a)
'''
array([[0, 1, 2],
       [3, 4, 5]])
'''
print(np.argmax(a))  # 5
print(np.argmax(a, axis=0))  # array([1, 1, 1])
print(np.argmax(a, axis=1))  # array([2, 2])

b = np.arange(6)
b[1] = 5
print(b)  # array([0, 5, 2, 3, 4, 5])
print(np.argmax(b))  # 只返回第一次出现的最大值的索引, 1


x = np.array(range(6))
print(x)  # [0 1 2 3 4 5]
print(x.shape)  # (6,)

x = x.reshape(6, 1)
print(x)
'''
[[0]
 [1]
 [2]
 [3]
 [4]
 [5]]
'''
print(x.shape)  # (6, 1)

print(np.random.randint(low=1, high=3, size=5))  # [1 2 1 1 1]
print(np.random.randint(low=1, high=8))  # 7

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x.shape)  # (2, 3)

y = np.expand_dims(x, axis=0)
print(y.shape)  # (1, 2, 3)
print(y[0][1])  # [4, 5, 6]

x = np.array([1, 2, 3])
y = np.expand_dims(x, axis=1)
print(y.shape)  # (3, 1)
print(y[1][0])  # 2
print(y)
'''
[[1]
 [2]
 [3]]
'''

# a float number in [0, 1)
x = np.random.random()

# an array of shape (4, 2), each element in [0, 1)
x = np.random.random((4, 2))
x = np.random.rand(4, 2)

# an array of shape (3, 3) with normal distribution: N(0, 1)
# N(0, 1): average = 0, var = 1
x = np.random.randn(3, 3)

# a random integer in [1, 5)
x = np.random.randint(1, 5)

# a random array of length 20 with each element in  [1, 5)
x = np.random.randint(1, 5, size=20)

# a random array of length 20 with each element in [0, 10)
x = np.random.randint(10, size=20)

demo_list = ['lenovo', 'sansumg', 'moto', 'xiaomi', 'iphone']
np.random.choice(demo_list, size=(3, 3), p=[0.1, 0.6, 0.1, 0.1, 0.1])

demo_list = ['lenovo', 'sansumg', 'moto', 'xiaomi', 'iphone']
np.random.choice(demo_list, size=(3, 3))

np.random.choice(5, size=(3, 2))
'''
array([[1, 0],
       [4, 2],
       [3, 3]])
'''
# set random seed so that random numbers are same at each time
np.random.seed(1676)

# numpy.random.normal(loc=0.0, scale=1.0, size=None)
# return a number if size == None
# y = np.random.normal(0.0, noise, n_samples)
