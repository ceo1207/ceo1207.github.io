# -*- coding: utf-8 -*-
# Author: Kayi
# create time: 2021/3/26
import sys
import gc
import random
random.random()

# 垃圾回收
class A(object):
    pass


a = A()
# 可以查看a对象的引用计数，但是比正常计数大1，因为调用函数的时候传入a，这会让a的引用计数+1
sys.getrefcount(a)
gc.collect()  # 显式执行垃圾回收

# 多线程测试
# error
# generater_list = (x for x in range(4))
# print(len(generater_list))
# import threading
# threading.current_thread()
# threading.enumerate()


if __name__ == '__main__':
    pass