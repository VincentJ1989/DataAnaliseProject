# 使用NumPy进行统计分析
import numpy as np

arr = np.arange(100).reshape(10, 10)
# 保存数组--如果不设置地址，则是默认地址
np.save("./save_arr", arr)
print('保存的数组为：\n', arr)

# savez保存多个数组数据
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.arange(0, 1.0, 0.1)
np.savez('./savez_arr', arr1, arr2)

# 读取文件的数据
loaded_data = np.load('./save_arr.npy')
print('读取出来的数据为：\n', loaded_data)
loaded_data2 = np.load('./savez_arr.npz')
print('读取多数组第一个数组的数据为：\n', loaded_data2['arr_0'])
print('读取多数组第二个数组的数据为：\n', loaded_data2['arr_1'])

# savatxt和loadtxt
arr = np.arange(0, 12, 0.5).reshape(4, -1)
# %d表示保存为整数，最后的参数表示分隔符
np.savetxt('./savetxt_arr', arr, fmt='%d', delimiter=',')
loaded_txt_data = np.loadtxt('./savetxt_arr', delimiter=',')
print('读取txt数据为：\n', loaded_txt_data)
loaded_txt_data2 = np.genfromtxt('./savetxt_arr', delimiter=',')
print('genfromtxt读取的数据为：\n', loaded_txt_data2)
