from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 使用sklearn估计器构建线性回归模型
# 加载数据
boston = load_boston()
X = boston['data']
y = boston['target']
names = boston['feature_names']
# 划分数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=125)
# 建立模型
clf = LinearRegression().fit(X_train, y_train)
print('建立的模型为:', clf)
# 预测训练集结果
y_pred = clf.predict(X_test)
print('预测的前20个结果为:\n', y_pred[:20])

# 回归结果可视化
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = 'SimHei'
fig = plt.figure(figsize=(10, 6))
plt.plot(range(y_test.shape[0]), y_test, linewidth=1.5, linestyle='-', color='blue')
plt.plot(range(y_test.shape[0]), y_pred, linewidth=1.5, linestyle='-', color='red')
plt.xlim((0, 102))
plt.ylim((0, 55))
plt.legend(['真实值', '预测值'])
plt.show()

# 评价回归模型
from sklearn.metrics import explained_variance_score, mean_absolute_error, mean_squared_error, median_absolute_error, \
    r2_score

print('平均绝对误差:', mean_absolute_error(y_test, y_pred))
print('均方误差:', mean_squared_error(y_test, y_pred))
print('中值绝对误差:', median_absolute_error(y_test, y_pred))
print('可解释方差:', explained_variance_score(y_test, y_pred))
print('R2值:', r2_score(y_test, y_pred))
