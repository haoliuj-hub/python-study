"""
字符串扩展内容
"""

# 字符串的定义
name = '测试1'
print(name)

name = "测试2"
print(name)

name = '''
        测试3
        '''
print(name)

name = "'"
print(name)

name = "\'"
print(name)

name = '"'
print(name)

name = '\\\\'
print(name)

# 字符串拼接
print("名字：" + "liuhao")

# print("名字：" + 123456) 其他类型不能 + 拼接

# 通过占位符拼接字符串
name = "liuhao"
age = 18
score = 95.999
print("名字：%s" % name)
print("名字：%s，年龄：%s" % (name, age))

print("名字：%s，年龄：%d" % (name, age))
print("名字：%s，年龄：%d，成绩：%f" % (name, age, score))

# 字符串格式化精度
print("名字：%s，年龄：%5d，成绩：%f" % (name, age, score))
print("名字：%s，年龄：%d，成绩：%.3f" % (name, age, score))
print("名字：%s，年龄：%d，成绩：%.2f" % (name, age, score))

print("名字：%s，年龄：%d，成绩：%7.3f" % (name, age, score))
z = "z名字：%s，年龄：%d，成绩：%7.3f" % (name, age, score)
print(z)

# 字符串格式化2
x = f"x名字：{name}，年龄：{age}，成绩：{score}"
print(x)

# 对表达式进行格式化
print("2 * 4 的结果是：%d" % (2 * 4))
print(f"2 * 4 的结果是：{2 * 4}")
