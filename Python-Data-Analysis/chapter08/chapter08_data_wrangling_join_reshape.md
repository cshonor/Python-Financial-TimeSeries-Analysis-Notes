# 第 8 章 数据规整：连接、联合和重塑

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 8 章。  
> 分析中的数据常分散在多个文件或库表中，或现有排列不利于建模。本章解决 **形状与组合**：**层次化索引（MultiIndex）** → **连接/合并（merge、join、concat、combine_first）** → **重塑与透视（stack/unstack、pivot、melt）**。

**前置**：[第 7 章 数据清洗和准备](../chapter07/chapter07_data_cleaning_preparation.md) → 本章 → [第 9 章 绘图和可视化](../chapter09/chapter09_plotting_visualization.md)。

**本仓库深化练习**（量化向，与本章并行）：

| 主题 | 路径 |
|------|------|
| merge / concat / join 基础 | [`../../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/07_dataframe_merge_concat_join.md`](../../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/07_dataframe_merge_concat_join.md) |
| merge / concat 进阶 | [`../../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/03_merge_and_concat.md`](../../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/03_merge_and_concat.md) |
| pivot / reshape | [`../../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/04_pivot_and_reshape.md`](../../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/04_pivot_and_reshape.md) |
| MultiIndex / 宽长表 | [`../../../Python-Financial-BigData-Analysis/code/pandas/04_multi_asset_data_handling/`](../../../Python-Financial-BigData-Analysis/code/pandas/04_multi_asset_data_handling/) |

**演示脚本**：[`./code/chapter08_data_wrangling_demo.py`](./code/chapter08_data_wrangling_demo.py)

---

## 章节总览

**小节统计**：4 个一级小节 + 10 个二级小节，共 **14 个核心小节**。

| 一级 | 二级 |
|------|------|
| 8.1 层次化索引 | 8.1.1 重排序；8.1.2 按层汇总；8.1.3 列作索引 |
| 8.2 联合与合并 | 8.2.1 merge；8.2.2 按索引；8.2.3 concat；8.2.4 combine_first |
| 8.3 重塑和透视 | 8.3.1 stack/unstack；8.3.2 pivot；8.3.3 melt |
| 8.4 总结 | — |

---

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [08_01_层次化索引](./sections/08_01_层次化索引.md) | 层次化索引 |
| [08_01_01_重排序和层级排序](./sections/08_01_01_重排序和层级排序.md) | 01 重排序和层级排序 |
| [08_01_02_按层级进行汇总统计](./sections/08_01_02_按层级进行汇总统计.md) | 02 按层级进行汇总统计 |
| [08_01_03_使用_DataFrame_的列进行索引](./sections/08_01_03_使用_DataFrame_的列进行索引.md) | 03 使用 DataFrame 的列进行索引 |
| [08_02_联合与合并数据集](./sections/08_02_联合与合并数据集.md) | 联合与合并数据集 |
| [08_02_01_数据库风格的_DataFrame_连接](./sections/08_02_01_数据库风格的_DataFrame_连接.md) | 01 数据库风格的 DataFrame 连接 |
| [08_02_02_根据索引合并](./sections/08_02_02_根据索引合并.md) | 02 根据索引合并 |
| [08_02_03_轴向拼接](./sections/08_02_03_轴向拼接.md) | 03 轴向拼接 |
| [08_02_04_联合重叠数据](./sections/08_02_04_联合重叠数据.md) | 04 联合重叠数据 |
| [08_03_重塑和透视](./sections/08_03_重塑和透视.md) | 重塑和透视 |
| [08_03_01_使用层次化索引进行重塑](./sections/08_03_01_使用层次化索引进行重塑.md) | 01 使用层次化索引进行重塑 |
| [08_03_02_长格式_宽格式](./sections/08_03_02_长格式_宽格式.md) | 02 长格式 宽格式 |
| [08_03_03_宽格式_长格式](./sections/08_03_03_宽格式_长格式.md) | 03 宽格式 长格式 |
| [08_04_总结](./sections/08_04_总结.md) | 总结 |

## 二、关键语法速查表

| 场景 | API |
|------|-----|
| 多层索引 | `pd.MultiIndex.from_arrays(...)`、`df.index.names` |
| 交换/排序层 | `df.swaplevel()`, `df.sort_index(level=0)` |
| 按层聚合 | `df.groupby(level=0).sum()` 或 `df.sum(level="code")` |
| 列 ↔ 索引 | `set_index()`, `reset_index()` |
| 键合并 | `pd.merge(a, b, on=["date","code"], how="left")` |
| 索引合并 | `merge(..., left_index=True)`, `left.join(right)` |
| 堆叠 | `pd.concat([df1, df2], keys=["A","B"])` |
| 补丁合并 | `primary.combine_first(backup)` |
| 列转行 | `df.stack()`, `df.unstack()` |
| 长→宽 | `df.pivot(index="date", columns="code", values="close")` |
| 宽→长 | `pd.melt(df, id_vars=["date"], value_vars=[...])` |

---

## 三、通用基础示例

见 [`./code/chapter08_data_wrangling_demo.py`](./code/chapter08_data_wrangling_demo.py)

---

## 四、【量化专属改造】金融实战衔接

1. **面板长表主键**：`(date, code)` 建 MultiIndex 或 merge 键；合并前 `duplicated(["date","code"]).sum()` 应为 0。
2. **行情 + 因子**：`merge(price, factor, on=["date","code"], how="left", validate="one_to_one")`（pandas 2+ 可用 `validate` 检查键关系）。
3. **多标的纵向拼接**：`concat` + `keys=代码列表` 区分来源；或保持长表不 concat，直接 groupby。
4. **复权/补丁行情**：新版本 `combine_first` 覆盖旧表 NA（注意业务上是否允许后填前）。
5. **宽表面板**：`pivot` 得 date × code 矩阵，便于算截面相关、画热力图；回测因子常保持**长表**再 groupby。
6. **因子库 melt**：多因子列 `melt(id_vars=["date","code"])` 进 tidy 格式，方便与 statsmodels 长表接口对接。
7. **外连接陷阱**：`how="outer"` 会引入非交易日或停牌日 NA，需与第 7 章清洗衔接。

---

## 五、与 statsmodels 建模的衔接要点

- 截面回归通常要 **同一 date 下多只股票一行观测**（长表）或 **宽表转 stack**；合并后确认每行 `(date, code)` 唯一。
- 时间序列单资产：常 `set_index("date")` 后 `join` 宏观因子（按月/季需先 `resample` 对齐频率）。
- `get_dummies`（第 7 章）与 `pivot` 不同：前者为分类哑变量，后者为指标展开；行业因子二选一，避免重复编码。
- 训练/测试拆分应在 **合并完成后** 按时间切，防止 merge 造成未来信息渗入（lookahead）。

---

## 本章自检清单

- [ ] 会用 MultiIndex 部分索引、`swaplevel`、`sort_index(level=...)`
- [ ] 会用 `set_index` / `reset_index`
- [ ] 会用 `merge` 的 `on`、`how`、`suffixes`
- [ ] 会用 `join` 与 `concat(keys=..., ignore_index=...)`
- [ ] 会用 `combine_first`
- [ ] 会用 `stack` / `unstack` / `pivot` / `melt`

---

## 后续扩展留白

### 8.1～8.3

（留白）
