#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: work.py
@time: 2019/7/30 10:07
"""


def main():
    # name = input("Username: ")
    # password = input("Password: ")
    # with open('password', 'r') as fd:
    #
    #     for line in fd:
    #         # fd.read()
    #         # line = line.strip()
    #         # print(line)
    #         if name == fd.read().split(':')[0].strip() and password == fd.read().split(':')[1].strip():
    #             print("Login sucessful.")
    #             break
    #         else:
    #             print("Sorry,user or password increcte.")
    #             break

    count = 0
    while True:
        name = input("Username: ")
        password = input("Password: ")

        # Check lock user.
        with open('lockuser','r') as lockuse:
            for user in lockuse:
                if name == user.strip():
                    print("{_user} is locked.".format(_user=name))
                    exit()


        # Login sucessful.
        if name == 'fxq' and password == "123456":
            print("Login sucessful.")
            print('''
            Welcome to My NGSOC.....Congretulations.
            
            ''')
            break

        # 输入错误3次，锁定并记录账号
        elif name =='fxq'and password != '123456':
            print("Sorry,username or password error.")
            count += 1
            if count == 3:
                print("Sorry,The user is Lock ,error 3 times")
                with open('lockuser', 'a+') as fd:
                    fd.write(name + "\n")
                    break

        # 用户不存在
        else:
            print("Sorry,The {_name} is not in userlist.".format(_name=name))
            break

if __name__ == "__main__":
    main()
