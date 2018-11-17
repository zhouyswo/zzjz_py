# 封装
# 封装就是对对象的成员进行访问限制
# public  protected private
# public  protected private 不是关键字

# 私有：私有成员是最高级别的封装，只能在当前类或对象中访问
# 定义方式：在成员前面添加两个下划线即可
# Python 私有不是真私有，是一种name mangling 的改名策略，可以使用 _classname__属性名  来访问
class Student():
    sex = "女"
    __age = 18
    name = "你咋还"

a = Student()
print(a._Student__age)
