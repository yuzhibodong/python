#---------------------
#数据类型和变量
#---------------------
#多行转义
r'''

'''

#ASCII
A = 65
z = 122
#ASCII转换
ord('A')
chr(65)
#Unicode表示的字符串用u'...'表示
u'A' == u'\u0041'
#把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法
>>> u'ABC'.encode('utf-8')
'ABC'
>>> u'中文'.encode('utf-8')
'\xe4\xb8\xad\xe6\x96\x87'
#英文字符转换后表示的UTF-8的值和Unicode值相等（但占用的存储空间不同）

#反过来，把UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')方法：
>>> 'abc'.decode('utf-8')
u'abc'
>>> '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
u'\u4e2d\u6587'
>>> print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
中文

#当Python解释器读取源代码时，为了让它按UTF-8编码读取，通常在文件开头写上两行
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------
#使用list和tuple
#---------------------
#列表
list []
#最后一个元素的索引
len(list)-1
list[-1]
#类推倒二
list[-2]
#追加元素到末尾
list.append('test')
#元素插入到1位置
list.insert(1, 'test')
#删除末尾元素
list.pop()
#删除指定位置元素
list.pop(i)
#替换
list[1] = 'test'

#元组
#tuple一旦初始化就不能修改
#也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的
#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
tuple()
#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
>>> t = (1, 2)
#定义一个只有1个元素的tuple,必须加一个逗号,，来消除歧义
#Python显示只有1个元素的tuple时，也会加一个逗号,以免误解成数学计算意义上的括号
t = (1,)

#---------------------
#条件判断和循环
#---------------------
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
if x:
    print 'True'

#---------------------
#字典
#无序
#---------------------
#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#init
d = {'Michael': 95, 'Tracy': 85}
#添加
d['Adam'] = 67
#判断Key是否存在1
>>>'Thomas' in d
False
#判断Key是否存在2
#如果key不存在，可以返回None，或者自己指定的value：
#注意：返回None的时候Python的交互式命令行不显示结果。
>>> d.get('Thomas')
>>> d.get('Thomas', -1)
-1

#------------------------------------------------------
#set
#无序
#------------------------------------------------------
#set和dict的唯一区别仅在于没有存储对应的value

#init 需要一个list, 但是s内的并不是list,所以s内不能存在变量 且重复值会被过滤
>>>s = set([1, 2, 3, 1])
>>>s
set([1, 2, 3])
#增删
s.add(4)
s.remove(4)
#set 可看成无序和无重复的集合, 可做交 并集操作
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
set([2, 3])
>>> s1 | s2
set([1, 2, 3, 4])

#------------------------------------------------------
#函数参数
#------------------------------------------------------
def fn(a, b, c=0, *args, **kw):
#必选参数, 默认参数, 可变参数, 关键字参数
#*args是可变参数，args接收的是一个tuple
#**kw是关键字参数，kw接收的是一个dict。
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
    print 'a=', a, ' b=', b, ' c=', c, ' args=', args, ' kw=', kw
print '\n==>fn(1, 2)'
fn(1, 2)
print '\n==> fn(1, 2, 3)'
fn(1, 2, 3)
print '\n==> fn(1, 2, 3, 4)'
fn(1, 2, 3, 4)
print '\n==> fn(1, 2, k1=8, k2=9)'
fn(1, 2, k1=8, k2=9)
print '\n==> fn(1, 2, 3, k1=8, k2=9)'
fn(1, 2, 3, k1=8, k2=9)
print '\n==> fn(1, 2, 3, 4, k1=8, k2=9)'
fn(1, 2, 3, 4, k1=8, k2=9)
# interesting part:
print '\n==> fn(*(1, 2))'
fn(*(1, 2))
print '\n==> fn(*(1, 2, 3))'
fn(*(1, 2, 3))
print '\n==> fn(*(1, 2, 3, 4))'
fn(*(1, 2, 3, 4))
print '\n==> fn(*(1, 2, 3, 4), **{ \'k1\': 8, \'k2\': 9 })'
fn(*(1, 2, 3, 4), **{ 'k1': 8, 'k2': 9 })
# TypeError: fn() takes at least 2 arguments (1 given)
print '\n==> fn(*(1, ))'
fn(*(1, ))

#------------------------------------------------------
#切片(Slice)
#list和tuple均支持
#------------------------------------------------------
l = range(100)
#从第二开始 取到10(不含), 步长2
l[1:10:2]
#倒数第一个和第二个元素
l[-2:-1]
#逆序list
l[::-1]

#------------------------------------------------------
#迭代
#------------------------------------------------------
d = {'a': 1, 'b': 2, 'c': 3}

#d.iterkeys()   a, b, c
#d.itervalues() 默认 1, 2, 3
#d.iteritems()  ('a', 1)('c', 3)('b', 2)
for x in d.iteritems():
    print x

#判断对象是否可迭代
>>>from collections import Iterable
>>>isinstance('abc', Iterable) #str是否可迭代
True

#对list实现类似Java那样的下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print i, value

#------------------------------------------------------
#生成器(generator)
#保存的是算法
#------------------------------------------------------
#方法一 由List生成
g = (x for x in range(10))
for x in g:
    print x
#方法二 由函数生成
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        #··· “=”右边先进行计算，即生成一个新的tuple：（b,a+b），之后依次赋值给左边a,b。在内存里是开辟了一个新空间来存储这个计算结果的
        a, b = b, a + b
        n = n + 1

for x in fib(6):
    print x

#------------------------------------------------------
#高阶函数
#map/reduce
#------------------------------------------------------
#map 序列依次代入第一个函数
#reduce 序列[1, 2]return的值再与后面的第三项作用  f(f(x1, x2),x3)
def char2num(s):
    #等价 d{...}   d['1']
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))

#------------------------------------------------------
#闭包(closure)
#难点 仍未完全理解
#------------------------------------------------------
#sum可以直接使用args, 且返回函数本身
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
