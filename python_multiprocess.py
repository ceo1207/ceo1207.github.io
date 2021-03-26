# -*- coding: utf-8 -*-
# Author: Kayi
# create time: 2021/3/25
import time
import multiprocessing
import os
import random
global_variable = 1200
# 多进程测试
def worker_1():
    time.sleep(2)
    print time.ctime(), 'current process:', multiprocessing.current_process()
    print global_variable

def worker_2():
    global global_variable
    global_variable = 12
    print time.ctime(), 'current process:', multiprocessing.current_process()


# 多进程方式 - 2
class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()

    def run(self):
        print 'current process:', multiprocessing.current_process(), os.getpid()


def work_file_with(mylock, myfile):
    with mylock:
        with open(myfile) as f:
            for line in f:
                print line
            f.write('some information')

def work_file_directly(mylock, myfile):
    '''
    使用try finally语句才是with语句的等价语句
    :param mylock:
    :param myfile:
    :return:
    '''
    mylock.acquire()
    try:
        with open(myfile) as f:
            for line in f:
                print line
            f.write('some information')
    except:
        pass
    finally:
        mylock.release()

# event 通信
'''
Flag值为 False，当程序执行event.wait()方法时就会阻塞，如果Flag值为True时，程序执行event.wait()方法时不会阻塞继续执行。
'''
def now():
    return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


def traffic_light(e):  # 红绿灯
    print now() + ' \033[31m红灯亮\033[0m'  # Flag 默认是False
    while True:
        if e.is_set():  # 如果是绿灯
            time.sleep(2)  # 2秒后
            print now() + ' \033[31m红灯亮\033[0m'  # 转为红灯
            e.clear()  # 设置为False

        else:  # 如果是红灯
            time.sleep(2)  # 2秒后
            print now() + ' \033[32m绿灯亮\033[0m'  # 转为绿灯
            e.set()  # 设置为True

def people(e, i):
    if not e.is_set():
        print now() + ' people %s 在等待' % i
        e.wait()
    print   now() +' people %s 通过了' % i


def test_pool():
    print 'Done'
    return True

if __name__=='__main__':
    # exe-1 多进程复制当前堆栈环境，形成独立的内存环境
    process1 = multiprocessing.Process(target=worker_1, )
    process2 = multiprocessing.Process(target=worker_2, )
    process2.start()
    process1.start()
    for item in multiprocessing.active_children():
        print item

    # exe-2 测试第二种方式创建多进程
    process3 = MyProcess()
    process3.start()

    # 使用lock 多进程访问同一个文件
    mylock = multiprocessing.Lock()
    test_file = 'log.txt'

    # 使用管道pipe

    # 使用event 模拟过红绿灯
    # e = multiprocessing.Event()  # 默认为 False，红灯亮
    # p = multiprocessing.Process(target=traffic_light, args=(e,))  # 红绿灯进程
    # p.daemon = True
    # p.start()
    # process_list = []
    # for i in range(6):  # 6人过马路
    #     time.sleep(random.randrange(0, 4, 2))
    #     p = multiprocessing.Process(target=people, args=(e, i))
    #     p.start()
    #     process_list.append(p)
    #
    # for p in process_list:
    #     p.join()

    # 使用进程池
    my_pool = multiprocessing.Pool(5)
    res = []
    for _ in range(5):
        res.append(my_pool.apply_async(test_pool, ))
    my_pool.close()
    my_pool.join()
    for i in res:
        print i
    # 关闭之后 没有函数可以再开启 重建一个吧
    # for _ in range(5):
    #     res.append(my_pool.apply_async(test_pool, ))
    # for i in res:
    #     print i
