def divide(a, b):
    if b==0:
        return "divide by 0"
    return a/b

d = {"+": lambda a, b: a+b,
     "-": lambda a, b: a-b,
     "*": lambda a, b: a*b,
     "/": divide
    }

s = input()
x, c, y = s.split()
x, y = int(x), int(y)

if c not in d:
    print("Undefined operator")
else:
    print(s, "=", d[c](x, y))

def square(x):
    return x*x

def f(func):
    def func_of_list(l):
        tmp = l[:]
        for i in range(len(tmp)):
            tmp[i] = func(tmp[i])
        return tmp
    return func_of_list

a = [-1, 2, 4, -3]

print(f(abs)(a))
print(f(square)(a))
print(f(lambda x: -x)(a))

print(a)
print(a[:])


