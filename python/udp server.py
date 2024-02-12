# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
import socket
sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#数据包协议UDP
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sk.bind(('0.0.0.0',1145))
while True:
    data,addr = sk.recvfrom(1024)
    data = data.decode('utf-8')
    if data == 'q':
        print("客户端断开连接！")
        break
    print(f'[*]收到客户端消息：{data}')
    sk.sendto('Hello client!'.encode('utf-8'),addr)
    print('[*]已经向客户端发送消息')
