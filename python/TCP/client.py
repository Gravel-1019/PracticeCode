# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
import socket
from threading import Thread
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.connect(('127.0.0.1',5001))
def task(sk):
    sk.send(str(i).encode('utf-8'))
for i in range(1000):
    Thread(target=task,args=(sk,)).start()