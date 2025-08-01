# python3
import collections

# 初始化字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# 初始化ChainMap
chain = collections.ChainMap(dict1, dict2)

# 使用maps输出chainMap
print(chain.maps)  # [{'b': 2, 'a': 1}, {'b': 3, 'c': 4}]

# 输出key
print(list(chain.keys()))  # ['b', 'c', 'a']

# 输出值
print(list(chain.values()))  # [2, 4, 1]

# 访问
print(chain['b'])  # 2
print(chain.get('b'))  # 2

# 使用new_child添加新字典
dict3 = {'f': 5}
new_chain = chain.new_child(dict3)
print(new_chain.maps)  # [{'f': 5}, {'b': 2, 'a': 1}, {'b': 3, 'c': 4}]

new_chain.maps = list(reversed(new_chain.maps))
print(new_chain.maps)
