import select
import socket
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('127.0.0.1',8001))
server.listen(5)
server.setblocking(False)
input_list = [server]#要select监管的对象
while True:
    rlist,wlist,xlist = select.select(input_list,[],[])#参数分别是：可读对象，可写对象，报错的对象
    for i in rlist:
        if i is server:#判断对象类型
            conn,addr = i.accept()
            input_list.append(conn)
            continue
        try:
            data = i.recv(1024)
            if not data:
                i.close()
                input_list.remove(i)
                continue
            i.send(data.upper())
        except ConnectionResetError:
            i.close()
            input_list.remove(i)
            continue