from functools import partial
x = 3


def funcA():
    global x
    x += 2
    return x


def funcB():
    x = funcA()  # the x here is local, and its value is assigned by funcA()
    print(x)  # print the lcoal x value


funcA()  # x += 2 -> x == 5
funcB()  # x += 2 -> x == 7, and funcB prints the value of x_local
print(x)


def add(a, b):
    return a+b


add_by_2 = partial(add, b=2)
print(add_by_2(3))

# 上述的add_by_2是一個partial()新産生的function,
# 它利用add(a, b)而將b的值固定為2. 所以呼叫add_by_2(3)會得到5

f = open('a.txt', 'r')
blocks = []
for block in iter(partial(f.read, 3), ""):
    blocks.append(block)
print(blocks)
f.close()
# is equivalent to:
f = open('a.txt', 'r')
blocks = []
while True:
    block = f.read(3)  # read 3 char at a time
    if block == "":  # when f.read() access no objects, it returns ""
        break
    blocks.append(block)
print(blocks)
f.close()


def magic(*args, **kwargs):
    print('unnamed args:', args)
    print('keywords args:', kwargs)


magic(1, 2, key='word', key2='word2')

# unnamed args: (1, 2)
# keywords args: {'key': 'word', 'key2': 'word2'}


def double(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g


def f2(x, y):
    return x + y


g = double(f2)
print(g(1, 2))  # 2(1+2) = 6


@double
def f3(x, y):
    return x - y


print(f3(7, 2))  # 2(7-2) = 10
