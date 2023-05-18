"""
序列切片
"""
# 切片操作符：[start:end:step]
# start:开始位置，默认为0
# end:结束位置，不包含结束位置的元素
# step:步长，默认为1
# 序列切片操作，会返回一个新的序列
# 序列切片操作，不会影响原来的序列

# 切片操作
str1 = "abcdefg"
print(str1[1:5:2])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 倒序需要注意，start和end的位置
print(my_list[3:1:-1])
print(my_list[1:3:-1])

# 从头开始，到尾结束，步长-2
print(my_list[::-2])
