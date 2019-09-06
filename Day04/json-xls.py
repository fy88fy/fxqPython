#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: json-xls.py
@time: 2019/9/2 16:10
"""
#
# import json,xlwt
# def main():
#     with open('chengji.txt','r') as f:
#         for line in f:
#             print(line.strip())

import json,xlwt
def readExcel(file):
    with open(file,'r',encoding='utf8') as f:
        data = json.load(f) # 用json中的load方法，将json串转换成字典
    return data

def writeM():
    a = readExcel('chengji.txt')
    print(a)
    title = ["学号","姓名","语文成绩","数学成绩","英语成绩","总分","平均分"]
    book = xlwt.Workbook() # 创建一个excel对象
    sheet = book.add_sheet('Sheet1',cell_overwrite_ok=True) # 添加一个sheet页
    for i in range(len(title)): # 循环列
        sheet.write(0,i,title[i]) # 将title数组中的字段写入到0行i列中
    for line in a: #　循环字典
        print('line:',line)
        sheet.write(int(line),0,line) #　将line写入到第int(line)行，第0列中
        summ = a[line][1] + a[line][2] + a[line][3] # 成绩总分
        sheet.write(int(line),5,summ) # 总分
        sheet.write(int(line),6,summ/3) # 平均分
        for i in range(len(a[line])):
            sheet.write(int(line),i+1,a[line][i])
    book.save('demo.xls')

if __name__ == '__main__':
    writeM()
# if __name__ == "__main__":
#     main()
