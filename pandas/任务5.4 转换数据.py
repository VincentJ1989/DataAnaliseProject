import numpy as np
import pandas as pd

detail = pd.read_csv('../data/detail.csv', encoding='gbk')

# 5.4.1哑变量处理类别型数据：主要是当一些算法只支持数值型数据而原始数据还有类别型数据时，
# 要经过哑变量处理用数值型替代，然后才能应用于那些算法--get_dummies
# 同时由于数据变为稀疏矩阵，加快了算法模型的运算速度
test_data = detail.loc[0:5, 'dishes_name']
print('哑变量处理前的数据为:\n', test_data)
print('哑变量处理后的数据为：\n', pd.get_dummies(test_data))

# 5.4.2 离散化连续性数据：因为某些算法模型(例如ID3决策树、Apriori)要求数据为离散
# 主要步骤：①确定分类数②如何进行映射
# 常用离散方法：等宽法、等频法、聚类分析法(一维)

# 等宽法:cut,对数据分布具有较高的要求
price = pd.cut(detail['amounts'], 5)
print('离散化后5条记录售价分布为:\n', price.value_counts())


# 等频法
def same_rate_cut(data, k):
    """自定义等频法离散化函数"""
    w = data.quantile(np.arange(0, 1 + 1.0 / k, 1.0 / k))
    data = pd.cut(data, w)
    return data


# 对菜品售价进行等频法离散化
result = same_rate_cut(detail['amounts'], 5).value_counts()
print('等频法离散化后各个类别数目分布状况:\n', result)


# 聚类分析法：(具体的后面学Ski-learn后再回来理解)
# 主要步骤：将连续型数据聚类+处理聚类得到的簇，为合并到一个簇的连续型数据做同一种标记
def kmean_cut(data, k):
    """自定义K-Mean聚类离散化函数"""
    from sklearn.cluster import KMeans
    kmodel = KMeans(n_clusters=k, n_jobs=4)  # 建立模型，n_jobs是并行数
    kmodel.fit(data.values.reshape((len(data), 1)))  # 训练模型
    c = pd.DataFrame(kmodel.cluster_centers_).sort_values(0)  # 输出聚类中心并排序
    w = c.rolling(2).mean().iloc[1:]  # 相邻两项求中点，作为边界点
    w = [0] + list(w[0]) + [data.max()]  # 把首末边界点加上
    data = pd.cut(data, w)
    return data


result1 = kmean_cut(detail['amounts'], 5).value_counts()
print('菜品售价聚类离散化后各个类别数目分布状况为:\n', result1)
