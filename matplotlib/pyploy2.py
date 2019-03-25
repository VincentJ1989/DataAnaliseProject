import matplotlib.pyplot as plt
import numpy as np

# 使用rc配置属性
# 原图
x = np.linspace(0, 4 * np.pi)
y = np.sin(x)

plt.plot(x, y, label="$sin(x)$")
plt.title('sin')
plt.savefig('../tmp/sin.png')
plt.show()

# 修改rc属性
plt.rcParams['lines.linestyle'] = "-."
plt.rcParams['lines.linewidth'] = 3
plt.plot(x, y, label="$sin(x)$")
plt.title('title')
plt.savefig('../tmp/修改rc后的sin曲线.png')
plt.show()

# 处理显示中文的问题
# 设置字体为SimHei显示中文--注意：这里可能是电脑上没这个字体库引起异常
plt.rcParams['font.sans-serif'] = 'SimHei'
# 设置正确显示符号
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x, y, label="$sin(x)$")
plt.title('title')
plt.savefig('../tmp/显示中文的png.png')
plt.show()
