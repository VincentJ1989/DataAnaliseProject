import numpy as np

# 创建数据类型
df = np.dtype([('name', np.str_, 40), ('numitems', np.int64), ('price', np.float64)])
print(np.dtype(df['name']))
# 数组的数据类型默认是浮点型
itemz = np.array([('tomatoes', 42, 4.14), ('cabbages', 13, 1.72)], dtype=df)
print('自定义数据为：', itemz)
