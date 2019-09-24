# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 23:33
# @Author  : Feng Xiaoqing
# @FileName: socket_client.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
# import socket
#
# client = socket.socket()#
# client.connect(('localhost',6962))
# client.send(b'11111111111')
# data = client.recv(1024)
# print('recv:',data)
# client.close()

import socket

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6913))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send(msg.encode("utf-8"))
    data = client.recv(10240)
    print("recv:",data.decode())

client.close()