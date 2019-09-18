# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 7:08
# @Author  : Feng Xiaoqing
# @FileName: fanshe.py
# @Software: PyCharm
# @Function：
#-----------------------------------

# def bulk(self):
#     print("%s is yall....," %self.name)
# class Dog(object):
#
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self,food):
#         print("%s is eating %s"  % (self.name,food))
#
# d = Dog("wangxiao")
# choice = input(">>:").strip()

names = ['fxq','ttt']
data = {}
try:
    open('1.xtx')
    data['name']
    names[3]
    a = 1
except (IndexError,KeyError) as e:
    print("No index.",e)
except Exception as e:
    print("未知错误")

else:
    print("一切正常")

finally:
    print("不管有没有错都执行，END")