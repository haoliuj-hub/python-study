"""
main
"""


def test(a, b):
    print(a + b)


def test_b(a, b):
    print(a - b)


if __name__ == '__main__':
    test(1, 2)

# from 导入模块时候，会执行模块中的代码，不会执行main变量中的代码

# import * 后只能使用__all__中的变量
__all__ = ['test']
