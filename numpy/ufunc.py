import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
# 四则运算
print('数组相加：\n', x + y)
print('数组相减：\n', x - y)
print('数组相乘：\n', x * y)
print('数组相除：\n', x / y)
print('数组幂运算：\n', x ** y)

# 比较运算
x = np.array([1, 3, 5])
y = np.array([2, 3, 4])
print('数组比较：\n', x <= y)
print('数组比较：\n', x > y)
print('数组比较：\n', x == y)
print('数组比较：\n', x != y)

print('逻辑and运算：\n', np.all(x == y))
print('逻辑or运算：\n', np.any(x == y))

# 广播机制
arr1 = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]])
arr2 = np.array([1, 2, 3])

print('数组相加为：\n', arr1 + arr2)
arr2 = np.array([1, 2, 3, 4]).reshape(4, 1)
print('数组相加为：\n', arr1 + arr2)
