# 第 4 章 用 NumPy 进行数值计算

> 对应教材：《Python金融大数据分析（第2版）》· 第2部分 掌握基础知识  
> **前置**：[第 3 章](../chapter03/chapter03_data_types_and_structures.md) → 本章 → [第 5 章](../chapter05/chapter05_pandas_data_analysis.md)  
> NumPy 的 **`ndarray`** 与 **向量化** 运算是金融量化与大数据分析的计算底座；本章从 Python 原生列表的局限出发，逐步建立 ndarray 与广播机制的系统直觉。

**并行参考**（Wes McKinney 体系更系统的 ndarray 专题）：[`../../Python-Data-Analysis/chapter04/`](../../Python-Data-Analysis/chapter04/chapter04_numpy_basics_arrays_vectorization.md)

---

## 章节总览

| 一级 | 二级 / 子模块 |
|------|----------------|
| 4.1 数据数组 | 4.1.1 用 Python 列表形成数组；4.1.2 Python `array` 类 |
| 4.2 常规 NumPy 数组 | 4.2.1 基础知识；4.2.2 多维数组；4.2.3 元信息；4.2.4 改变组成与大小；4.2.5 布尔数组；4.2.6 速度对比 |
| 4.3 NumPy 结构数组 | — |
| 4.4 代码向量化 | 4.4.1 基本向量化；4.4.2 内存布局 |
| 4.5 结语 | — |
| 4.6 延伸阅读 | — |

**本章演示脚本**：[`./code/chapter04_numpy_demo.py`](./code/chapter04_numpy_demo.py)

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [04_01_数据数组](./sections/04_01_数据数组.md) | 从 list 到 ndarray 的演进 |
| [04_01_01_用_Python_列表形成数组](./sections/04_01_01_用_Python_列表形成数组.md) | 嵌套列表与引用陷阱 |
| [04_01_02_Python_array_类](./sections/04_01_02_Python_array_类.md) | 内置 `array` 模块 |
| [04_02_01_基础知识](./sections/04_02_01_基础知识.md) | ndarray 创建与 ufunc |
| [04_02_02_多维数组](./sections/04_02_02_多维数组.md) | 初始化捷径与 axis |
| [04_02_03_元信息](./sections/04_02_03_元信息.md) | shape / dtype 等属性 |
| [04_02_04_改变组成与大小](./sections/04_02_04_改变组成与大小.md) | reshape / stack / flatten |
| [04_02_05_布尔数组](./sections/04_02_05_布尔数组.md) | 布尔遮罩与 `np.where` |
| [04_02_06_速度对比](./sections/04_02_06_速度对比.md) | 纯 Python vs NumPy 性能 |
| [04_03_Numpy_结构数组](./sections/04_03_Numpy_结构数组.md) | 结构化 dtype |
| [04_04_01_基本向量化](./sections/04_04_01_基本向量化.md) | 广播机制 |
| [04_04_02_内存布局](./sections/04_04_02_内存布局.md) | C / Fortran 连续 |
| [04_05_结语](./sections/04_05_结语.md) | 本章总结 |

---

## 关键语法速查

| 主题 | API |
|------|-----|
| 创建 | `np.array`, `np.arange`, `np.zeros`, `np.ones`, `np.eye`, `np.linspace` |
| 元信息 | `ndim`, `shape`, `size`, `itemsize`, `dtype` |
| 变形 | `reshape`, `resize`, `hstack`, `vstack`, `ravel`, `flatten` |
| 条件 | `arr > 8`, `np.where(cond, x, y)` |
| 轴聚合 | `arr.sum(axis=0)`, `arr.sum(axis=1)` |
| 统计 | `sum`, `std`, `cumsum` |
| 结构数组 | `np.dtype([('Name', 'S10'), ('Age', 'i4')])` |

---

[← 返回本册目录](../README.md)
