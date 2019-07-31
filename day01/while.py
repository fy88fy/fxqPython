#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: while.py
@time: 2019/7/30 8:51
"""


# def main():
#     # for i in range(0,10):
#     #     if i < 3:
#     #         print("loop",i)
#     #     else:
#     #         continue
#     #     print("hehe...")
#     for i in range(10):
#         print('---------',i)
#         for j in range(10):
#             print(j)
#             if j > 5:
#                 break
#
# if __name__ == "__main__":
#     main()

def main():
    count = 0
    while True:
        username = 'fxq'
        age_of_fxq = 42

        guess_age = int(input("guess age: "))
        if guess_age == age_of_fxq:
            print("Yes,you got it.")
            break
        elif guess_age > age_of_fxq:
            print("Think small")
        else:
            print("Think bigger.")
        count += 1
        if count == 3:
            countinue_confirm = input("Do you want to keep guessing.?")
            if countinue_confirm != 'n':
                count = 0


if __name__ == "__main__":
    main()