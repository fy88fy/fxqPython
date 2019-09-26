# -*- coding: utf-8 -*-
# @Time    : 2019/9/26 23:34
# @Author  : Feng Xiaoqing
# @FileName: socket_server.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
import socket

server = socket.socket()
server.bind(('localhost', 8090))
server.listen(5)
print("Waiting for client....")

while True:
    conn,addr = server.accept()
    print(conn,addr)
    data = conn.recv(1024)
    print(data)
    conn.send(data.upper())

server.close()

