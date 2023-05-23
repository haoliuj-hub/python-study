"""
循环猜数字
"""

import random

num = random.randint(1, 100)

i = 0
flag = True
while flag:
    guest_num = int(input("请输入猜想的数字："))
    i += 1
    if guest_num > num:
        print("大了")
    elif guest_num < num:
        print("小了")
    else:
        flag = False
print(f"猜对了，总共猜了{i}次")
