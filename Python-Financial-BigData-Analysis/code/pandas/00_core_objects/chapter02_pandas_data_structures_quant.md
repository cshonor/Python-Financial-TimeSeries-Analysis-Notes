# 第 2 章对齐笔记：pandas 的数据结构（Series / DataFrame）与量化存储约定

> 对应原书：**第 2 章 pandas 的数据结构**。  
> 本章目标：能**正确设计**行情与因子在 pandas 里的形态（索引、`dtype`、长表/宽表），为后续读取、清洗、时间序列与 statsmodels 输入打地基。

---

## 一、书本原文核心知识点提炼

1. **Series**：一维、带索引的序列；可视为「单列」或「带标签的 ndarray」。  
2. **DataFrame**：二维表；行索引 + 列名；每列可视为共享同一行索引的 Series。  
3. **索引 Index**：标签与对齐的语义来源；时间序列场景下常用 `DatetimeIndex`。  
4. **dtype**：决定内存与计算行为；混用 `object` 会拖慢且易错。  
5. **对齐（alignment）**：运算与合并按索引对齐，是 pandas 与裸 NumPy 的核心差异之一。

---

## 二、关键语法速查表

| API / 概念 | 用途（一句话） |
|-------------|----------------|
| `pd.Series(data, index=..., name=...)` | 构造一维序列 |
| `pd.DataFrame(data, index=..., columns=...)` | 构造二维表 |
| `df.index` / `df.columns` | 行标签 / 列名 |
| `df.dtypes` | 各列数据类型 |
| `df.set_index` / `reset_index` | 列与索引互换 |
| `pd.to_datetime` | 把日期列或字符串转为时间类型 |
| `pd.MultiIndex.from_arrays` | 多标的 `(date, code)` 等多级索引 |

---

## 三、通用基础示例

```python
import pandas as pd

s = pd.Series([1, 2, 3], index=["a", "b", "c"], name="x")
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]}, index=["r0", "r1"])
```

要点：**先确定「行代表什么」**（一天？一根 K 线？一只票在某个时点？），再选索引。

---

## 四、【量化专属改造】金融实战代码

### 4.1 单标的日频 OHLCV：行 = 交易日，`DatetimeIndex`

- 行索引：`DatetimeIndex`（升序、唯一）。  
- 列：至少 `open, high, low, close, volume`；衍生列 `ret` 等后续再算。  
- **不要**用默认 `RangeIndex` 存日频行情作为主键（合并、对齐、画图都痛苦）。

### 4.2 多标的长表（panel 风格）：`(date, code)` 唯一

- 每行：`date, code, close, ...`；同一 `(date, code)` 只能一行（否则 merge/pivot 会炸或静默重复）。  
- 进阶：用 `MultiIndex.from_arrays([date, code])` 做行索引，便于 `xs` 截面切片。

### 4.3 宽表（矩阵风格）：行 = 日期，列 = 股票代码

- 适合相关矩阵、部分向量化运算；**列数极大时注意内存**。  
- 因子回测更常见的是**长表 + groupby**；宽表多用于协方差/相关。

完整可运行示例见同目录：`chapter02_pandas_data_structures_quant.py`。

---

## 五、与 statsmodels 建模的衔接要点

1. **横截面回归（如因子收益 OLS）**：通常需要一张 `DataFrame`，行为股票、列为 `y` 与多个 `X`；分类变量需先 **`pd.get_dummies`** 或手动构造哑变量；若带截距，记得在 statsmodels 里 `add_constant`。  
2. **时间序列（如 ARIMA）**：目标序列多为 **单变量 `Series`**，且索引为 **规则或不规则的 DatetimeIndex**；需要严格区分「样本内/样本外」与**信息泄漏**（预测变量只能用到 \(t\) 及以前）。  
3. **本章你要带走的习惯**：  
   - 行情主键：**日期有序 + 唯一**；  
   - 多标的主键：**(date, code) 唯一**；  
   - 数值列尽量 **float64/int64**，避免整表 `object`。

---

## 本章自检清单

- [ ] 能说清「长表 vs 宽表」各自适合什么量化任务。  
- [ ] 会构造 `DatetimeIndex` 的 OHLCV `DataFrame`。  
- [ ] 会构造 `(date, code)` 的 `MultiIndex` 长表。  
- [ ] 能解释「为什么 merge 前要先检查重复键」。
