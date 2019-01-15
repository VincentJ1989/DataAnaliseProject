# 创建矩阵
import numpy as np

# ；号而不是，
matr1 = np.mat('1 2 3;4 5 6;7 8 9')
print('mat创建矩阵为:\n', matr1)

matr2 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('matrix创建矩阵:\n', matr2)

# 使用bmat分块矩阵函数实现将小矩阵组合成大矩阵--其运算速度比for循环快
arr1 = np.eye(3)
arr2 = arr1 * 3
print('bmat组合矩阵为：\n', np.bmat('arr1 arr2'))
print('bmat组合矩阵为：\n', np.bmat('arr1 arr2;arr1 arr2'))
print('bmat组合矩阵相加为：\n', np.bmat(arr1 + arr2))
print('bmat组合矩阵相减为：\n', np.bmat(arr2 - arr1))
print('bmat组合矩阵相乘为：\n', np.bmat(arr1 * arr2))
print('bmat组合矩阵对应元素相乘为：\n', np.multiply(arr1, arr2))

# 其他一些矩阵特有的属性
print('转置：\n', matr1.T)
# 实数的共轭就是其自身
print('共轭转置：\n', matr1.H)
print('矩阵二维数组：\n', matr1.A)
# print('逆矩阵：\n', matr1.I)
