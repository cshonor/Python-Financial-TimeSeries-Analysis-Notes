# ndarray 的基本运算

NumPy 的 ndarray 支持逐元素运算，无需循环，效率高。

## 一、算术运算

| 运算符 | 函数 | 说明 |
|--------|------|------|
| `+` | `np.add` | 加法 |
| `-` | `np.subtract` | 减法 |
| `*` | `np.multiply` | 逐元素乘法 |
| `/` | `np.divide` | 除法 |
| `**` | `np.power` | 幂运算 |
| `//` | `np.floor_divide` | 整除 |
| `%` | `np.mod` | 取余 |

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a - b)   # [-3 -3 -3]
print(a * b)   # [ 4 10 18]  逐元素乘，非矩阵乘
print(a / b)   # [0.25 0.4  0.5]
print(a ** 2)  # [1 4 9]
```

## 二、比较运算

| 运算符 | 说明 |
|--------|------|
| `==` | 等于 |
| `!=` | 不等于 |
| `>`, `>=`, `<`, `<=` | 大小比较 |

```python
a = np.array([1, 2, 3, 4, 5])
print(a > 3)    # [False False False  True  True]
print(a == 2)   # [False  True False False False]
```

## 三、矩阵乘法

- `*`：逐元素乘法
- `@` 或 `np.dot()`：矩阵乘法

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a * b)      # 逐元素乘
print(a @ b)      # 矩阵乘
print(np.dot(a, b))  # 同上
```

## 四、标量与数组运算（广播）

标量会与数组每个元素运算：

```python
arr = np.array([1, 2, 3])
print(arr + 10)   # [11 12 13]
print(arr * 2)    # [2 4 6]
```

## 五、聚合函数（简要）

| 函数 | 说明 |
|------|------|
| `np.sum(arr)` | 求和 |
| `np.mean(arr)` | 均值 |
| `np.max(arr)` | 最大值 |
| `np.min(arr)` | 最小值 |
| `np.std(arr)` | 标准差 |
| `axis` 参数 | 沿指定轴计算，如 `axis=0` 按列、`axis=1` 按行 |

## 要点

- 算术、比较运算均为**逐元素**，要求形状相同或满足广播规则
- 矩阵乘法用 `@` 或 `np.dot`，注意维度匹配
- 支持 `axis` 的聚合函数可在指定维度上汇总
