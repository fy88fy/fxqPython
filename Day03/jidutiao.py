# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 7:30
# @Author  : Feng Xiaoqing
# @FileName: jidutiao.py
# @Software: PyCharm
# @Function：
#-----------------------------------
import  sys,time

for i in range(20):
    sys.stdout.write('>')
    sys.stdout.flush()
    time.sleep(0.2)

print("\n")


for i in range(1,101):
    print('>'* i+("(%s" %i+"%)" ))
    time.sleep(0.1)