# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 7:50
# @Author  : Feng Xiaoqing
# @FileName: file.py
# @Software: PyCharm
# @Function：
#----------------------------------- 

# f = open('password','r',encoding='utf-8')
# f_new = open('password2','w',encoding='utf-8')
# for line in f:
#     if 'fxq' in line:
#         line = 'fxq:12345678'
#     f_new.write(line)
# f.close()
# f_new.close()


#
with  open('password','r',encoding='utf-8') as f:
    with open('password4','w',encoding='utf-8') as f_new:
        for line in f:
            if 'fxq' in line:
                line = 'fxq:12345678'
            f_new.write(line)

