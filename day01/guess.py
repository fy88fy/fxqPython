#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: guess.py
@time: 2019/7/29 18:49
"""

def main():
    count = 0
    while count < 3 :
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
