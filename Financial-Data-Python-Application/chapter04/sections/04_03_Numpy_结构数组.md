# 4.3 NumPy 结构数组

> 所属：[第 4 章](../chapter04_numpy_numerical_computation.md) · 《金融数据分析及其 Python 应用》

---

## 核心主旨

揭示如何使用底层 NumPy 搭建类似传统 SQL 数据库条目或 Excel 大宽表的混合结构模型，规避原生单一类型的壁垒。

## 定义及操作

核心突破口在于初始化时深度定制化 `dtype` 参数：

```python
dt = np.dtype([('Name', 'S10'), ('Age', 'i4'), ('Height', 'f4')])
s = np.array([('Alice', 25, 1.68)], dtype=dt)
s['Name']   # 按列名索引
```

## 现状说明

尽管 NumPy 支持此种结构封装，但在现代金融分析场景下，这种结构已被自带复杂索引对齐能力且语法更易学的 **pandas.DataFrame** 体系深度接管，大多退隐至框架底层。

## 【后续拓展补充空间】

- 内存极其受限的边缘计算场景下，为何放弃 Pandas 而使用 NumPy 结构数组

---

[← 返回第 4 章](../chapter04_numpy_numerical_computation.md)
