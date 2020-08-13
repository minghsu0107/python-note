# coding=utf-8
import pickle
# 注意：使用 pickle 的時候，檔名不可以命名成 pickle.py

a = [1, 3, 5, 7, 9]
d = {'cat': 1000, 2: ['1', 'a', 'XX', 3], '3': {'k': 'tao', 6: 10}}
s = 'my name'

# 存資料
with open('my_file.pickle', 'wb') as file:
    pickle.dump(a, file)  # 使用 dump 把 data 倒進去 file 裡面
    pickle.dump(d, file)
    pickle.dump(s, file)


# coding=utf-8
# 注意：使用 pickle 的時候，檔名不可以命名成 pickle.py

# 拿資料
with open('my_file.pickle', 'r') as file1:
    a = pickle.load(file1)  # 逐行拿資料，包括可以拿到 data type
    d = pickle.load(file1)
    s = pickle.load(file1)
    print(a)
    print(d)
    print(s)
