"""
NumPy 04 - ndarray 读写

1.4.2 列表/ndarray 访问：类似 Python list，arr[1] 取第 2 行
  l2 = [[1,2,3],[2,3,4]]  →  l2[1] = [2,3,4]
  arr = np.array(l2)       →  arr[1] = array([2,3,4])

文件读写：.npy（二进制）/ .npz（压缩）/ .txt .csv（文本）
"""
import numpy as np
import os

# 列表/ndarray 访问：正索引、负索引、嵌套
l1 = [1, 2, 3, 4, 5]
print("l1[1]:", l1[1])      # 2
print("l1[-1]:", l1[-1])    # 5 负索引取最后

# 1D ndarray：直接索引、变量索引
np.random.seed(42)
arr1 = np.random.randint(0, 100, size=10)
print("arr1:", arr1)
print("arr1[1], arr1[2]:", arr1[1], arr1[2])  # 直接索引
index = 1
print("arr1[index]:", arr1[index])  # 变量索引
# fancy indexing：用整数列表作为索引，按顺序、可重复取元素
index1 = [1, 2, 1, 2, 1, 2]
print("arr1[index1]:", arr1[index1])

l2 = [[1, 2, 3], [2, 3, 4]]
arr = np.array(l2)
print("l2[1]:", l2[1])      # [2, 3, 4]
print("l2[1][0]:", l2[1][0])  # 2 嵌套访问
print("arr[1]:", arr[1])    # array([2, 3, 4])
# ndarray[dim1_index, dim2_index, ...]  dim_index 可为: int / [int] / 切片
print("arr[1,0]:", arr[1, 0])  # 2

# 2D fancy indexing：取多行、取多列
arr2 = np.random.randint(0, 100, size=(5, 5))
print("\narr2 (5x5):\n", arr2)
print("arr2[[0, 1]] 取第 0、1 行:\n", arr2[[0, 1]])
print("arr2[:, [0, 1]] 取第 0、1 列:\n", arr2[:, [0, 1]])
print("arr2[:, [1, 2]] 取第 1、2 列:\n", arr2[:, [1, 2]])




# ndarray 索引总结

## arr[1, 0] 与 arr2[[0, 1]] 的区别

### arr[1, 0] — 标量索引（取单个元素）

#- `1` 和 `0` 分别表示**行索引**和**列索引**
#- 得到的是**一个标量值**（比如 2）
#- 等价于 `arr[1][0]`

### arr2[[0, 1]] — Fancy indexing（取多行）

#- `[0, 1]` 是一个**索引列表**，表示要取第 0 行和第 1 行
#- 得到的是**一个新的二维数组**（包含这两行）
#- 可以取任意顺序、可重复，例如：`arr2[[2, 0, 1]]`、`arr2[[1, 1, 0]]`

## 对比表

#| 写法 | 含义 | 结果形状 |
#|------|------|----------|
#| `arr[1, 0]` | 第 1 行、第 0 列的元素 | 标量 |
#| `arr2[[0, 1]]` | 第 0 行和第 1 行 | 2×列数 |
#| `arr2[:, [0, 1]]` | 所有行、第 0 列和第 1 列 | 行数×2 |

## 要点

#- **单层方括号** `[1, 0]`：表示不同维度的索引，取单个元素
#- **双层方括号** `[[0, 1]]`：列表表示用索引数组做 fancy indexing，取多行或多列



# 1.4.3 切片访问
print("\n=== 1.4.3 切片访问 ===")
# arr1 切片：正索引、负索引、步长
print("arr1[0:3]:", arr1[0:3])     # 前 3 个元素
print("arr1[-4:]:", arr1[-4:])     # 后 4 个元素
print("arr1[0:-1:2]:", arr1[0:-1:2])  # 从索引 0 到倒数第 2 个，步长 2
print("arr1[::-1]:", arr1[::-1])      # 反转
print("arr1[::-2]:", arr1[::-2])      # 反转后每 2 个取 1 个
perm = np.random.permutation(10)
print("np.random.permutation(10):", perm)  # 生成 0-9 的随机排列
# 切片 [start:stop:step]，与 Python list 一致
print("perm[2:5]:", perm[2:5])   # 索引 2 到 4
print("perm[::2]:", perm[::2])   # 步长 2
print("perm[::-1]:", perm[::-1]) # 反转
# 在原始数据中，随机取3个数
rand_indices = np.random.permutation(10)[[0, 1, 2]]  # 或 [:3] 这行代码的作用是生成 0-9 的随机乱序数组，然后取前 3 个元素
#[[0, 1, 2]]：这是双层中括号，表示取前 3 个元素。
#这是 NumPy 的花式索引（Fancy Indexing），表示从前面的乱序数组中，取出索引为 0、1、2 的元素（也就是前 3 个元素）。
#注意：这里用双层中括号 [[0,1,2]] 和单层 [0,1,2] 效果一致，都是取这三个索引的元素，返回一维数组。
print("随机3个索引:", rand_indices)
print("arr1中对应值:", arr1[rand_indices])

# 1.4.4 习题
print("\n=== 1.4.4 习题 ===")
# 1. 构建长度为10的随机数组，逆序输出
ex1 = np.random.randint(0, 100, 10)
print("1. 随机数组逆序:", ex1, "->", ex1[::-1])

# 2. 形状(5,4)的二维数组，提取最后两列，3种方法
ex2 = np.random.randint(0, 100, (5, 4))
print("2. 提取最后两列，方法1 切片[:, 2:]:\n", ex2[:, 2:])
print("   方法2 负索引[:, -2:]:\n", ex2[:, -2:])
print("   方法3 fancy indexing[:, [2,3]]:\n", ex2[:, [2, 3]])

# 3. 6行5列数组，行方向随机排序
ex3 = np.random.randint(0, 100, (6, 5))
row_perm = np.random.permutation(6)
print("3. 行方向随机排序:\n", ex3[row_perm])

print("\n=== 1. 二进制格式 .npy（推荐，保留 dtype 等完整信息）===")
np.save("temp_array.npy", arr)#将数组保存为二进制文件，文件名是temp_array.npy np.save() 是 NumPy 库中用于将数组保存到二进制文件（.npy 格式）的核心函数
loaded = np.load("temp_array.npy")#从二进制文件中加载数组，文件名是temp_array.npy
print("保存后读取:", loaded)
os.remove("temp_array.npy")  # 清理文件

print("\n=== 2. 文本格式 .txt / .csv ===")
np.savetxt("temp_data.txt", arr, fmt="%d")#将数组保存为文本文件，文件名是temp_data.txt
loaded_txt = np.loadtxt("temp_data.txt")#从文本文件中加载数组，文件名是temp_data.txt
print("savetxt 保存后 loadtxt 读取:\n", loaded_txt)
os.remove("temp_data.txt")

print("\n=== 3. CSV 格式（指定分隔符）===")
np.savetxt("temp_data.csv", arr, delimiter=",", fmt="%d")#将数组保存为CSV文件，文件名是temp_data.csv
loaded_csv = np.loadtxt("temp_data.csv", delimiter=",")#从CSV文件中加载数组，文件名是temp_data.csv
print("CSV 读取:\n", loaded_csv)
os.remove("temp_data.csv")
