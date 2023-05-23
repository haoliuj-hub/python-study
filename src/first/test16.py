"""
函数
"""


# 1. 函数的定义
# 函数是一段具有特定功能的代码块，可以通过给函数起一个名字，来实现对这段代码的复用
# 函数的定义格式
# def 函数名(参数1, 参数2, ...):
#     代码块
#     return 返回值
# 函数名：函数的名字，命名规则和变量一样
# 参数：函数的输入，可以有多个，也可以没有
# return：函数的输出，可以有多个，也可以没有
# 代码块：函数的功能，可以有多行，也可以没有
# 函数的调用格式
# 函数名(参数1, 参数2, ...)
# 函数的调用，就是执行函数的代码块
# 函数的调用，可以有返回值，也可以没有返回值
# 函数的调用，可以有参数，也可以没有参数
# 函数的调用，可以有多个参数，也可以有多个返回值


def length(str1):
    count = 0
    for i in str1:
        count += 1
    return count


print(length("士大夫士大夫豆腐干是否"))


# 函数返回值 None类型
def say_hello():
    print("hello world")
    # 等同于 return None


result = say_hello()
print(f"无返回值的结果{result}，类型为{type(result)}")

# None用于if判断
if result:
    print("有返回值")
else:
    print("无返回值")

# None申明无初始内容的变量
a = None


# 函数说明文档
def func(x, y):
    """
    这是一个函数说明文档
    :param x: 参数1
    :param y: 参数2
    :return: 返回值
    """
    return x + y


num = 100


def testA(x):
    # 设置内部定义的变量变成全局变量
    global num
    num = x - 50
    print(num)


def testB():
    print(num)


testA(num)
testB()
