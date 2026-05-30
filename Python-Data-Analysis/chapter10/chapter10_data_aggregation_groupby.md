# 第 10 章 数据聚合与分组操作

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 10 章。  
> 加载、合并、清洗之后，常需按类别计算统计或生成透视表。本章深入 **pandas `groupby`**：拆分-应用-联合（split-apply-combine），并覆盖 **聚合、apply、transform、透视表/交叉表**。

**前置**：[第 9 章 绘图和可视化](../chapter09/chapter09_plotting_visualization.md) → 本章 → [第 11 章 时间序列](../chapter11/chapter11_time_series.md)。

**本仓库深化练习**（量化向）：

| 主题 | 路径 |
|------|------|
| groupby 基础 | [`../../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/08_groupby_basics.md`](../../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/08_groupby_basics.md) |
| groupby 进阶 | [`../../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/02_groupby_and_aggregation.md`](../../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/02_groupby_and_aggregation.md) |
| pivot_table | [`../../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/09_pivot_table_and_reshape.md`](../../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/09_pivot_table_and_reshape.md) |
| 分组回测 | [`../../../Python-Financial-BigData-Analysis/code/pandas/04_multi_asset_data_handling/03_groupby_backtest.md`](../../../Python-Financial-BigData-Analysis/code/pandas/04_multi_asset_data_handling/03_groupby_backtest.md) |

**演示脚本**：[`./code/chapter10_groupby_demo.py`](./code/chapter10_groupby_demo.py)

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

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [10_01_GroupBy_机制](./sections/10_01_GroupBy_机制.md) | GroupBy 机制 |
| [10_01_01_对分组进行迭代](./sections/10_01_01_对分组进行迭代.md) | 01 对分组进行迭代 |
| [10_01_02_选取一列或多列](./sections/10_01_02_选取一列或多列.md) | 02 选取一列或多列 |
| [10_01_03_利用字典和_Series_分组](./sections/10_01_03_利用字典和_Series_分组.md) | 03 利用字典和 Series 分组 |
| [10_01_04_利用函数进行分组](./sections/10_01_04_利用函数进行分组.md) | 04 利用函数进行分组 |
| [10_01_05_根据索引层级分组](./sections/10_01_05_根据索引层级分组.md) | 05 根据索引层级分组 |
| [10_02_数据聚合](./sections/10_02_数据聚合.md) | 数据聚合 |
| [10_02_01_逐列操作和多函数应用](./sections/10_02_01_逐列操作和多函数应用.md) | 01 逐列操作和多函数应用 |
| [10_02_02_返回不含行索引的聚合数据](./sections/10_02_02_返回不含行索引的聚合数据.md) | 02 返回不含行索引的聚合数据 |
| [10_03_Apply](./sections/10_03_Apply.md) | Apply |
| [10_03_01_禁用分组键](./sections/10_03_01_禁用分组键.md) | 01 禁用分组键 |
| [10_03_02_分位数和桶分析](./sections/10_03_02_分位数和桶分析.md) | 02 分位数和桶分析 |
| [10_03_03_示例_分组填充缺失值](./sections/10_03_03_示例_分组填充缺失值.md) | 03 示例 分组填充缺失值 |
| [10_03_04_示例_分组随机采样](./sections/10_03_04_示例_分组随机采样.md) | 04 示例 分组随机采样 |
| [10_03_05_示例_加权平均与相关系数](./sections/10_03_05_示例_加权平均与相关系数.md) | 05 示例 加权平均与相关系数 |
| [10_03_06_示例_分组线性回归](./sections/10_03_06_示例_分组线性回归.md) | 06 示例 分组线性回归 |
| [10_04_分组转换和展开式_GroupBy](./sections/10_04_分组转换和展开式_GroupBy.md) | 分组转换和展开式 GroupBy |
| [10_05_透视表和交叉表](./sections/10_05_透视表和交叉表.md) | 透视表和交叉表 |
| [10_06_总结](./sections/10_06_总结.md) | 总结 |

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

见 [`./code/chapter10_groupby_demo.py`](./code/chapter10_groupby_demo.py)

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
