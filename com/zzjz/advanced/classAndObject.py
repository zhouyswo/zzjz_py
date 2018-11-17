# oop 面向对象编程
# OOA OOD OOI OOP

# 类：抽象名词，代表一个集合，共性的事物
# 类包括以下的内容：表明事物的特征，叫做属性
#                  表明事物的功能或动作，称为成员方法（函数）
# 类必须用class 关键字
# 如果是空类，必须用pass关键字
# 如果属性值未定，使用None赋值
# 定义的方法默认有一个self参数
# class Student():
#    name = 12

#   def func(self):
#      print(" i am")


# jinkong = Student()
# jinkong.func()

# 对象：具象的东西，代表一个个体
# 对象所有成员检查 obj.__dist__
# 类所有成员检查 class_name.__dist__
# print(jinkong.__dict__)
# print(Student.__dict__)

# 类实例只有一个，对象实例有多个
# 在对象不对属性进行赋值的时候，类实例的属性和对象的属性相同（id ）
# 当对象访问成员时，如果对象中没有该成员，则尝试访问类中的同名成员，如果对象中有该成员，则优先使用对象中的成员。
# 类存储成员时使用的是与类关联的一个对象
# 独享存储成员是存储在当前对象中
# 创建对象时，类中的成员不会放入对象中，而是得到一个空对象，没有成员
# 通过对象对成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类中的成员

# self
# self 在对象方法中表示对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数中
# self  不是关键字，只是一个用于接收对象的普通参数，可以用任何一个普通参数变量名代替
# 方法中有self形参的方法成为非绑定类方法，可以在对象中访问，没有self形参的方法是绑定类的方法，只能通过类访问。
# 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过 __class__成员名来访问
class Student():
    name = 12

    def func(self):
        print(" i am {0}".format(self.name))

    def fun2(self):
        print(" i am {0}".format(__class__.name))


class People():
    name = 54


a = Student()
a.func()
a.name=100
a.fun2()
Student.func(a)
Student.func(Student)
Student.func(People)
