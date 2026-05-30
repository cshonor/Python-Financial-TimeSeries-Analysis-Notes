# 8.2.1 数据库风格的 DataFrame 连接

> 所属：[第 8 章](../chapter08_data_wrangling_join_reshape.md) · 《利用 Python 进行数据分析》

---

#### 8.2.1 数据库风格的 DataFrame 连接

- **`pd.merge(left, right, on=..., how=...)`**
- 未指定键时默认用**两表同名列**；推荐显式 `on`；列名不同用 `left_on` / `right_on`。
- **`how`**：`inner`（默认，交集）、`outer`（并集+NA）、`left` / `right`。
- 多对多键 → 笛卡儿积行数膨胀；重名列用 **`suffixes=("_x","_y")`**。

---

[← 返回第 8 章](../chapter08_data_wrangling_join_reshape.md)
