#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: file.py
@time: 2019/8/8 20:47
"""


def main():
    #data = open('sing.txt',encoding='utf-8').read()
    #print(data)
    f1 =open('sing.txt','r',encoding='utf-8')#文件句柄
    # print(f.read())

# #wirte
#     f = open('sing1.txt','a',encoding='utf-8')
#     f.write('\n213423432\n')
#     f.write(f1.read())
# #close
#     print(f1.readline())
#     f.close()

#low
    # f1 = open('sing.txt', 'r', encoding='utf-8')  # 文件句柄
    # for index,line in enumerate(f1.readlines()):
    #     print(line.strip())

#high
    # f1 = open('sing.txt', 'r', encoding='utf-8')  # 文件句柄
    # conut = 0
    # for line in f1:
    #     if conut == 9:
    #         print('------10-------')
    #         conut += 1
    #         continue
    #     print(line.strip())
    #     conut += 1
#seek 回到起始位置
    f =open('sing.txt','r',encoding='utf-8')#文件句柄
    print(f.tell())
    print(f.read(5))
    print(f.tell())
    f.seek(0)
    print(f.readline())

# what coding in file
    print(f.encoding)

#flush
    print(f.flush())#往硬盘写

    f = open('sing2.txt')

#truncate()
    f.truncate(20)  #截断，从头到20个字符，读时候。

#r+

#rb  不传encoding=... 网络传输过程会用
    f = open('sing.txt','rb')
    print(f.readline())



if __name__ == "__main__":
    main()
