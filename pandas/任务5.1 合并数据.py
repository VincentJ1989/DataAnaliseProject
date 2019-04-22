import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:12345678@127.0.0.1:3306/testdb?charset=utf8")
print(engine)

detail = pd.read_sql_table('meal_order_detail1', con=engine)
# 横向堆叠
# 前10列数据
df1 = detail.iloc[:, :10]
# # 后9列
df2 = detail.iloc[:, -9:]
print('合并df1的大小为%s,df2的大小为%s。' % (df1.shape, df2.shape))
# axix = 0表示列对齐
print('外连接合并后的大小为：', pd.concat([df1, df2], axis=1, join='inner').shape)
print('内连接合并后的大小为：', pd.concat([df1, df2], axis=1, join='outer').shape)

# 纵向堆叠:concat、append(要求表的列名要完全一致)
df3 = detail.iloc[:1500, :]
df4 = detail.iloc[1500:, :]
print('合并df3的大小为%s,df4的大小为%s' % (df3.shape, df4.shape))
print('内连接合并后的大小为:', pd.concat([df3, df4], axis=1, join='inner').shape)
print('外链接合并后的大小为:', pd.concat([df3, df4], axis=1, join='outer').shape)

print('append纵向堆叠后的数据大小为:', df3.append(df4).shape)

# 主键合并数据：类似sql中的join--merge、join(主键名必须一样)
order = pd.read_csv('../data/meal_order_info.csv', sep=',', encoding='gb18030')
# 将info_id转换为字符串格式，为合并做准备
order['info_id'] = order['info_id'].astype(str)
# 都有订单id
order_detail = pd.merge(detail, order, left_on='order_id', right_on='info_id')
print('detail的大小为%s,order的大小为%s' % (detail.shape, order.shape))
print('detail和order按订单id主键合并后的数据大小为：%s', order_detail.shape)

order.rename({'info_id': 'order_id'}, inplace=True)
# rsuffix表示用于追加右侧重叠列名的尾缀(无默认)--报错了
# order_detail2 = detail.join(order,on='order_id', rsuffix='1')
# print('使用join合并后的大小为:',order_detail2.shape)

# 重叠合并数据
dict1 = {'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
         'System': ['win10', 'win10', np.nan, 'win10', np.nan, np.nan, 'win7', 'win7', 'win8'],
         'cpu': ['i7', 'i5', np.nan, 'i7', np.nan, np.nan, 'i5', 'i5', 'i3']}

dict2 = {'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
         'System': [np.nan, np.nan, 'win7', np.nan, 'win8', 'win7', np.nan, np.nan, np.nan],
         'cpu': [np.nan, np.nan, 'i3', np.nan, 'i7', 'i5', np.nan, np.nan, np.nan]}

# 把字典转换为DF
df5 = pd.DataFrame(dict1)
df6 = pd.DataFrame(dict2)
print('经过重叠合并后的数据为:\n', df5.combine_first(df6))
