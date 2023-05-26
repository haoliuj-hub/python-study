"""
mysql案例分析
"""
from pymysql import Connection

from second.test48_file_define import Record
from second.test48_file_reader import TxtReader, JSONReader

txt_reader = TxtReader('../../resource/2011年1月销售数据.txt')
data: list[Record] = txt_reader.read_data()

json_reader = JSONReader('../../resource/2011年2月销售数据JSON.txt')
data2: list[Record] = json_reader.read_data()

data_all = data + data2

conn = Connection(
    host='119.91.195.22',
    port=3306,
    user='testdb',
    password='TPpjjizZ7dCz86t4',
    database='testdb',
    autocommit=True
)

cursor = conn.cursor()

for record in data_all:
    cursor.execute('insert into orders (order_date, order_id, money, province) values (%s, %s, %s, %s)',
                   (record.date, record.order_id, record.money, record.province))

conn.close()
