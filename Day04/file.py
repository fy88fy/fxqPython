#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: file.py
@time: 2019/9/2 18:38
"""

import xlwt
import json

# 创建excel工作表
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')

# 设置表头
worksheet.write(0, 0, label='PER')
worksheet.write(0, 1, label='NUM')
worksheet.write(0, 2, label='USER')
worksheet.write(0, 3, label='GROUP')
worksheet.write(0, 4, label='SIZE')
worksheet.write(0, 5, label='MON')
worksheet.write(0, 6, label='DATE')
worksheet.write(0, 7, label='TIME')
worksheet.write(0, 8, label='NAME')

def count():
    count = 0
    # for index, line in enumerate(open('file.txt','r')):
    #     # print(count)


    with open('file.txt', 'r') as f:
        for line in f:
            line = line.replace('\t',',')
            print(count, line.strip())
            count += 1
            # worksheet.write(count, 1, value)

# 读取json文件
count=count()

        # worksheet.write(val2, 1, value)





# # 将json字典写入excel
# # 变量用来循环时控制写入单元格，感觉有更好的表达方式
# val1 = 1
# val2 = 1
# val3 = 1
# val4 = 1
# for list_item in data:
#  for key, value in list_item.items():
#   if key == "NAME":
#    worksheet.write(val1, 0, value)
#    val1 += 1
#   elif key == "LEN":
#    worksheet.write(val2, 1, value)
#    val2 += 1
#   elif key == "ID":
#    worksheet.write(val3, 2, value)
#    val3 += 1
#   elif key == "OTHER":
#    worksheet.write(val4, 3, value)
#    val4 += 1
#   else:
#    pass

# 保存
workbook.save('file.csv')
