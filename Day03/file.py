# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 7:12
# @Author  : Feng Xiaoqing
# @FileName: file.py
# @Software: PyCharm
# @Function：
#----------------------------------- 

with  open('password','r',encoding='utf-8') as f,\
     open('password4','w',encoding='utf-8') as f_new:
        for line in f:
            if 'fxq' in line:
                line = 'fxq:12345678'
            f_new.write(line)