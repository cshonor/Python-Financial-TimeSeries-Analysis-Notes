# ndarray 的聚合函数

聚合函数对数组进行统计汇总，返回标量或沿指定轴的结果。支持 `axis` 参数控制沿哪个维度计算。

## 常用聚合函数

| 函数 | 说明 | 示例 |
|------|------|------|
| `np.sum(arr, axis=None)` | 求和 | `arr.sum()` |
| `np.mean(arr, axis=None)` | 均值 | `arr.mean()` |
| `np.max(arr, axis=None)` | 最大值 | `arr.max()` |
| `np.min(arr, axis=None)` | 最小值 | `arr.min()` |
| `np.std(arr, axis=None)` | 标准差 | `arr.std()` |
| `np.var(arr, axis=None)` | 方差 | `arr.var()` |
| `np.argmax(arr, axis=None)` | 最大值的索引 | `arr.argmax()` |
| `np.argmin(arr, axis=None)` | 最小值的索引 | `arr.argmin()` |
| `np.prod(arr, axis=None)` | 连乘 | `arr.prod()` |

## axis 参数

- `axis=None`（默认）：对整个数组计算，返回标量
- `axis=0`：沿行方向（按列），每列一个结果
- `axis=1`：沿列方向（按行），每行一个结果

```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(np.sum(arr))       # 45，全数组求和
print(np.sum(arr, axis=0))   # [12 15 18]，每列求和
print(np.sum(arr, axis=1))   # [ 6 15 24]，每行求和

print(np.mean(arr, axis=0))  # [4. 5. 6.]
print(np.max(arr, axis=1))   # [3 6 9]
```

## 累积类函数

| 函数 | 说明 |
|------|------|
| `np.cumsum(arr, axis=None)` | 累加和 |
| `np.cumprod(arr, axis=None)` | 累乘 |

```python
arr = np.array([1, 2, 3, 4, 5])
print(np.cumsum(arr))   # [ 1  3  6 10 15]
print(np.cumprod(arr))  # [  1   2   6  24 120]
```

## 布尔聚合

| 函数 | 说明 |
|------|------|
| `np.all(arr)` | 是否全为 True |
| `np.any(arr)` | 是否存在 True |

```python
arr = np.array([True, True, False])
print(np.all(arr))   # False
print(np.any(arr))   # True
```

## 要点

- 不指定 `axis` 时对整数组计算，返回标量
- `axis=0` 沿行（纵向），结果维度减少一行；`axis=1` 沿列（横向）
- 可用 `arr.sum()` 等价于 `np.sum(arr)`
