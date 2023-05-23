"""
面向对象-类
"""

"""
类的定义
class 类名:
    类属性
    类方法
"""


class Student:
    """
    学生类
    """
    name = None
    gender = None
    age = None

    def say_hi(self):
        """
        打招呼
        :return: None
        """
        print(f"Hi，大家好，我是{self.name}")

    def say_hi2(self, msg):
        """
        打招呼
        :return: None
        """
        print(f"Hi，大家好，我是{self.name}，{msg}")


stu_1 = Student()
stu_1.name = "张三"
stu_1.gender = "男"
stu_1.age = 18

stu_2 = Student()
stu_2.name = "李四"
stu_2.gender = "女"
stu_2.age = 20

print(type(stu_1))
print(stu_1 == stu_2)

stu_1.say_hi()
stu_2.say_hi()

stu_1.say_hi2("你好")
stu_2.say_hi2("你好")

stu_3 = Student()
stu_3.say_hi()


class Clock:
    """
    时钟类
    """
    id = None
    price = None

    def ring(self):
        """
        响铃
        :return: None
        """
        # 判断操作系统是windows还是mac
        import platform
        system = platform.system()
        if system == "Windows":
            # windows下的语音播报
            import winsound
            winsound.Beep(600, 1000)
        elif system == "Darwin":
            # mac下的语音播报
            import os
            os.system(f"say 你好，我是你的闹钟，编号是{self.id}，价格是{self.price}")
        else:
            print("不支持的操作系统")


clock_1 = Clock()
clock_1.id = "001"
clock_1.price = 100

clock_1.ring()

clock_2 = Clock()
clock_2.id = "002"
clock_2.price = 200

clock_2.ring()
