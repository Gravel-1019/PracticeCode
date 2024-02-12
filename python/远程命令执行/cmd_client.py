# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
import socket
ip = '47.99.33.90'
port = 1146
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#TCP
client.connect((ip,port))
while True:
    com = input("输入终端命令>>> ").strip()
    if com == '':
        print("请输入指令！")
        continue
    if com == 'exit':
        break
    client.send(com.encode('utf-8'))
    data_size = int(client.recv(8).decode("utf-8"))
    rece_size = 0
    data = b''
    while rece_size < data_size:
        res = client.recv(1024)
        rece_size += len(res)
        data += res
    print(data.decode('utf-8'))
    print(len(data))
client.close()