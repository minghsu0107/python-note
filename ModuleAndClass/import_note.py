import math as m
print(m.ceil(66.6))
print(m.floor(66.6))
print(m.pow(100, 2))
print(m.sqrt(100))
print(m.exp(100))
print(m.log(100))
print(m.log2(100))
print(m.log10(100))

print(m.pi)
print(m.e)

import random
random.seed(10) # 把 seed 設為 10
print(random.random()) # 0.5714025946899135
random.seed(10) # 把 seed 設為 10
print(random.random()) # 0.5714025946899135

print(random.random())      # return a float in [0, 1)
print(random.uniform(2, 5)) # return a float in [a, b]
print(2 + random.random() * 3)

print(random.randint(2, 5)) # return an int in [a, b]
print(random.randrange(2, 11, 2)) # (start, stop, step)
nums = range(10)
print(random.sample(nums, 3))
# 從 nums 中挑選 3 個且不會被重複挑中
# 直接回傳新的序列，不會影響傳入的 nums
print(random.choice(range(2, 11, 2))) # random.choice(x) returns an element in x
                                      # 隨機取樣放回(next time may 重複挑中)
x = ['mocha', 'melody', 'rilak', 'hortune', 'abbie', 'piepie']
print(random.choice(x))
random.shuffle(x) # shuffle x
print(x)

X  = [i for i in range(50, 100)]
Y = [i for i in range(200, 250)]
shuffledRange = [i for i in range(len(X))]
n_iter = 1
for n in range(n_iter):
    random.shuffle(shuffledRange)
    shuffledX = [X[i] for i in shuffledRange]
    shuffledY = [Y[i] for i in shuffledRange]
    print(shuffledX)
    print(shuffledY)

import sys
import os
print(sys.version) # get the version of python
print(sys.platform)
print(os.getcwd()) # get the dictionary right now
print(os.listdir())
print(os.path.join('testdir', 'testfile')) # 組合成完整路徑名
print(os.path.exists('/home/minghsu/Desktop/python/code/basic/ModuleAndClass'))
## os.path.remove(path)

import time
print(time.time())
print(time.localtime())
print(time.asctime())

import calendar
print(calendar.month(2019, 2))
print(calendar.weekday(2019, 2, 21)) #  returns the day of the week (0 is Monday)

import time
start_time = time.time()
a = 0
for i in range(10000):
    a += 1
end_time = time.time()
print(end_time - start_time)

