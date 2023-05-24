"""
继承
"""


class Phone:
    no = None
    producer = None

    def __init__(self, no, producer):
        self.no = no
        self.producer = producer

    def call_by_4g(self):
        print(f"{self.no}使用4G通话")


# 单继承
class SmartPhone(Phone):
    face_id = None

    def __init__(self, no, producer='小米', face_id=None):
        super().__init__(no, producer)
        self.face_id = face_id

    def call_by_5g(self):
        print(f"{self.no}使用5G通话")


phone = SmartPhone('15338869880')

phone.call_by_4g()
phone.call_by_5g()

phone2 = SmartPhone('15338869880', '华为')
print(phone2.producer)
print(phone2.face_id)


# 多继承
class NFCReader:
    nfc_type = '第五代'
    producer = 'HM'

    def read(self):
        print(f'{self.producer} 读取NFC卡信息')

    def write(self):
        print(f'{self.producer} 写入NFC卡信息')

    def use_nfc_type(self):
        print(f'NFCReader的NFC卡类型：{self.nfc_type} ')


class MyPhone(SmartPhone, NFCReader):
    pass


myPhone = MyPhone('15338869880')

myPhone.call_by_4g()
myPhone.call_by_5g()
myPhone.read()
myPhone.write()

# 同名属性或者方法，先继承的优先级最高（左边先）
print(myPhone.producer)


# 复写和使用父类成员
class MyPhone2(SmartPhone, NFCReader):
    nfc_type = '第六代'

    def call_by_5g(self):
        print(f"{self.no}使用自己的5G通话")
        super().call_by_5g()

    def use_nfc_type(self):
        print(f'自己的NFC卡类型：{self.nfc_type} ')
        # 第一种方式
        print('第一种方式')
        print(f'父类的NFC卡类型：{NFCReader.nfc_type} ')
        # 调用父类方法，被覆盖的属性还是子类的
        NFCReader.use_nfc_type(self)

        # 第二种方式，使用super()
        print('第二种方式，使用super()')
        print(f'父类的NFC卡类型：{super().nfc_type} ')
        # 调用父类方法，被覆盖的属性还是子类的
        super().use_nfc_type()


myPhone2 = MyPhone2('15338869880')

myPhone2.call_by_4g()
myPhone2.call_by_5g()

print(myPhone2.nfc_type)

myPhone2.use_nfc_type()
