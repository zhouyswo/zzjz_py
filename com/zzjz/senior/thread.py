# 进程：程序运行的一个状态
# 包含地址空间、内存、数据栈等
# 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
# 每个进程有自己完全独立的运行环境，多进程共享数据是一个问题


# 线程
# 一个进程的独立运行片段，一个进程可以有多个线程
# 轻量化的进程
# 一个进程的多个线程间共享数据和上下文运行环境
# 共享互斥问题

# 全局解释器锁（GIL）
# python代码的执行是由python虚拟机进行控制
# 在主循环中只能有一个控制线程在执行

import time
# import _thread  as td
# def fc1():
#     time.sleep(3)
#     print("i am walking")
# def fc2():
#     time.sleep(2)
#     print("i am walking to")
# def ff():
#     td.start_new_thread(fc1, ())
#     td.start_new_thread(fc2, ())
#     time.sleep(7)
#     print("finish")
# ff()

# threading
# 直接利用threading.Thread 生成Thread示例
# threading.Thread(target="",args=(''''''))创建一个线程对象，再使用start方法启动
# 守护线程 daemon
#
import threading
#
# def fc1():
#     time.sleep(3)
#     print("i am walking")
# def fc2():
#     time.sleep(2)
#     print("i am walking to")
# def ff():
#     # td.start_new_thread(fc1, ())
#     t1=threading.Thread(target=fc1,args=())
#     # td.start_new_thread(fc2, ())
#     t2 =threading.Thread(target=fc2, args=())
#     t1.start()
#     t2.start()
#     time.sleep(7)
#     print("finish")
# ff()


# 可以继承自threading.Thread创建一个线程
# 需要重写run方法

# class NyThread(threading.Thread):
#     def run(self):
#         print("i am custom thread")
#
# t = NyThread()
# t.start()
