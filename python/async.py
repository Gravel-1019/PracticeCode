import asyncio
async def nets():
    print("进入IO")
    await asyncio.sleep(3)
    print("结束IO")
    return 43
async def main(name):
    print(name, 'start')

    task_list = [
        asyncio.create_task(nets()),asyncio.create_task(nets())
    ]
    done,pending = await asyncio.wait(task_list,timeout=3.1)
    for task in done:
        print(task.result())
    print(done)
    print(pending)


asyncio.run(main('qqq'))
