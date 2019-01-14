import numpy as np

# 创建数组
arr1 = np.array([1, 2, 3, 4])
print('创建的数组为：', arr1)

arr2 = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
print('创建的数组为：\n', arr2)

# 查看数组结构
print('数组结构：', arr2.shape)
# 查看数组类型
print('数组类型：', arr2.dtype)
# 查看数组元素个数
print('数组元素个数为：', arr2.size)
# 查看数组每个元素大小
print('数组每个元素大小为：', arr2.itemsize)

# 从(3,4)-->(4,3):不是矩阵的转置，仅仅是行列数变化而已!
arr2.shape = 4, 3
print('重新设置shape后的arr2:\n', arr2)

# 内置的一些创建数组的函数
# arange--开始值，终值，步长
print('使用arange函数创建的数组为:\n', np.arange(0, 1, 0.1))
# linspace--开始值，终值，元素个数
print('使用lispace函数创建的数组为：\n', np.linspace(0, 9, 10))
# logspace:和linspace差不多，这个是等比数列--10^0~10^2，分割成3个等比
print('使用logspace函数创建的数组为:\n', np.logspace(0, 2, 3))

# 其他的一些创建函数
# 生成都是0的数组
print('使用zeros创建的0数组：\n', np.zeros((2, 3)))
# 生成主对角线上元素为1，其他元素为0的数组
print('使用eye函数创建的数组：\n', np.eye(3))
# 生成对角线上数值自定义，其他元素为0的数组
print('使用diag函数创建的数组：\n', np.diag([1, 2, 3, 4]))
# 生成所有元素都是1的数组（行*列）
print('使用ones函数闯将的数组：\n', np.ones((5, 3)))

# 数据类型转换
print('数据转换结果：', np.float64(42))
print('数组转换结果：', np.int8(42.0))
print('数据转换结果：', np.bool(42))
print('数据转换结果：', np.bool(0))
print('数据转换结果：', np.float(True))
print('数据转换结果：', np.float(False))

# 随机数生成

# rand:均分布随机数
print('生成均分布随机数：\n', np.random.rand(10))
# randn:生成服从正态分布的随机数
print('生成服从正态分布随机数：\n', np.random.randn(10))
# randint:生成给定上下限范围的随机数
print('生成上下限范围的随机数：\n', np.random.randint(2, 10, size=(2, 5)))
