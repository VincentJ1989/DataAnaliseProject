from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler

iris = load_iris()

# 6.2.1使用sklearn估计器构建聚类模型
iris_data = iris['data']
iris_target = iris['target']
iris_names = iris['feature_names']
# 训练规则
scale = MinMaxScaler().fit(iris_data)
# 把规则应用与数据
iris_data_scale = scale.transform(iris_data)
# 构建并训练模型
kmeans = KMeans(n_clusters=3, random_state=123).fit(iris_data_scale)
print('构建的KMean模型为:\n', kmeans)

result = kmeans.predict([[1.5, 1.5, 1.5, 1.5]])
print('化板宽度都是1.5的花的预测类别为:', result[0])
# 通过sklearn的manifold模块的TSNE函数进行可视化
import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# 使用TSNE进行数据降维，降成两维
tsne = TSNE(n_components=2, init='random', random_state=177).fit(iris_data)
df = pd.DataFrame(tsne.embedding_)  # 将原始数据转化为DF
df['labels'] = kmeans.labels_  # 将聚类结果存到df数据表中
# 提取不同标签的数据
df1 = df[df['labels'] == 0]
df2 = df[df['labels'] == 1]
df3 = df[df['labels'] == 2]
# 画图
fig = plt.figure(figsize=(9, 6))
# 用不同的颜色表示不同数据
plt.plot(df1[0], df1[1], 'bo', df2[0], df2[1], 'r*', df3[0], df3[1], 'gD')

plt.savefig('../tmp/聚类结果.png')
plt.show()

# 6.2.2评价聚类模型
# 聚类评价的标准是组内的对象相互之间是相似的(相关的)，而不同组中的对象是不同的(不相关的)。
# sklearn中的metrics模块提供的聚类模型评价指标(6大方法)。
# 使用FMI评价法评价K-Means聚类模型
from sklearn.metrics import fowlkes_mallows_score

for i in range(2, 7):
    # 构建并训练模型
    kmeans = KMeans(n_clusters=i, random_state=123).fit(iris_data)
    score = fowlkes_mallows_score(iris_target, kmeans.labels_)
    print('iris数据集%d类FMI的评分值为:%f' % (i, score))

# 使用轮廓系数评价法评价K-Means聚类模型
from sklearn.metrics import silhouette_score

slihhouettteScore = []
for i in range(2, 15):
    # 构建并训练模型
    kmeans = KMeans(n_clusters=i, random_state=123).fit(iris_data)
    score = silhouette_score(iris_data, kmeans.labels_)
    slihhouettteScore.append(score)

plt.figure(figsize=(10, 6))
plt.plot(range(2, 15), slihhouettteScore, linewidth=1.5, linestyle='-')
plt.show()

# 使用Calinski-Harabasz指数评价K-Means聚类模型
from sklearn.metrics import calinski_harabaz_score

for i in range(2, 7):
    # 构建并训练模型
    kmeans = KMeans(n_clusters=i, random_state=123).fit(iris_data)
    score = calinski_harabaz_score(iris_data, kmeans.labels_)
    print('iris数据聚%d类calinski_harabaz指数为:%f' % (i, score))
