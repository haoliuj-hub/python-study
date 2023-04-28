"""
数据类型转换
"""

# 1. int() 转换成整数
# 2. float() 转换成浮点数
# 3. str() 转换成字符串
# 4. list() 转换成列表
# 5. tuple() 转换成元组
# 6. dict() 转换成字典
# 7. set() 转换成集合
# 8. bool() 转换成布尔值

a = 100
print(type(a), a)

b = float(a)
print(type(b), b)

c = str(a)
print(type(c), c)

d = list(c)
print(type(d), d)

e = tuple(c)
print(type(e), e)

h = bool(a)
print(type(h), h)

float_num = 3.64
print(int(float_num))
