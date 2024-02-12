import asyncio


class Myrange(object):
    def __init__(self,start,end=None):
        if end:
            self.count = start - 1
            self.end = end
        else:
            self.count = -1
            self.end = start
    async def add_count(self):
        await asyncio.sleep(1)
        self.count += 1
        if self.count == self.end:
            return None
        return self.count
    def __aiter__(self):
        return self
    async def __anext__(self):
        value = await self.add_count()
        if value is None:
            raise StopAsyncIteration
        return value

async def main():
    async for i in Myrange(10):
        print(i)

asyncio.run(main())