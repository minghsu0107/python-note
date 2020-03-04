abs(-5) # 5
chr(65) # A
divmod(44, 6) # (7, 2)
float("56") # 56.0
hex(34) # ox22
int(34.21) # 34
oct(34) # 0o42
pow(2, 3) # 2^3
round(45.8) # 46
round(3.75, 1) # 3.8 (round two one digit after decimal)
sorted([3, 1, 7, 5]) # [1, 3, 5, 7]
sorted([3, 1, 7, 5], reverse=True) # [7, 5, 3, 1]
str(56) # "56"
sum([1, 3, 5, 7]) # 16
type(34.0) # <class 'float'>

def sum(a, b, c = 0):
    return a + b + c

print(sum(10, 20, 30))   # 顯示 60
print(sum(10, 20))       # 顯示 30
print(sum(c = 30, a = 10, b = 20))  # 顯示 60