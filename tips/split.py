# split() returns a list
u = "www.doiido.com.cn"

# 使用默认分隔符
print(u.split())
# ['www.doiido.com.cn']

# 以"."为分隔符
print(u.split('.'))
#['www', 'doiido', 'com', 'cn']

# 分割0次
print(u.split('.', 0))
# ['www.doiido.com.cn']

# 分割一次
print(u.split('.', 1))
#['www', 'doiido.com.cn']

# 分割两次
print(u.split('.', 2))
#['www', 'doiido', 'com.cn']

# 分割两次，并取序列为1的项
print(u.split('.', 2)[1])
# doiido

# 分割最多次（实际与不加num参数相同）
print(u.split('.', -1))
#['www', 'doiido', 'com', 'cn']

# 分割两次，并把分割后的三个部分保存到三个文件
(u1, u2, u3) = u.split('.', 2)
print(u1)
# www
print(u2)
# doiido
print(u3)
# com.cn

time = "2011/03/12 15:34"
# solution1
day, t = time.split()
result = day.split('/') + t.split(':')
print(result)
# solution2
time = time.replace('/', ' ')
time = time.replace(':', ' ')
result = time.split()
print(result)
# solution3
print(time.replace('/', ' ').replace(':', ' ').split())
# ['2011', '03', '12', '15', '34']

# INPUT: 23 24 100
#        23 24 100

a = input().split()
b = list(map(int, input().split()))
a.sort()
b.sort()
print(a)  # ['100', '23', '24']
print(b)  # [23, 24, 100]
