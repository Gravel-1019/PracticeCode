# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
import socket
server = socket.socket()
server.bind(('127.0.0.1',8000))
server.listen(5)
server.setblocking(False)
c_list = []

d_list = []
while True:
    try:
        conn,addr = server.accept()
        c_list.append(conn)
    except BlockingIOError:
        for conn in c_list:
            try:
                data = conn.recv(1024)
                if not data:
                    conn.close()
                    d_list.append(conn)
                conn.send(data.upper())
            except BlockingIOError:
                pass

            except ConnectionRefusedError:
                conn.close()
                d_list.append(conn)
        for conn in d_list:
            c_list.remove(conn)
            d_list.clear()
        