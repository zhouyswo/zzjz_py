# 内置数据结构
# list 一组有顺序的数据结构，顺序是指元素存入list的顺序，list元素索引从0开始
# 创建空列表  list=[] 或者 list =[100] 或者 lis = list()
# lis = list()
# lis.append(1)
# lis.append(1)
# lis.append(1)
# print(lis[0:3])

# 分片可以控制增长幅度，默认增长幅度为1
# print(lis[0:3:2])

# 下标可以超出范围，超出后不再考虑多余下标内容
# 下标为负数表示从右往左，最后一个元素下标为-1
# lis =[1,3,56,32,665,3232,6,32,6,8,2,0,23]
# print(lis[1:8:2])
# print(lis[1:100:2])
# print(lis[-1:-6:-2])

# 分片操作是生成了一个新的list
# 内置函数 id ，负责显示一个变量或者数据的唯一编号
# a=10
# b=9
# c=a
# print(id(a))
# print(id(b))
# print(id(c))
# a=101
# print(id(a))
# print(id(c))

# del  删除变量

# 双层列表循环  此处为特例
# a = [["g", 2], ["ds", 4], ["fsr", 1]]
# for k, v in a:
#    print(k, v)

# 列表内涵：list content  通过简单的方法创建列表
# a = [1, 2, 3, 4, 5, 6]
# b = [i for i in a]
# a中元素乘以10放入新列表中
# c = [i * 10 for i in a]
# 过滤原来列表中的元素，并生成新的列表
# d = [i for i in a if i % 2 == 0]
# 列表嵌套
# e = [i + j for i in c for j in d]
# print(e)
# 列表函数
# len：求列表长度  使用方法 len(列表)
# max：求最大值，使用方法 max(列表)
# append:在列表末尾插入元素  使用方法 列表.append(元素)
# insert:指定位置插入元素,插入位置是index的前面  使用方法  列表.insert(index,元素)
# del
# pop 从对应位置拿出一个元素
# remove  用remove 删除没有的元素会报错，remove操作后列表内存地址不变，即任然是同一列表
# clear  清除元素，list的内存地址不变。

# reverse:翻转列表内容
# extend:扩展列表，把一个列表直接拼接到另一个列表上
# count:查到列表中指定元素的个数

# copy:拷贝，浅拷贝
# 传址 深拷贝
# a = [5, 3, 6, 32, 54, 65, 57]
# print(a)
# b = a
# b[2] = 693
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# 传值 浅拷贝
# a = [5, 3, 6, 32, 54, 65, 57]
# b = a.copy()
# print(id(a))
# print(id(b))
# b[3]=837
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# 深拷贝，浅拷贝区别
# 浅拷贝只拷贝一层内容，当出现多级列表嵌套时，只拷贝最外一层列表，内部的列表任然是传址
# a=[32,5,34,[4,53,12,5]]
# b = a.copy()
# print(id(a))
# print(id(b))
# print(id(a[3]))
# print(id(b[3]))
# b[3][1]=100
# print(a[3])
# print(b[3])
# print(id(a[3]))
# print(id(b[3]))

# 元组 tuple
# 元组可以看做一个不可更改的list
# t = (3,4)   t = 3,4
# tuple()方法创建元组
# a = [4,5,3]
# t = tuple(a)

# 元组的特性：
# 1、是有序列表
# 2、 元组元素可以查看，不能修改(内容不可修改，可以进行传址操作)
# 3、元组数据可以是任意类型
# 4、list具有的一些操作，例如索引、切片、序列相加、相乘、成员资格操作等

# 不允许修改内容
# t1 = (1,3,5)
# print(t1)
# t1[2]=8
# print(t1)


# t1 = (1, 3, 5)
# t2 = (4, 52, 5)
# t3 = t1 + t2
# print(t3)

# tuple * 3 表示将元组中的元素拷贝3次

# 成员检测 使用  if  i in  tuple 格式
#t1 = (1, 3, 5)
#if 2 in t1:
#    print("i am in ")

#双层元组遍历
#t =((2,3,4),(5,7,3),(7,32,6))
#for k,v,y in t:
#    print(k,v,y)

#元素变量交换法
a =2
b =4
print(a,"--",b)
a,b = b,a
print(a,"--",b)