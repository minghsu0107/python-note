basket = {'apple', 'orange', 'apple', 'banana'}
basket.add('grape')
print(basket)               # {'orange', 'banana', 'apple', 'grape'}
basket.update(['melon', 'pear', 'guava'])
print(basket)
print('orange' in basket)          # True
print('berry' in basket)           # False
a = set('hello')
print(a)                           # {'h', 'e', 'l', 'o'}
b = set('world')
print(b)                           # {'w', 'o', 'r', 'l', 'd'}
print(a & b)                       # {'l', 'o'}
print(a | b)                       # {'e', 'h', 'o', 'r', 'w', 'd', 'l'}

animals = {'cat', 'dog', 'fish'}
for animal in animals:                 # (may) print
    print(animal)  # cat
    #  fish
    #  dog

for idx, animal in enumerate(animals):  # (may) print
    print(idx, animal)  # 0 cat
    #  1 fish
    #  2 dog

set_e = {x for x in range(1, 101)if x % 2 != 0 and x % 3 != 0 and x % 5 != 0}
print(set_e)

my_set = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'e', 'ee', 'e']

# 利用 set 將不重複的種類印出來
print(set(my_set))  # {'d', 'e', 'b', 'a', 'c', 'ee'}

# 使用 set 把一個句子裡面的字元集合找出來
sentence = 'Today is Tuesday, said tao'
# {'d', 'T', 'i', 'y', 'e', 'u', ' ', 't', ',', 'a', 'o', 's'}
print(set(sentence))

# 新增與刪除
unique_char = set(my_set)  # {'d', 'e', 'b', 'a', 'c', 'ee'}
unique_char.add('x')
unique_char.remove('a')
print(unique_char)      # {'e', 'b', 'c', 'x', 'd', 'ee'}

# 交集與差集
set1 = set(my_set)
set2 = set(sentence)
# 交集：找出 set1 與 set2 都有的元素
print(set1.intersection(set2))  # {'d', 'e', 'a'}
# 差集：找出 set1 裡面有 但是在 set2 裡面沒有的
print(set1.difference(set2))  # {'b', 'c', 'ee'}
