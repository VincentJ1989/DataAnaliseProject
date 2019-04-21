import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:12345678@127.0.0.1:3306/testdb?charset=utf8')
print(engine)
detail = pd.read_sql_table('meal_order_detail1', con=engine)
detail_group = detail[['order_id', 'counts', 'amounts']].groupby(by='order_id')
# 不能直接查看detail_group，输出的是内存地址
print('分组后的订单详情页的前6组每组的均值为:\n', detail_group.mean().head(6))
print('分组后前3组的标准差为:\n', detail_group.std().head(3))
print('分组后前4组的size为:\n', detail_group.size().head(4))

# 使用agg进行聚合数据
print('订单详情表的菜品销量与售价的和与均值为:\n', detail[['counts', 'amounts']].agg([np.sum, np.mean]))
# 其实就是对不同的列数据进行不同的取值，前者则会产生冗余的数据
print('订单详情标的菜品销售量总和与售价的均值为:\n', detail.agg({'counts': np.sum, 'amounts': np.mean}))
print('订单详情表的菜品销售量总和与售价的总和与均值为:\n', detail.agg({'counts': np.sum, 'amounts': [np.sum, np.mean]}))


# 使用自定义的函数替代NumPy的函数
def double_sum(data):
    """数量变为2倍"""
    s = np.sum(data) * 2
    return s


print('订单详情表的菜品销售量的2倍总和为:\n', detail.agg({'counts': double_sum}).head())
print('订单详情表的菜品销售量与售价的和的2倍为:\n', detail[['counts', 'amounts']].agg(double_sum))

# 使用apply函数聚合数据(传入的函数只能作用于整个DF或者Series,不能像agg那样对不同字段应用不同的函数)
print('订单详情表的菜品销售量与售价的均值为:\n', detail[['counts', 'amounts']].apply(np.mean))

print('订单详情表分组后前3组的每组的均值为:\n', detail_group.apply(np.mean).head(3))

# 使用transform函数进行聚合数据(只有一个func形参，能对整个的DF的元素进行操作)
print('订单详情表的菜品销售量与售价的2倍(前4个)为:\n', detail[['counts', 'amounts']].transform(lambda x: x * 2).head(4))
print('订单详情表分组后实现组内离差标准化后前5行为为:\n', detail_group.transform(lambda x: (x.mean() - x.min()) / (x.max() - x.min())).head())
