import socket
sk = socket.socket()
sk.connect(("127.0.0.1",4000))
while True:
    sk.send(b'hello')
    data = sk.recv(1024)
    print(data)