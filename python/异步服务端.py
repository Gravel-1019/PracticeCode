import socket
import asyncio
async def main(ip,port):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind((ip,port))
    server.listen(5)
    server.setblocking(False)
    loop = asyncio.get_running_loop()
    while True:
        conn,addr = await loop.sock_accept(server)
        while True:
            await loop.create_task(waiter(conn,loop))
        conn.close()
async def waiter(conn,loop):
    while True:
        data = await loop.sock_recv(conn,1024)
        if not data:
            break
        print('data')
        await loop.sock_sendall(conn,data.upper())

asyncio.run(main('127.0.0.1',8888))