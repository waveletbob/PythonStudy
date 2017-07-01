#coding=utf-8
#函数式编程
lambda_add=lambda x,y:x+y

def  greeter():
	print "hello"
def repeat(fn,times):
	for i in range(times):
		fn()
repeat(greeter,5)

#闭包
a=0
def get_a():
	return a
get_a()
a=3
print(get_a())

#装饰器
import time  
def timeit(func):  
    def wrapper():  
        start = time.clock()  
        func()  
        end =time.clock()  
        print 'used:', end - start  
    return wrapper  

@timeit  
def foo():  
    print 'in foo()'  
foo()  

#內建函数
#Comprehensions
num=[1,4,-5,10,-7,2,3,-1]
# filtered_and_squared=[]

# for number in num:
# 	if number>0:
# 		filtered_and_squared.append(number**2)
# print filtered_and_squared

# filtered_and_squared=map(lambda x:x**2,filter(lambda x:x>0,num))
# print filtered_and_squared 

filtered_and_squared=[x**2 for x in num if x>0]
print filtered_and_squared

def square_generator(optional_parameter):
	return (x**2 for x in num if x>optional_parameter)

for k in square_generator(2):
	print k
g=list(square_generator(1))
print g

alist=['a1','a2','a3','a4']
blist=['1','2','3','4']
for a,b in zip(alist,blist):
	print a,b

# import os
# def tree(top):
#     for path, names, fnames in os.walk(top):
#         for fname in fnames:
#             yield os.path.join(path, fname)
 
# for name in tree('C:\Users\\bob\Downloads'):
#     print name

#装饰器
import time
from functools import wraps
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper
@timethis
def countdown(n):
    while n > 0:
        n -= 1
countdown(100)

# class decorator(object):
#     def __init__(self, f):
#         print("inside decorator.__init__()")
#         f() # Prove that function definition has completed
#     def __call__(self):
#         print("inside decorator.__call__()")
# @decorator
# def function():
#     print("inside function()")
# print("Finished decorating function()")
# function()

# def decorator(func):
#     def modify(*args, **kwargs):
#         variable = kwargs.pop('variable', None)
#         print variable
#         x,y=func(*args, **kwargs)
#         return x,y
#     return modify 
# @decorator
# def func(a,b):
#     print a**2,b**2
#     return a**2,b**2
# func(a=4, b=5, variable="hi")
# func(a=4, b=5)

class demo(object):
	pass
obj=demo()
print "class of obj is {0}".format(obj.__class__)
print "class of obj is {0}".format(demo.__class__)


class Celsius(object):
    def __init__(self, value=0.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)
class Temperature(object):
    celsius = Celsius()
temp=Temperature()
print(temp.celsius) #calls Celsius.__get__
import weakref
class lazyattribute(object):
    def __init__(self, f):
        self.data = weakref.WeakKeyDictionary()
        self.f = f
    def __get__(self, obj, cls):
        if obj not in self.data:
            self.data[obj] = self.f(obj)
        return self.data[obj]
class Foo(object):
    @lazyattribute
    def bar(self):
        print "Being lazy"
        return 42
f = Foo()
print f.bar
# Being lazy
# 42
print f.bar
# 42

import time
class demo:
    def __init__(self, label):
        self.label = label
 
    def __enter__(self):
        self.start = time.time()
 
    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))
with demo('counting'):
    n = 10000000
    while n > 0:
        n -= 1

from contextlib import contextmanager
import time
@contextmanager
def demo(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start)) 
with demo('counting'):
    n = 10000000
    while n > 0:
        n -= 1

matrix=[[1,2,3],[4,5,6]]
res=zip(*matrix)
calculator{
	'plus':lambda x,y:x+y,
	'minus':lambda x,y:x-y
}
res=calculator['plus'](2,3)
def my_function():
	"""
	hello worlkajfk
	"""
	pass
print my_function.__doc__


#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#导入
from module import name
name()
from module import name as myname
#调试
if __name__ == '__main__':
	foo()
with open('','a') as f:
	f.write('hello world')
#上下文管理器
class OpenContext(object):

    def __init__(self, filename, mode):
        self.fp = open(filename, mode)

    def __enter__(self):
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()


with OpenContext('/tmp/a', 'a') as f:
    f.write('hello world')

from contextlib import contextmanager


@contextmanager
def make_open_context(filename, mode):
    fp = open(filename, mode)
    try:
        yield fp
    finally:
        fp.close()
with make_open_context('/tmp/a', 'a') as f:
    f.write('hello world')
#total ordering
@functools.total_ordering
class Size(object):
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value < other.value
 	def __eq__(self, other):
		return self.value == other.value
#调试找bug常用
import sys
def get_cur_info():
    print sys._getframe().f_code.co_filename  # 当前文件名
    print sys._getframe(0).f_code.co_name  # 当前函数名
    print sys._getframe(1).f_code.co_name　# 调用该函数的函数的名字，如果没有被调用，则返回module
    print sys._getframe().f_lineno # 当前行号
#自省（反射）
import inspect
def add(a, b=1):
	return a + b
inspect.getsourcelines(add)
inspect.getargspec(add)
inspect.getcallargs(add, 10, 2)
inspect.isclass(add)
inspect.isfunction(add)

#Mixin模式
#兼容2.3版本导入
try:
    from UserDict import DictMixin
except ImportError:
    from collections import MutableMapping as DictMixin
class MyDict(DictMixin):
    def __init__(self, dict=None, **kwargs):
        self.data = {}
        if dict is not None:
            self.update(dict)
        if len(kwargs):
            self.update(kwargs)

    def __getitem__(self, id):
        return self.data[id]

    def __setitem__(self, id, value):
        self.data[id] = value

    def __delitem__(self, id):
        del self.data[id]

    def keys(self):
        return self.data.keys()
