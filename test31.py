"""
python 包
"""

# import my_package.my_module2
# import my_package.my_module3
#
# my_package.my_module2.info()
# my_package.my_module3.info()

# from my_package import my_module2
# from my_package import my_module3
#
# my_module2.info()
# my_module3.info()

# from my_package.my_module2 import info as info1
# from my_package.my_module3 import info as info2
#
# info1()
# info2()

from my_package import *

my_module2.info()

# init中all变量未定义module3 不能使用
# my_module3.info()
