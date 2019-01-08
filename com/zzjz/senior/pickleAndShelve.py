# pickle  持久化
# pickle python提供的序列化模块
# pickle.dump 序列化
# pickle.load 反序列化

# import pickle
#
# # 序列化
# age = 19
# with open(r"jjdsds.txt", "w") as f:
#     pickle.dump(age, f)
# # 反序列化
# with open(r"jjdsds.txt", "r") as f:
#     aaa = pickle.load(f)
#     print(aaa)

# shelve  持久化工具
# 类似字典，用键值对保存数据，存取方式跟字典也类似
# 主要方法  open  close

import shelve

# shv = shelve.open(r"jjdsds.txt")
# shv["aaa"] = 1
# shv["bbb"] = 2
# shv["ccc"] = 3
# shv.close()

# shelve会自动创建的多个文件，并将数据保存在文件中
# shelve读取数据时，如果键不存在会报错
# shelve不支持并行写入，但支持并行读取

# shelve只读方式打开
# shv = shelve.open(r"jjdsds.txt", flag="r")
# print(shv["aaa"])
# shv.close()

# shelve 强制写回
# shv = shelve.open(r"jjdsds.txt", writeback=True)

# shelve使用weith管理上下文
# with shelve.open(r"jjdsds.txt", writeback=True) as shv:
#     aaa = shv["aaa"]
#     print(aaa)
