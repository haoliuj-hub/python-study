"""
python io操作
"""
import time

# 1.文件操作
f = open("../../resource/测试.txt", "r", encoding="utf-8")
print(type(f))

# print(f.read(1))
# print(f.read())
# print(f"剩余：{f.read()}")

# 读取全部行返回列表，每行是列表一个元素
# lines = f.readlines()
# print(type(lines))
# print(lines)

# 读取一行
# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)

# for循环遍历文件对象
for line in f:
    print(line)

# 关闭文件
f.close()
print("----------------")
# 自动关闭
with open("../../resource/测试.txt", "r", encoding="utf-8") as f2:
    print(f2.read())


# 2.文件写入
# w 覆盖写入
# a 追加写入
with open("../../resource/测试2.txt", "w", encoding="utf-8") as f3:
    f3.write("hello world，水水水水")
    f3.flush()


