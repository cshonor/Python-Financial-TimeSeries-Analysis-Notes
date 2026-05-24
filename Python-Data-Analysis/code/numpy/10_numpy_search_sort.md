# NumPy 查找与排序

## 一、查找

### 条件查找

| 函数 | 说明 |
|------|------|
| `np.where(condition)` | 返回满足条件的索引 |
| `np.where(cond, x, y)` | 满足 cond 取 x，否则取 y（三元运算） |

```python
import numpy as np

arr = np.array([1, 3, 5, 7, 9])
idx = np.where(arr > 5)      # (array([3, 4]),)
res = np.where(arr > 5, 1, 0)  # [0 0 0 1 1]
```

### 最值索引

| 函数 | 说明 |
|------|------|
| `np.argmax(arr)` | 最大值索引 |
| `np.argmin(arr)` | 最小值索引 |
| `np.argmax(arr, axis=1)` | 沿指定轴的最大值索引 |

### 搜索插入位置

| 函数 | 说明 |
|------|------|
| `np.searchsorted(a, v)` | 在有序数组 a 中查找 v 的插入位置，保持有序 |

```python
a = np.array([1, 3, 5, 7])
np.searchsorted(a, 4)   # 2（插入到索引 2）
np.searchsorted(a, [2, 6])  # [1 3]
```

### 非零元素

| 函数 | 说明 |
|------|------|
| `np.nonzero(arr)` | 返回非零元素的索引（多维时返回各轴索引元组） |

```python
arr = np.array([0, 1, 0, 2, 0])
np.nonzero(arr)  # (array([1, 3]),)
```

### 唯一值与计数

| 函数 | 说明 |
|------|------|
| `np.unique(arr)` | 去重并排序 |
| `np.unique(arr, return_counts=True)` | 同时返回各值出现次数 |

```python
arr = np.array([1, 2, 2, 3, 1, 3])
np.unique(arr)  # [1 2 3]
vals, cnt = np.unique(arr, return_counts=True)
```

## 二、排序

### 排序函数

| 函数 | 说明 |
|------|------|
| `np.sort(arr)` | 返回排序后的新数组，不修改原数组 |
| `arr.sort()` | 原地排序，修改原数组 |
| `np.argsort(arr)` | 返回排序后的索引 |

```python
arr = np.array([3, 1, 4, 1, 5])
np.sort(arr)      # [1 1 3 4 5]
np.argsort(arr)   # [1 3 0 2 4]
```

### 指定轴排序

```python
arr = np.array([[3, 1, 4], [1, 5, 2]])
np.sort(arr, axis=0)   # 按列排序
np.sort(arr, axis=1)   # 按行排序
```

### 降序

```python
np.sort(arr)[::-1]           # 一维降序
-np.sort(-arr)               # 或
np.sort(arr, order=...)      # 结构化数组可按字段排序
```

### 部分排序

| 函数 | 说明 |
|------|------|
| `np.partition(arr, k)` | 使第 k 小的元素在正确位置，左侧更小、右侧更大 |
| `np.argpartition(arr, k)` | 返回 partition 的索引 |

## 要点

- `where` 可用于条件索引或三元选择
- `argmax`/`argmin` 返回索引，`searchsorted` 要求数组有序
- `np.sort` 不改变原数组，`arr.sort()` 原地排序
- `argsort` 用于按某列/行对数据重排
