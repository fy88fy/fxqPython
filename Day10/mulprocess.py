# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 7:39
# @Author  : Feng Xiaoqing
# @FileName: mulprocess.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
from multiprocessing import Process
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("\n\n")


def f(name):
    info('\033[31;1mcalled from child process function f\033[0m')
    print('hello', name)

if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    p = Process(target=f, args=('bob',))
    p.start()
    # p.join()