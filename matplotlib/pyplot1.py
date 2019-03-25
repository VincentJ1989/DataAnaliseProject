import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0, 1.1, 0.01)
# 设置标题
plt.title('lines')
# 添加轴名称和范围
plt.xlabel('x')
plt.xlim(0, 1)
plt.ylabel('y')
plt.ylim(0, 1)
# 设置刻度
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])

# 添加曲线
# 添加y = x^2和y = x^4曲线
plt.plot(data, data ** 2)
plt.plot(data, data ** 4)
# 设置图例
plt.legend(['y = x^2', 'y = x^4'])
# 保存图片
plt.savefig('../tmp/y=x^2.png')
# 展示图片
plt.show()

# 例子2
rad = np.arange(0, np.pi * 2, 0.01)
# 第一个子图
# 确定画布的大小
p1 = plt.figure(figsize=(8, 6), dpi=80)
# 创建一个2行1列的子图，并开始绘制第一幅
ax1 = p1.add_subplot(2, 1, 1)
plt.title('lines')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim((0, 1))
plt.xlim((0, 1))
plt.xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
plt.plot(rad, rad ** 2)
plt.plot(rad, rad ** 4)
plt.legend(['y=x^2', 'y=x^4'])
# 第二个子图
ax2 = p1.add_subplot(2, 1, 2)
plt.title('sin/cos')
plt.xlabel('rad')
plt.ylabel('value')
plt.xlim((0, np.pi * 2))
plt.ylim((-1, 1))
plt.xticks([0, np.pi / 2, np.pi, np.pi * 1.5, np.pi * 2])
plt.yticks([-1, -0.5, 0, 0.5, 1])
plt.plot(rad, np.sin(rad))
plt.plot(rad, np.cos(rad))
plt.legend(['sin', 'cos'])
plt.savefig('../tmp/sincos.png')
plt.show()
