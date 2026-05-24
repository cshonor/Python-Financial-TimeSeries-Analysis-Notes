# ndarray 的拆分

ndarray 拆分是级联的逆操作，将单个数组沿指定轴分割成多个子数组。

## 常用函数

| 函数 | 说明 | 等价于 |
|------|------|--------|
| `np.split(arr, indices, axis=0)` | 沿轴等分或按索引切分 | — |
| `np.array_split(arr, n, axis=0)` | 分成 n 份（可不等分） | — |
| `np.vsplit(arr, indices)` | 垂直拆分（按行） | `np.split(..., axis=0)` |
| `np.hsplit(arr, indices)` | 水平拆分（按列） | `np.split(..., axis=1)` |

## np.split

```python
import numpy as np

arr = np.arange(12).reshape(3, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# 按索引切分：在第 1、2 行之间切
parts = np.split(arr, [1, 2], axis=0)  # 分成 3 份
# parts[0]: [[0 1 2 3]]
# parts[1]: [[4 5 6 7]]
# parts[2]: [[8 9 10 11]]

# 按列切分
cols = np.split(arr, 2, axis=1)  # 均分 2 份
# cols[0]: 前 2 列, cols[1]: 后 2 列
```

## np.array_split（可不等分）

```python
# 将 7 个元素分成 3 份，最后一份元素少
arr1d = np.array([1, 2, 3, 4, 5, 6, 7])
parts = np.array_split(arr1d, 3)
# [array([1, 2, 3]), array([4, 5]), array([6, 7])]
```

## np.vsplit / np.hsplit

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 按行拆成 3 份
v = np.vsplit(arr, 3)  # 每行一份

# 按列拆成 3 份
h = np.hsplit(arr, 3)  # 每列一份
```

## 要点

- **split**：`indices` 为整数时均分；为列表时表示切分点位置
- **array_split**：无法均分时，前面的子数组会多分一些元素
- **vsplit**：沿行切分，相当于 `axis=0`
- **hsplit**：沿列切分，相当于 `axis=1`
