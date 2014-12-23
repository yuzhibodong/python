# -*- coding:utf-8 -*-
def prod(*s):
    return reduce(lambda x,y:x+y,s)

l = [1,2,3,4]

print prod(l)
