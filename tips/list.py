x = [8, 9]
list1 = [1, 2, 3, 4, 5, 6]
print(list1)

a = list([1, 2, 3])
b = list(range(0, 4)) # [0, 1, 2, 3]
c = list("abc")  # ["a", "b", "c"]

list2 = list1*2 # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
list2 = list1[1:4] #[2, 3, 4]
list2 = list1[1:4:2] #[2, 4]

n = len(list1) 
n = min(list1) # largest element
n = max(list1) # smallest element

n = list1.index(3) # the index of the first 3 in list1
n = list1.count(3) # the number of elements with a value of 3

list1.append(8) # push_back
list1.append([8, 9]) # list1 = [1, 2, 3, 4, 5, 6, [8, 9]]
list1.extend(x) # list1 = [1, 2, 3, 4 ,5, 6, 8, 9]
list1.insert(3, 8) # list1 = [1, 2, 3, 8, 4 ,5, 6 ,8 ,9]
n = list1.pop() # n = 6, list1 = [1, 2, 3, 4, 5]
n = list1.pop(3) # n = 4, list1 = [1, 2, 3, 5]
list1.remove(3) # remove the first 3 in list1
list1.reverse() 
list2.sort()

del list1[1:4]  # list1 = [1, 5, 6]
del list1[1:4:2] # list1 = [1, 3, 5, 6]

y = [3, 1, 4, 2]
y[:-2] # [3, 1]
y[:-1] # [3, 1, 4]
y[1:-2] # [1]

# sliced
demo = [x for x in range(10)]
s1 = demo[:]
print( "sliced 1:{}".format(s1) )

s2 = demo[2:]
print( "sliced 2:{}".format(s2) )

s3 = demo[2:5]
print( "sliced 3:{}".format(s3) )

s4 = demo[:5]
print( "sliced 4:{}".format(s4) )

s5 = demo[-3:]
print( "sliced 5:{}".format(s5) )

s6 = demo[::2]
print( "sliced 6:{}".format(s6) )

s7 = demo[1::2]
print( "sliced 7:{}".format(s7) )

# sliced 1:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sliced 2:[2, 3, 4, 5, 6, 7, 8, 9]
# sliced 3:[2, 3, 4]
# sliced 4:[0, 1, 2, 3, 4]
# sliced 5:[7, 8, 9]
# sliced 6:[0, 2, 4, 6, 8]
# sliced 7:[1, 3, 5, 7, 9]

# filter for DNA
# Input : ATCGATGCHATGCATFC
print("".join([i for i in input() if i in "ATGC"]))

identity = []
for i in range(5):
	row = []
	for j in range(5):
		row.append(1 if i == j else 0)
	identity.append(row)
print(identity)
### is equivalent to
identity = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
print(identity)
print(identity[0][2])