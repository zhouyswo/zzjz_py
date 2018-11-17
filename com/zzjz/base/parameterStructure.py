# 函数
# 函数定义符 def
# 定义格式 def  函数名():  函数名要遵守命名规则
# 函数名后的括号和冒号不能省，括号内可以定义参数
# 函数内所有代码缩进
# def fu():
#   print('sasasa')
# fu ()

# 形参：定义函数时使用的参数，没有具体值，只是一个占位的符号
# 实参：调用函数使用的参数
# 函数返回用return语句 如果没有热return 默认返回None 函数执行到return时无条件返回

# 查找函数帮助文档 使用help
# help(print)
# print("1",sep=" ",end="")

# 参数分类：普通参数、默认参数、关键字参数、收集参数
# 默认参数：形参带有默认值，如果在调用的时候没有对相应的形参赋值，则使用默认值。
# 关键字参数  格式：def func(p1=value1,p2=value2........),p1,p2 就是关键字参数
# def g1(p1=1, p2=2):
#    print("这个是{0}，这个是{1}".format(p1, p2))
# a = 3
# b = 4
# g1(p1=a, p2=b)

# 收集参数   把没有位置，不能和定义时的参数位置相对应的参数放入一个特定的数据结构中,定义时参数名前带*号，对应的参数看做一个列表  语法 def func(*args),调用 func(p1,p2,p3....)
# def f2(*args):
#    for item in args:
#        print(item)
# f2(2, 4, "32", "多少呢")


# 带关键字参数的收集参数 def  func(**keywordargs)  调用方式 func(p1=v1,p2=v2,p3=v3......)
# def f3(**args):
#    for k,v in args:
#       print(k,"    ",v)
# f3(p1=76, p2=55, p3="33", p4="多少呢")


# 混合参数定义格式  def  func(a,*args,b="",**keys) 注意：关键字参数要后置
#def func(a,*args, b="", **keys):
#    print(" i am {0}".format(a))
#    for im in args:
#        print("{0} is a collect para".format(im))
#    print(" i am {0}".format(b))
#    for id in keys:
#        print("{0} is a collect keyword para".format(id))
#a = "people"
#b = "boy"
#c = "niwa"
#d = "tih"
#e = "jok"
#func(a,c,d,b=b,p=e)


#收集参数的解包问题： 把参数放入list或者字典中，直接把list/dist中的值放入收集参数中,
# 调用的时候需要解包，解包符号为*
#def func(*args):
#    for it in args:
#        print(" i an is {0} and type is{1}".format(it,type(it)))
#lis = list()
#lis.append("star")
#lis.append("jfja")
#lis.append(987)
#func(*lis)

# "*" * 20 表示 20个"*"
#print("*"*20)
