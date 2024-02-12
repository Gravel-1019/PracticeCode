import asyncio
import socket
class Client(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.loop = asyncio.get_running_loop()
    async def recv(self):
        data = await self.loop.sock_recv(self.c,1024)
        return data
    async def send(self,data):
        await self.loop.sock_sendall(self.c,data.encode('utf-8'))
    async def __aenter__(self):
        self.c = socket.socket()

        await self.loop.sock_connect(self.c,(self.ip,self.port))
        return self
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.c.close()
async def main():
    async with Client('127.0.0.1',8888)as f:
        while True:
            await f.send('abc')
            data = await f.recv()
asyncio.run(main())