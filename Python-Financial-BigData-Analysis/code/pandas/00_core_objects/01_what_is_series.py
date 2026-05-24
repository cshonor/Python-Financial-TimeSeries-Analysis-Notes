"""
Pandas 01 - 什么是 Series

Series 是一维的、带标签的数组，由两部分组成：
  - values：实际数据，类型 numpy.ndarray（用于计算）
  - index：索引标签，类型 pandas.Index（非 list，可 .tolist() 转 list）

特点：既像数组（array-like）可向量化运算，又像字典（dict-like）可按标签访问。
"""
import pandas as pd

print("=== 创建 Series ===")
s1 = pd.Series([1, 2, 3, 4, 5])
print("默认索引 0,1,2...:\n", s1)

s2 = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("\n自定义索引:\n", s2)

print("\n=== 获取数值 values ===")
print("s.values:", s2.values)           # [10 20 30]，类型 numpy.ndarray
print("type(s.values):", type(s2.values))
print("s.values.tolist():", s2.values.tolist())  # 转成 Python 列表 [10, 20, 30]
print("s['b'] 或 s.iloc[1]:", s2["b"])  # 单个数值 20
#iloc 是 pandas 中用于基于整数位置（integer location）进行数据选择的属性，
# s.iloc[1] 表示选取 Series 对象 s 中位置索引为 1 的元素（注意：pandas 的整数位置索引从 0 开始）。 

# 注意：values 是属性（无括号）；value_counts() 是方法（有括号）统计出现次数  

print("\n=== values 与 index 的类型 ===")
print("type(s.values):", type(s2.values))   # numpy.ndarray，用于向量化计算
print("type(s.index):", type(s2.index))     # pandas.Index（非 list），支持快速查找、对齐
print("s.index.tolist():", s2.index.tolist())  # 转成 Python 列表 ['a','b','c']

# === Series 速查 ===
# values → numpy.ndarray | index → pandas.Index，两者都可 .tolist() 转 list
# 访问: s[label] s.iloc[i] | 切片 s['a':'c']
