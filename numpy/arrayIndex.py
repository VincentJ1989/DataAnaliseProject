# 通过索引访问数组
import numpy as np

# 一维数组
# 记住左闭右开即可
arr = np.arange(10)
print(arr[5])
print(arr[3:5])
print(arr[:5])
print(arr[-5:])
# 第一个到倒数第一个，步长2
print(arr[1:-1:2])
# 通过索引修改值
arr[2:4] = 100, 101
print(arr)

# 多维数组
arr2 = np.array([[1, 2, 3, 4, 5], [4, 5, 6, 7, 8], [7, 8, 9, 10, 11]])
print('创建的二维数组为：\n', arr2)
# 获取第0行中，第3,4个数
print('索引结果为：]\n', arr2[0, 3:5])
# 获取第3~5列数
print("索引结果为：\n", arr2[:, 3:])
# 组合横纵坐标取值
print('索引结果为：\n', arr2[[(0, 1, 2), (1, 2, 3)]])

# 获取1，3行第2列数据--使用布尔值索引访问数组
mark = np.array([1, 0, 1], dtype=np.bool)
print('索引结果为：\n', arr2[mark, 2])

# 变换数组的形态
arr3 = np.arange(12)
print('创建的一维数组为：', arr3)
print('reshape之后的数组为：\n', arr3.reshape(3, 4))
print('reshape后的维度为：', arr3.reshape(3, 4).ndim)

# ravel展开数据（横向）
arr4 = np.arange(12).reshape(3, 4)
print('创建的二维数组为：\n', arr4)
print('数组展开后：', arr4.ravel())

# flatten展开数据(可以横向，也可以纵向)
print('横向展开：', arr4.flatten())
print('纵向展开：', arr4.flatten('F'))

# 数组的组合
# hstack函数横向组合，vstack纵向组合
arr5 = np.arange(12).reshape(3, 4)
arr6 = arr5 * 3
print('横向组合为：\n', np.hstack((arr5, arr6)))
print('纵向组合为：\n', np.vstack((arr5, arr6)))
# 使用concatenate+axis也可以实现组合，其中axis=1横向组合，为0则纵向组合
print('concatenate横向组合：\n', np.concatenate((arr5, arr6), 1))
print('concatenate纵向组合：\n', np.concatenate((arr5, arr6), 0))

# 数组分割
arr7 = np.arange(16).reshape(4, 4)
# 分割为左右2部分
print('横向分割：\n', np.hsplit(arr7, 2))
# 分割为上下2部分
print('纵向分割:\n', np.vsplit(arr7, 2))

# 同样的，split+axis也可以实现分割，其中axis=1为横向分割，为0即纵向分割
print('split横向分割：\n', np.split(arr7, 2, axis=1))
print('splie纵向分割：\n', np.split(arr7, 2, axis=0))
