# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
ip = '0.0.0.0'
port = 1146
import socket
import subprocess
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sk.bind((ip,port))
sk.listen(5)
print("开始监听".center(30,'='))
while True:
    conn,addr = sk.accept()
    print(f"接收到{addr}")
    while True:
        com = conn.recv(1024)
        com = com.decode('utf-8')
        if not com:
            break
        obj = subprocess.Popen(com,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out_res = obj.stdout.read()
        err_res = obj.stderr.read()
        data_size = len(out_res) + len(err_res)
        header = bytes(str(data_size),'utf-8').zfill(8)
        conn.send(header)
        conn.send(out_res)
        conn.send(err_res)
        print(len(out_res) + len(err_res))
    conn.close()