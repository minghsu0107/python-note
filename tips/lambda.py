l = [3, 1, 4, 2, 5]
## 计算l中每个元素的两倍和平方，并将两种组成一个列表
## lambda表达式和python函数一样，也可以接受函数作为参数
twoTimes = lambda x: x * 2
square = lambda x: x ** 2
# Python2和Python3的map并不兼容，所以使用list(map)
print( [  list(map(lambda x: x(i), [twoTimes, square])) for i in l  ] )
# [[6, 9], [2, 1], [8, 16], [4, 4], [10, 25]]

## 内置filter函数，选择l中的偶数
# Python2和Python3的filter并不兼容，所以使用list(filter)
print(list(filter(lambda x: x % 2 == 0, l)))

def b():
    return lambda x: x + 2

c = b()
print(c(18))

a = lambda x: x ** 5 + 2
print(a(2))

e = [1, 7, 13, 19, 25]
f = []
for i in filter(lambda x: x > 10, e):
    f.append(i)
print(f)

data = [['Julia', 58], ['Abby', 58], ['Jane', 31], ['Stephen', 76], ['Ryn', 82], ['Justin', 99], ['Caroline', 65], ['James', 87], ['Damon', 25], ['Elena', 76]]

def bucketsort_hash(data):
    max_score = 100
    bucket = []
    bucket_num = lambda x: int(x/10)
    
    for i in range(bucket_num(max_score)+1):
        bucket.append([])

    for x in data:
        index = bucket_num(x[1])
        bucket[index].append(x)

    for i, flag in enumerate(bucket):
        if flag != [] :
            bucket[i] = sorted(bucket[i], key=lambda x: x[1])

    index = 0
    for i in bucket:
        if i != []:
            for j in i:
                data[index] = j
                index += 1

bucketsort_hash(data)
print(data)