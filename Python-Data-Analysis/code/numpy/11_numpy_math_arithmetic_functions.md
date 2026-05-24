# NumPy 的数学函数和算术函数

NumPy 提供大量数学与算术函数，对数组逐元素计算，支持 `axis` 指定计算维度。

## 算术函数

| 函数 | 说明 |
|------|------|
| `np.add(a, b)` | 加法 |
| `np.subtract(a, b)` | 减法 |
| `np.multiply(a, b)` | 逐元素乘法 |
| `np.divide(a, b)` | 除法 |
| `np.floor_divide(a, b)` | 整除 |
| `np.power(a, b)` | 幂运算 |
| `np.mod(a, b)` | 取余 |
| `np.negative(a)` | 取负 |
| `np.reciprocal(a)` | 倒数 |

## 数学函数

### 三角函数

| 函数 | 说明 |
|------|------|
| `np.sin(x)`, `np.cos(x)`, `np.tan(x)` | 正弦、余弦、正切 |
| `np.arcsin(x)`, `np.arccos(x)`, `np.arctan(x)` | 反三角函数 |
| `np.deg2rad(x)`, `np.rad2deg(x)` | 角度与弧度转换 |

### 指数与对数

| 函数 | 说明 |
|------|------|
| `np.exp(x)` | e^x |
| `np.exp2(x)` | 2^x |
| `np.log(x)` | ln(x) |
| `np.log2(x)` | log₂(x) |
| `np.log10(x)` | lg(x) |

### 舍入与符号

| 函数 | 说明 |
|------|------|
| `np.ceil(x)` | 向上取整 |
| `np.floor(x)` | 向下取整 |
| `np.trunc(x)` | 截断小数 |
| `np.round(x, decimals)` | 四舍五入 |
| `np.sign(x)` | 符号（-1/0/1） |
| `np.abs(x)` | 绝对值 |

### 其他

| 函数 | 说明 |
|------|------|
| `np.sqrt(x)` | 平方根 |
| `np.square(x)` | 平方 |
| `np.clip(x, min, max)` | 限制在 [min, max] 区间 |

## 示例

```python
import numpy as np

x = np.array([0, np.pi/2, np.pi])
print(np.sin(x))     # [0. 1. 0.]

arr = np.array([1, 4, 9, 16])
print(np.sqrt(arr))  # [1. 2. 3. 4.]

a = np.array([1.2, 2.7, -1.5])
print(np.floor(a))   # [ 1.  2. -2.]
print(np.round(a))   # [ 1.  3. -2.]
print(np.clip(a, 0, 2))  # [1.2 2.  0.]
```

## 要点

- 多为逐元素计算，形状相同或满足广播规则
- 支持 `axis` 的可在指定维度上运算
- 运算符 `+ - * / **` 与对应函数等价
