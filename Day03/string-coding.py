# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 7:17
# @Author  : Feng Xiaoqing
# @FileName: string-coding.py
# @Software: PyCharm
# @Function：
#-----------------------------------

#unicode 占2字符
#ansic码 只能存英文和特殊字符
#utf8  中文3个字节

# -*- coding:gbk -*-

s = '你好'
print(s)
s_to_gbk= s.encode('utf8').decode('gbk')
print(s_to_gbk)

