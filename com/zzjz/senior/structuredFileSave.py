# 结构化文件：xml,json,为了解决不同设备之间的信息交换
# xml可扩展标记语言
# 标记语言：语言中使用尖括号括起来的文本字符串标记
# 可扩展：用户可以自定义标准
# xml文档结构：处理指令、根元素、子元素、属性、内容、注释

# 正则表达式 RegularExpression re
# .(点号)：表示任意一个字符，除了\n，例如查找所有的一个字符 \.
# []:匹配括号中列列举的任意字符
# \d:任意一个数字
# \D;除了数字都可以
# \s:表示空格，tab键
# \S:除了空白符号
# \w:单次字符，a-z,A-Z,0-9,_
# \W:除了
# *：表示前面的内容重复0次或多次
# +：表示前面内容至少出现一次
# ?:前面才出现的内容0次或一次
# {m,n}:前面的内容最少出现m次最好出现n次
# ^：从字符串的开始进行匹配
# $:匹配到字符串的尾部
#|：左右任意一个