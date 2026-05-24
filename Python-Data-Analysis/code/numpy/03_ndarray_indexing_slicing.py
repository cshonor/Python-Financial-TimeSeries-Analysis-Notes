"""
NumPy 05 - ndarray 索引与切片

与 Python 列表类似，支持下标、切片；多维数组用逗号分隔各维度。
"""
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print("原数组:\n", arr)

print("\n=== 索引 ===")
print("arr[0] 第一行:", arr[0])
print("arr[1, 2] 第2行第3列:", arr[1, 2])

print("\n=== 切片 ===")
print("arr[:, 0] 第一列:", arr[:, 0])
print("arr[1:3, 1:3] 子数组:\n", arr[1:3, 1:3])
print("arr[::2] 隔行取:", arr[::2])
