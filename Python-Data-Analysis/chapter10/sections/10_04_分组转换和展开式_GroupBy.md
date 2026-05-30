# 10.4 分组转换和展开式 GroupBy

> 所属：[第 10 章](../chapter10_data_aggregation_groupby.md) · 《利用 Python 进行数据分析》

---

### 10.4 分组转换和展开式 GroupBy

- **`transform`**：输出须能广播到组形状或与组同形；不能改输入。
- 内置 `'mean'`, `'sum'` 等走**高速路径**；组间算术如 `(x - x.groupby().transform('mean'))` 即截面去均值/标准化。

---

[← 返回第 10 章](../chapter10_data_aggregation_groupby.md)
