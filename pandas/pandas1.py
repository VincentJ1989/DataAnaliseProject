# 读取数据:数据库数据、文本文件(一般文本和CSV文件)以及Excel文件
import pandas as pd

from sqlalchemy import create_engine

# ①读取数据库
# 创建一个MySql连接器，用户名为root，密码为1234
# 地址为127.0.0.1，数据库名为test.db,编码为utf-8
engine = create_engine('mysql+pymysql://root:12345678@127.0.0.1:3306/testdb?charset=utf8')
print(engine)

# 读取数据
formlist = pd.read_sql_query('show tables', con=engine)
print('testdb数据库表清单为：', '\n', formlist)
student_data = pd.read_sql('SELECT * FROM student', con=engine)
# 这样也可以student_data = pd.read_sql_table('student', con=engine)
print(student_data)
# 增加表
student_table = pd.read_sql_table('student', con=engine)
student_table.to_sql('boss', con=engine, index=False, if_exists='replace')
formlist = pd.read_sql_query('show tables', con=engine)
print('testdb数据库表清单为：', '\n', formlist)

# ②读写CSV文件
# 使用read_table读取--使用read_csv更佳
order = pd.read_table('../data/meal_order_info.csv', sep=',', encoding='gbk')
print('使用read_table进行读取：', order)
# 使用to_csv存
import os

print('写入csv前目录内文件列表为：\n', os.listdir('../tmp'))
# 开始写入
order.to_csv('../tmp/orderInfo.csv', sep=';', index=False)
print('写入csv后目录内文件列表为：\n', os.listdir('../tmp'))

# ③读写Excel文件（读需要pip3 install xrld，写需要pip3 install openpyxl）
# 使用read_excel读取
user = pd.read_excel('../data/users.xlsx')
print('客户用户信息的长度：', len(user))
# 使用to_excel存为excel
print('写入excel前目录内文件列表为：\n', os.listdir('../tmp'))
# 开始写入
user.to_excel('../tmp/userInfo.xlsx')
print('写入excel后目录内文件列表为：\n', os.listdir('../tmp'))
