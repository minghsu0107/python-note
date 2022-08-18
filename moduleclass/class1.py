class Some:
    def __init__(self, x):
        self.x = x

    def service(self, y):
        print('do service...', self.x + y)


s = Some(10)
s.service(2)  # do service... 12
# same as:
s = Some(10)
Some.service(s, 2)
# s所參考的實例，會綁定至service()的第一個參數
# 在這類的情況下，service()方法是一個綁定方法（Bound method）
# 每個實例會有自己的綁定方法。例如：
s1 = Some(10)
service = s1.service
service(5)    # do service... 15

s2 = Some(20)
service = s2.service
service(5)    # do service... 25

service = Some.service
service(s1, 5)       # do service... 15
service(s2, 5)       # do service... 25

# 如果在定義類別時，類別中的函式沒有任何參數，則該函式無法成為綁定方法


class Other:
    def service():
        print('do service...')


# o = Other()
# o.service()  # TypeError: service() takes no arguments (1 given)
Other.service()     # do service...


class Some:
    @staticmethod
    def service(x, y):
        print('do service...', x + y)


Some.service(10, 20)  # do service... 30

s = Some()
s.service(10, 20)    # do service... 30
# s.service(10)        # TypeError: service() takes exactly 2 positional arguments (1 given)


class Some:
    def __init__(self, x):
        self.x = x

    def service(self, y):
        print('do service...', self.x + y)


class Other:
    pass


o = Other()
o.x = 100
Some.service(o, 200)    # do service... 300
# Some.service()的第一個參數可以任何物件，只要它有個x屬性
