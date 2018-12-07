# 常用模块
# calendar
# time
# datatime
# timeit
# os
# shutil
# zip
# math
# string
# 上述所有模块使用理论上都应先导入，string是特例

# *************************************calendar 模块*****************************************************
# calendar  跟日历相关的模块
# 参数: w = 每个日期之间的间隔符
#      l = 每周所占的行数
#      c = 每个月之间的间隔字符数
# import calendar as cal
# ca = cal.calendar(2017,l=0,c=5)
# print(type(ca))
# print(ca)

# isleap 判断一年是否是闰年
# print(cal.isleap(2018))

# leapdays 获取指定年份之间的闰年个数
# print(cal.leapdays(1980,2030))

# month 获取某个月的日历字符串 格式 calendar,month(年,月)

# monthrange 获取某个月周几开始和天数 格式 calendar,monthrange(年,月)

# monthcalendar 获取某个月天的矩阵列表 格式 calendar,monthcalendar(年,月)

# weekday 获取指定某天是周几 格式 calendar,weekday(年,月,日)

# *************************************time 模块*****************************************************
# time  时间戳
# 一个时间的表示，根据语言的不同，可以是整数或者浮点数
# 32位系统只能支持到2038年
# 时间元组 一个包含时间内容的普通元组

# import time

# 时间模块的属性
# timezone: 当前时区和UTC时间相差的秒数，在没有夏令时的情况下，东八区是 -28800
# altzone 在有夏令时的情况下当前时区与UTC相差的秒数
# time()  得到时间戳
# localtime 得到当前时间的时间结构，可以通过点号操作符得到相应的属性元素的内容
# print(time.timezone)
# print(time.altzone)
# print(time.time())

# ctime 获取字符串化的当前时间
# mktime  使用时间元组获取对应的时间戳,返回浮点数时间戳
# perf_counter 获取CPU时间
# sleep(n) 使程序进入睡眠，n秒后继续
# time.sleep(5)
# print("999999")

# strftime 将时间元组转化为自定义的字符串
# %y 两位数的年份表示（00 - 99）
# %Y 四位数的年份表示（000 - 9999）
# %m 月份（01 - 12）
# %d 月内中的一天（0 - 31）
# %H 24小时制小时数（0 - 23）
# %I 12小时制小时数（01 - 12）
# %M 分钟数（00 = 59）
# %S 秒（00 - 59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001 - 366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00 - 53）星期天为星期的开始
# %w 星期（0 - 6），星期天为星期的开始
# %W 一年中的星期数（00 - 53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身
# t = time.localtime()
# ft = time.strftime("%Y-%m-%d %H:%M:%S",t)
# print(ft)

# *************************************datetime 模块*****************************************************
# datetime 模块
# datetime 提供日期和时间的运算和表示
# datetime.date 一个理想的日期，提供year,month，day属性
import datetime
# dt = datetime.date(2018, 5, 31)
# print(dt.day)
# print(dt.month)

# datetime.time
# datetime.datetime  提供日期和时间的组合
# datetime.timedelta  提供一个时间差，时间长度

# datetime.datetime
# from datetime import datetime, timedelta

# today
# now
# utcnow
# fromtimestamp 从时间戳中返回本地时间
# t1 = datetime.now()
# 1小时时间长度
# td = timedelta(hours=1)
# 当前时间加1小时输出
# print((t1 + td).strftime("%Y-%m-%d %H:%M:%S"))


# timeit 时间测量工具
import timeit
# 利用timeit调用代码，执行1000次，
# t1 = timeit.timeit(stmt="[i for i in range(1000)]",number=1000)
# print(t1)

# def do():
#     print("o")
# t2 = timeit.timeit(stmt=do,number=10)
# print(t2)


# setup负责把环境准备好
# s='''
#     def do(i):
#         print(i)
# '''
#
# t2 = timeit.timeit("do(i)",setup=s+"i=9",number=10)
# print(t2)

# *************************************os 模块*****************************************************
# os 操作系统相关
# 主要是文件操作，主要包含在3个模块里:
#  os 操作系统目录相关
#  os.path 系统路径相关操作
#  shutil 高级文件操作，目录树的操作，文件赋值、删除、移动
# 路径：绝对路径-总是从根目录上开始
#       相对路径-基本以当前环境开始的一个相对的路径

import os
# getcwd() 获取当前的工作目录
# print(os.getcwd())

# chdir改变当前的工作目录，格式 chdir(路径)，无返回值

# listdir 获取一个目录中所有子目录和文件的名称列表，格式listdir(路径)


