import matplotlib.pyplot as plt
import numpy as np

# 绘制直方图、饼图、箱线图
plt.rcParams['font.sans-serif'] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False

data = np.load('../data/国民经济核算季度数据.npz')
name = data['columns']
values = data['values']

label = ['第一产业', '第二产业', '第三产业']

plt.figure(figsize=(6, 5))
# 绘制直方图
plt.bar(range(3), values[-1, 3:6], width=0.5)

plt.xlabel('产业')
plt.ylabel('生产总值(亿元)')
plt.xticks(range(3), label)
plt.title('2017年第一季度各产业国民生产总值直方图')
plt.savefig('../tmp/直方图.png')
plt.show()

# 绘制饼图
plt.figure(figsize=(6, 6))
label = ['第一产业', '第二产业', '第三产业']
# 设置各个数据的半径
explode = [0.01, 0.01, 0.01]
# 绘制饼图
plt.pie(values[-1, 3:6], explode=explode, labels=label, autopct='%1.1f%%')
plt.title('2017年第一季度个产业国民生产总值饼图')
plt.savefig('../tmp/生产总值饼图.png')
plt.show()

# 绘制箱线图
plt.figure(figsize=(6, 4))
label = ['第一产业', '第二产业', '第三产业']
gdp = (list(values[:, 3]), list(values[:, 4]), list(values[:, 5]))
plt.boxplot(gdp, notch=True, labels=label, meanline=True, sym='o')
plt.title('2017年第一季度各产业国民生产总值箱线图')
plt.savefig('../tmp/生产总值箱线图.png')
plt.show()
