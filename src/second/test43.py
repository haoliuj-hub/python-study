"""
类-构造方法
类-魔术方法
"""


class Person:

    # 可以省略
    # name = None
    # age = None

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("我是%s,今年%d岁" % (self.name, self.age))


p1 = Person("张三", 18)
p1.say()

# p2 = Person("李四")
# p2.say()
#
# p3 = Person()
# p2.say()


