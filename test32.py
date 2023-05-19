"""
异常-模块-包 案例
"""

from my_utils.str_util import str_reverse, substr
from my_utils import file_util

# str_reverse(12)
print(str_reverse('hello'))
print(substr('hello', 1, 3))

file_util.print_file_info('resource/test.txt')
file_util.print_file_info('resource/测试.txt')

file_util.append_to_file('resource/测试.txt', '你好')
