#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: homework_shopping_cart.py
@time: 2019/7/31 11:11
"""


def main():
    salary = int(input('Please input your salary: '))
    remain = salary
    buylist = []
    while True:

        print('''
        ---------------------
        ------Sale list------
        1. Cell Phone  5000
        2. Book         200
        3. coffe        20
        4. Bycle        800
        5. Laptop       8000
        6. Pen          10
        ---------------------
        ---------------------    
        ''')
        list = [
                ['salary',salary],
                ['Cell Phone',5000],
                ['Book',200],
                ['coffe',20],
                ['Bycle',800],
                ['Laptop',8000],
                ['Pen',10]
                ]

        print("Please input the number of something. ")
        select = input("Plese input number(1/2/3...,and exit): ")
        if select == 'q' or select == 'Q' or select == 'exit' or select == 'quit':
            break
        elif select == 'list':
            print(buylist)
            continue
        else:
            print("ERROR")

        select = int(select)
        cost = int(list[select][1])
        remain = remain-cost

        if remain < 0:
            print("Sorry,you money is not enough.")
            continue

        buylist.append(list[select][0])

        # print(list[select])
        # print(cost)
        # print(remain)
        print("You buy: \033[31m%s\033[0m " % (buylist))
        print("You cost is :",salary-remain)


if __name__ == "__main__":
    main()
