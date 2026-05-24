"""
Pandas 03 - DataFrame

DataFrame 是二维表格，可理解为多个 Series 按列排列。
- 行索引 index，列索引 columns（都是 pandas.Index）
- 每列是一个 Series
"""
import pandas as pd
import numpy as np

print("=== 创建 DataFrame ===")
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})
print(df)

print("\n=== 属性 ===")
print("df.columns:", df.columns)
print("df.index:", df.index)
print("df.shape:", df.shape)
print("df['A'] 单列是 Series:\n", df["A"])

print("\n=== 访问 ===")
print("df.loc[0] 按行标签:", df.loc[0])
print("df.iloc[0, 1] 按位置:", df.iloc[0, 1])
