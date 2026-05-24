# 第 5 章 pandas 入门

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 5 章。  
> pandas 是本书后续最核心的工具：面向 **表格型、异构数据**，提供 Series / DataFrame、索引对齐、描述统计等能力。与 NumPy 的同构数值数组不同，pandas 专为 **带标签的表** 设计。

**前置**：[第 4 章 NumPy](./chapter04_numpy_basics_arrays_vectorization.md) → 本章 → 原书第 6 章起数据读写与规整。

**本仓库深化练习**（量化向，与本书第 5 章并行）：

| 主题 | 路径 |
|------|------|
| Series / DataFrame 基础 | [`../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/`](../../Python-Financial-BigData-Analysis/code/pandas/00_core_objects/) |
| loc / iloc / merge | 同上 + [`01_core_data_operations/`](../../Python-Financial-BigData-Analysis/code/pandas/01_core_data_operations/) |

**本章综合演示**：[`../code/chapter05_pandas_intro_demo.py`](../code/chapter05_pandas_intro_demo.py)

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

## 一、书本原文核心知识点提炼

### 5.1 数据结构

#### 5.1.1 Series

- 一维带标签数组：`values` + `index`；未指定索引则 0…N-1。
- 可由 **dict** 创建；指定 `index` 时按列表对齐，缺键 → `NaN`。
- `pd.isna` / `pd.notna` 检测缺失。
- **算术自动按索引对齐**（类似 join）；Series 与 index 可有 `name`。

#### 5.1.2 DataFrame

- 二维表：行索引 + 列索引；列可异构 dtype；可视为 **共享行索引的 Series 字典**。
- 常用 `pd.DataFrame(dict_of_lists)`；`columns` 指定列顺序；`head()` / `tail()`。
- **取列常为视图**：`df["col"]` 修改会影响原表；需隔离用 `.copy()`。

#### 5.1.3 Index

- 轴标签容器；支持集合运算（`union`、`intersection`、`isin`…）。
- **Index 不可变**；允许 **重复标签**（与 set 不同）。

### 5.2 基本功能

#### 5.2.1 `reindex`

- 按新索引重排；新标签 → `NaN`；`method="ffill"` 等填充。
- DataFrame 可同时 `reindex` 行/列。
- **`loc` 只能选已有标签**；`reindex` 可引入新标签。

#### 5.2.2 `drop`

- 删行/列；默认 **返回新对象**；列删除用 `columns=` 或 `axis=1`。

#### 5.2.3 索引、选取、过滤

- **`loc`**：按标签；切片 **含末端**（`loc["b":"c"]`）。
- **`iloc`**：按整数位置；切片规则同 Python（不含 stop）。
- 避免 `[]` 在整数标签上的歧义；**避免链式赋值**，用 `df.loc[mask, "col"] = v`。

#### 5.2.4 算术与对齐

- 索引 **并集外连接**；无重叠处为 `NaN`。
- `add(..., fill_value=0)` 等可先填缺失再算。
- DataFrame ± Series：默认 **按列广播**；行方向广播需 `axis="index"`。

#### 5.2.5 函数应用

- NumPy ufunc 可直接用于 pandas 对象。
- `apply`：按行/列应用函数；（新版 pandas 元素级映射常用 `map` / `applymap`→`map` 按版本）

#### 5.2.7 重复索引

- `index.is_unique` 检查；重复标签选取可能返回多行 Series 或标量，类型不稳定。

### 5.3 描述性统计

- `mean` / `sum` 等默认 **按列**；`axis=1` 按行。
- 默认 `skipna=True`；`idxmax` / `idxmin` 返回标签。
- `cumsum` 等累计；`describe()` 数值列与非数值列输出不同。

#### 5.3.1 相关与协方差

- Series：`corr()` / `cov()`；DataFrame：相关/协方差矩阵。
- `corrwith`：与外部 Series/DataFrame 按列相关。

#### 5.3.2 唯一值与计数

- `unique()`、`value_counts()`、`isin()` 过滤。
- DataFrame 多列频次可用 `apply(pd.value_counts)`。

### 5.4 总结

- 下一章：读写数据集；本章是后续高级规整的基础。

---

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

见 [`../code/chapter05_pandas_intro_demo.py`](../code/chapter05_pandas_intro_demo.py)

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
