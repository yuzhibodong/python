#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
#Unicode表示的字符串用u''表示
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
    #等价 d{}   d['1']
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

#------------------------------------------------------
#偏函数
#给函数设定默认参数并生成新函数
#------------------------------------------------------
import functools

#int 参数从base进制转换为10进制
#4
print int('100', base=2)
#4
int2 = functools.partial(int, base=2)
print int2()
#多参数固定
fun3 = functools.partial(fun, b=2, c=3)

#------------------------------------------------------
#别名
#------------------------------------------------------
#应用场景
try:
    import cStringIO as StringIO #cStringIO用C写的 速度快
except ImportError: # 导入失败会捕获到ImportError
    import StringIO

#------------------------------------------------------
#类(Class)和实例(Instance)
#类内函数(Method)第一个参数永远是实例变量self,
#并且,调用时,不用传递该参数
#成员不需要预定义,可以直接在实例中增加(不影响其他实例)
#------------------------------------------------------

#------------------------------------------------------
#获取对象信息
#------------------------------------------------------
#-----------type()
#判断对象的引用  的类型
>>>type(123)
<type 'int'>
>>>import types
>>>type('abc')==types.StringType
>>>type(int)==types.TypeType
#---------instance()
isinstance('a', str)
#判断变量是某些类型中的一种
isinstance('a', (str, unicode))
#-------------dir()
#获得一个对象的所有属性和方法
>>>dir('abc')
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.xclass MyObject(object):
obj = MyObject()
hasattr(obj, 'x') #是否存在?True
setattr(obj, 'y', 19) #设置
getattr(obj, 'y') #获取属性
getattr(obj, 'y', 404) #获取属性,若不存在,返回默认值404

#------------------------------------------------------
#__slots__
#限定可以绑定的方法和属性
#仅对当前类起作用, 子类需增加__slots__才能继承
#------------------------------------------------------
class Sample(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的属性

#------------------------------------------------------
#定制类
#下列均为方法
#------------------------------------------------------

#__str__()-----------------
#定义打印类时输出(用户)
c = class()
print '%s' % c
#__repr__()----------------
#定义直接显示变量时输出(开发者), 且一般与__str__一致
__repr__ = __str__
print '%r' % c

#__iter__()-----------------
#实现循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值
for n in Fib():
    print n

#__getitem__()-----------------
#自定义实现类似list[1]取出下标元素的方法名

#__getattr__()-----------------
#动态返回属性或者方法, 区别为返回值, 见下面
#此方法默认返回None, 否则需要抛出AttributeError
#当调用不存在的属性或者方法时,会尝试调用__getattr__来获得
def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        elif attr=='name':
            return 'Hello'
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s.name #attr return attr
s.age() #method return lambda: attr

#这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
#这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

#上述用例 SDK调用API时
class Chain2(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print 'self._path:{0}\tpath:{1}'.format(self._path, path)
        #返回一个完整的字符串作为新的Chain2的输入
        return Chain2('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, user):
        print 'self._path:{0}\tuser:{1}'.format(self._path, user)
        return Chain2('%s/%s' % (self._path, user))

#/users/:user/repos
print Chain2().users('michael').repos

#__call__()-----------------
# s()状态下(即实例(instance)本身上调用)调用, 而不是调用s.method()
#此时对象和函数的界限已区别不大
#没有__call__,返回TypeError

#判断一个变量是否能被调用
>>>callable(Chain2())
True
>>>callable(max)
True
>>>callable('string')
False

#------------------------------------------------------
#错误处理
#错误捕获可以跨越多层调用, 即子函数错误可由父函数捕获
#------------------------------------------------------

#常见的错误类型和继承关系
https://docs.python.org/2/library/exceptions.html#exception-hierarchy

#trt
#try运行,执行出错,跳转except
try:
    pass
#捕获异常,处理后跳转finally
except Exception, e:
    raise
#如果没有捕获错误, 则会执行else
else:
    pass
#可没有, 如果存在finally, 则一定会执行
finally:
    pass

#logging
#记录错误, 捕获错误后程序会继续执行
########
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'
########

#raise
#raise语句如果不带参数，就会把当前错误原样抛出
#此例中捕获错误后有raise错误,在于当前函数不知道怎么处理错误,继续向上抛出,让上层调用者处理
#raise还可以抛出其他类型错误(转换错误类型,但应做到逻辑合理)
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise

def main():
    bar('0')

main()

#------------------------------------------------------
#调试
#------------------------------------------------------

#断言
#如果表达式false, 输出后半句, 同时抛出AssertionError
assert n!=0, 'n is zero!'
#程序运行时可以用-O参数关闭, 此时assert语句相当于 pass
python -O err.py

#logging
#允许指定信息记录的级别,debug, info, warning, error
import logging
#指定level=INFO时,logging,debug就不起作用了,类推
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n

#pdb
#单步调试
#l 查看代码
#n 下一步
#s 步进
#h help
#p [变量] 查看变量值
#q 结束调试
$ python -m pdb err.py

#pdb.set_trace()
#p 查看变量
#c 继续运行
#err.py
import pdb
..........
pdb.set_trace() #运行到这里自动暂停
..........

#------------------------------------------------------
#文件读写
#------------------------------------------------------
#with语句来自动帮我们调用close()方法
with open('/path/to/file', 'r') as f:
    print f.read()
#读取非ASCII编码的文本文件, 必须要二进制打开, 再解码
import codecs
with codecs.open('/usr/michael/gbk.txt', 'r', 'gbk') as f:
    f.read() #u'\u6d4b\u8bd5'

#文件写入同读取 'w' 'wb'->二进制

#------------------------------------------------------
#操作文件和目录
#------------------------------------------------------
#显示操作系统名称
os.name #nt->Windows posix->Linux Unix Mac OS X
#获取系统详细信息(非Windows)
os.uname
#环境变量
os.environ #查看
os.getenv('PATH') #获取
#操作文件和目录
import os.path
#查看当前目录的绝对路径
os.path.abspath('.')
#当前目录下新建目录
os.mkdir('./testdir')
#删除目录
os.rmdir('./testdir')

#路径合成,不要直接拼接字符串, 可以正确处理不同操作系统的路径分隔符
#不要求路径真实存在,仅是对字符串进行操作
os.path.join('./part-1', 'part-2')
#Linux/Unix/Mac
part-1/part-2
#Windows
part-1\part-2
#路径拆分
os.path.split()
#拆分路径, 后一部分总是最后级别的目录或文件名
>>>os.path.split('Users/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
#可以直接得到文件扩展名
>>>os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')

#重命名
os.rename('test.txt', 'test.py')
#删除文件
os.remove('test.py')
#复制,不在os模块, 在shutil中
import shutil
shutil.copyfile(src, dst)

#列出当前目录下的所有目录(利用Python的特性来过滤文件)
x for x in os.listdir('.') if os.path.isdir(x)
#列出所有.py文件
x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'

#------------------------------------------------------
#序列化
#------------------------------------------------------
#cPickle是C语言写的,速度快,pickle是纯Python写的
#仅能用于Python
try:
    import cPickle as pickle
except ImportError:
    import pickle

#把对象序列化为一个str
d = dict()
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
#反序列化
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()

#JSON
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d) #dumps返回一个str,内容是标准JSON
#反序列化
>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
>>> json.loads(json_str)
{u'age': 20, u'score': 88, u'name': u'Bob'}
#dumps,loads 针对字符串, dump load 针对file-like Object
#反序列化得到的所有字符串对象默认都是unicode而不是str。由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。

#------------------------------------------------------
#多进程
#multiprocessing
#------------------------------------------------------

#进程池
#Pool
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time() #起始时间
    time.sleep(random.random() * 3) #延时
    end = time.time() #停止时间
    #%0.2f 0->有效数字位数 .2->小数点后保留位数
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    print 'Parent process %s' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocess done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
