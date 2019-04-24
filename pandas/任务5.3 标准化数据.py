import numpy as np
import pandas as pd

detail = pd.read_csv('../data/detail.csv', index_col=0, encoding='gbk')


# 5.3.1 离差标准化：转化为[0,1]之间,不改变数据分布
def min_max_scale(data):
    """定义离差标准化函数"""
    data = (data - data.min()) / (data.max() - data.min())
    return data


# 对菜品订单表售价和销量做离差标准化
count_data = min_max_scale(detail['counts'])
amount_data = min_max_scale(detail['amounts'])
data3 = pd.concat([count_data, amount_data], axis=1)
print('原始数据前5个为:\n', detail[['counts', 'amounts']].head())
print('离差标准化之后的前5个为:\n', data3.head())


# 5.3.2 标准差标准化数据：也叫0均值标准化或者z分数标准化，不改变数据分布--应用最为广泛的方法
# 处理后的数据均值为0,标准差为1(???高斯分布么?),取值的区间不限制为[0,1],可能为负值
def std_scale(data):
    """定义标准差标准化函数"""
    data = (data - data.mean()) / data.std()
    return data


# 对菜品订单表售价和销量做标准差
count_std_data = std_scale(detail['counts'])
amount_std_data = std_scale(detail['amounts'])
std_data = pd.concat([count_std_data, amount_std_data], axis=1)
print('原始数据前5为:\n', detail[['counts', 'amounts']].head())
print('标准差标准化之后前5位:\n', std_data.head())


# 5.3.3 小数定标标准化数据：通过移动数据的小数位数，将数据映射到[-1,1]，移动端额小数位数取决于数据绝对值的最大值
def decimal_scale(data):
    data = data / 10 ** np.ceil(np.log10(data.abs().max()))
    return data


# 对菜品订单表售价和销量做标准化
count_decimal_data = decimal_scale(detail['counts'])
amount_decimal_data = decimal_scale(detail['amounts'])
decimal_data = pd.concat([count_decimal_data, amount_decimal_data], axis=1)
print('原始数据前5为：\n', detail[['counts', 'amounts']].head())
print('小数定标标准化之后前5为：\n', decimal_data.head())
