import functools


def log(func):
    def wrapper(*args ,**kw):
        print('before call %s' % func.__name__)
        value = func(*args, **kw)
        print('after call %s' % func.__name__)
        return value
    return wrapper


@log
def sum2(a, b):
    print("%d + %d", (a, b))
    return a+b


sum2(2, 3)