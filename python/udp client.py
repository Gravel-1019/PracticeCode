# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    msg = input("输入消息 >>> ").strip()
    sk.sendto(msg.encode('utf-8'),('0.0.0.0',1145))
    if msg == 'q':
        break
    print("已向服务端发送数据")
    data,addr = sk.recvfrom(1024)
    data = data.decode('utf-8')
    print(data)

sk.close()