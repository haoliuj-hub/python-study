"""
判断
"""

# bool类型
active = True
no_active = False

result = 5 > 3
print(type(result))
print(result)

# if语句
age = 30
if age >= 18:
    print("成年人")
    print("可以去网吧了")
elif age >= 12:
    print("青少年")
else:
    print("小孩子")

# if嵌套
age = 30
if age >= 18:
    print("成年人")
    if age >= 60:
        print("老年人")
    else:
        print("中年人")
else:
    print("小孩子")

# 猜数字
num = 10
# if int(input("请输入第一次猜想的数字：")) != num:
#     if int(input("不对，再猜一次：")) != num:
#         if int(input("不对，再猜最后一次：")) != num:
#             print("猜错了")

if int(input("请输入第一次猜想的数字：")) == num:
    print("第一次猜对了")
elif int(input("不对，再猜一次：")) == num:
    print("第二次猜对了")
elif int(input("不对，再猜最后一次：")) == num:
    print("最后一次猜对了")
else:
    print("猜错了")

