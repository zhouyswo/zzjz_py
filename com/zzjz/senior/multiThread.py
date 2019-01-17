# 创建进程
# 生成实例对象
# 生成派生对象
import multiprocessing  as mp
from time import sleep, ctime

# 实例对象
# def clock(timeInterval):
#     print("the time is %s" % ctime())
#     sleep(timeInterval)
#
# if __name__ == '__main__':
#     p = mp.Process(target=clock,args=(5,))
#     p.start()

# 派生对象
# class ClockProcess(mp.Process):
#     """
#     init 函数
#     run 函数
#     """
#
#     def __init__(self, timeInterval):
#         super().__init__()
#         self.timeInterval = timeInterval
#
#     def run(self):
#         print("the time is %s" % ctime())
#         sleep(self.timeInterval)


# if __name__ == '__main__':
#     p = ClockProcess(3)
#     p.start()

# os 中查看进程
import os


#
#
# def info():
#     # 父进程ID
#     print("parent process", os.getppid())
#     # zi=自个进程ID
#     print("self process", os.getpid())
#
#
# if __name__ == '__main__':
#     info()
#     p = ClockProcess(3)
#     p.start()


# 生产者消费者
# JoinableQueue
# 队列里添加哨兵，起到通知的作用
input_q = mp.JoinableQueue
def conumer(input_q):
    print("into consumer:", ctime())
    while True:
        item = input_q
