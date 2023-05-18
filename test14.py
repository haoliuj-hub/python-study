"""
for循环
"""

name = "liuhao"
for x in name:
    print(x)

code = "abcfwsadfgahwerwfadf sdfgfgsdsasdf"
count = 0;
for z in code:
    if z == "a":
        count += 1
print(f"a出现的次数：{count}")

# range 语句
# range(start, stop[, step])
print(range(5))
print(type(range(5)))
print(range(1, 5))
print(range(1, 5, 2))

for i in range(1, 10, 2):
    print(i)

print("从0开始，到9循环：")
for i in range(10):
    print(i)
# 临时变量在for循环外部可以访问，但规范上不建议
print(i)

# for循环打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}\t", end="")
    print()

