#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: passwd.py
@time: 2019/7/29 18:38
"""
#密文密码
import getpass



_username = 'fxq'
_password = '123456'

username = input("username:")
password = input("password:")
if _username == username and _password == password:
    # print(username,password)
    print("Welcome User {name} login.".format(name = username))
else:
    print("Invalid username or password!")

