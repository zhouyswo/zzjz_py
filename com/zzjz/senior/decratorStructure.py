# 装饰器（decrator）
# 装饰器可以在不改变现有的代码的情况下对功能进行扩展，装饰器是一个返回函数的高阶函数
# 装饰器的使用：使用@语法，即调用的时候使用@+函数名
# 装饰器在定义方法之前使用

# import time
# def printTime(f):
#     def wrapper(*args,**kewargs):
#         print("time:",time.ctime())
#         return f(*args,**kewargs)
#     return wrapper
#
# @ printTime
# def hello():
#     print('hello!')
#
# hello()


# 偏函数
# 参数固定的函数，相当于一个由特定参数的函数体
# functools.partial的作用，把一个函数某些函数固定，返回一个新函数
# import functools
#
# int16 = functools.partial(int, base=16)
# print(int16("27163"))


# zip
# 把两个可迭代的内容生成一个可迭代的tuple
# l1 = [1, 4, 2, 3, 5]
# l2 = [43, 32, 132, 423, 442]
# z = zip(l1, l2)
# for i in z:
#     print(i)


# enumerate
# 对可迭代对象里的每个元素配上一个索引，构成一个tuple，元素索引从0开始
# l2 = [43, 32, 132, 423, 442]
# # l3 = enumerate(l2)
# # 从100开始编号
# l3 = enumerate(l2, start=100)
# for i in l3:
#     print(i)


# collections 模块
# namedtuple  tuple类型，是一个可命名的tuple

# import collections as ct
# Point = ct.namedtuple("Point",["x","y"])
# p = Point(12,34)
# print(p.x)
# print(type(p))


# deque 双端队列，比较方便的解决了频繁添加和删除带来的效率问题
# from collections import deque
#
# q = deque([3, 54, 21, 4, 43])
# print(q)
# q.append(66)
# print(q)
# 默认插入方式是从右边插入，可以使用appendleft方法从左边插入


# defaultdict  就是一个dict,当直接读取不存在的属性时直接返回默认值
# import collections
#
# func = lambda: "haha"
# d = collections.defaultdict(func)
# d["o"]=1
# d["t"]=2
# print(d["s"])


#counter 统计字符个数
# from collections import Counter
# s = "sasasa"
# s1=["sasa","r33","bh7","988f"]
# print(Counter(s))
# print(Counter(s1))


