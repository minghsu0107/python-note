coding=utf-8
import copy

a = [1,2,[3,4]]

b = a                       # [1,2,[3,4]]
print("*** assign ***")     # 指到同一塊記憶體空間
print(id(a)==id(b))         # True
print(id(a[2])==id(b[2]))   # True

d = copy.copy(a)            # [1,2,[3,4]]
print("*** shallow copy ***" ) # 淺複製 只在淺部分開一塊新的空間
print(id(a)==id(d))         # False
print(id(a[2])==id(d[2]))   # True  # 深的部分仍然是使用同一塊記憶體

e = copy.deepcopy(a)        # [1,2,[3,4]]
print("*** deep copy ***" ) # 深複製 完全開另一塊全新的空間
print(id(a)==id(e))         # False
print(id(a[2])==id(e[2]))   # False

# 改變值的實驗 demo
a[0] = 11  # [1, 2, [3, 4]] -> [11, 2, [3, 4]]
print(b)   # [11, 2, [3, 4]] 跟著改變
print(d)   # [1, 2, [3, 4]]  不受影響
print(e)   # [1, 2, [3, 4]]  不受影響

a[2][0] = 333 # [11, 2, [3, 4]] -> [11, 2, [333, 4]]
print(b)   # [11, 2, [333, 4]] 跟著改變
print(d)   # [1, 2, [333, 4]]  跟著改變（深層的部分)
print(e)   # [1, 2, [3, 4]]    不受影響

a = [1,2,3]
b = a        # 等號代表 assign

print(id(a)) # 4432640984 記憶體位址
print(id(b)) # 4432640984 記憶體位址
print(id(a)==id(b)) # True

b[0] = 11
print(a)     # [11, 2, 3]
a[1] = 22
print(b)     # [11, 22, 3]

c = copy.copy(a)    # 淺複製
print(id(a)==id(c)) # False
c[1] = 22222
print(a)      # [11, 22, 3]
print(c)      # [11, 22222, 3]