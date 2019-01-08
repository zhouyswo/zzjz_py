# 函数式编程
# 基于lambda演算的一种编程方式
# 函数可以作为参数，也可以作为返回值
# 高阶函数、返回函数、匿名函数、装饰器、偏函数


# ***********************lambda 表达式****************************
# lambda 表达式  也叫匿名函数，函数体相对简单
# 可以有参数，多个参数使用逗号隔开
# 用法：以lambda开头，参数后用冒号将参数和函数主体分开,没有return语句，表达式的计算结果即为表达式的返回结果

# 一个数乘以100
# stm = lambda x: x * 100
# print(stm(2))

# ***********************高阶函数****************************
# 把函数当做参数使用的函数叫做高阶函数
# 函数名称也是一个变量

# def a(n):
#     return n * 100
# def b(m):
#     return m * 2
# # print(b(a(2)))
# def c(n, f):
#     return f(n) * 1.5
# print(c(6, b))


# map函数
# 映射，即把集合或者列表的元素每一个元素都按照一定规则进行操作，生成一个新的列表或集合
# map函数式系统提供的具有映射功能的函数，返回值是一个迭代对象，可以使用for循环遍历

# l1 = [i for i in range(10)]
# def miii(n):
#     return n * 2
# l2 = map(miii, l1)
# for i in l2:
#     print(i)


# reduce函数
# 把一个可迭代的对象最后归并成一个结果
# 函数要求:必须有两个参数，必须有返回结果
# reduce 需要导入functools包
# import functools as f
# l1 = [i for i in range(10)]
# def miii(n1,n2):
#     return n1 +n2
# v = f.reduce(miii,l1)
# print(v)


# filter函数
# 对一组数据进行过滤，符合条件的数据会生成一个新的列表并返回
#
# l1 = [i for i in range(10)]
# def fil(f):
#     if (f > 5):
#         return True
#     else:
#         return False
# l2 = filter(fil,l1)
# for i in l2:
#     print(i)


# 排序
# s = [43, 6, 21, 565, 21, -4, 5, 43, -753, 215, 63]
# reverse 设置是顺序还是倒叙
# key 可以设置为abs 即按绝对值，str.lower 按小写排序
# ss = sorted(s,reverse=False)
# ss2 = sorted(s, key=abs, reverse=False)
# print(ss2)


# 函数作为返回值返回，被返回的函数在函数体内定义
# def aaa(f):
#     def bbb(g):
#         return g * 100
#     return bbb(f)


# 闭包（closure）
# 返回闭包的时候返回函数不能引用循环变量
# 解决方案：在创建一个函数，用该函数的参数绑定循环变量的当前值，无论该循环变量以后如何改变，已经绑定的函数参数值不再改变

# def count():
#     fs=[]
#     for i in range(2,5):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
# f1,f2,f3 = count()
# print(f1())
# print(f2())


# def count():
#     fs=[]
#     def f(h):
#         return h * h
#     for i in range(2,5):
#         fs.append(f(i))
#     return fs
# f1,f2,f3 = count()
# print(f1)
# print(f2)


