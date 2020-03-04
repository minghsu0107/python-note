a = b = c = 20
age, name = 18, "ming"
# age = 18, name = "ming"
del a

num = 34
flag = True
str1 = 'he says "hello"'
print(str1)

print(100, "hi", 60)
print(100, "hi", 60, sep="&") 
print(100, 60, sep="&", end="") #do not change line at last
print('')
print("%3s  %2d  %3d  %3d  %3d" % ("ming", 1, 100, 95, 7))

print("%5d %5s %8.2f" % (300, "hello", 24.567))

name = "ming"
score = 112
print("{}'s score is {}".format(name, score))

print(type(56))
print(type(True))
print(type("hello"))

num1 = 5 + 7.8 #12.8, float
num2 = 5 + True #6, int

num3 = 34 + int("67")
score = 60
print("her score is " + str(score))
print(10 // 3)