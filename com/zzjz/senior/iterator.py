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
def ff():
    print(1)
    yield 1
    print(2)
    yield 2
g = ff()
n = next(g)
print(n)
n2 = next(g)
print(n2)

