# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
#协程实现TCP服务端并发
import socket
from gevent import monkey;monkey.patch_all()
from gevent import spawn
IP = "127.0.0.1"
PORT = 5001
def run(IP,PORT):
    sk = socket.socket()#TCP
    sk.bind((IP,PORT))
    sk.listen(5)
    while True:
        conn,addr = sk.accept()
        spawn(link,conn)


def link(conn):
    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            conn.close()
        print(f"收到服务端信息{data}")



if __name__ == "__main__":
    g = spawn(run,IP,PORT)
    g.join()