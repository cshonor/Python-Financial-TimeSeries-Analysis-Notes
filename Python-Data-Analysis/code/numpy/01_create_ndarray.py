"""
NumPy 01 - 创建 ndarray
"""
import numpy as np

#ndarray（N-dimensional array）即N 维数组，是 NumPy 库的核心数据结构，专门用于高效存储和操作同类型的数值数据（比如整数、浮点数）。
#可以把它理解为：
#1 维 ndarray = 普通的一维数组 / 列表（但性能远优于 Python 原生列表）
#2 维 ndarray = 表格 / 矩阵（行 + 列）
#3 维 ndarray = 立方体（行 + 列 + 深度）
#N 维 ndarray = 更高维度的数值集合

# 1. 创建数组
print("=== 创建数组 ===")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.zeros((3, 3))
arr4 = np.ones((2, 4))
#这行代码是基于 NumPy 库创建一个指定形状的数组，核心作用是生成一个2 行 4 列、所有元素值都为 1 的二维数组。
arr5 = np.arange(0, 10, 2)
#arange 的核心逻辑是指定 “起始值、终止值、步长”，而非 “指定个数”
#这行代码含义：从 0 开始，以 2 为步长，生成小于 10 的整数序列（不包含终止值 10）
#计算过程：0 → 0+2=2 → 2+2=4 → 4+2=6 → 6+2=8（下一个是 10，等于终止值，停止）
arr6 = np.linspace(0, 1, 5)
#linspace 的核心逻辑是指定 “起始值、终止值、元素个数”
#这行代码的核心作用是：在指定的数值范围 [0, 1] 内，生成5 个等间距、均匀分布的数值，最终返回一个一维数组。
#计算过程：0 → 0.25 → 0.5 → 0.75 → 1.0（正好 5 个值）
print(f"一维数组: {arr1}")
print(f"类型验证 type(arr1): {type(arr1)}")  # numpy.ndarray
print(f"二维数组:\n{arr2}")
print(f"零矩阵:\n{arr3}")
print(f"全1矩阵:\n{arr4}")
print(f"等差数列 arange(0,10,2): {arr5}")
print(f"线性间隔 linspace(0,1,5): {arr6}")

# 2. 数组属性 (arr2 为 [[1,2,3],[4,5,6]]，2行3列)
print("\n=== 数组属性 ===")
print(f"shape 形状: {arr2.shape}")    # (2, 3)
print(f"ndim 维度: {arr2.ndim}")      # 2
print(f"size 元素个数: {arr2.size}")  # 6
print(f"dtype 数据类型: {arr2.dtype}")  # int64 或 int32
