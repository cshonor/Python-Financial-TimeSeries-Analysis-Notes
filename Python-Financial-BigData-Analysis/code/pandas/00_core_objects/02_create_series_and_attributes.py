"""
Pandas 02.1 - 创建 Series 与 Series 属性

1.2.1 构造 Series：
  - From ndarray：引用对象
  - From List：副本对象
  - From dict：键→index，值→values
  - From scalar：必须指定 index，标量重复匹配每个 index

1.2.2 Series 属性：name / shape / size / index / values
"""
import pandas as pd
import numpy as np

print("=== 1.2.1 构造 Series ===")
arr = np.array([1, 2, 3])
s1 = pd.Series(arr)           # From ndarray（引用）
s2 = pd.Series([1, 2, 3])     # From List（副本）
s3 = pd.Series({"a": 10, "b": 20, "c": 30})  # From dict
s4 = pd.Series(99, index=["x", "y", "z"])
#这段代码的作用是：创建一个 pandas 的 Series 对象 s4，其中所有元素的值都是 99，并且自定义了索引标签为 ["x", "y", "z"]。
# From scalar，必须指定 index
print("From ndarray:", s1.values)   # [1 2 3]
print("From dict:\n", s3)           # a 10, b 20, c 30
print("From scalar:\n", s4)         # x 99, y 99, z 99

print("\n=== 1.2.2 Series 属性 ===")
s = pd.Series([10, 20, 30], index=["a", "b", "c"], name="my_series")
print("name:", s.name)     # my_series
print("shape:", s.shape)   # (3,)
print("size:", s.size)     # 3
print("index:", s.index)   # Index(['a','b','c'], dtype='object')
print("values:", s.values) # [10 20 30]
