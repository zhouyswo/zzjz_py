# 一个模块就是一个包含python代码的文件，后缀名就是.py就可以，模块就是python文件
# 为什么使用模块
#  - 程序太大，编写维护不方便，需要拆分
#  - 模块可以增加代码重复利用的方式
#  - 当做命名空间使用，避免命名冲突

# 如何定义模块
# - 模块就是一个普通文件，所以任何代码都可以直接书写
# - 函数（单一功能）
# - 类（相似功能的组合，或者类似业务模块）
# - 测试代码

# 导入模块
# import 模块名
# 使用方式
# model_name.function_name
# model_name.class_name

# 也可以借助importlib包实现包导入
# import importlib
# aaa = importlib.import_module("ccc")

# 模块取别名
# import mode_name as 别名

# 从模块中导入方法和类
# from model_name  import func_name or class_name
# 此种方法引入的类或方法可以直接引用，不需要带前缀
# 禁止 from model_name import *  ，这样会导致环境污染


# 建议将如下判断句作为程序的入口,可以有效避免模块代码被导入的时候被动执行的问题
# if __name__ == "__main__":
#    pass

# 模块的搜索路径和存储
# 模块的搜索路径：
# - 加载模块的时候系统会在哪些地方寻找此模块
# - 系统默认模块的搜索路径 sys.path
# - 添加搜索路径 sys.path.append(dir)

# 模块的加载路径
# 1、搜索内存中已经加载好的模块
# 2、搜索python的内置模块
# 3、搜索sys.path路径

# 包
# 包是一种组织管理代码的方式，包里存放的是模块
# 用于将模块包含一起的文件夹就是包
# 自定义包结构：

# 包的导入操作
# import package_name
# 直接导入一个包，可以使用__init__.py中的内容
# 使用方式：
#   package_name.func_name
#   package_name.class_name.func_name

# import sys
# print(type(sys.path))
# print(sys.path)

# 包的别名
# import  pkg_name as 别名
# 注意此种方式默认是对__init__.py内容的导入

# 导入包中具体模块
# import pag_name.model_name
# import pag_name.model_name as 别名
# from pachage import model1,model2..
# from package import *
# from  pag_name.model_name import *


# __all__的用法
# from package import * ，*表示可以导入的内容
#  __init__.py 中如果文件为空，或者没有 __all__，那么只可以把__init__中的内容导入
# __init__ 如果设置了__all__，那么则按照__all__指定的子包或者模块进行导入，如果这样则不会导入__init__中的内容
#__all__=['model1','model2',"package1","package2"....]

