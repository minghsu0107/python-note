def square(x):            # 计算平方数
    return x ** 2


x = list(map(square, [1, 2, 3, 4, 5]))  # 计算列表各个元素的平方
print(x)
# x = [1, 4, 9, 16, 25]
y = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))  # 使用 lambda 匿名函数
print(y)
# [1, 4, 9, 16, 25]

# 提供了两个列表，对相同位置的列表数据进行相加
z = list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
print(z)
# [3, 7, 11, 15, 19]

'''
>>> l = [1] * 4
>>> print(l)
>>> [1, 1, 1, 1]

*操作符在複製了值的引用，而不是創建了新的對象。所以以下的list中，是4個指向同一個dict對象的引用。
>>> l = [{'a': 1}] * 4
>>> print(l)
>>> [{'a': 1}, {'a': 1}, {'a': 1}, {'a': 1}] 
>>> l[0]['a'] = 2
>>> print(l)
>>> [{'a': 2}, {'a': 2}, {'a': 2}, {'a': 2}]


>>> l = [{'a': 1} for _ in range(4)]
>>> print(l)
>>> [{'a': 1}, {'a': 1}, {'a': 1}, {'a': 1}]
>>> l[0]['a'] = 2
>>> print(l)
>>> [{'a': 2}, {'a': 1}, {'a': 1}, {'a': 1}]


>>> listA = ['1','2','3']
>>> print map(int,listA)
[1, 2, 3]


>>> def multiple2(x):
... return x*2
...
>>> list1 = [1,3,5,7,9]
>>> print map(multiple2,list1)
[2, 6, 10, 14, 18]
>>>
>>> print [multiple2(x) for x in list1]
[2, 6, 10, 14, 18]


>>> def adder(x,y,z):
... return x+y+z
...
>>> list1 = [1,3,5,7,9]
>>> list2 = [2,4,6,8,10]
>>> list3 = [100,100,100,100,100]
>>>
>>> print map(adder,list1,list2,list3)
[103, 107, 111, 115, 119]
>>>
>>> print [adder(x,y,z) for x,y,z in zip(list1,list2,list3)]
[103, 107, 111, 115, 119]
```
