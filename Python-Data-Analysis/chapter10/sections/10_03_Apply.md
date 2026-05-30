# 10.3 Apply

> 所属：[第 10 章](../chapter10_data_aggregation_groupby.md) · 《利用 Python 进行数据分析》

---

### 10.3 Apply

- **`apply(func)`**：最通用；各组独立调用 `func`，再 `concat` 拼接。
- 函数须返回 pandas 对象或标量；额外参数写在 `apply` 后：`apply(f, arg1=v)`。
- `groupby().describe()` 本质是 apply 快捷方式。

---

[← 返回第 10 章](../chapter10_data_aggregation_groupby.md)
