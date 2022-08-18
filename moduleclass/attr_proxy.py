class Wrapper(object):
    def __init__(self, wrappee):
        self.wrappee = wrappee

    def foo(self):
        print('foo')

    def __getattr__(self, attr):
        return getattr(self.wrappee, attr)


class Wrappee(object):
    def bar(self):
        print('bar')

o2 = Wrappee()
o1 = Wrapper(o2)

o1.foo()
o1.bar()
