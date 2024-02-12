# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
from multiprocessing import Process,Queue
def task(q):
    q.put('Hello world')
if __name__ == "__main__":
    q = Queue()
    p = Process(target=task,args=(q,))
    p.start()
    print(q.get())