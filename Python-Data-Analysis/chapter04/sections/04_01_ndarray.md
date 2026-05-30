# 4.1 ndarray

> 所属：[第 4 章](../chapter04_numpy_basics_arrays_vectorization.md) · 《利用 Python 进行数据分析》

---

### 4.1 ndarray

- **创建**：`np.array`；`zeros` / `ones` / `empty` / `arange` 等按形状创建。
- **4.1.2 dtype**：`astype` **总是新数组**；整型截断小数等。
- **4.1.3 运算**：同形状 **元素级** 算术；与标量运算；不同形状见 **广播**（附录 A 深入）。
- **4.1.4 切片**：高维 `arr[i, j]`、`arr[:2, 1:]`；**切片是视图**，改切片会改原数组。
- **4.1.5 布尔索引**：`arr[mask]`；`&` `|` 组合条件；**结果是副本**。
- **4.1.6 花式索引**：整数数组选行/元素；**复制到新数组**。
- **4.1.7 转置**：`.T` / `transpose` / `swapaxes`；多为 **视图**。

---

[← 返回第 4 章](../chapter04_numpy_basics_arrays_vectorization.md)
