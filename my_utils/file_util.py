"""
文件工具包
"""


def print_file_info(file_name):
    """
    打印文件内容
    :param file_name:文件名称或者带路径名称
    :return:None
    """
    f = None
    try:
        f = open(file_name, 'r', encoding='utf-8')
    except FileNotFoundError:
        print(f"文件{file_name}不存在")
    else:
        print(f.read())
    finally:
        if f:
            f.close()


def append_to_file(file_name, data):
    """
    追加内容到文件
    :param file_name: 文件名称或者带路径名称
    :param data: 追加内容
    :return:None
    """
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(data)
        f.flush()


if __name__ == '__main__':
    print_file_info('resource/test.txt')
    print_file_info('resource/测试.txt')

    append_to_file('resource/测试.txt', '你好')
