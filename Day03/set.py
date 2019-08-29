#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: set.py
@time: 2019/8/8 20:11
"""


def main():
    list_1 = [1,4,6,6,3,6,3,3,7]
    list_1 =set(list_1)

    list_2 = set([2,5,6,22,33,4])
    print(list_1,list_2)
#交集
    print(list_1.intersection(list_2))
    print(list_1 & list_2)

#并集
    print(list_1.union(list_2))
    print(list_1 | list_2)

#差集(in list_1  but not in list_2)
    print(list_1.difference(list_2))
    print(list_1 - list_2)

#子集
    list_3 = set([1,3,7])
    print(list_1.issubset(list_2))
    print(list_3.issubset(list_1))

#父集
    print(list_1.issuperset(list_2))

#对称差集：把重复的去掉
    print(list_1.symmetric_difference(list_2))
    print(list_1 ^ list_2)

#############################################################
    print('----------------------')

    #list_2.isdisjoint()
    list_4 = set([1,4,5,7])
    list_4.add('9889')
    print(list_4)
    list_4.update([11,33,44,66])
    print(list_4)
    print(list_4.remove(11))#删除不存在时候会报错
    print(list_4.pop()) #随意删除,并返回删除的值
    list_4.discard('9888') #删除不存在时候，也删除不会报错
    print(list_4)
#长度
    print(len(list_4))
#是否在其中
    if 33 in list_4:
        print('in')
if __name__ == "__main__":
    main()
