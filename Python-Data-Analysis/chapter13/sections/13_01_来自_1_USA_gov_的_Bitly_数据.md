# 13.1 来自 1.USA.gov 的 Bitly 数据

> 所属：[第 13 章](../chapter13_data_analysis_case_studies.md) · 《利用 Python 进行数据分析》

---

### 13.1 来自 1.USA.gov 的 Bitly 数据

- JSON 按小时日志；嵌套字段（如 `tz` 时区）。
- **13.1.1**：`json` + `Counter` / `defaultdict` 统计 `tz` Top10。
- **13.1.2**：`pd.DataFrame(records)`、`value_counts()`、`fillna`、布尔过滤；`seaborn.barplot`。
- **延伸**：解析 User-Agent → `str.contains` + `groupby` + `unstack` 对比各时区 Windows 占比。

---

[← 返回第 13 章](../chapter13_data_analysis_case_studies.md)
