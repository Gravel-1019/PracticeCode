# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
from multiprocessing import Process,JoinableQueue
import time
import random
def producer(name,food,q):
    for i in range(8):
        time.sleep(random.randint(1,3))
        print(f'{name}生产了{food}{i}')
        q.put(f'{food}{i}')
def consumer(name,q):
    while True:
        food = q.get()
        q.task_down()#告诉队列已经拿走数据并且处理完了
        time.sleep(random.randint(1,3))
        print(f'{name}吃了{food}')
if __name__ == "__main__":
    q = JoinableQueue()
    p1 = Process(target=producer,args=('cook1','beef',q))
    p2 = Process(target=producer,args=('cook2','apple',q))
    p3 = Process(target=consumer,args=('gravel',q))
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    