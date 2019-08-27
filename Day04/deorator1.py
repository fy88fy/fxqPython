# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 23:36
# @Author  : Feng Xiaoqing
# @FileName: deorator1.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
def bar():
    print("in the bar.")

def foo():
    print("in the foo.")
    bar()

foo()




def foo(func):
    def war():
        print("head")
        func()
        print("end")
    return war

@foo
def bar():
    print("in the bar.")

bar()

#匿名函数
calc = lambda x:x*3
print(calc(2))