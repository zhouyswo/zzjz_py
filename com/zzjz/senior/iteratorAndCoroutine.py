# 迭代器
# 可迭代（iterable）:直接作用于for循环的变量
# 迭代器（iterator）:不仅可以用于for循环，还可以被next调用
# list 是典型的可迭代对象，但不是迭代器
# 可迭代的对象不一定是迭代器，迭代器一定是可迭代对象
# 可通过isinstance判断

from collections import Iterable
from collections import Iterator

l = [1, 2, 3, 4]
# print(isinstance(l,Iterable))
# print(isinstance(l,Iterator))

# 可迭代对象转换为迭代器

# it = iter(l)
# print(isinstance(it, Iterable))
# print(isinstance(it, Iterator))


# 生成器
# generator:一边循环，一边计算下一个元素的机制或算法
# 需要满足3个条件：
# -每次调用都产生出for循环需要的下一个元素
# -如果达到最后一个后，爆出stopIteration异常
# -可以被next函数调用

# 列表生成器
l = [x * x for x in range(6)]
# 放在小括号中就是生成器
g = (x * x for x in range(6))


# 定义生成器
# 如果包含yield，则这个函数就叫做生成器
# next调用函数，遇到yield返回
# def ff():
#     print(1)
#     yield 1
#     print(2)
#     yield 2
#
#
# g = ff()
# n = next(g)
# print(n)
# n2 = next(g)
# print(n2)


# 协程
# 3.4引入协程，用yield实现
# 实现协程比较好的包有asyncio,tornado,gevent
# 协程：是为抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序
# 从技术角度讲，协程就是一个可以暂停执行的函数
# 协程的实现：yield返回、send调用


# def simple_coroutine():
#     print("->start")
#     x = yield
#     print("->recived", x)
#
#
# # 主线程
# sc = simple_coroutine()
# print("aaaa")
# # 预激 可以使用sc.send(None)，效果一样
# next(sc)
# print("bbbb")
# sc.send("cccc")

# 协程的4个状态
# inspect.getgeneratorstate(...)函数确定，该函数会返回下述字符串中的一个
# GEN_CREATED:等待开始执行
# GEN_RUNNING:解释器正在执行
# GEN_SUSPENED:在yield表达式处暂停
# GEN_CLOSED:执行结束
# next预激活


# def simple_coroutine(a):
#     print("->start")
#     b = yield a
#     print("->recived", a, b)
#     c = yield a + b
#     print("->recived", a, b, c)
#
#
# # 主线程
# sc = simple_coroutine(3)
# aa = next(sc)
# print(aa)
# bb = sc.send(4)
# print(bb)
# cc = sc.send(5)
# print(cc)


# 协程中未处理的异常会向上冒泡，传给next函数或send方法的调用方（即触发协程对象）
# 停止协程的一种方式：发送某个哨符值，让协程退出，内置的None和Ellipsis等常亮经常用作哨符值


# yield from
# 调用协程为了得到返回值，协程必须正常终止
# 生成器正常终止会发出StopIteration异常，异常对象的vlaue属性保存返回值
# yield from从内部捕获StopIteration异常

# 委派生成器
# -包含yield from表达式生成器函数
# -委派生成器在yield from表达式处暂停，调用方可以直接把数据发给生成器
# -子生成器把产出的值发给调用方
# -子生成器在最后，解释器会抛出StopIteration异常，并且把返回值附加到异常对象上

def gen():
    for c in "ab":
        yield c


def gen_new():
    yield from "cd"


print(list(gen()))
print(list(gen_new()))
