# ndarray 的 append 和 insert

用于在数组中追加或插入元素。注意：NumPy 的 `append`/`insert` 会**返回新数组**，不修改原数组。

## np.append

```python
import numpy as np

arr = np.array([1, 2, 3])

# 末尾追加元素
res = np.append(arr, 4)           # [1 2 3 4]
res = np.append(arr, [4, 5])      # [1 2 3 4 5]

# 二维数组：不指定 axis 会先扁平化再拼接
a = np.array([[1, 2], [3, 4]])
np.append(a, [[5, 6]], axis=0)    # 按行追加
np.append(a, [[7], [8]], axis=1)  # 按列追加
```

| 参数 | 说明 |
|------|------|
| `arr` | 原数组 |
| `values` | 要追加的值（标量或数组） |
| `axis` | 可选，沿哪一轴追加；不指定则先展平为一维 |

## np.insert

```python
arr = np.array([1, 2, 3, 4, 5])

# 在索引 2 处插入 99
np.insert(arr, 2, 99)             # [ 1  2 99  3  4  5]

# 在多个位置插入同一值
np.insert(arr, [1, 3], 0)         # [1 0 2 3 0 4 5]

# 插入多个值
np.insert(arr, 2, [10, 20])       # [ 1  2 10 20  3  4  5]

# 二维：指定 axis
a = np.array([[1, 2], [3, 4]])
np.insert(a, 1, [0, 0], axis=0)   # 在第 1 行插入
np.insert(a, 1, 0, axis=1)        # 在第 1 列插入 0
```

| 参数 | 说明 |
|------|------|
| `arr` | 原数组 |
| `obj` | 插入位置（索引或索引列表） |
| `values` | 要插入的值 |
| `axis` | 可选，沿哪一轴插入 |

## 要点

- `append` / `insert` 均返回**新数组**，不修改原数组
- 频繁追加时效率较低，建议先用列表收集再一次性 `np.array()`
- 二维以上需显式指定 `axis`，否则会先展平
