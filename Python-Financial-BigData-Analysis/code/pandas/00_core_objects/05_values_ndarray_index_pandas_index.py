"""
Pandas 02 - 为什么 values 是 ndarray，index 是 pandas.Index？

- values 用 ndarray：为了快，对接 NumPy 生态
- index 用 pandas.Index：为了灵活的标签定位、对齐
- 多维数据：用 DataFrame，不要塞进 Series
"""
import pandas as pd
import numpy as np

print("=== 1. values 用 ndarray：为了高性能计算 ===")
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("type(s.values):", type(s.values))  # numpy.ndarray
# ndarray 支持向量化运算、广播，可复用 NumPy/NumPy 生态函数

print("\n=== 2. index 用 pandas.Index：为了灵活的标签定位 ===")
print("type(s.index):", type(s.index))    # pandas.Index
# 支持自定义标签、快速查找、不可变性、按标签对齐（两 Series 运算时匹配）

print("\n=== 3. Series 不支持多维 values，用 DataFrame ===")
arr_2d = np.array([[1, 2], [3, 4]])
df = pd.DataFrame(arr_2d, columns=["col1", "col2"], index=["row1", "row2"])
print(df)
# DataFrame 每列是 Series，values 一维；行 index + 列 columns 都是 Index