# cannot change elements in a tuple -> safer
# tuple is faster than list
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, "banana", True)
tuple3 = tuple(range(5))
tuple4 = (7,)
print(tuple3)
print(tuple4)
print(tuple2[1])

list1 = list(tuple1)

list2 = [1, 2, 3]
tuple2 = tuple(list2)

d = {(x, x+1): x for x in range(3)}  # {(0, 1): 0, (1, 2): 1, (2, 3): 2}
print(d[(1, 2)])             # 1

book = ("#123", "Python Programming", 250)
(id, title, price) = book
print(id, title, price)

a = [(1, 'a'), (2, 'c'), (2, 'b'), (3, 'c'), (2, 'd')]
print(max(a, key=lambda x: x[0]))

# tuple基本操作
# 初始化一个tuple类型变量z
z = ("a", "b", "c", "d", "e")
print(z)

# 读取z中的元素，与list类似
print(z[0])
print(z[-1])
