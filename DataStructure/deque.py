from collections import deque
d = deque('abc')
for element in d:
    print(element.upper())

d.append('j')
d.appendleft('i')
print(d)

print(d.pop())
print(d.popleft())

print(d[0])
print(d[-1])
