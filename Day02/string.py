# -*- coding: utf-8 -*-
# @Time    : 2019/8/3 22:26
# @Author  : Feng Xiaoqing
# @FileName: string.py
# @Software: PyCharm
# @Function：
#----------------------------------- 


name = "my\tname is {name} fxqingfeng"

print(name.capitalize())
print(name.count('f'))
print(name.center(50,'-'))
print(name.endswith('g'))
print(name.expandtabs(tabsize=30))  #\t 30bit
print(name.format(name = 'fengxiaoqing',year = 20))
print(name.format_map({'name':'fengxiaoqing','year':20}))#处理字典
print('ab23'.isalpha())
print('ab23'.isalnum())
print('ab23'.isdigit()) #整数
print('1A'.isidentifier())#判断是不是一个合法的标识符
print(' '.isspace())#不是一个合法的标识符
print(' '.istitle())
print('BC'.isupper())
print('BC'.isupper())
print('BSCCdgs'.lower())
print('BSCCdgs'.upper())
print('+'.join(['1','2','3','4']))
print('  afsdfas  '.strip())
print('fxq  \n'.strip())
p = str.maketrans('abce1313f','124535345')

print('alix'.translate(p))
print('abcd'.replace('a','u',1))
print('abcdef'.rfind('b'))
print('alfeng'.split('l'))
print('1+2\n3+4'.splitlines())
print('abc, 65'.swapcase())#大写变小定
print('abdfad'.title())
print('abdfad'.zfill(9))


