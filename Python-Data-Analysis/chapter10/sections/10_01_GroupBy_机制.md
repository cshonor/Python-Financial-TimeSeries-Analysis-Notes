# 10.1 GroupBy 机制

> 所属：[第 10 章](../chapter10_data_aggregation_groupby.md) · 《利用 Python 进行数据分析》

---

### 10.1 GroupBy 机制

- **拆分-应用-联合**：按键拆组 → 对每组应用函数 → 合并结果。
- **分组键**：等长列表/数组、列名、dict/Series 映射、轴上的函数、`level=`（MultiIndex）。
- **`GroupBy` 是延迟对象**：调用 `mean()`、`size()`、`count()` 等才真正计算；默认跳过 NA（`dropna=False` 可改）。

---

[← 返回第 10 章](../chapter10_data_aggregation_groupby.md)
