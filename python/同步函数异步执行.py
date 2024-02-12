import asyncio
import time
def f1(s):
    time.sleep(s)
    print('f1 done')
    return 'f1'
def f2():
    time.sleep(4)
    print('f2 done')
    return 'f2'
async def main():
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None,f1,1)
    future2 = loop.run_in_executor(None,f2)
    res = await future
    res2 = await future2
    print(res)
    print(res2)
asyncio.run(main())