a = []


def change_mutable_object(a):
    a.append(1)


change_mutable_object(a)
print(a)  # [1]


def add(s):
    s += 'b'
    print("In add function :", s)


str2_ = "aaa"
add(str2_)

str_ = list("aaa")
add(str_)

b = 0


def immutable(b):
    b += 1  # the b here is local, not the global one, though the b

    # in the parameter is the global one
immutable(b)
print(b)  # 0


def change():
    global b
    b += 1


change()
print(b)

var1 = 5


def test():
    global var1  # regard var1 as a global variable
    var1 = 10


def test2():
    print(var1)  # regard var1 as a global variable


test()
print(var1)
# output:
# 10
test2()

c = [1, 2, 3]

d = c[:]
d.append(4)
print(c)  # [1, 2, 3]

d = c
d.append(4)
print(c)  # [1, 2, 3, 4]


def GetArea(width, height=12):
    return width * height


ret1 = GetArea(6)  # 6 * 12
ret2 = GetArea(6, 9)  # 6 * 9


def multiple_return_value(a, b):
    x = a + 1
    y = b * 10
    return x, y


x, y = multiple_return_value(1, 2)
print(x, y)


def accumulate(*params):
    total = 0
    for i in params:
        total += i
    return total


arr = [1, 2, 4, 5, 4]
arr2 = (1, 2, 4, 5, 4)
# 使用*，表示該參數接受不定長度引數
# 傳入函式的引數，會被收集在一個Tuple中，再設定給params參數
print(accumulate(1, 2, 4, 5, 4))
print(accumulate(*[1, 2, 4, 5, 4]))
print(accumulate(*arr))
print(accumulate(*arr2))


def pr(x, y, z):
    print(x, y, z)


a = [11, 22, 33]
pr(*a)  # splat operators(*)

mp = {'x': 11, 'y': 22, 'z': 33}
pr(*mp)  # x y z
pr(**mp)  # 11 22 33


def dosome(**args):
    print(args)


dosome(name='Justin', passwd=123456, job='?')
#{'passwd': 123456, 'job': '?', 'name': 'Justin'}
dosome(**mp)

# pass parameters for specific key words


def sum3(a, b, c):
    return a + b + c


args = {'a': 1, 'b': 2, 'c': 3}
print(sum3(**args))  # 6

x = 0


def f():
    x = 1

    def g():
        global x
        x = 2
    g()
    print("In f: x =", x)


f()
print("outside: x =", x)

# In f: x = 1
# outside: x = 2

x = 0


def f():
    x = 1

    def g():
        nonlocal x
        x = 2
    g()
    print("In f: x =", x)


f()
print("outside: x =", x)


# In f: x = 2
# outside: x = 0
