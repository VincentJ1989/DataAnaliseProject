# 进行简单的统计分析
import numpy as np

# ①排序--直接排序、间接排序

# 直接排序sort:无返回值
arr = np.random.randint(1, 10, size=10)
print('创建的数组为：\n', arr)
print('排序后的数组为：\n', np.sort(arr))

# 注意原始数据被修改了
arr = np.random.randint(1, 10, size=(3, 3))
print('原始数组为：\n', arr)
print('X纵排序后的数组为：\n', np.sort(arr, axis=1))
print('Y排序后的数组为：\n', np.sort(arr, axis=0))

# 间接排序
# argsort排序--有返回值，返回对应的索引数组
arr = np.array([2, 3, 6, 8, 0, 7])
print('argsort排序后返回的索引数组：\n', np.argsort(arr))
# lexsort进行多个数组的排序:只接收一个参数
a = np.array([3, 2, 6, 4, 5])
b = np.array([50, 30, 40, 20, 10])
c = np.array([400, 300, 600, 100, 200])
d = np.lexsort((a, b, c))
# 多个键值排序时是按照最后一个传入数据计算的(所以下面的结果是按最后一列大小排序的)
print('lexsort排序后的数组为：\n', list(zip(a[d], b[d], c[d])))

# ②去重与重复数据
names = np.array(['小明', '小黄', '小花', '小明', '小花', '小兰', '小白'])
print('原始数据为：\n', names)
print('去重之后的数据为:\n', np.unique(names))
# 等价实现
print('去重之后的数据为:\n', sorted(set(names)))

# 复制数据：title、repeat
arr = np.arange(5)
print('复制数据为:\n', np.tile(arr, 3))
arr1 = np.random.randint(1, 9, size=(3, 3))
print('多维数组原始数据为：\n', arr1)
print('延X轴复制2次为：\n', arr1.repeat(2, axis=1))
print('延Y轴复制2次为：\n', arr1.repeat(2, axis=0))

# ③常用的统计函数
arr = np.arange(20).reshape(4, 5)
print('原始数组数据为：\n', arr)
print('数组的和为：', np.sum(arr))
print('数组纵向和为：', arr.sum(axis=1))
print('数组横向和为：', arr.sum(axis=0))
print('数组的均值为：', np.mean(arr))
print('数组的方差为:', np.var(arr))
print('数组的标准差为：', np.std(arr))
print('数组的最小值为：', np.min(arr))
print('数组的最大值为：', np.max(arr))
print('数组最小值的索引为：', np.argmin(arr))
print('数组最大值的索引为：', np.argmax(arr))

# 前面的都是聚合计算，直接显示计算的最终结果，这里使用sumsum和sumprod函数实现不聚合计算
arr = np.arange(2, 10)
print('数据元素的累计和为：', np.cumsum(arr))
print('数据元素的累计积为：', np.cumprod(arr))
