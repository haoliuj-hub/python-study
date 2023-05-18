"""
集合Set
"""

# 集合的创建
# 1.使用set()函数
# 2.使用{}创建
# 3.使用推导式创建

set1 = {1}
print(type(set1))

# 去重，顺序无法保证
set1 = {"你好", "liuhao", "liuhao", "liuhao"}
print(set1)

# 添加
set1.add("liuhao2")
print(set1)

# 删除
set1.remove("liuhao2")
print(set1)

# 随机取一个元素，并删除
element = set1.pop()
print(element)
print(set1)

# 取出2个集合的差集
set1 = {"你好", "liuhao"}
set2 = {"liuhao", "liuhao2"}
set3 = set1.difference(set2)
print(set3)

# 取出2个集合的交集
set1 = {"你好", "liuhao"}
set2 = {"liuhao", "liuhao2"}
set3 = set1.intersection(set2)

# 取出2个集合的并集
set1 = {"你好", "liuhao"}
set2 = {"liuhao", "liuhao2"}
set3 = set1.union(set2)

# 判断是否是子集
set1 = {"你好", "liuhao"}
set2 = {"liuhao", "liuhao2"}
print(set1.issubset(set2))

# 判断是否是父集
set1 = {"你好", "liuhao"}
set2 = {"liuhao", "liuhao2"}
print(set1.issuperset(set2))

# 判断是否有交集
set1 = {"你好", "liuhao"}
set2 = {"liuhao", "liuhao2"}
print(set1.isdisjoint(set2))

# 消除差集
set1 = {"你好", "liuhao"}
set2 = {"liuhao", "liuhao2"}
set1.difference_update(set2)
print(set1)

set1.pop()
print(set1)
if set1 != set():
    print("空集合")
    set1.pop()
    print(set1)
