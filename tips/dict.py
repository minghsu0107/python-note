dict1 = {"banana":10, "apple":20, "orange": 30}
dict1["pineapple"] = 40
print(dict1["apple"])
print(dict1.pop("banana"))
print(dict1) # the order in a dictionary is random, so dict1[0] is an error
#if there are multiple keys, the previous one will be covered
del dict1["apple"]
dict1.clear()
del dict1

dict1 = {"joe":5, "marry":8}
n = len(dict1)
dict2 = dict1.copy() # copy dict1
## get(key, default_value) return the value to the key
## if key does not exist, return default_value
print(dict1.get("joe")) # 5
print(dict1.get("joe", 11)) # 5
print(dict1.get("Jack")) # none
print(dict1.get("Simmon", 6)) # 6

b = "joe" in dict1 # b == True
dict2 = dict1.items() # dict2 = [("joe":5), ("mary:"8)]
dict2 = dict1.keys()  # dict2 = ["joe", "mary"]
dict2 = dict1.values() # dict2 = [5, 8]

## same as get()
print(dict1.setdefault("joe")) # 5; if key does not exist, make a new one
print(dict1.setdefault("joe", 12)) # 5
print(dict1.setdefault("john")) # none
print(dict1.setdefault("May", 7)) # 7

dict2 = dict1.clear()
dict1 = {"ming":100, "Jack": 85, "Mandy": 90}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
	print(listkey[i], listvalue[i])

listitem = dict1.items()  # create a tuple
for name, score in listitem:
	print(name, score)

dictx = dict({'a': 1, 'b': 2})
dictz = dict([('a', 1), ('b', 2)])

nums = [0, 1, 2, 3]
sqs = {x: x ** 2 for x in nums}  # { 0: 0, 1: 1, 2: 4, 3: 9 }
print(sqs[2])                           # 4

evens = {x: x ** 2 for x in nums if x % 2 == 0}  # { 0: 0, 2: 4 }
print(evens[2])                                         # 4

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
c = {k:d[k] for k in d if not k.startswith('r')}
print(c)


names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(zip(names, colors))
print(d)
### {'raymond':'red', 'rachel': 'green', 'matthew':'blue'}

d = dict(enumerate(names))
### {0:'raymond', 1:'rachel', 2:'matthew'}
print(0 in d.keys()) # True
print(0 not in d.keys()) # False

d = {1: "one", 2: "three"}
d1 = {2: "two"}

# updates the value of key 2
d.update(d1)
print(d) # {1: 'one', 2: 'two'}

d1 = {3: "three"}

# adds element with key 3
d.update(d1)
print(d) # {1: 'one', 2: 'two', 3: 'three'}