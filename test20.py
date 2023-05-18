"""
元组
"""

# 元组的创建
tup1 = (1, 2, 3, 4, 5)

# 内部嵌套是list的话可以修改
tup2 = (1, 2, [1, 2, 3], 4, 5)
tup2[2][0] = 100
print(tup2)

# 不能修改
# tup2[3] = 400
# print(tup2)

# tup3 = ()
tup3 = tuple()

# 注意,一个元素时候要定义元组必须使用逗号
tup4 = (1)
print(type(tup4))
tup4 = (1,)
print(type(tup4))

index = tup2.index(2)
print(index)
