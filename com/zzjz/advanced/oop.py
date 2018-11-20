# 封装
# 封装就是对对象的成员进行访问限制
# public  protected private
# public  protected private 不是关键字

# 私有：私有成员是最高级别的封装，只能在当前类或对象中访问
# 定义方式：在成员前面添加两个下划线即可
# Python 私有不是真私有，是一种name mangling 的改名策略，可以使用 _classname__属性名  来访问
# class Student():
#    sex = "女"
#    __age = 18
#   name = "你咋还"
# a = Student()
# print(a._Student__age)


# 受保护的封装 protected
# protected  可以在类或者子类中访问
# 方法：在成员名称前添加一个下划线即可


# 继承
# 继承就是一个类可以获得另外一个类中的成员属性和成员方法
# 作用：减少代码，增加代码的复用功能
# 被继承的类叫做父类，也叫基类、超类
# 用于继承的类叫做子类或者派生类
# 任何一个类都有一个共同的父类叫做object
# 继承的语法：父类写在子类的括号内
# 子类一旦继承父类，则可以使用父类中除私有成员外所有的属性或方法
# 子类可以定义独有的属性或方法
# 子类中如果存在于父类一样的成员，优先使用子类的成员
# 子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码重用。
# 可以使用 父类名.属性名来访问，或者使用super().属性来访问
# class People():
#    name = "jj"
# class Student(People):
#   pass
# t = Student()
# print(t.name)


