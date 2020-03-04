# a decorator adds additional function to the original function
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "a":
                print("level a")
            elif level == "b":
                print("level b")
            return func(*args, **kwargs)
        return wrapper

    return decorator

@use_logging(level="a") # pass parameter to the decorator
def foo(name='foo'):
    print("i am %s" % name)

foo()
'''
level a
i =am foo
'''

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()
'''
class decorator runing
bar
class decorator ending
'''