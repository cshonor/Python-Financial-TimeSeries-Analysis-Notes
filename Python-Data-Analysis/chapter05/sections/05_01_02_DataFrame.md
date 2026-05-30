# 5.1.2 DataFrame

> 所属：[第 5 章](../chapter05_pandas_introduction.md) · 《利用 Python 进行数据分析》

---

#### 5.1.2 DataFrame

- 二维表：行索引 + 列索引；列可异构 dtype；可视为 **共享行索引的 Series 字典**。
- 常用 `pd.DataFrame(dict_of_lists)`；`columns` 指定列顺序；`head()` / `tail()`。
- **取列常为视图**：`df["col"]` 修改会影响原表；需隔离用 `.copy()`。

---

[← 返回第 5 章](../chapter05_pandas_introduction.md)
