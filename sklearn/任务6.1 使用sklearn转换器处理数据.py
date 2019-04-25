from sklearn.datasets import load_breast_cancer

# 6.1.1加载dataset模块中的数据集
cancer = load_breast_cancer()
print('cancer数据集的大小为:', len(cancer))
print('cancer数据集的类型为:', type(cancer))
# 常用属性:data、target、feature_names、DESCR
print('cancer数据集的数据为:\n', cancer['data'])
print('cancer数据集的标签为:\n', cancer['target'])
print('cancer数据集的特征名为:\n', cancer['feature_names'])
print('cancer数据集的描述为:\n', cancer['DESCR'])

# 6.1.2将数据集划分为训练集和测试集
# 一般需要把数据分为训练集(估计模型-50%)、验证集(确定网络结构或者控制模型复杂程度的参数-25%)、测试集(检验最优模型性能-25%)3个
# 当数据较少时，上面分3组的方法则不合适，常用的是留少部分作为测试集，对其余的N个样本采用K折交叉验证法。
# K折交叉验证法：把其余的N个样本均匀分为K份，轮流选其中的K-1份做训练，剩余1份做验证，计算预测误差平方和，最后把K次的预测误差平方和的均值作为选择最优模型结构的依据。

# sklearn的model_selection的train_test_split函数可以对数据集进行划分
cancer_data = cancer['data']
cancer_target = cancer['target']
print('原始数据集数据的shape为:\n', cancer_data.shape)
print('原始数据集标签的shape为:\n', cancer_target.shape)
from sklearn.model_selection import train_test_split

cancer_data_train, cancer_data_test, cancer_target_train, cancer_target_test = train_test_split(cancer_data,
                                                                                                cancer_target,
                                                                                                test_size=0.2,
                                                                                                random_state=42)
print('训练集数据的形状为：', cancer_data_train.shape)
print('训练集标签的形状为：', cancer_target_train.shape)
print('测试集数据的形状为：', cancer_data_test.shape)
print('测试集标签的形状为：', cancer_target_test.shape)

# 6.1.3 使用sklearn转换器进行数据预处理与降维
# 主要函数有3个：fit、transform、fit_transform
# 对iris数据进行离差标准化
import numpy as np
# 还有StandardScaler、Normalizer、Binarizer、OneHotEncoder、FunctionTransform
from sklearn.preprocessing import MinMaxScaler

# 生成规则
scaler = MinMaxScaler().fit(cancer_data_train)
# 将规则应用于训练集
cancer_train_scaler = scaler.transform(cancer_data_train)
# 将规则应用于测试集
cancer_test_scaler = scaler.transform(cancer_data_test)

print('离差标准化前训练集数据的最小值为:', np.min(cancer_data_train))
print('离差标准化后训练集数据的最小值为:', np.min(cancer_train_scaler))
print('离差标准化前训练集数据的最大值为:', np.max(cancer_data_train))
print('离差标准化后训练集数据的最大值为:', np.max(cancer_train_scaler))

print('离差标准化前测试集数据的最小值为:', np.min(cancer_data_test))
print('离差标准化后测试集数据的最小值为:', np.min(cancer_test_scaler))
print('离差标准化前测试集数据的最大值为:', np.max(cancer_data_test))
print('离差标准化后测试集数据的最大值为:', np.max(cancer_test_scaler))

# 对breast_cancer数据集PCA降维
from sklearn.decomposition import PCA

# 生成规则
# 参数含义：维度、是否复制一份原始数据、是否对将为后的数据进行归一化、代表使用的SVD算法(auto,full,arpack,randomized)
pca_model = PCA(n_components=10, copy=True, whiten=False, svd_solver='auto').fit(cancer_train_scaler)
# 将规则应用于训练集
cancer_train_pca = pca_model.transform(cancer_train_scaler)
# 将规则应用于测试集
cancer_test_pca = pca_model.transform(cancer_test_scaler)

print('PCA降维前训练集数据的shape为:', cancer_train_scaler.shape)
print('PCA降维后训练集数据的shape为:', cancer_train_pca.shape)
print('PCA降维前测试集数据的shape为:', cancer_test_scaler.shape)
print('PCA降维后测试集数据的shape为:', cancer_test_pca.shape)
