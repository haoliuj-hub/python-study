"""
银行取钱案例
"""
money = 500000
flag = True
while flag:
    print("-------------------主菜单-------------------")
    print("liuhao，您好，欢迎使用ATM取款机")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")

    num = int(input("请输入您的选择："))

    if num == 1:
        print(f"您的余额为：{money}")
    elif num == 2:
        print("您好，你存款50000元成功")
        money = money + 50000
        print(f"您的余额为：{money}")
    elif num == 3:
        print("您好，你取款50000元成功")
        money = money - 50000
        print(f"您的余额为：{money}")
    else:
        flag = False
        print("欢迎下次使用")
