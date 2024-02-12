import asyncio
async def f1(future):
    await asyncio.sleep(3)
    future.set_result('hello')
async def main():
    loop = asyncio.get_running_loop()#获取当前的事件循环
    future = loop.create_future()#创建Future对象
    loop.create_task(f1(future))
    res = await future
    print(res)
asyncio.run(main())