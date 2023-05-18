"""
数据容器
"""
# list
name_list = ['aa', 'bb', 'cc', 'dd', 'ee']
empty1_list = []
empty2_list = list()
my1_list = ["zz", 2, True]
my2_list = ["zz", 2, True, [1, 2, 3]]

print(my1_list[0])
print(my2_list[3][1])

# 倒序取元素
print(my1_list[-1])

# 索引
print(my1_list.index("zz"))

# 修改
my1_list[0] = "liuhao"

# 插入
my1_list.insert(1, "liuhao2")

# 追加
my1_list.append("liuhao3")

# 追加多个
my1_list.extend(["liuhao4", "liuhao5"])

# 删除第一个匹配的元素，有多个匹配的只删除第一个
my1_list.remove("liuhao2")

# 删除指定索引的元素
del my1_list[0]

# 从列表中取出元素（列表中不存在）
element = my1_list.pop(0)

# 统计元素出现的次数
print(my1_list.count("liuhao"))

# 排序
my1_list.sort()

# 反转
my1_list.reverse()

# 清空
my1_list.clear()

# 删除列表
del my1_list

# 长度
print(len(my1_list))

# 判断元素是否存在
print("liuhao" in my1_list)

# 判断元素是否不存在
print("liuhao" not in my1_list)

# for循环遍历
for x in my1_list:
    print(x)

# while循环遍历
index = 0
while index < len(my1_list):
    print(my1_list[index])
    index += 1

print(my1_list)

# 切片
print(my1_list[0:2])
