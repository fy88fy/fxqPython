# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 7:37
# @Author  : Feng Xiaoqing
# @FileName: sock_server_ssh.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
# import socket,os
#
# server = socket.socket()
# server.bind(('localhost',9991))
#
# server.listen()
#
# while True:
#     conn,addr = server.accept()
#     print("New conn:",addr)
#     while True:
#         data = conn.recv(1024)
#         if not data:
#             print("Client is off...")
#             break
#         print('Run cmd :',data)
#         cmd_res = os.popen(data.decode()).read()
#         print("before send",len(cmd_res))
#         if len(cmd_res) == 0:
#             cmd_res = "Cmd has no output..."
#         conn.send(cmd_res.encode("utf-8"))
#         print("send done")
#
# server.close()


import socket ,os,time
server = socket.socket()
server.bind(('localhost',9992) )

server.listen()

while True:
    conn, addr = server.accept()
    print("new conn:",addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        print("执行指令:",data)
        cmd_res = os.popen(data.decode()).read() #接受字符串，执行结果也是字符串
        print("before send",len(cmd_res))
        if len(cmd_res) ==0:
            cmd_res = "cmd has no output..."

        conn.send( str(len(cmd_res.encode())).encode("utf-8")    )     #先发大小给客户端
        time.sleep(0.5)
        conn.send(cmd_res.encode("utf-8"))
        print("send done")
        os.path.isfile()
        os.stat("sock")
server.close()

import hashlib
m = hashlib.md5()
client.close()