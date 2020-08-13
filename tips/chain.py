# 使用3.x版的函式print
from __future__ import print_function
from itertools import chain

a = [70, 81, 92]
b = ['hi', 'hello', 'aloha', 'ahoy']
c = [31.3, 32.5, 29.2, 28.5]


print(list(chain(a, b, c)))
# [70, 81, 92, 'hi', 'hello', 'aloha', 'ahoy', 31.3, 32.5, 29.2, 28.5]

print(list(chain(*b)))
# ['h', 'i', 'h', 'e', 'l', 'l', 'o', 'a', 'l', 'o', 'h', 'a', 'a', 'h', 'o', 'y']


def my_chain(*iterables):
    for it in iterables:
        for e in it:
            yield e


print(list(my_chain(a, b, c)))
# [70, 81, 92, 'hi', 'hello', 'aloha', 'ahoy', 31.3, 32.5, 29.2, 28.5]


def foo(x):
    i = 1
    while i <= x:
        yield range(0, i)
        i += 1


print(list(chain.from_iterable(foo(4))))
# [0, 0, 1, 0, 1, 2, 0, 1, 2, 3]


def my_chain_from_iterable(iterables):
    for it in iterables:
        for e in it:
            yield e


print(list(my_chain_from_iterable(foo(4))))
# [0, 0, 1, 0, 1, 2, 0, 1, 2, 3]
