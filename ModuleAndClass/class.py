class Greeter:
    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable
        self.__age = 100  # private(but can still access; not encouraged)
    # Instance method

    def greet(self, loud=False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)


g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"
# print(g.__age) cannot access
print(g._Greeter__age)  # 100

print(g.__dict__)
print(vars(g))

# 為類別動態地添加方法


class Some:
    def __init__(self, x):
        self.x = x


s = Some(1)
Some.service = lambda self, y: print('do service...', self.x + y)
s.service(2)    # do service... 3
