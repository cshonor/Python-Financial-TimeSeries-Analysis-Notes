# 第 10 章 数据聚合与分组操作

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 10 章。  
> 加载、合并、清洗之后，常需按类别计算统计或生成透视表。本章深入 **pandas `groupby`**：拆分-应用-联合（split-apply-combine），并覆盖 **聚合、apply、transform、透视表/交叉表**。

**前置**：[第 9 章 绘图和可视化](./chapter09_plotting_visualization.md) → 本章 → [第 11 章 时间序列](./chapter11_time_series.md)。

**本仓库深化练习**（量化向）：

| 主题 | 路径 |
|------|------|
| groupby 基础 | [`../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/08_groupby_basics.md`](../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/08_groupby_basics.md) |
| groupby 进阶 | [`../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/02_groupby_and_aggregation.md`](../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/02_groupby_and_aggregation.md) |
| pivot_table | [`../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/09_pivot_table_and_reshape.md`](../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/09_pivot_table_and_reshape.md) |
| 分组回测 | [`../../Python-Financial-BigData-Analysis/code/pandas/04_multi_asset_data_handling/03_groupby_backtest.md`](../../Python-Financial-BigData-Analysis/code/pandas/04_multi_asset_data_handling/03_groupby_backtest.md) |

**演示脚本**：[`../code/chapter10_groupby_demo.py`](../code/chapter10_groupby_demo.py)

---

## 章节总览

**小节统计**：6 个一级小节 + 15 个二级小节，共 **21 个核心小节**。

| 一级 | 二级 |
|------|------|
| 10.1 GroupBy 机制 | 10.1.1～10.1.5 |
| 10.2 数据聚合 | 10.2.1、10.2.2 |
| 10.3 Apply | 10.3.1～10.3.6 |
| 10.4 分组转换 | — |
| 10.5 透视表与交叉表 | — |
| 10.6 总结 | — |

---

## 一、书本原文核心知识点提炼

### 10.1 GroupBy 机制

- **拆分-应用-联合**：按键拆组 → 对每组应用函数 → 合并结果。
- **分组键**：等长列表/数组、列名、dict/Series 映射、轴上的函数、`level=`（MultiIndex）。
- **`GroupBy` 是延迟对象**：调用 `mean()`、`size()`、`count()` 等才真正计算；默认跳过 NA（`dropna=False` 可改）。

#### 10.1.1 对分组进行迭代

- `for name, group in df.groupby("key"):` 得到组名与数据块；多键时 `name` 为元组。
- 字典推导：`{n: g for n, g in df.groupby("key")}` 快速得到分块字典。

#### 10.1.2 选取一列或多列

- `df.groupby("k")["col"]` ≡ `df["col"].groupby(df["k"])`。
- 标量列名 → 分组 Series；列表 → 分组 DataFrame。

#### 10.1.3 利用字典和 Series 分组

- 外部映射 dict/Series 可直接传给 `groupby`。
- `groupby(mapping, axis="columns")` 可按类合并多列。

#### 10.1.4 利用函数进行分组

- 函数对每个索引值调用一次，返回值作组名（如 `len` 按索引长度分组）。
- 函数可与数组、列表、dict 混用，底层统一对齐为数组。

#### 10.1.5 根据索引层级分组

- MultiIndex：`groupby(level=0)` 或 `level="name"`。

### 10.2 数据聚合

- 内置优化：`count, sum, mean, median, std, min, max, first, last`…
- 自定义：`agg(func)` / `aggregate(func)`（通常慢于内置）。

#### 10.2.1 逐列操作和多函数应用

- `agg(["mean", "std"])` 多函数；`agg([("m", "mean"), ("s", "std")])` 自定义列名。
- `agg({"col1": "sum", "col2": np.max})` 按列不同规则。

#### 10.2.2 返回不含行索引的聚合数据

- **`groupby(..., as_index=False)`**：分组键不作为结果行索引，直接得规整 DataFrame。

### 10.3 Apply

- **`apply(func)`**：最通用；各组独立调用 `func`，再 `concat` 拼接。
- 函数须返回 pandas 对象或标量；额外参数写在 `apply` 后：`apply(f, arg1=v)`。
- `groupby().describe()` 本质是 apply 快捷方式。

#### 10.3.1 禁用分组键

- **`group_keys=False`**：避免 apply 拼接后外层多余 MultiIndex。

#### 10.3.2 分位数和桶分析

- **`groupby(pd.cut(...))`** / **`groupby(pd.qcut(...))`** 做分桶统计。

#### 10.3.3 示例：分组填充缺失值

- `groupby(...).apply(lambda g: g.fillna(g.mean()))` 用组内均值填 NA。

#### 10.3.4 示例：分组随机采样

- `groupby(...).apply(lambda g: g.sample(n=2))` 等。

#### 10.3.5 示例：加权平均与相关系数

- 组内 `np.average(x, weights=w)`；按年 `corrwith` 算与基准相关。

#### 10.3.6 示例：分组线性回归

- `apply` 内嵌 **statsmodels OLS**，各组独立拟合（见演示脚本注释）。

### 10.4 分组转换和展开式 GroupBy

- **`transform`**：输出须能广播到组形状或与组同形；不能改输入。
- 内置 `'mean'`, `'sum'` 等走**高速路径**；组间算术如 `(x - x.groupby().transform('mean'))` 即截面去均值/标准化。

### 10.5 透视表和交叉表

- **`pivot_table(index=, columns=, values=, aggfunc=, margins=True)`** 默认 `mean`；`margins` 行列合计。
- **`pd.crosstab(index, columns)`** 专做分类频次矩阵。

### 10.6 总结

- groupby / apply / transform 是复杂统计与建模的前置技能；第 13 章有更多实战案例。
- 下一章：[第 11 章 时间序列](./chapter11_time_series.md)。

---

## 二、关键语法速查表

| 场景 | API |
|------|-----|
| 分组 | `df.groupby("col")`, `df.groupby(["d","code"])` |
| 聚合 | `.mean()`, `.agg(["sum","std"])` |
| 列选择 | `df.groupby("k")["v"]` |
| 无索引结果 | `groupby(..., as_index=False).mean()` |
| 通用函数 | `.apply(func, group_keys=False)` |
| 组内填 NA | `.transform("mean")`, `.apply(lambda g: g.fillna(...))` |
| 截面标准化 | `df["x"] - df.groupby("date")["x"].transform("mean")` |
| 分桶 | `df.groupby(pd.qcut(df["f"], 5))` |
| 透视 | `df.pivot_table(index=, columns=, values=, aggfunc=)` |
| 交叉表 | `pd.crosstab(df["a"], df["b"])` |

---

## 三、通用基础示例

见 [`../code/chapter10_groupby_demo.py`](../code/chapter10_groupby_demo.py)

---

## 四、【量化专属改造】金融实战衔接

1. **截面分组**：`groupby("date")` 做每日行业均值、因子排名、五分位多空组合收益。
2. **多维**：`groupby(["date", "industry"])` 行业内标准化因子。
3. **因子分层回测**：`qcut` + `groupby` 算各层次日平均收益；注意 **lookahead**（用 t 期因子预测 t+1 收益）。
4. **`as_index=False`**：合并进报表或 SQL 式长表时更顺手。
5. **`transform`**：组内 z-score、去均值，保持原行数，适合作为回归前的截面调整。
6. **`pivot_table`**：date × 行业 平均 PE；`margins=True` 看全市场。
7. **避免滥用 `apply`**：能 `agg`/`transform` 就不用 apply，大面板回测性能差一个数量级很常见。

---

## 五、与 statsmodels 建模的衔接要点

- **分组 OLS**：`apply` 内 `sm.OLS(y, X).fit()` 适合横截面逐日回归（Fama-MacBeth 第一步）；注意每组样本量与共线性。
- 聚合后再回归 vs 池化回归：信息损失不同；高频因子检验常用逐日 `groupby("date").apply(regress)`。
- `transform` 去均值后的残差式变量，与回归中加入固定效应有联系，但不完全等价。
- 透视表汇总统计不能替代显著性检验；需配合第 9 章可视化与 statsmodels 推断。

---

## 本章自检清单

- [ ] 理解 GroupBy 延迟计算  
- [ ] 会 `groupby` 单列/多列、`as_index=False`  
- [ ] 会 `agg` 多函数与按列字典  
- [ ] 会 `apply` 与 `group_keys=False`  
- [ ] 会 `transform` 做组内标准化  
- [ ] 会 `pivot_table` 与 `crosstab`  

---

## 后续扩展留白

### 10.1～10.5

（留白）
