"""
多态：父类定义声明。子类实现，用于获得同一行为，不同状态

抽象类
"""


class Animal():
    def run(self):
        pass


class Dog(Animal):
    def run(self):
        print('dog run')


class Cat(Animal):
    def run(self):
        print('cat run')


def run_twice(data: Animal):
    data.run()
    data.run()


run_twice(Dog())
run_twice(Cat())


class Duck(Animal):
    def run(self):
        print('duck run')
