"""
数据类型转换
"""

print("test")
print("tes")
print("sdf")

# 1. int() 转换成整数
# 2. float() 转换成浮点数
# 3. str() 转换成字符串
# 4. list() 转换成列表
# 5. tuple() 转换成元组
# 6. dict() 转换成字典
# 7. set() 转换成集合
# 8. bool() 转换成布尔值

a = 100
print(type(a))

b = float(a)
print(type(b))

c = str(a)
print(type(c))

d = list(c)
print(type(d))

e = tuple(c)
print(type(e))

f = dict()
print(type(f))

g = set()
print(type(g))

h = bool(a)
print(type(h))
print(h)

i = bool(0)
print(type(i))
print(i)

j = bool(1)
print(type(j))
print(j)

k = bool(-1)
print(type(k))
print(k)

l = bool(0.0)
print(type(l))
print(l)

m = bool(0.1)
print(type(m))
print(m)

n = bool(0.0000001)
print(type(n))
print(n)

o = bool(-0.0000001)
print(type(o))
print(o)

p = bool(-0.0000000)
print(type(p))
print(p)



