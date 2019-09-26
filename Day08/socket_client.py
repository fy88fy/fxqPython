# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 23:34
# @Author  : Feng Xiaoqing
# @FileName: socket_client.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
import  socket

while True:
    client = socket.socket()
    client.connect(('localhost',8090))
    name = input(">>:")
    if name:
        client.send(name.encode('utf-8'))
        data = client.recv(10240)
        print("recv:",data.decode())
    else:
        print('It is Null,please input something')

client.close()
