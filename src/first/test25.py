"""
通用操作
"""

# max() min() sum()
# max() 返回最大值
# min() 返回最小值
# sum() 返回总和

# 1. max()
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max_value = max(my_list)
print(max_value)

# 2. min()
min_value = min(my_list)
print(min_value)

# 3. sum()
sum_value = sum(my_list)
print(sum_value)

# 列表转列表
# list() 将其他序列转换为列表
# tuple() 将其他序列转换为元组
# str() 将其他序列转换为字符串

# 1. list()
my_list = list("abcdefg")
print(my_list)

# 2. tuple()
my_tuple = tuple("abcdefg")
print(my_tuple)

# 3. str()
my_str = str([1, 2, 3, 4, 5])
print(my_str)

# 容器排序
# sorted() 排序
# sorted(my_list, reverse=True) 倒序

# 1. sorted()
my_list = [1, 7, 5, 4, 3, 6, 2, 8, 9]
new_list = sorted(my_list)
print(new_list)

# 2. sorted(my_list, reverse=True)
my_list = [1, 7, 5, 4, 3, 6, 2, 8, 9]
new_list = sorted(my_list, reverse=True)
print(new_list)

# 字符串大小比较
# 字符串比较大小，是按照ASCII码进行比较的

