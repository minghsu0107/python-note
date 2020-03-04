class Rational:
    def __init__(self, n, d):  # 物件建立之後所要建立的初始化動作
        self.numer = n
        self.denom = d
    
    def __str__(self):   # 定義物件的字串描述
        return str(self.numer) + '/' + str(self.denom)
    
    def __add__(self, that):  # 定義 + 運算
        return Rational(self.numer * that.denom + that.numer * self.denom, 
                        self.denom * that.denom)
    
    def __sub__(self, that):  # 定義 - 運算
        return Rational(self.numer * that.denom - that.numer * self.denom,
                        self.denom * that.denom)
                           
    def __mul__(self, that):  # 定義 * 運算
        return Rational(self.numer * that.numer, 
                        self.denom * that.denom)
        
    def __truediv__(self, that):   # 定義 / 運算
        return Rational(self.numer * that.denom,
                        self.denom * that.denom)

    def __eq__(self, that):   # 定義 == 運算
        return self.numer * that.denom == that.numer * self.denom

x = Rational(1, 2)
y = Rational(2, 3)
z = Rational(2, 3)
print(x)       # 1/2
print(y)       # 2/3
print(x + y)   # 7/6
print(x - y)   # -1/6
print(x * y)   # 2/6
print(x / y)   # 3/6
print(x == y)  # False
print(y == z)  # True