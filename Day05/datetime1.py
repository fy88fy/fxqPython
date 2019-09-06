#!/usr/bin/env python
#-*- coding:utf-8 _*-

"""
@author: Fengxiaoqing
@contact: fy88fy@163.com
@software: PyCharm
@file: datetime1.py
@time: 2019/9/3 11:51
"""
import time,os,sys
def logger():
    global  LogFile
    LogFile="logs/"+time.strftime("%Y-%m-%d-%H-%M-%S")+".log"
    with open(LogFile,'w',encoding="UTF-8") as f:
        f.write(str(time.time()))
        print("Log file (%s) was created successfully!" % LogFile.split('/')[1] )

def rm_logs():
    os.remove('logs')

def main():
    for i in range(1):
        logger()
        time.sleep(1)

    # rm_logs()

    print(os.getcwd())
if __name__ == "__main__":
    main()
