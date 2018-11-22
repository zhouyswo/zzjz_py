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
# __new__:对象实例化方法
