# 13.2 MovieLens 1M

> 所属：[第 13 章](../chapter13_data_analysis_case_studies.md) · 《利用 Python 进行数据分析》

---

### 13.2 MovieLens 1M

- 三表：`users`、`ratings`、`movies` → **`pd.merge`** 成大表。
- 争议最大电影：`groupby(title).rating.std()` 降序。
- **genres**：`str.split("|")` → **`explode()`** 一行一类，再 `groupby` 统计。

---

[← 返回第 13 章](../chapter13_data_analysis_case_studies.md)
