# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 23:12
# @Author  : Feng Xiaoqing
# @FileName: neizhi_fangfa.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
#abs()
print(abs(-11))

#all() 非0为真
print(all([1,-5,3]))

#any() 有一个为真，就是真，
print(any([]))

#ascii() 变成字符串类型
print(ascii([1,3,'哎呀']))

#bin() 把10进制整数转二进制
print(bin(8))

#bool()
print(bool(0))

#bytearray()
print(bytes(98))

#callable() 是否可调用，函数，可加括号
def sa():pass
print(callable(sa()))

#chr()
print(chr(67))

#ord('b') >assic
print(ord('c'))

#exec()执行字符串
code = '''
print(123)
'''
print(exec(code))

#dir() 看有什么方法

#divmod()

#enumerate()

#eval 字符串变成字典

#filter() 过滤
calc = lambda n:3 if n<4 else n
print(calc(5))

res = filter(lambda n:n>5,range(10))
for i in res:
    print(i)

res = map(lambda n:n*n,range(10))
for i in res:
    print(i)

#reduce()
import functools
res1 = functools.reduce(lambda x,y:x+y,range(10))
print(res1)

#globals() 看程序所有的变量。

#hash() md5

#hex(15) 转成16进制

#locals()

#oct() 转8进制
print(oct(8))

#
#pow(3.2)  3的2次方

#round() 保留多少位小数
print(round(1.334,2))

#sorted() 排序
a = {6:2,8:0,1:4,-5:6,99:11,4:22}
print(a)
print(sorted(a.items()))