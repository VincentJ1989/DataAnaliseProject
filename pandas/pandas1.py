# 读取数据:数据库数据、文本文件(一般文本和CSV文件)以及Excel文件
import pandas as pd

from sqlalchemy import create_engine

# 创建一个MySql连接器，用户名为root，密码为1234
# 地址为127.0.0.1，数据库名为test.db,编码为utf-8
engine = create_engine('mysql+pymysql://root:12345678@127.0.0.1:3306/testdb?charset=utf8')
print(engine)

# 读取数据
formlist = pd.read_sql_query('show tables', con=engine)
print('testdb数据库表清单为：', '\n', formlist)
student_data = pd.read_sql('SELECT * FROM student', con=engine)
print(student_data)
# 增加表
student_table = pd.read_sql_table('student', con=engine)
student_table.to_sql('boss', con=engine, index=False, if_exists='replace')
