# -*- coding: utf-8 -*-
# @Time    : 2019/9/19 23:37
# @Author  : Feng Xiaoqing
# @FileName: socket_server.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
# import socket
#
# server = socket.socket()
#
# server.bind(('localhost',6969))
# server.listen()
#
# print('wait for call..')
# # server.accept()
# conn,addr =server.accept()
# print(conn,addr)
# print('call is comming....')
# data = conn.recv(1024)
# print('recv:',data)
#
# conn.send(data.upper())
#
# server.close()

import socket
server = socket.socket()
server.bind(('localhost',6915)) #绑定要监听端口
server.listen(5) #监听

print("我要开始等电话了")
while True:
    conn, addr = server.accept()  # 等电话打进来
    # conn就是客户端连过来而在服务器端为其生成的一个连接实例
    print(conn, addr)
    print("电话来了")
    count = 0
    while True:
        data = conn.recv(1024)
        print("recv:",data)
        if not data:
            print("client has lost...")
            break
        conn.send(data.upper())
        count+=1
        if count >10:break

server.close()