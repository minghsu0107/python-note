a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)  # [(1, 4), (2, 5), (3, 6)]
zipped2 = zip(a, c)  # [(1, 4), (2, 5), (3, 6)]

x, y = zip(*list(zipped))  # unpack zipped to list -> zipped is now empty
print(x)  # (1, 2, 3)
print(y)  # (4, 5, 6)
print(list(zipped))  # []

d = list(zip(*zipped2))
print(d)  # [(1, 2, 3), (4, 5, 6)]

# get all columns
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sol 1
print([[row[col] for row in a] for col in range(len(a[0]))])
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# sol 2
print(list(map(list, zip(*a))))  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(list(zip(*a)))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
