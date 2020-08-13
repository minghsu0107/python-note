import sys


def readInput():
    for line in sys.stdin:
        print(line)
# input:
# ming
# jack
# bob
# output:
# ming
#
# jack
#
# bob
# since stdin reads '\n' too, we can use strip()
# to get rid of special character at head and tail


def readInput2():
    for line in sys.stdin:
        print(line.strip())
# input: 1 2 3 4 5


def sum():
    line = input()  # read a whole line as a string
    tokens = line.split()
    sum = 0
    for token in tokens:
        sum += int(token)
    print(sum)


def read_a_line():
    a = list(map(int, input().split()))
    print(a)
# input().split() returns a list of splited strings
# and we use map to change every strings in the list into integer iteratively
# in: 1 2 3 4 5
# out: [1, 2, 3, 4, 5]
