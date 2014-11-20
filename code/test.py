def add(x):
    return x+1

# def my_map(fun, *args):
#     L = []
#     L.append(fun(x) for x in args)
#     return L

# print my_map(add, [1, 2, 3])
def my(f, l):
    return [f(i) for i in l]

print my(add, [1, 2])

def prod(*l):
    return reduce(lambda x, y: x * y, l)

print prod([1,2,3])
