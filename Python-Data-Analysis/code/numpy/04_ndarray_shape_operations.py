"""
NumPy 06 - ndarray 形状操作

reshape、ravel、flatten、resize 等，用于改变数组形状。
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print("原数组:", arr)

print("\n=== reshape 重塑（不改变原数组）===")
arr_2x3 = arr.reshape(2, 3)
print("reshape(2, 3):\n", arr_2x3)

print("\n=== flatten / ravel 展平为一维 ===")
print("flatten():", arr_2x3.flatten())
print("ravel():", arr_2x3.ravel())

print("\n=== 转置 T ===")
print("arr_2x3.T:\n", arr_2x3.T)
