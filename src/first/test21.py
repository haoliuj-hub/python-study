"""
 字符串也是容器
"""

name = "liuhao"
print(name[0])
print(name[-1])

# 字符串无法修改 name[0] = "z"

index = name.index("iu")
print(index)

# replace替换字符串得到新的字符串
new_name = name.replace("iu", "IU")
print(new_name)

# split分割字符串得到列表
name_list = name.split("u")
print(name_list)

# strip去除字符串两边的空格
name = " liuhao "
print(name.strip())

# strip去除指定的字符，去除首尾的字符，多个字符只要有一个在首尾就去除
name = "121liuhao21"
print(name.strip("12"))

# count统计字符串出现的次数
name = "liuhao"
print(name.count("i"))

# 字符串长度
print(len(name))

for i in name:
    print(i)

index = 0
while index < len(name):
    print(name[index])
    index += 1
