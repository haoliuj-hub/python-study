"""
自定义模块
"""

__all__ = ["add"]  # 指定允许导入的成员


def add(x, y):
    print("调用add方法")
    return x + y


def sub(x, y):
    print("调用sub方法")
    return x - y


if __name__ == '__main__':
    print(add(1, 2))
    print(sub(1, 2))
