# logging 日志模块
# 日志的级别  level
# DEBUG 	详细信息，典型地调试问题时会感兴趣。 详细的debug信息。
# INFO 	证明事情按预期工作。 关键事件。
# WARNING 	表明发生了一些意外，或者不久的将来会发生问题（如‘磁盘满了’）。软件还是在正常工作。
# ERROR 	由于更严重的问题，软件已不能执行一些功能了。 一般错误消息。
# CRITICAL 	严重错误，表明软件已不能继续运行了。
# NOTICE 	不是错误，但是可能需要处理。普通但是重要的事件。
# ALERT 	需要立即修复，例如系统数据库损坏。
# EMERGENCY 	紧急情况，系统不可用（例如系统崩溃），一般会通知所有用户

# 默认情况下Python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，
# 这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG）

# 写日志是IO操作
# 作用：调试，了解软件的运行情况，分析定位问题


# 初始化日志或写日志的时候需要制定级别，只有信息的级别等于或高于指定级别才会被记录

# logging.debug(msg, *args, **kwargs) 创建一条严重级别为DEBUG的日志记录
# logging.info(msg, *args, **kwargs) 创建一条严重级别为INFO的日志记录
# logging.warning(msg, *args, **kwargs) 创建一条严重级别为WARNING的日志记录
# logging.error(msg, *args, **kwargs) 创建一条严重级别为ERROR的日志记录
# logging.critical(msg, *args, **kwargs) 创建一条严重级别为CRITICAL的日志记录
# logging.log(level, *args, **kwargs) 创建一条严重级别为level的日志记录
# logging.basicConfig(**kwargs) 对root logger进行一次性配置


# logging.basicConfig()函数包含参数说明

# filename 	指定日志输出目标文件的文件名（可以写文件名也可以写文件的完整的绝对路径，写文件名日志放执行文件目录下，写完整路径按照完整路径生成日志文件），指定该设置项后日志信心就不会被输出到控制台了
# filemode 	指定日志文件的打开模式，默认为'a'。需要注意的是，该选项要在filename指定时才有效
# format 	指定日志格式字符串，即指定日志输出时所包含的字段信息以及它们的顺序。logging模块定义的格式字段下面会列出。
# datefmt 	指定日期/时间格式。需要注意的是，该选项要在format中包含时间字段%(asctime)s时才有效
# level 	指定日志器的日志级别
# stream 	指定日志输出目标stream，如sys.stdout、sys.stderr以及网络stream。需要说明的是，stream和filename不能同时提供，否则会引发 ValueError异常
# style 	Python 3.2中新添加的配置项。指定format格式字符串的风格，可取值为'%'、'{'和'$'，默认为'%'
# handlers 	Python 3.3中新添加的配置项。该选项如果被指定，它应该是一个创建了多个Handler的可迭代对象，这些handler将会被添加到root logger。需要说明的是：filename、stream和handlers这三个配置项只能有一个存在，不能同时出现2个或3个，否则会引发ValueError异常。


# logging模块中定义好的可以用于format格式字符串说明
# 字段/属性名称	使用格式	描述
# asctime 	%(asctime)s 	将日志的时间构造成可读的形式，默认情况下是‘2016-02-08 12:00:00,123’精确到毫秒
# name 	%(name)s 	所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
# filename 	%(filename)s 	调用日志输出函数的模块的文件名； pathname的文件名部分，包含文件后缀
# funcName 	%(funcName)s 	由哪个function发出的log， 调用日志输出函数的函数名
# levelname 	%(levelname)s 	日志的最终等级（被filter修改后的）
# message 	%(message)s 	日志信息， 日志记录的文本内容
# lineno 	%(lineno)d 	当前日志的行号， 调用日志输出函数的语句所在的代码行
# levelno 	%(levelno)s 	该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
# pathname 	%(pathname)s 	完整路径 ，调用日志输出函数的模块的完整路径名，可能没有
# process 	%(process)s 	当前进程， 进程ID。可能没有
# processName 	%(processName)s 	进程名称，Python 3.1新增
# thread 	%(thread)s 	当前线程， 线程ID。可能没有
# threadName 	%(thread)s 	线程名称
# module 	%(module)s 	调用日志输出函数的模块名， filename的名称部分，不包含后缀即不包含文件后缀的文件名
# created 	%(created)f 	当前时间，用UNIX标准的表示时间的浮点数表示； 日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
# relativeCreated 	%(relativeCreated)d 	输出日志信息时的，自Logger创建以 来的毫秒数； 日志事件发生的时间相对于logging模块加载时间的相对毫秒数
# msecs 	%(msecs)d 	日志事件发生事件的毫秒部分。logging.basicConfig()中用了参数datefmt，将会去掉asctime中产生的毫秒部分，可以用这个加上


import logging
# 配置输出日志格式
# LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
# # 配置输出时间的格式，注意月份和天数不要搞乱了
# DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '
# logging.basicConfig(level=logging.DEBUG,
#                     format=LOG_FORMAT,
#                     datefmt = DATE_FORMAT ,
# #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
#                     filename=r"d:\test\test.log"
#                     )
# logging.debug("msg1")
# logging.info("msg2")
# logging.warning("msg3")
# logging.error("msg4")
# logging.critical("msg5")


# logging.basicConfig()函数是一个一次性的简单配置工具使，也就是说只有在第一次调用该函数时会起作用，后续再次调用该函数时完全不会产生任何操作的，多次调用的设置并不是累加操作。
#
# 日志器（Logger）是有层级关系的，上面调用的logging模块级别的函数所使用的日志器是RootLogger类的实例，其名称为'root'，它是处于日志器层级关系最顶层的日志器，且该实例是以单例模式存在的。
#
# 如果要记录的日志中包含变量数据，可使用一个格式字符串作为这个事件的描述消息（logging.debug、logging.info等函数的第一个参数），然后将变量数据作为第二个参数*args的值进行传递，


# *************************logging日志模块四大组件******************************
# 组件名称	对应类名	功能描述
# 日志器 	Logger 	提供了应用程序可一直使用的接口
# 处理器 	Handler 	将logger创建的日志记录发送到合适的目的输出
# 过滤器 	Filter 	提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
# 格式器 	Formatter 	决定日志记录的最终输出格式

# 组件之间的关系
# 日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络等；
# 不同的处理器（handler）可以将日志输出到不同的位置；
# 日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
# 每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
# 每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方。


# Logger
# 向应用程序代码暴露几个方法，使应用程序可以在运行时记录日志消息；
# 基于日志严重等级（默认的过滤设施）或filter对象来决定要对哪些日志进行后续处理；
# 将日志消息传送给所有感兴趣的日志handlers。
# Logger.setLevel() 	设置日志器将会处理的日志消息的最低严重级别
# Logger.addHandler() 和 Logger.removeHandler() 	为该logger对象添加 和 移除一个handler对象
# Logger.addFilter() 和 Logger.removeFilter() 	为该logger对象添加 和 移除一个filter对象
# Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), Logger.critical() 	创建一个与它们的方法名对应等级的日志记录
# Logger.exception() 	创建一个类似于Logger.error()的日志消息
# Logger.log() 	需要获取一个明确的日志level参数来创建一个日志记录

# 获取logger
# 实例化或者logging.getLogger()

# handler
# logging.StreamHandler 	将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。
# logging.FileHandler 	将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
# logging.handlers.RotatingFileHandler 	将日志消息发送到磁盘文件，并支持日志文件按大小切割
# logging.hanlders.TimedRotatingFileHandler 	将日志消息发送到磁盘文件，并支持日志文件按时间切割
# logging.handlers.HTTPHandler 	将日志消息以GET或POST的方式发送给一个HTTP服务器
# logging.handlers.SMTPHandler 	将日志消息发送给一个指定的email地址
# logging.NullHandler 	该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免'No handlers could be found for logger XXX'信息的出现。

# format
# 可直接实例化
# 构造方法：logging.Formatter.__init__(fmt=None, datefmt=None, style='%')
# fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
# datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
# style：可取值为'%', '{'和'$'，如果不指定该参数则默认使用'%'


# Filter
# Filter可以被Handler和Logger用来做比level更细粒度的、更复杂的过滤功能。Filter是一个过滤器基类，它只允许某个logger层级下的日志事件通过过滤。
