# -*- coding: utf-8 -*-
# @Author: Gravel
# @Email:  3575160075@qq.com
from gevent import monkey
monkey.patch_all()#给spawn打猴子补丁
from gevent import spawn#无法检测所有io操作，需要补丁
import time
def da():
    for _ in range(3):
        print("da")
        time.sleep(2)
def mie():
    for _ in range(3):
        print("mie")
        time.sleep(2)

g1 = spawn(da)
g2 = spawn(mie)
g1.join()
g2.join()
