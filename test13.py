"""
while循环 打印九九乘法表
"""

print("Hello", end="")
print("Word")

print("Hello\tWord")
print("test\tSecond")

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i * j}\t", end="")
        j += 1
    print()
    i += 1
