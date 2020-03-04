s = "hello"
print(len(s))

s[1]   ## 'e'
s[1:3] ## 'el'
s[1:]  ## 'ello'
s[:3]  ## 'hel'

ord('a')
chr(97)

print(s.replace('ello', 'i'))  # replace() returns a new string
print(s) ## does not change, since string is immutable

x = '  A  '
print(x.strip())
print(x) ## immutable

a = "ab"
b = "cd"
c = a + b
print(c)
c += "e"
print(c)

print("MuQ" * 10)
# "MuQMuQMuQMuQMuQMuQMuQMuQMuQMuQ"

x = "-"
d = "123456"
e = ['1', '2', '3'] # Warning : list裡都要是字串
print(x.join(d))
print(x.join(e))

# 從第start個字開始找str，回傳其index，start可不填
a = "rilak achine pie arbuz"
print(a.find("e "))
# 11
print(a.find("e ",12)) #故意跳過第一個
# 15

a = "Hello world"
print(a[:a.find(" ")])
# "Hello"
print(a[a.find(" ")+1:])
# "world"
print(a[::-1]) # 翻轉 [::-1]會製造一個新的
# "dlrow olleH"
print(a[::-2])

"hello".upper()
# HELLO
"HELLO".lower()
# hello
"123".isalpha()
# False
"abc".isalpha()
# True

# * list可以用來展開list，然後當成function的input
string = "10 : 10 : 10"
print("{}h {}m {}s".format(*string.split(" : ")))

print("{} {}".format(1,2))
# 1 2
print("{0} {1}".format(1,2))
# 1 2
print("{1} {0}".format(1,2))
# 2 1

s = ("this is a very"
     "long string too"
     "for sure ..."
    )
print(s)
# 'this is a verylong string toofor sure ...'
