#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: top.py
@time: 2019/9/2 16:36
"""
import json,xlwt
def readExcel(file):
    with open(file,'r',encoding='utf8') as f:
        data = json.load(f) # 用json中的load方法，将json串转换成字典
    return data

def writeM():
    a = readExcel('top1.txt')
    print(a)
    title = ["NO","IFACE","rxpck/s","txpck/s"]
    book = xlwt.Workbook() # 创建一个excel对象
    sheet = book.add_sheet('Sheet1',cell_overwrite_ok=True) # 添加一个sheet页
    for i in range(len(title)): # 循环列
        sheet.write(0,i,title[i]) # 将title数组中的字段写入到0行i列中
    # for line in a: #　循环字典
    #     print('line:',line)
    #     sheet.write(int(line),0,line) #　将line写入到第int(line)行，第0列中
    #     for i in range(len(a[line])):
    #         sheet.write(int(line),i+1,a[line][i])
    book.save('top1.xls')

if __name__ == '__main__':
    writeM()
