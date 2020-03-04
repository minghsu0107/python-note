colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d = {}
for color in colors:
    if not color in d:
        d[color] = 0
    d[color] += 1
print(d)

from collections import defaultdict
d = defaultdict(int)
for color in colors:
    d[color] += 1
print(d)

### defaultdict(default_factory)會産生一個以default_factory為基本的dictionary, 
### 也就是key不需要存在這個dictionary當中, 它的d[key]值便會是default_factory這個type的預設值(int為0).

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']
d = {}
for name in names:
    key = len(name)
    if not key in d:
        d[key] = []
    d[key].append(name)
print(d)

d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
print(d)

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
print(d)