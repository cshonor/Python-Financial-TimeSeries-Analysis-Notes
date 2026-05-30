# 第 4 章核心速查：4.3～4.6（ufunc / 数组编程 / I/O / 线代）

> 所属：[第 4 章](../chapter04_numpy_basics_arrays_vectorization.md) · 整章复习 **一页合并表**  
> 详细笔记：[4.3](./04_03_ufunc.md) · [4.4](./04_04_面向数组编程.md) · [4.5](./04_05_文件_I_O.md) · [4.6](./04_06_线性代数.md)

---

## 4.3 ufunc

| 要点 | 内容 |
|------|------|
| 定义 | **逐元素**向量化 |
| 一元 | `sqrt` `exp` `log` `abs` |
| 二元 | `add` `multiply` `maximum` |
| **`out=`** | 写入已有数组，省内存 |

---

## 4.4 面向数组编程

| 要点 | API |
|------|-----|
| 条件 | `np.where(cond, x, y)` |
| 聚合 | `mean/sum/std` + **`axis=0` 列，`axis=1` 行** |
| 累计 | `cumsum` `cumprod` |
| 布尔 | `(mask).sum()`；`any()` `all()` |
| 排序 | **`arr.sort()` 就地**；**`np.sort` 副本** |
| 集合 | `unique(..., return_counts=True)`；`isin` |

---

## 4.5 文件 I/O

| 格式 | API | 用途 |
|------|-----|------|
| `.npy` | `save` / `load` | 单数组 |
| `.npz` | `savez` / `savez_compressed` | 多数组 |
| 表格 | **`pd.read_csv`** | 实务主力 |

---

## 4.6 线性代数

| 主题 | API | 要点 |
|------|-----|------|
| 元素乘 | **`A * B`** | 逐元素，shape 同 |
| 矩阵乘 | **`A @ B`**、`dot(A,B)` | (m,n)@(n,p) |
| 解方程 | **`linalg.solve(A,b)`** | Ax=b，优于 inv@b |
| 逆 | `linalg.inv(A)` | 满秩方阵 |
| QR | `linalg.qr(A)` | 最小二乘/正交 |
| SVD | `linalg.svd(A)` | PCA/降维/伪逆 |
| 伪逆 | `linalg.pinv(A)` | 奇异/非方阵 |

---

## 联合易错点（4.3～4.6）

| # | 易错 | 正确 |
|---|------|------|
| 1 | `*` 当矩阵乘 | **`@`** 矩阵乘，`*` 逐元素 |
| 2 | `inv(A) @ b` | **`solve(A, b)`** |
| 3 | `axis=0` 当按行 | **axis=0 = 按列** |
| 4 | `arr.sort()` 有返回值 | 返回 **None**，就地改 |
| 5 | npy 存行情表 | **read_csv** |

---

## 量化一条龙

```python
import numpy as np

rets = np.diff(np.log(close))              # 4.3 ufunc
signal = np.where(rets > 0, 1, -1)         # 4.4 where
nav = np.cumprod(1 + rets)                 # 4.4 累计
np.savez_compressed("c.npz", nav=nav)      # 4.5 I/O

# 4.6：组合方差 w @ Sigma @ w；OLS 用 solve(X.T@X, X.T@y) 概念
```

---

[← 返回第 4 章](../chapter04_numpy_basics_arrays_vectorization.md)
