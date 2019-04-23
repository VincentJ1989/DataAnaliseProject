import pandas as pd

detail = pd.read_csv('../data/detail.csv', index_col=0, encoding='gbk')


# 5.2.1 检测与处理重复值
# ①记录重复：一个或者多个特征的某几条记录的值完全相同
# 方法一:用列表(list)去重
def del_rep(list1):
    """去重"""
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)

    return list2


print('记录去重开始................')
dishes = list(detail['dishes_name'])
print('去重前的数据长度为:', len(dishes))
print('去重后的数据长度为:', len(del_rep(dishes)))
# 方法二：用集合(set元素的唯一性)去重--这个会引起数据的排列顺序发生改变！！
dish_set = set(dishes)
print('去重前的数据长度为:', len(dishes))
print('去重后的数据长度为:', len(dish_set))
# 方法③：pandas内置函数drop_duplicates,只对DF和Series起作用，排序不会改变，而且还能对多个特征去重
print('去重后的数据长度为:', len(detail['dishes_name'].drop_duplicates()))
print('多特征去重前的shape:', detail.shape)
shape_det = detail.drop_duplicates(subset=['order_id', 'emp_id']).shape
print('多特征去重后的shape:', shape_det)

# ②特征重复：存在一个或者多个特征名称不同，但数据完全相同的情况
print('特征去重开始................')
# 通过相似度矩阵去重只能针对数值型重复特征
corr_det = detail[['counts', 'amounts']].corr(method='kendall')
print('销量和售价的kendall法相似度矩阵为:\n', corr_det)


# 使用DF.equals去重
def feature_equals(df):
    """equals去重函数"""
    df_equals = pd.DataFrame([], columns=df.columns, index=df.columns)
    for i in df.columns:
        for j in df.columns:
            df_equals.loc[i, j] = df.loc[:, i].equals(df.loc[:, j])
    return df_equals


det_equals = feature_equals(detail)
print('detail特征相等的矩阵的前5行5列为：\n', det_equals.iloc[:5, :5])
# 再遍历筛选出完全重复的特征
len_det = det_equals.shape[0]
dup_col = []
for k in range(len_det):
    for m in range(k + 1, len_det):
        if det_equals.iloc[k, m] & (det_equals.columns[m] not in dup_col):
            dup_col.append(det_equals.columns[m])

# 去重
print('需要删除的列为：\n', dup_col)
detail.drop(dup_col, axis=1, inplace=True)
print('删除多余列后detail的特征数目为:', detail.shape[1])

# 5.2.2 检测与处理缺失值：isnull、notnull
print('每个特征缺失的数目为:', detail.isnull().sum())
print('每个特征非缺失的数目为:', detail.notnull().sum())
# ①删除法：将含有缺失值的特征或者记录删除(删除观测记录+删除特征)-dropna(2个都可以删除)
print('删除缺失值前的shape:', detail.shape)
# 0表示行(观测记录),1表示列(特征)
print('删除缺失值后的shape:', detail.dropna(axis=1, how='any').shape)
# ②替换法：特定值替换(数值型和类别型)--fillna（替换的值可以是自定义的，也可以用上一个或者下一个非空值）
detail = detail.fillna(-99)
print('detail填充默认值(-99)后，缺失的数目为:', detail.isnull().sum())
# ③插值法：线性插值、多项式插值(拉格朗日插值、牛顿插值)、样条插值--interpolate
# 虽然pandas有提供，但是SciPy中的interpolate更加强大

import numpy as np

x = np.array([1, 2, 3, 4, 5, 8, 9, 10])
y1 = np.array([2, 8, 18, 32, 50, 128, 162, 200])
y2 = np.array([3, 5, 7, 9, 11, 17, 19, 21])
# 线性插值
from scipy.interpolate import interp1d

linear_ins_value1 = interp1d(x, y1)
linear_ins_value2 = interp1d(x, y2)
print('当x为6,7时，对应的线性插值y1的值为：', linear_ins_value1([6, 7]))
print('当x为6,7时，对应的线性插值y2的值为：', linear_ins_value2([6, 7]))

# 拉格朗日插值
from scipy.interpolate import lagrange

lg_ins_value1 = lagrange(x, y1)
lg_ins_value2 = lagrange(x, y2)
print('当x为6,7时，对应的拉格朗日插值y1的值为：', lg_ins_value1([6, 7]))
print('当x为6,7时，对应的拉格朗日插值y2的值为：', lg_ins_value2([6, 7]))

# 样条插值--推荐用BSpline替换
from scipy.interpolate import spline

spline_ins_value1 = spline(x, y1, xnew=np.array([6, 7]))
spline_ins_value2 = spline(x, y2, xnew=np.array([6, 7]))
print('当x为6,7时，对应的样条插值y1的值为：', spline_ins_value1)
print('当x为6,7时，对应的样条插值y2的值为：', spline_ins_value2)


# 5.2.3检测与处理异常值：3σ原则和箱线图
# ①3σ原则：局限性只能针对正态分布或者近似正态分布的数据有效
def out_range(ser1):
    bool_ind = (ser1.mean() - 3 * ser1.std() > ser1) | (ser1.mean() + 3 * ser1.var() < ser1)
    index = np.arange(ser1.shape[0])[bool_ind]
    outrange = ser1.iloc[index]
    return outrange


outlier = out_range(detail['counts'])
print('使用3σ原则判定异常值的个数为:', outlier.shape[0])
print('异常值的最大值为:', outlier.max())
print('异常值的最小值为:', outlier.min())
# ②箱线图：QL(下四分位数)，QU(上四分位数)，IQR(四分位数间距)--不像3σ存在那样对分布的局限性
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
p = plt.boxplot(detail['counts'].values, notch=True)
# fliers为异常值的标签
outlier1 = p['fliers'][0].get_ydata()
plt.savefig('../tmp/菜品异常数据识别.png')
plt.show()
print('销售量数据异常值的个数为:', len(outlier1))
print('销售量数据异常值的最大值为:', max(outlier1))
print('销售量数据异常值的最小值为:', min(outlier1))
