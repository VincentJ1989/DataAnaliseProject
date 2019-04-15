# 4.2.3 描述分析DataFrame数据
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:12345678@127.0.0.1:3306/testdb?charset=utf8')
detail = pd.read_sql_table('meal_order_detail1', con=engine)
# ①数值型特征
# 均值:mean
print('订单详情表中amounts(价格)的平均值为:', detail['amounts'].mean())
# 均值，四分位数，标准差std：describe
print('counts和amounts两列的描述性统计为:\n', detail[['counts', 'amounts']].describe())

# ②类别型特征--频数统计表
print('dishes_name频数统计结果前10为：\n', detail['dishes_name'].value_counts()[:10])
detail['dishes_name'] = detail['dishes_name'].astype('category')
print('类型转换后的类型为:',detail['dishes_name'].dtype)
# 对应的字段分别为：列非空元素的数目、类别的数目、数目最多的类别和数目最多类别的数据
print('dishes_name的描述统计结果：\n',detail['dishes_name'].describe())
