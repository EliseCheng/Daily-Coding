#! /usr/bin/env python
#coding=utf-8
from time import ctime

def tcfunc(func):
    #import pdb
    #pdb.set_trace()
    def wrappedFunc():
        print '[%s] %s() called' %(ctime(), func) #5
        #return func()
    print "in tcfunc called" #1
    print "wrapped func %s" %wrappedFunc #2
    print "--------------------------" #3
    return wrappedFunc

# decorator
# 仅调用tcfunc函数，该函数将foo作为一个参数，返回一个
# wrappedFunc函数对象，用该对象来取代foo函数在外部的调用，foo
# 定义的函数只能够在内部进行调用，外部无法获取其调用方式！！
@tcfunc         # call sequence is : tcfunc(func) --> wrappedFunc -- > func
def foo():
    print "+++++++++" #6
    print "in foo called" #7
    pass
print "foo func : %s" %foo #4
foo()
