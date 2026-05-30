# 第 4 章 NumPy 基础：数组和向量化计算

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 4 章。  
> NumPy 提供 **`ndarray`** 与 **向量化** 运算，是 pandas、statsmodels 等库的底层数据容器与算力基础。数据存放在 **连续内存块**，由 C 实现的核心算法避免 Python 逐元素循环开销。

**前置章节**：[第 2 章](../chapter02/chapter02_python_syntax_ipython_jupyter.md)（引用语义）→ [第 3 章](../chapter03/chapter03_data_structures_functions_files.md)（列表/切片直觉）。

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
| 4.1 创建 / dtype | [`./code/numpy/01_create_ndarray.py`](./code/numpy/01_create_ndarray.py)、[`02_numpy_data_types.py`](./code/numpy/02_numpy_data_types.py) |
| 4.1.4～4.1.6 索引 | [`03_ndarray_indexing_slicing.py`](./code/numpy/03_ndarray_indexing_slicing.py)、[`18_numpy_mask_boolean_index.py`](./code/numpy/18_numpy_mask_boolean_index.py) |
| 4.1.3 / 广播 | [`05_ndarray_basic_operations.md`](./code/numpy/05_ndarray_basic_operations.md)、[`08_broadcasting_mechanism.md`](./code/numpy/08_broadcasting_mechanism.md) |
| 4.2 随机 | [`14_numpy_routines.py`](./code/numpy/14_numpy_routines.py)、[`17_numpy_random_module.py`](./code/numpy/17_numpy_random_module.py) |
| 4.3 ufunc / where | [`11_numpy_math_arithmetic_functions.md`](./code/numpy/11_numpy_math_arithmetic_functions.md) |
| 4.4 聚合 / 排序 | [`09_ndarray_aggregation_functions.md`](./code/numpy/09_ndarray_aggregation_functions.md)、[`10_numpy_search_sort.md`](./code/numpy/10_numpy_search_sort.md) |
| 4.5 I/O | [`04.ndarray读写.py`](./code/numpy/04.ndarray读写.py) |
| 4.6 线代 | [`19_numpy_matrix_linear_algebra.md`](./code/numpy/19_numpy_matrix_linear_algebra.md) |
| 避坑 | [`20_numpy_performance_tips.md`](./code/numpy/20_numpy_performance_tips.md) |

本章 **综合演示脚本**：[`./code/chapter04_numpy_basics_demo.py`](./code/chapter04_numpy_basics_demo.py)

---

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [04_01_ndarray](./sections/04_01_ndarray.md) | ndarray（4.1.1～4.1.7 + 视图/副本速查） |
| [04_02_伪随机数](./sections/04_02_伪随机数.md) | 伪随机数（**default_rng** + 新旧 API 对照） |
| [04_03_ufunc](./sections/04_03_ufunc.md) | ufunc（一元/二元 + **`out=`**） |
| [04_04_面向数组编程](./sections/04_04_面向数组编程.md) | 面向数组编程（4.4.1～4.4.5 + 易错点速查） |
| [04_05_文件_I_O](./sections/04_05_文件_I_O.md) | 文件 I/O（**npy/npz** + vs read_csv） |
| [**4.3～4.6 合并速查**](./sections/chapter04_核心速查_4_3_4_6.md) | ufunc / 4.4 / I/O / 线代 整章复习 |
| [04_06_线性代数](./sections/04_06_线性代数.md) | 线性代数（**`*` vs `@`** + linalg 速查） |
| [04_07_随机漫步](./sections/04_07_随机漫步.md) | 随机漫步 |
| [04_08_总结](./sections/04_08_总结.md) | 总结 |

## 二、关键语法速查表

| 主题 | API |
|------|-----|
| 创建 | `np.array`, `np.zeros`, `np.arange` |
| ufunc | `np.sqrt`, `np.exp`, `np.add`, `ufunc(..., out=buf)` |
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

见 [`./code/chapter04_numpy_basics_demo.py`](./code/chapter04_numpy_basics_demo.py)

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

已整理：[04_01_ndarray](./sections/04_01_ndarray.md)（4.1.1～4.1.7 完整笔记 + **视图 vs 副本速查**）

### 4.2 伪随机数

已整理：[04_02_伪随机数](./sections/04_02_伪随机数.md)（新旧 API 对照 + 常用分布速查）

### 4.4 面向数组编程

已整理：[04_04_面向数组编程](./sections/04_04_面向数组编程.md)（where / axis / 布尔 / sort / unique 速查）

### 4.5 文件 I/O

已整理：[04_05_文件_I_O](./sections/04_05_文件_I_O.md)（save/load/savez 速查 + NumPy vs pandas）

### 4.3 ufunc

已整理：[04_03_ufunc](./sections/04_03_ufunc.md)（一元/二元 + **`out=`**）；**4.3～4.6 合并速查** → [chapter04_核心速查_4_3_4_6.md](./sections/chapter04_核心速查_4_3_4_6.md)

### 4.6 线性代数

已整理：[04_06_线性代数](./sections/04_06_线性代数.md)（`*` vs `@`、solve/qr/svd）

### 4.7～4.8

（留白）
