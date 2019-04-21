import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:12345678@127.0.0.1:3306/testdb?charset=utf8')
print(engine)

detail = pd.read_sql_table('meal_order_detail1', con=engine)
detail_pivot = pd.pivot_table(detail[['order_id', 'counts', 'amounts']], index='order_id')
# 默认的函数是np.mean
print('以order_id作为分组键创建的订单透视表前5个元素为:\n', detail_pivot.head())
detail_pivot1 = pd.pivot_table(detail[['order_id', 'counts', 'amounts']], index='order_id', aggfunc=np.sum)
print('以order_id作为分组键创建的订单销售量与售价总和的订单透视表为:\n', detail_pivot1.head(4))

detail_pivot2 = pd.pivot_table(detail[['order_id', 'dishes_name', 'counts', 'amounts']],
                               index=['order_id', 'dishes_name'],
                               aggfunc=np.sum)
print('以order_id和dishes_name为分组键创建的透视表为:\n', detail_pivot2.head(3))
# NaN设置为0
detail_pivot3 = pd.pivot_table(detail[['order_id', 'dishes_name', 'counts', 'amounts']], index='order_id',
                               columns='dishes_name', fill_value=0, aggfunc=np.sum)
print('以order_id和dishes_name为行列分组键创建的透视表为:\n', print(detail_pivot3.iloc[:5, :4]))

# 使用crosstab函数创建交叉表--特殊的透视表，主要用于计算分组频率
detail_cross = pd.crosstab(index=detail['order_id'], columns=detail['dishes_name'], values=detail['counts'],
                           aggfunc=np.sum)
print('以order_id和dishes_name为分组键，counts为值的透视表的前6行5列为:\n', detail_cross.iloc[:6, :5])
