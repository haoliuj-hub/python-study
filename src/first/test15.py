"""
发工资案例
"""
import random

total = 10000

for i in range(1, 21):
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}，绩效{score}，不发工资，下一位")
        continue
    else:
        if total < 1000:
            print("账户余额不足，无法发工资，下个月领取吧")
            break
        total -= 1000
        print(f"向员工{i}发工资1000元，账户余额还剩余{total}元")