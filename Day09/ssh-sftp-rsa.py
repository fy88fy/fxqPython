# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 8:25
# @Author  : Feng Xiaoqing
# @FileName: ssh-sftp-rsa.py
# @Software: PyCharm
# @Function：
#----------------------------------- 
import paramiko
private_key = paramiko.RSAKey.from_private_key_file('id_rsa')

transport = paramiko.Transport(('192.168.100.140', 22))
transport.connect(username='root',pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
#sftp.put('ssh.py', '/tmp/test_from_win')
# 将remove_path 下载到本地 local_path
sftp.get('/tmp/test_from_win', 'fromlinux1.txt')

transport.close()