# 函数和过程的区别：有无返回值
# 函数返回值需要使用return显示返回内容
# 如果没有返回值，则返回None，也可以说python里函数都有返回值
# def f1():
#    print("no return")
# def f2():
#    print("have return")
#    return 7
# a = f1()
# b = f2()
# print(a)
# print(b)


# 给函数定义说明:在函数内部开始的第一行使用三字符串定义符
# def f(a, b, c):
#    """
#    :param a:这个是a
#    :param b:这个是b
#    :param c:这个是c
#    :return:没有返回
#    """
# help(f)


# 变量分为全局变量和局部变量
# global 全局：在函数外部定义，在整个全局范围内都有效，可以在局部直接使用
# local 局部：在函数内部定义，只在函数内部有效,局部变量在全局范围内无法使用
# glob = "haha"
# def func():
#    local = "local"
#    print("i am is {0} variable".format(local))
#    print("i am is {0} variable".format(glob))
# func()

# LEGB原则
# L:局部作用域
# E:外部嵌套函数作用域
# G:函数定义所在模块作用域
# B:python内置魔抗的作用域
# 访问原则：从里边访问外边,如果存在多个名称相同的变量，有里向外先找到谁就使用谁


# 提升局部变量为全局变量 在变量名前加 global修饰符
# def func():
#    global  a
#    a=100
#    print(a)
# func()
# print(a)

# 可以通过globals()和locals()显示出全局变量和局部变量

# eval()  把一个字符串当做代码来执行，并返回表达式执行的结果 格式 eval(String_code,globals=None,locals=None)
#x = 100
#y = 200
#z = eval("x+y")
#print(z)