#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: list.py
@time: 2019/7/31 10:55
"""


def main():
    import copy  # copy全量
    names = ["zhangsan", "lisi", ["fxq", "nihao"], "wangwu", "fengxiaoqing"]

    names.append("guyun")  # 增
    names.insert(1, "xiaobao")  # 插在1的位置
    names[2] = "lisi2"  # 改
    names.remove(names[0])  # 删除
    names.pop(0)  # 不写0时是删除最后一个  #删除
    print(names)
    del names[1]  # 删除
    print(names)
    print(names[names.index("fengxiaoqing")])  # 查找下标位置
    print(names.count("fengxiaoqing"))  # 计数
    # names.clear()#清空列表
    names.reverse()  # 反转
    names.sort()  # 排序  （特殊符号  数字  大写  小写 ） 的顺序
    names2 = [1, 2, 3, 4]
    names.extend(names2)
    del names2  # 删除变量
    # print(names2)
    print(names)
    print("#" * 50)

    print(names[1:3])  # 顾头不顾尾 切片
    print(names[-2:])

    print(names[0:3])
    print(names[:3])  # 前面是0 可以忽略

    names3 = names.copy()  # 浅copy 复制不全
    print(names3)

    names3[2] = "lisi3"
    print(names3)

    names3[0] = "fxq"
    print(names3)
    names4 = copy.deepcopy(names3)  # 深copy
    print(names4)

    # 列表循环
    for i in names4[0:-1:2]:  # 跳着切 可写成[::2]
        print(i)


if __name__ == "__main__":
    main()
