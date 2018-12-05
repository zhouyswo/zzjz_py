# 异常
# 在python中异常是一个类，可以处理和使用
#
# try catch
# try:
#    程序块
# except 异常类型1：
#     解决方式1
# except 异常类型2：
#      解决方式2
# else:
#       如果没有出现任何异常，将会执行此处代码
# finally:
#       无论是否存在异常，都会执行此处代码

# 捕获异常后，将异常实例化，出错信息在实例里
# 需要把越明确的异常或者范围越小的异常放在前面

# try:
#     num = int(input("input =:"))
#     ret = 100 / num
#     print(ret)
# except ZeroDivisionError as zeroe:
#     print("---",zeroe)
#     # 退出程序
#     exit()
# except Exception as e:
#     print("!!!!",e)
#     exit()

# 当某些情况下，用户希望自己触发一个异常，可以使用 raise 关键字来触发
# 自定义异常必须是系统异常类的子类
# class AaaEeeor(ValueError):
#     pass
#
# try:
#     print("sasasasa")
#     raise AaaEeeor
# except AaaEeeor as e:
#     print("aaa error")
#     exit()
# except Exception as e:
#     print(e)
#     exit()
