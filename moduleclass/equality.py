# 如果你定義了類別時沒有定義__eq__()方法，
# 則預設使用==比較兩個實例時，會得到與使用is比較相同的結果
# is will return True if two variables point to the same object
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, name, value):
        if not name in self.__dict__:
            self.__dict__[name] = value
        elif name == 'x' or name == 'y':
            raise TypeError('Point(x, y) is immutable')

    def __eq__(self, that):
        if not isinstance(that, Point):
            return False
        return self.x == that.x and self.y == that.y

    def __hash__(self):
        return 41 * (41 + self.x) + self.y


p1 = Point(1, 1)
p2 = Point(1, 1)
print(p1 == p2)    # True
print(p1 is p2)    # False

# rule to obey:
# 在同一個應用程式執行期間，對同一物件呼叫 __hash__()方法，必須回傳相同的整數結果。
# 如果兩個物件使用__eq__()測試 結果為相等, 則這兩個物件呼叫__hash__()時，必須獲得相同的整數結果。
# z如果兩個物件使用 __eq__()測試結果為不相等, 則這兩個物件呼叫__hash__()時，可以獲得不同的整數結果。


pset = {p1}
print(p1 in pset)  # True
print(p2 in pset)  # True, since hash is same, and __eq()__ is true
# p1.x = 2   # TypeError: Point(x, y) is immutable


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, that):
        if not isinstance(that, Point):
            return False
        return self.x == that.x and self.y == that.y


class Point3D(Point):
    def __init__(self, x, y, z):
        super(Point3D, self).__init__(x, y)
        self.z = z

    def __eq__(self, that):
        if not isinstance(that, Point3D):
            return False
        return super(Point3D, self).__eq__(that) and self.z == that.z


p1 = Point(1, 1)
p2 = Point3D(1, 1, 1)

print(p1 == p2)
# 在繼承的情況下，若==兩旁運算元有一個是子類別實例，則會使用子類別的__eq__()版本進行比對
