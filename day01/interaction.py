#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: interaction.py
@time: 2019/7/29 18:00
"""


def main():
    name = input("Name: ")
    age = int(input("Age: "))
    job = input("Job: ")
    salary = int(input("Salary: "))
    info = '''
    ------------Info of %s---------------------
    Name:%s
    Age:%d
    Job:%s
    Salary:%s
    ''' % (name,name,age,job,salary)
    print(info)

    info2 = '''
    ------------Info2 of {_name}---------------------
    Name:{_name}
    Age:{_age}
    Job:{_job}
    Salary:{_salary}
    '''.format(_name= name,
              _age = age,
              _job = job,
             _salary = salary)
    print(info2)

    info3='''
    ------------Info3 of {0}---------------------
    Name:{0}
    Age:{1}
    Job:{2}
    Salary:{3}
    '''.format(name,age,job,salary)
    print(info3)




if __name__ == "__main__":
    main()
