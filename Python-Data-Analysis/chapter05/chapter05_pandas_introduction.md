# 第 5 章 pandas 入门

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 5 章。  
> pandas 是本书后续最核心的工具：面向 **表格型、异构数据**，提供 Series / DataFrame、索引对齐、描述统计等能力。与 NumPy 的同构数值数组不同，pandas 专为 **带标签的表** 设计。

**前置**：[第 4 章 NumPy](../chapter04/chapter04_numpy_basics_arrays_vectorization.md) → 本章 → 原书第 6 章起数据读写与规整。

**本仓库深化练习**（量化向，与本书第 5 章并行）：

| 主题 | 路径 |
|------|------|
| Series / DataFrame 基础 | [`../../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/`](../../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/) |
| loc / iloc / merge | 同上 + [`01_core_data_operations/`](../../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/) |

**本章综合演示**：[`./code/chapter05_pandas_intro_demo.py`](./code/chapter05_pandas_intro_demo.py)

---

## 章节总览

**小节统计**：4 个一级小节 + 11 个二级小节（资料中 5.2.6 未出现，直接到 5.2.7），共 **15 个小节**。

| 一级 | 二级 |
|------|------|
| 5.1 数据结构 | 5.1.1 Series；5.1.2 DataFrame；5.1.3 Index |
| 5.2 基本功能 | 5.2.1～5.2.5；5.2.7 重复标签 |
| 5.3 描述性统计 | 5.3.1 相关/协方差；5.3.2 唯一值/计数 |
| 5.4 总结 | — |

---

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [05_01_数据结构](./sections/05_01_数据结构.md) | 数据结构 |
| [05_01_01_Series](./sections/05_01_01_Series.md) | 01 Series |
| [05_01_02_DataFrame](./sections/05_01_02_DataFrame.md) | 02 DataFrame |
| [05_01_03_Index](./sections/05_01_03_Index.md) | 03 Index |
| [05_02_基本功能](./sections/05_02_基本功能.md) | 基本功能 |
| [05_02_01_reindex](./sections/05_02_01_reindex.md) | 01 reindex |
| [05_02_02_drop](./sections/05_02_02_drop.md) | 02 drop |
| [05_02_03_索引_选取_过滤](./sections/05_02_03_索引_选取_过滤.md) | 03 索引 选取 过滤 |
| [05_02_04_算术与对齐](./sections/05_02_04_算术与对齐.md) | 04 算术与对齐 |
| [05_02_05_函数应用](./sections/05_02_05_函数应用.md) | 05 函数应用 |
| [05_02_07_重复索引](./sections/05_02_07_重复索引.md) | 07 重复索引 |
| [05_03_描述性统计](./sections/05_03_描述性统计.md) | 描述性统计 |
| [05_03_01_相关与协方差](./sections/05_03_01_相关与协方差.md) | 01 相关与协方差 |
| [05_03_02_唯一值与计数](./sections/05_03_02_唯一值与计数.md) | 02 唯一值与计数 |
| [05_04_总结](./sections/05_04_总结.md) | 总结 |

## 二、关键语法速查表

| 主题 | API |
|------|-----|
| 创建 | `pd.Series`, `pd.DataFrame` |
| 缺失 | `pd.isna`, `fillna` |
| 选取 | `df.loc[...]`, `df.iloc[...]` |
| 重排 | `df.reindex`, `df.drop` |
| 对齐运算 | `s1 + s2`, `df.add(other, fill_value=0)` |
| 统计 | `df.mean()`, `df.describe()`, `df.corr()` |
| 成员 | `s.isin([...])`, `s.value_counts()` |

---

## 三、通用基础示例

见 [`./code/chapter05_pandas_intro_demo.py`](./code/chapter05_pandas_intro_demo.py)

---

## 四、【量化专属改造】金融实战衔接

1. **OHLCV 表**：`DataFrame` + `DatetimeIndex`；列 `open/high/low/close/volume`。
2. **对齐即 join**：两只股票收益序列相加前索引自动对齐——与多表 merge 思想一致。
3. **视图陷阱**：`df["close"] *= 1.01` 会改原表；策略中间表用 `.copy()`。
4. **loc 含末端**：日期切片 `df.loc["2025-01-01":"2025-01-31"]` 包含 1 月 31 日（若存在）。
5. **链式赋值**：写信号列用 `df.loc[mask, "signal"] = 1`，避免 `SettingWithCopyWarning`。
6. **`describe` / `corr`**：因子 EDA、检查共线性（建模前必做）。

---

## 五、与 statsmodels 建模的衔接要点

- 回归前常用 `df.describe()`、`df.corr()` 做 EDA；高相关因子考虑剔除。
- `df[["y","x1","x2"]].dropna()` 得到 OLS 干净样本；理解 **索引对齐** 可避免 y 与 X 行错位。
- `value_counts` / `isin` 用于分类变量检查；哑变量构造在后续章节完成。

---

## 本章自检清单

- [ ] 能解释 Series 索引对齐与 DataFrame 列视图  
- [ ] 会用 `loc` / `iloc`，并知道 loc 切片含末端  
- [ ] 会用 `reindex` 与 `drop`  
- [ ] 会用 `add(fill_value=...)` 处理对齐缺失  
- [ ] 能避免链式赋值  
- [ ] 会用 `describe`、`corr`、`value_counts`  

---

## 后续扩展留白

### 5.1～5.3

（留白）
