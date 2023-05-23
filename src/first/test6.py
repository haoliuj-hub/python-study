"""
算术运算符
"""
a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# // 取整除  ** 指数
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)

a = 10
b = 3
c = a // b
print("7 - c 的值为：", c)

# 复合赋值运算符 += -= *= /= %= **= //=
c += a
print("8 - c 的值为：", c)

c *= a
print("9 - c 的值为：", c)

c /= a
print("10 - c 的值为：", c)

c = 2
c %= a
print("11 - c 的值为：", c)

c **= a
print("12 - c 的值为：", c)

c //= a
print("13 - c 的值为：", c)
