"""
mysql
"""

from pymysql import Connection

# 获取mysql数据库链接

conn = Connection(
    host='119.91.195.22',
    port=3306,
    user='testdb',
    password='TPpjjizZ7dCz86t4',
    database='testdb',
    autocommit=True
)

print(conn.get_server_info())

# 执行非查询性质的SQL语句
cursor = conn.cursor()
cursor.execute('create table if not exists user (id int primary key, name varchar(20))')

# 执行查询性质的SQL语句
cursor.execute('select * from user')

# 获取查询结果
results: tuple = cursor.fetchall()

print(results)
# 打印查询结果
for r in results:
    print(r)


# 插入数据
cursor.execute('insert into user (id, name) values (3, "王五")')

# 提交 加入了autocommit=True，不需要手动提交
conn.commit()

conn.close()
