score = input("please enter a number")  # input read a whole line
print(score)

a = 2
b = 4
print(b // a)
print(b**2)

if (not (a > b)):
    print("ya")

elif (a % 2 == 0):
    print("hoo")
else:
    print("oh")

list1 = [1, 2, 3, 4, 5]
list2 = ["banana", 1, True, "apple"]
print(list2[0])
print(list2[-1])
print(list2[-2])

list3 = [[1, 2], [3, 4], ["John", "Marry", "Ming"]]
print(list3[2][1])

list4 = range(5)  # 0 to 4
list5 = range(3, 8)  # 3 to 7
list6 = range(-6, -2)  # -6 to -3
list7 = range(3, 8, 2)  # 3, 5, 7
list8 = range(8, 3, -1)  # 8, 7, 6, 5, 4
print(list7[2])

for s in list2:
    print(s, end=",")
print("")

for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        print("%d*%d=%-2d  " % (i, j, product), end="")
        # -2d: width = 2 char; aligned with left
    print()

for i in range(1, 11):
    if (i == 6):
        break
    if (i == 3):
        continue
    print(i, end=",")
print()
