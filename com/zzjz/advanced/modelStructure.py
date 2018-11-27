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
