n = int(input("please enter a number"))
if (n == 2):
    print("2 is a prime number!")
else:
    for i in range(2, n):
        if (n % i == 0):
	    print("{} is not a prime number!".format(n))
	    break
    else:
        print("{} is a prime number!".format(n))

# 如果for迴圈被完整執行, 那就執行else的部份. 
# 如果迴圈被中斷了(break), 那else的部份也不會被執行.
