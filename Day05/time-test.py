#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: time-test.py
@time: 2019/9/3 10:28
"""
import  time

# a = time.sleep(2)

# s = time.time()  #时间戳

# a = time.gmtime() #UTC struct_ime格式
# a = time.gmtime(12341235) #UTC struct_ime格式

# a = time.localtime() #struct_ime格式 本地时间
# a = time.localtime(232465134) #struct_ime格式 本地时间

# x = time.localtime() #struct_ime格式 本地时间
# a = time.mktime(x)  # 转换元组到时间戳

# x = time.gmtime(12341235) #UTC struct_ime格式
# a = time.strftime("%Y-%m-%d %H:%M:%S",x)  # struct---> 格式化字符串


# a = time.strptime("1970-05-23 20:07:15","%Y-%m-%d %H:%M:%S") #格式化字符串 > struct_time

# a = time.asctime() # struct_time ->Tue Sep  3 11:11:19 2019
a = time.ctime(34234) # 时间戳 -> Thu Jan  1 17:30:34 1970

print(a)

