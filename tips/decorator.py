# a decorator adds additional function to the original function
import time
from functools import wraps


# use functools.wraps to keep foo.__name__ and foo.__doc__
def use_logging(level):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if level == "a":
                print("level a")
            elif level == "b":
                print("level b")
            return func(*args, **kwargs)
        return wrapper

    return decorator

@use_logging(level="a")  # pass parameter to the decorator
def foo(name='foo'):
    print("i am %s" % name)

foo()
'''
level a
i am foo
'''

class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')

@Foo
def bar():
    print('bar')

bar()
'''
class decorator runing
bar
class decorator ending
'''

def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' %
              (f.__name__, (time2 - time1) * 1000.0))
        return ret
    return wrap

@timing
def run():
    for i in range(1000):
        continue

run()
