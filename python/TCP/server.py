# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
import socket
from threading import Thread
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk.bind(('0.0.0.0', 1145))
sk.listen(5)
print("开始监听".center(30, '='))


def task(conn):
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        if not data:
            print("客户端断开连接！")
            break
        print(f'[*]收到客户端消息：{data}')
        conn.send('Hello client!'.encode('utf-8'))
        print('[*]已经向客户端发送消息')
    conn.close()


print("服务端绑定1145端口")
while True:
    conn, addr = sk.accept()
    print(f"[*]连接到客户端{addr}")
    Thread(target=task, args=(conn,))
