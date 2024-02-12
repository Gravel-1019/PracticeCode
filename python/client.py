# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
import socket
import time
c = socket.socket()
c.connect(('0.0.0.0', 12345))
while True:
    c.send(b'hello')
    data = c.recv(1024)
    print(data.decode('utf-8'))
    time.sleep(2)
