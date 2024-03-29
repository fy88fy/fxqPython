# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 7:42
# @Author  : Feng Xiaoqing
# @FileName: socket_server_client.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
# import socket
#
# client = socket.socket()
#
# client.connect(('localhost',9991))
#
# while True:
#     cmd = input(">>:").strip()
#     if len(cmd) == 0:continue
#     client.send(cmd.encode('utf8'))
#     cmd_res = client.recv(1024)
#     print(cmd_res.encode())
#
#
#
# client.close()

import socket
client = socket.socket()

#client.connect(('192.168.16.200',9999))
client.connect(('localhost',9992))

while True:
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode("utf-8"))
    cmd_res_size = client.recv(1024) ##接受命令结果的长度
    print("命令结果大小:",cmd_res_size)
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()) :
        data = client.recv(1024)
        received_size += len(data) #每次收到的有可能小于1024，所以必须用len判断
        #print(data.decode())
        received_data += data
    else:
        print("cmd res receive done...",received_size)
        print(received_data.decode())


client.close()

