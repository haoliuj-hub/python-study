"""
文件定义
"""


class Record:
    """
    记录
    """

    def __init__(self, date: str, order_id: str, money: int, province: str):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        return f"Record({self.date},{self.order_id},{self.money},{self.province})"
