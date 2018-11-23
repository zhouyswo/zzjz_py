# 属性
# get
# set
# delete
# class Persion():
#   def get(self):
#        return self.name
#
#    def set(self, name):
#        self.name = name
#
#   def delete(self):
#       self.name = None
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
