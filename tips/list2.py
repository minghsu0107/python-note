### list comprehension ###
import functools
from math import pi
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)  # prints [0, 1, 4, 9, 16]

squares = [x ** 2 for x in nums]
print(squares)  # prints [0, 1, 4, 9, 16]

nums = [-2, -1, 0, 1, 2]
ds = [abs(x) for x in nums if abs(x) < 2]
print(ds)      # prints [1, 0, 1]

pi             # 3.141592653589793
round(pi, 3)  # 3.142
x = [str(round(pi, i)) for i in range(1, 6)]
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']
print(x)

colors = [1, 2, 3]
for color in reversed(colors):
    print(color)  # [3, 2, 1]
rev_colors = list(reversed(colors))
print(rev_colors)

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
# zip returns a list of tuples
for name, color in zip(names, colors):
    print(name, '-->', color)

colors = ['red', 'green', 'blue', 'yellow']
for color in sorted(colors):
    print(color)

for color in sorted(colors, reverse=True):
    print(color)

colors = ['red', 'green', 'blue', 'yellow']
print(colors.sort())  # none, does not return


def compare_length(c1, c2):
    if len(c1) < len(c2):
        return -1
    if len(c1) > len(c2):
        return 1
    return 0


print(sorted(colors, key=functools.cmp_to_key(compare_length)))
sorted_colors = sorted(colors, key=len)
print(sorted_colors)

iter_string = "some text"
comp_list = [x for x in iter_string if x != " "]
print(comp_list)
# ['s', 'o', 'm', 'e', 't', 'e', 'x', 't']

nums = [1, 2, 3, 4, 5]
letters = ['A', 'B', 'C', 'D', 'E']
nums_letters = [[n, l] for n in nums for l in letters]
# the comprehensions list combines two simple lists in a complex list of lists.
print(nums_letters)

print([(i, j, i*j) for i in range(1, 10) for j in range(1, 10)])
x = [print(i, j, i*j) for i in range(1, 10)
     for j in range(1, 10) if j % 2 == 0]  # only in python3
'''
在python3，print是一個function，也就是說他屬於expression，而輸出是他的副作用，
在python2，print是一個statement，因此無法丟到list comprehension內。 
'''
print(x)  # none
### Generator comprehensions ###
my_gen = (x + 1 for x in range(5))
print()
print(next(my_gen))
print()

for x in my_gen:
    print(x)
print()


def sq_num(n):
    for num in (x**2 for x in range(n)):
        yield num


print(next(sq_num(10)))
print()
for x in sq_num(10):
    print(x)
