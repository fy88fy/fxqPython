# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 8:15
# @Author  : Feng Xiaoqing
# @FileName: manager2.py
# @Software: PyCharm
# @Function：实现进程之间数据的共享
#-----------------------------------
#实现进程之间数据的共享
from multiprocessing import Process, Manager
import os
def f(d, l):
    d[os.getpid()] =os.getpid()
    l.append(os.getpid())
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict() #{} #生成一个字典，可在多个进程间共享和传递

        l = manager.list(range(5))#生成一个列表，可在多个进程间共享和传递
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list: #等待结果
            res.join()

        print(d)
        print(l)
