# 属性
# get
# set
# delete
# property的四个参数的顺序是固定的
# 第一个参数代表读取的时候需要调用的函数
# 第二个参数代表写入的时候需要调用的函数
# 第三个是参数
# 第四个是需要设置的值

# class Persion():
#    def get(self):
#        return self.name

#   def set(self, name):
#       self.name = name

#   def delete(self):
#        self.name = None

#    name2 = property(set, get, delete, "电视剧方")

# p = Persion()
# p.set("htyu")
# print(p.get())

# 类的内置属性
# __dist__  以字典的方式显示类的成员组成
# __doc__  获取类的文档信息
# __name__  获取类的名称，如果在模块中使用。获取模块的名称
# __bases__  获取某个类的所有父类，以元组的方式显示
#

# 类的常用魔法方法
# 魔术方法就是不需要人为调用的方法，基本是在特定的时刻自动触发
# 魔术方法的同一特征，方法名被前后各两个下划线包裹
# __init__:构造函数
# __new__:对象实例化方法，一般先调__new__，再调用__init__
# __str__:当对象被当做字符串使用的时候调用
# __call__:对象调用方法的时候触发
# __repr__:返回字符串
# class Student():
#    def __init__(a):
#        print(" i an init")
#   def __new__(a):
#       print(" i an new")
#   def __str__(a):
#        print(" i an str")
#   def __call__(a):
#       print(" i an call")
#   def repr(a):
#       print(" i an call")

# 描述相关
# __getattr__:访问一个不存在的属性时触发
# 参数如下：
#   -self:用来获取当前对象
#   -获取属性的名称

# __setattr__:对成员属性进行设置的时候触发
# 参数如下：
#   -self 用来获取当前对象
#   -被设置的属性名称，以字符串的形式出现
#   -需要设置的值

# class Persion():
#     def __init__(self):
#        pass

#     def __setattr__(self, key, value):
#       如果在该方法内直接对属性赋值，则会调用方法本身，此时就会出现死循环，因此在此处使用super来赋值
#        super().__setattr__(key, value)

# 运算分类相关的魔术方法
# __gt__:进行大于判断的时候触发的函数
# -参数：
#  -self
#  -第二个参数是第二个对象
#  -返回值可以是任意值，推荐返回布尔值

# class Persion():
#    def __init__(self):
#        self._name = "asas"
#    def __gt__(self, obj):
#        return self._name > obj

# 类和对象的三种方法
# -实例方法
#   -需要实例化才能用的方法，使用过程中可能需要截止对象的其他对象的方法完成
# -静态方法
#   -不需要实例化，通过类直接访问
# -类方法
#   -不需要实例化，实例化对象也可以调用


# 抽象
# 抽象方法：没有实现的方法，在python中体现为方法定义内容为pass
# 抽象类：包含抽象方法的类叫做抽象类，
# 抽象类的使用：
#   -抽象类可以包含抽象方法，也可以包含具体方法
#   -抽象类中可以有方法也可以有属性
#   -抽象类不允许直接实例化
#   -必须继承才能使用，用继承的子类必须实现所有继承来的抽象方法
#   -抽象类的主要作用是设定类的标准，以便于开发的时候具有统一的规范
# class Animal():
#     def sayHello(self):
#         pass
#
#
# class Dog(Animal):
#     def sayHello(self):
#         print("hahahah")
#
#
# class People(Animal):
#     def sayHello(self):
#         print("哈哈哈出来啦")
#
#
# d = Dog()
# d.sayHello()
# p = People()
# p.sayHello()

# 自定义类
# 类其实是一个类定义和各种方法的自由组合
# 可以定义类和函数，然后自己通过类直接赋值
# 可以借助MethodType实现
# 借助于type实现
# 使用元类实现-MetaClass
#   - 元类是类

# 利用MethodType实现方法绑定
# from types import MethodType
# class A():
#     pass
# def say(self):
#     print("say")
# a = A()
# a.say = MethodType(say,A)
# a.say()


# 利用type制造一个类
# 先定义应该具有的成员函数
# def say(self):
#     print("say")
# def talk(self):
#     print("talk")
# 利用type来创建一个类
# A = type("Aname", (object,), {"class_say": say, "class_talk": talk})
# a = A()
# dir(a)


# 利用元类创造类
# 元类的写法是固定的，他必须继承自type,元类命名以MetaClass结尾
class AMetaClass(type):
    def __new__(cls, *args, **kwargs):
        args["id"]="asasa"
        args["addr"]="jjd"
        return type.__new__(cls,*args, **kwargs)


class Teacher(object, metaclass=AMetaClass):
    pass
t = Teacher()

