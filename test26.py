"""
函数进阶
"""


# 函数多返回值
def func():
    return 1, "hello", True


x, y, z = func()
print(x, y, z)


# 函数多种参数
def user_info(name, age, gender="男"):
    print(f"姓名是：{name}，年龄是：{age}，性别是：{gender}")


# 1. 位置参数
user_info("小明", 18, "男")
# 2. 关键字参数
user_info(age=12, name="小小", gender="女")
user_info("大大", gender="男", age=14)

# 3. 默认参数
user_info("小红", 16)


# 4. 不定长参数
# *args 接收元组
# **kwargs 接收字典
# *args **kwargs 顺序必须是：位置参数、*args、默认参数、**kwargs
def func2(*args, **kwargs):
    print(args)
    print(kwargs)


func2('Tom', 18, '男', '北京市', '北京市', '中国', 100, 200, 300, a=1, b=2, c=3)


# 函数传递
def test_func(compute):
    print(type(compute))
    print(compute(1, 2))


def compute(x, y):
    return x + y


test_func(compute)

# 匿名函数
# lambda 参数列表: 返回值
# 匿名函数的参数列表可以有多个，用逗号隔开，但是只能有一个返回值
# 匿名函数的返回值就是函数的返回值
# 匿名函数一般是作为参数传递给其他函数使用
# 匿名函数也可以作为其他函数的返回值
# 匿名函数也可以赋值给一个变量，然后通过这个变量间接调用这个匿名函数
# 匿名函数的作用：简化代码
# 匿名函数的缺点：不方便阅读

# 1. 匿名函数的基本使用  lambda 参数列表: 函数体返回值
test_func(lambda x, y: x - y)
