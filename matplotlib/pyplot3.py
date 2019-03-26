import matplotlib.pyplot as plt
import numpy as np

# 散点图和折线图
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
data = np.load('../data/国民经济核算季度数据.npz')
# 提取列内容
name = data['columns']
values = data['values']
plt.figure(figsize=(8, 7))
plt.scatter(values[:, 0], values[:, 2], marker='o')
plt.xlabel('年份')
plt.ylabel('生产总值(亿元)')
plt.ylim((0, 225000))
plt.xticks(range(0, 70, 4), values[range(0, 70, 4), 1], rotation=45)
plt.title('2000~2017年各季度国民生产总值散点图')
plt.savefig('../tmp/生产总值散点图.png')
plt.show()

# 设置不同散点的颜色
plt.figure(figsize=(8, 7))
# 散点1
plt.scatter(values[:, 0], values[:, 3], marker='o', c='red')
# 散点2
plt.scatter(values[:, 0], values[:, 4], marker='D', c='blue')
# 散点3
plt.scatter(values[:, 0], values[:, 5], marker='v', c='yellow')

plt.xlabel('年份')
plt.ylabel('生产总值(亿元)')
plt.xticks(range(0, 70, 4), values[range(0, 70, 4), 1], rotation=45)
plt.title('2000~2017年各产业各季度国民生产总值散点图')
plt.legend(['第一产业', '第二产业', '第三产业', "第四产业"])
plt.savefig('../tmp/多颜色散点图.png')
plt.show()

# 绘制折线图
plt.figure(figsize=(8, 7))
plt.plot(values[:, 0], values[:, 2], color='r', marker='o', linestyle='--')
plt.xlabel = '年份'
plt.ylabel = '生产总值(亿元)'
plt.ylim((0, 225000))
plt.xticks(range(0, 70, 4), values[range(0, 70, 4), 1], rotation=45)
plt.title = '2000~2017年各季度国民生产总值折线图'
plt.savefig('../tmp/生产总值折线图.png')
plt.show()
