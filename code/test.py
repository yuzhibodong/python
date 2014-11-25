import functools

def fun(a, b, c):
    return a+b+c

fun3 = functools.partial(fun, b=2, c=3)

print fun3(1)

int2 = functools.partial(int, '100', base=2)

print int2()
