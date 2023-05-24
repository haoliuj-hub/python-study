"""
封装
"""


class Phone:
    no = None

    __current_voltage = None

    def __init__(self, no, current_voltage):
        self.no = no
        self.__current_voltage = current_voltage

    def __keep_voltage(self):
        print("保持电压在5V")

    def call_by_5g(self):
        if self.__current_voltage >= 5:
            print("使用5G通话")
        else:
            self.__keep_voltage()


p1 = Phone("华为", 5)
print(p1.no)

# 私有成员无法访问
# print(p1.__current_voltage)

# 私有方法无法访问
# p1.__keep_voltage()

p1.call_by_5g()
