# 第 8 章 数据规整：连接、联合和重塑

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 8 章。  
> 分析中的数据常分散在多个文件或库表中，或现有排列不利于建模。本章解决 **形状与组合**：**层次化索引（MultiIndex）** → **连接/合并（merge、join、concat、combine_first）** → **重塑与透视（stack/unstack、pivot、melt）**。

**前置**：[第 7 章 数据清洗和准备](./chapter07_data_cleaning_preparation.md) → 本章 → [第 9 章 绘图和可视化](./chapter09_plotting_visualization.md)。

**本仓库深化练习**（量化向，与本章并行）：

| 主题 | 路径 |
|------|------|
| merge / concat / join 基础 | [`../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/07_dataframe_merge_concat_join.md`](../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/07_dataframe_merge_concat_join.md) |
| merge / concat 进阶 | [`../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/03_merge_and_concat.md`](../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/03_merge_and_concat.md) |
| pivot / reshape | [`../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/04_pivot_and_reshape.md`](../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/04_pivot_and_reshape.md) |
| MultiIndex / 宽长表 | [`../../Python-Financial-BigData-Analysis/code/pandas/04_multi_asset_data_handling/`](../../Python-Financial-BigData-Analysis/code/pandas/04_multi_asset_data_handling/) |

**演示脚本**：[`../code/chapter08_data_wrangling_demo.py`](../code/chapter08_data_wrangling_demo.py)

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

## 一、书本原文核心知识点提炼

### 8.1 层次化索引

- **MultiIndex**：单轴上多个索引层级，用低维 Series/DataFrame 表达高维数据。
- **部分索引**：可只取最外层标签，也可在内部层级切片；行、列轴均可分层，层名用 **`names`** 与行标签区分。
- **地位**：后续重塑、透视表、分组操作的基础。

#### 8.1.1 重排序和层级排序

- **`swaplevel()`**：交换两个层级位置（改索引外观，不改底层数据顺序）。
- **`sort_index()`**：默认按各层字母序排序；`level=` 指定只排某一层。
- **性能**：最外层已排序（如 `sort_index(level=0)`）时，切片选取更快。

#### 8.1.2 按层级进行汇总统计

- `sum()`、`mean()` 等支持 **`level="层级名"`**，沿该层聚合。
- 底层等价于 **`groupby`** 机制。

#### 8.1.3 使用 DataFrame 的列进行索引

- **`set_index(cols)`**：列 → 行索引；默认从数据中移除列，`drop=False` 可保留。
- **`reset_index()`**：索引层级 → 普通列，恢复默认整数索引。

### 8.2 联合与合并数据集

三种思路：**merge（键连接）**、**concat（堆叠）**、**combine_first（填补）**。

#### 8.2.1 数据库风格的 DataFrame 连接

- **`pd.merge(left, right, on=..., how=...)`**
- 未指定键时默认用**两表同名列**；推荐显式 `on`；列名不同用 `left_on` / `right_on`。
- **`how`**：`inner`（默认，交集）、`outer`（并集+NA）、`left` / `right`。
- 多对多键 → 笛卡儿积行数膨胀；重名列用 **`suffixes=("_x","_y")`**。

#### 8.2.2 根据索引合并

- **`left_index=True` / `right_index=True`**：以索引为键；层次化索引等价多键合并。
- **`df.join(other)`**：按索引合并，默认 **left join**；要求列名不重叠；可传入 DataFrame 列表多表拼接。

#### 8.2.3 轴向拼接

- **`pd.concat(objs, axis=0|1, join="inner"|"outer", keys=..., ignore_index=...)`**
- 默认沿**行**堆叠；`axis=1` 横向拼列。
- **`keys`**：在拼接轴上建 MultiIndex，区分来源对象。
- **`ignore_index=True`**：丢弃无业务意义的原行索引，生成 0…N-1。

#### 8.2.4 联合重叠数据

- 优先 A，A 为 NA 时用 B 补：**`a.combine_first(b)`**（自动对齐索引）。
- NumPy 可用 `np.where(pd.isna(a), b, a)`，但**不对齐标签**。

### 8.3 重塑和透视

#### 8.3.1 使用层次化索引进行重塑

- **`stack()`**：列 → 行（DataFrame → 带 MultiIndex 的 Series）。
- **`unstack()`**：行 → 列（stack 的逆）；默认操作**最内层**，可指定 `level`。
- `unstack` 可能引入 NA；`stack` 默认丢弃 NA，整齐数据上二者常可逆。

#### 8.3.2 长格式 → 宽格式（pivot）

- 长表：每行一次观测（如 date, item, value）。
- **`df.pivot(index=..., columns=..., values=...)`**；省略 `values` 时剩余列都作值列 → 层次化列索引。
- 等价于 **`set_index` + `unstack`**；要求 (index, columns) 组合唯一，否则用 **`pivot_table` + 聚合**。

#### 8.3.3 宽格式 → 长格式（melt）

- **`pd.melt(df, id_vars=..., value_vars=..., var_name=..., value_name=...)`**
- `id_vars`：保持不动的键列；其余列折叠为 `variable` / `value`（列名可自定义）。

### 8.4 总结

- 至此完成 pandas **导入、清洗、重组** 的核心基础；下一章：[第 9 章 绘图和可视化](./chapter09_plotting_visualization.md)。

---

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

见 [`../code/chapter08_data_wrangling_demo.py`](../code/chapter08_data_wrangling_demo.py)

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
