class A(object):
    def __init__(self):
        print("Enter A")
        print("Leave A")


class B(A):
    def __init__(self):
        print("Enter B")
        A.__init__(self)
        print("Leave B")


class C(A):
    def __init__(self):
        print("Enter C")
        A.__init__(self)
        print("Leave C")


class D(A):
    def __init__(self):
        print("Enter D")
        A.__init__(self)
        print("Leave D")


class E(B, C, D):
    def __init__(self):
        print("Enter E")
        B.__init__(self)
        C.__init__(self)
        D.__init__(self)
        print("Leave E")


E()
print()


class A(object):
    def __init__(self):
        print("Enter A")
        print("Leave A")


class B(A):
    def __init__(self):
        print("Enter B")
        # in python3, this equals to super().__init__()
        super(B, self).__init__()
        print("Leave B")


class C(A):
    def __init__(self):
        print("Enter C")
        super(C, self).__init__()
        print("Leave C")


class D(A):
    def __init__(self):
        print("Enter D")
        super(D, self).__init__()
        print("Leave D")


class E(B, C, D):
    def __init__(self):
        print("Enter E")
        super(E, self).__init__()
        print("Leave E")


E()
# 在super機制裏可以保證公共父類(A)僅被執行一次，至於執行的順序，是按照mro進行的（E.__mro__）


class A(object):
    def method1(self):
        print('A.method1')

    def method2(self):
        print('A.method2')


class B(A):
    def method3(self):
        print('B.method3')


class C(A):
    def method2(self):
        print('C.method2')

    def method3(self):
        print('C.method3')


class D(B, C):
    def method4(self):
        print('D.method4')


d = D()
d.method4()  # 在 D 找到，D.method4
d.method3()  # 以 D->B 順序找到，B.method3
d.method2()  # 以 D->B->C 順序找到，C.method2
d.method1()  # 以 D->B->C->A 順序找到，A.method1
