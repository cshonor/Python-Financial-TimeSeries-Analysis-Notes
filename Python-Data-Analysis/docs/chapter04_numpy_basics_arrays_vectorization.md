# 第 4 章 NumPy 基础：数组和向量化计算

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 4 章。  
> NumPy 提供 **`ndarray`** 与 **向量化** 运算，是 pandas、statsmodels 等库的底层数据容器与算力基础。数据存放在 **连续内存块**，由 C 实现的核心算法避免 Python 逐元素循环开销。

**前置章节**：[第 2 章](./chapter02_python_syntax_ipython_jupyter.md)（引用语义）→ [第 3 章](./chapter03_data_structures_functions_files.md)（列表/切片直觉）。

---

## 章节总览

**小节统计**：8 个一级小节 + 约 11 个二级/子模块，共 **19 个小节**。

| 一级 | 二级 / 子模块 |
|------|----------------|
| 4.1 ndarray | 4.1.1 创建；4.1.2 dtype；4.1.3 运算；4.1.4 索引切片；4.1.5 布尔索引；4.1.6 花式索引；4.1.7 转置 |
| 4.2 伪随机数 | — |
| 4.3 通用函数 ufunc | — |
| 4.4 面向数组编程 | 4.4.1～4.4.5 |
| 4.5 数组文件 I/O | — |
| 4.6 线性代数 | — |
| 4.7 随机漫步示例 | — |
| 4.8 总结 | — |

**本仓库专题脚本对照**（建议边读边跑）：

| 原书小节 | 仓库路径 |
|----------|----------|
| 4.1 创建 / dtype | [`../code/numpy/01_create_ndarray.py`](../code/numpy/01_create_ndarray.py)、[`02_numpy_data_types.py`](../code/numpy/02_numpy_data_types.py) |
| 4.1.4～4.1.6 索引 | [`03_ndarray_indexing_slicing.py`](../code/numpy/03_ndarray_indexing_slicing.py)、[`18_numpy_mask_boolean_index.py`](../code/numpy/18_numpy_mask_boolean_index.py) |
| 4.1.3 / 广播 | [`05_ndarray_basic_operations.md`](../code/numpy/05_ndarray_basic_operations.md)、[`08_broadcasting_mechanism.md`](../code/numpy/08_broadcasting_mechanism.md) |
| 4.2 随机 | [`14_numpy_routines.py`](../code/numpy/14_numpy_routines.py)、[`17_numpy_random_module.py`](../code/numpy/17_numpy_random_module.py) |
| 4.3 ufunc / where | [`11_numpy_math_arithmetic_functions.md`](../code/numpy/11_numpy_math_arithmetic_functions.md) |
| 4.4 聚合 / 排序 | [`09_ndarray_aggregation_functions.md`](../code/numpy/09_ndarray_aggregation_functions.md)、[`10_numpy_search_sort.md`](../code/numpy/10_numpy_search_sort.md) |
| 4.5 I/O | [`04.ndarray读写.py`](../code/numpy/04.ndarray读写.py) |
| 4.6 线代 | [`19_numpy_matrix_linear_algebra.md`](../code/numpy/19_numpy_matrix_linear_algebra.md) |
| 避坑 | [`20_numpy_performance_tips.md`](../code/numpy/20_numpy_performance_tips.md) |

本章 **综合演示脚本**：[`../code/chapter04_numpy_basics_demo.py`](../code/chapter04_numpy_basics_demo.py)

---

## 一、书本原文核心知识点提炼

### 4.1 ndarray

- **创建**：`np.array`；`zeros` / `ones` / `empty` / `arange` 等按形状创建。
- **4.1.2 dtype**：`astype` **总是新数组**；整型截断小数等。
- **4.1.3 运算**：同形状 **元素级** 算术；与标量运算；不同形状见 **广播**（附录 A 深入）。
- **4.1.4 切片**：高维 `arr[i, j]`、`arr[:2, 1:]`；**切片是视图**，改切片会改原数组。
- **4.1.5 布尔索引**：`arr[mask]`；`&` `|` 组合条件；**结果是副本**。
- **4.1.6 花式索引**：整数数组选行/元素；**复制到新数组**。
- **4.1.7 转置**：`.T` / `transpose` / `swapaxes`；多为 **视图**。

### 4.2 伪随机数

- `np.random` / 推荐 **`np.random.default_rng(seed)`** 隔离生成器。
- 批量生成比 `random` 模块快得多；可复现。

### 4.3 ufunc

- 一元：`sqrt`、`exp`、`log`、`abs`…
- 二元：`add`、`maximum`…
- 可选 **`out=`** 写入已有数组，省内存。

### 4.4 面向数组编程

- **4.4.1** `np.where(cond, x, y)` 向量化三元逻辑。
- **4.4.2** `mean/sum/std` + **`axis`**；`cumsum` / `cumprod` 累计。
- **4.4.3** 布尔数组：`sum` 计 True 个数；`any` / `all`。
- **4.4.4** `arr.sort()` 就地；`np.sort(arr)` 返回副本。
- **4.4.5** `unique`、`in1d`、集合运算等。

### 4.5 文件 I/O

- `np.save` / `np.load` / `np.savez`；实务中大量用 `pd.read_csv`。

### 4.6 线性代数

- **`*`** 元素乘；**`@` / `dot`** 矩阵乘。
- `np.linalg`：`inv`、`qr`、`svd`、`solve` 等。

### 4.7 随机漫步

- 向量化：`integers` → `where` 映射步长 → **`cumsum`**；`argmax` 找首次触界。

### 4.8 总结

- 第 5 章起以 pandas 为主，但底层仍是 ndarray 逻辑；广播详见附录 A。

---

## 二、关键语法速查表

| 主题 | API |
|------|-----|
| 创建 | `np.array`, `np.zeros`, `np.arange` |
| 类型 | `arr.dtype`, `arr.astype(np.float64)` |
| 视图 vs 副本 | 切片→视图；布尔/花式→副本 |
| 条件 | `np.where`, `(a > 0) & (b < 1)` |
| 轴聚合 | `arr.mean(axis=0)`, `arr.sum(axis=1)` |
| 累计 | `np.cumsum`, `np.cumprod` |
| 矩阵乘 | `A @ B`, `np.dot(A, B)` |
| 随机 | `rng = np.random.default_rng(0)` |
| 存盘 | `np.save`, `np.load` |

---

## 三、通用基础示例

见 [`../code/chapter04_numpy_basics_demo.py`](../code/chapter04_numpy_basics_demo.py)

---

## 四、【量化专属改造】金融实战衔接

1. **收益序列**：`close` 转 `ndarray` 后 `np.diff(close)/close[:-1]`，再交给 pandas 加索引。
2. **信号向量化**：`np.where(ma_short > ma_long, 1, 0)` 生成持仓数组；注意与 **shift** 的配合在 pandas 章完成。
3. **截面统计**：因子矩阵 `(n_stock,)` 上 `mean/std`；多股票可用二维数组 + `axis=0`。
4. **视图陷阱**：对 `arr_slice` 原地赋值会改共享内存；回测中间结果需要隔离时用 **`.copy()`**。
5. **随机模拟**：`default_rng` 生成路径 → `cumsum` 得价格/净值曲线（见 4.7 随机漫步）。
6. **不要重复造轮子**：大规模清洗优先 pandas；NumPy 负责「单数组上的快算」与理解 `values` 底层。

---

## 五、与 statsmodels 建模的衔接要点

- OLS 的 `y`、`X` 常来自 `df.values` 或 `df[["x1","x2"]].to_numpy()`；理解 **dtype=float64** 与 **缺失值必须先处理**（NaN 进回归会坏）。
- `np.linalg` / `@` 与 statsmodels 内部矩阵运算一致；`solve` 思想对应正规方程（概念层）。
- 累计收益 `np.cumprod(1 + rets)` 与策略净值曲线是时序回归、残差分析的前置图形。

---

## 本章自检清单

- [ ] 能解释切片视图 vs 布尔索引副本  
- [ ] 会用 `axis` 做按行/列聚合  
- [ ] 会用 `np.where` 代替 Python 循环条件赋值  
- [ ] 会用 `default_rng` 固定种子  
- [ ] 区分 `*` 与 `@`  
- [ ] 能口述随机漫步的向量化三步（步长 → cumsum）  

---

## 后续扩展留白

### 4.1 ndarray

（留白）

### 4.2～4.7

（留白）
