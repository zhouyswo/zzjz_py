# 长久保存信息的一种数据信息集合
# 常用操作
# --- 打开关闭（文件一旦打开需要关闭操作）
# ---读写内容
# ---查找

# open函数
# open函数负责打开文件，带有很多参数
# 第一个参数：必须有，文件的路径和名称
# 打开模式 model
#   r:以只读的方式打开
#   w:写方式打开，会覆盖之前的内容
#   x:创建方式打开，如文件已存在，报错
#   a:append方式，已追加的方式对文件内容进行写入
#   b:binary方式，二进制方式写入
#   t:文本方式打开
#   +：可读写

# f = open(r"test.txt", "w")
# r表示后面字符串不需要转义
# f称之为文件句柄
# 文件打开后必须关闭
# f.close()

# with语句
# with语句使用的技术是一种成为上下文管理协议的技术，自动判断文件的作用域，自动关闭不再使用的打开的文件句柄

# with open(r"test.txt", "w") as f:
#     pass
# pass部分开始对文件f进行操作，在with模块中不需要在使用close关闭文件


# with open(r"E:\TestDatas\111.txt", "r") as f:
#     # 按行读取
#     line = f.readline()
#     # 此结构保证能够完整的读取文件直到结束
#     while line:
#         print(line)
#         line = f.readline()


# list能用打开的文件作为参数，把文件内容每一行内容作为一个元素
# with open(r"decratorStructure.py", "r") as f:
#     line = list(f)


# read是按字符读取文件内容
# 允许输入参数决定读取几个字符，如果没有指定，从当前位置读取到结尾，否则从当前位置读取指定个数的字符
# with open(r"decratorStructure.py", "r") as f:
#     cha = f.read(5)
#     print(cha)


# seek(offset,from)
# 移动文件的读取位置，也叫读取指针
# from的取值范围:
#   0:从文件头开始偏移
#   1:从文件当前位置开始偏移
#   2:从文件末尾开始偏移
# 移动的单位是字节（byte）
# 一个汉字由若干个字节构成
# 移动的位置是从当前位置开始

# with open(r"decratorStructure.py", "r") as f:
#     f.seek(4, 0)
#     chr = f.read()
#     print(chr)

# time的sleep可以让程序睡眠
# import time
#
# for i in range(2,5):
#     print(i)
#     time.sleep(1)

# tell函数：用来显示文件读写指针当前位置
# with open(r"decratorStructure.py", "r") as f:
#     str = f.read(3)
#     pos = f.tell()
#     while str:
#         print(str)
#         print(pos)
#
#         str = f.read(3)
#         pos = f.tell()
# tell的返回数字是以byte为单位

# write
# write(str):把字符串写入文件
# writelines(str):把字符串按行写入文件
# 区别：write写入只能是字符串，writelines参数可以时字符串也可以是字符序列

