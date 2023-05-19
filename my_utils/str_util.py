"""
字符串工具
"""


def str_reverse(s):
    """
    字符串反转
    :param s:字符串
    :return: 反转的字符串
    """
    if isinstance(s, str) is False:
        raise TypeError('s must be str')
    return s[::-1]


def substr(s, x, y):
    """
    截取字符串
    :param s:字符串
    :param x: 起始索引
    :param y: 截止索引（不包含）
    :return: 截取的字符串
    """
    if isinstance(s, str) is False:
        raise TypeError('s must be str')
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse('hello'))
    print(substr('hello', 1, 3))
