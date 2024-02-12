# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
from concurrent.futures import ThreadPoolExecutor
import time
pool = ThreadPoolExecutor()
def task(name):
    print(f"任务{name}开始")
    time.sleep(3)
    print(f"任务{name}结束")
    return f"res:{name}"
def call_back(res):
    print(res.result())
for i in range(10):
    pool.submit(task,i).add_done_callback(call_back)

   
