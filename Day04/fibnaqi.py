# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 22:54
# @Author  : Feng Xiaoqing
# @FileName: fibnaqi.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
def fib(max): #10
    n, a, b = 0, 0, 1
    while n < max: #n<10
        #print(b)
        yield b
        a, b = b, a + b
        #a = b     a =1, b=2, a=b , a=2,
        # b = a +b b = 2+2 = 4
        n = n + 1
    return '---done---'
# f = fib(10)
# print(f.__next__())
# print("###########")
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

g = fib(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
