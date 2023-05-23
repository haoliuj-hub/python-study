"""
猜数字的案例
"""
import random

num = random.randint(1, 10)
guest_num = int(input("请输入第一次猜想的数字："))
if guest_num == num:
    print("第一次猜对了")
else:
    if guest_num > num:
        print("大了")
    else:
        print("小了")
    guest_num = int(input("不对，再猜一次："))
    if guest_num == num:
        print("第二次猜对了")
    else:
        if guest_num > num:
            print("大了")
        else:
            print("小了")
        guest_num = int(input("不对，再猜最后一次："))
        if guest_num == num:
            print("最后一次猜对了")
        else:
            print("猜错了")
