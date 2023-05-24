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

    # 魔术方法
    def __str__(self):
        return f"Person对象的name属性值是{self.name},age属性值是{self.age}"

    # 小于
    def __lt__(self, other):
        return self.age < other.age

    # 小于等于
    def __le__(self, other):
        return self.age <= other.age

    # 等于
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name


p1 = Person("张三", 18)
p1.say()

# p2 = Person("李四")
# p2.say()
#
# p3 = Person()
# p2.say()

# 字符串方法
print(p1)

p2 = Person("李四", 20)
print(p1 < p2)

print(p1 <= p2)

p3 = Person("张是", 18)
print(f"p1是否小于p3:{p1 < p3}")
print(f"p1是否小于等于p3:{p1 <= p3}")
print(f"p1是否等于p3:{p1 == p3}")
