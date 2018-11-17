# 集合 set
# 定义集合的方法 ：
# s = set()
# s = {3,4,6} 如果使用大括号，括号里必须要有值

# 集合的特性：
# 1、无序，python 的集合无法使用索引和分片，因为在Set内部元素的顺序是由元素的hash值决定的
# 2、元素唯一性，可以用于排除重复数据
# 3、集合的元素必须是可hash的
# 4、集合本身不能hash

# remove  discard 的区别
# remove  移除指定的值，直接改变原有的值，如果要删除的值不存在，会报错
# discard 移除指定的值，如果要删除的值不存在，不会报错
# s ={43,3,54,3,2,5}
# s.remove(3)
# print(s)
# s.discard(3)
# print(s)

# pop 随机移除一个元素

# intersection 交集
# difference 差集
# union 并集
# issubset 检查一个集合是否是另一个的子集
# issuperset 检查一个子集是否是另一个的超级
#s = {43, 3, 54, 3, 2, 5}

#forzen set：冰冻集合，不能修改的集合叫做冰冻集合
# s = forzenset()


