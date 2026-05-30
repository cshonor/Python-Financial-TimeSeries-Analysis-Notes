# 第 7 章 数据清洗和准备

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 7 章。  
> 数据准备（加载、清理、转换、重塑）常占分析工作 **80%+** 时间。本章讲解 pandas 与标准库在 **缺失值、重复、映射、分箱、异常值、字符串、分类数据** 上的工具。

**前置**：[第 6 章 数据 I/O](../chapter06/chapter06_data_io_file_formats.md) → 本章 → [第 8 章 数据规整](../chapter08/chapter08_data_wrangling_join_reshape.md)。

**量化专题练习**（与本章并行深化）：  
[`../../../Python-Financial-BigData-Analysis/code/pandas/02_data_cleaning_preprocessing/`](../../../Python-Financial-BigData-Analysis/code/pandas/02_data_cleaning_preprocessing/)

**演示脚本**：[`./code/chapter07_data_cleaning_demo.py`](./code/chapter07_data_cleaning_demo.py)

---

## 章节总览

**小节统计**：6 个一级小节 + 14 个二级小节（资料中 7.5.3 未出现），共 **20 个小节**。

| 一级 | 二级 |
|------|------|
| 7.1 缺失数据 | 7.1.1 过滤；7.1.2 填充 |
| 7.2 数据转换 | 7.2.1～7.2.7 |
| 7.3 扩展数据类型 | — |
| 7.4 字符串 | 7.4.1～7.4.3 |
| 7.5 分类数据 | 7.5.1、7.5.2、7.5.4 |
| 7.6 总结 | — |

---

---

## 小节笔记索引

| 文件 | 说明 |
|------|------|
| [07_01_处理缺失数据](./sections/07_01_处理缺失数据.md) | 处理缺失数据 |
| [07_01_01_过滤](./sections/07_01_01_过滤.md) | 01 过滤 |
| [07_01_02_填充](./sections/07_01_02_填充.md) | 02 填充 |
| [07_02_数据转换](./sections/07_02_数据转换.md) | 数据转换 |
| [07_03_扩展数据类型](./sections/07_03_扩展数据类型.md) | 扩展数据类型 |
| [07_04_字符串操作](./sections/07_04_字符串操作.md) | 字符串操作 |
| [07_05_分类数据](./sections/07_05_分类数据.md) | 分类数据 |
| [07_06_总结](./sections/07_06_总结.md) | 总结 |

## 二、关键语法速查表

| 场景 | API |
|------|-----|
| 缺失检测 | `df.isna()` |
| 删缺失行 | `df.dropna(how="all", thresh=2)` |
| 填缺失 | `df.fillna(0)`, `df.ffill()` |
| 去重 | `df.drop_duplicates(subset=["date","code"])` |
| 映射 | `s.map({...})` |
| 替换 | `df.replace(-999, np.nan)` |
| 分箱 | `pd.cut(s, bins)`, `pd.qcut(s, 5)` |
| 异常 | `df[df["ret"].abs() > 0.1]` |
| 字符串 | `s.str.contains(...)`, `s.str.extract(...)` |
| 哑变量 | `pd.get_dummies(df, columns=[...])` |

---

## 三、通用基础示例

见 [`./code/chapter07_data_cleaning_demo.py`](./code/chapter07_data_cleaning_demo.py)

---

## 四、【量化专属改造】金融实战衔接

1. **停牌/缺失交易日**：价格 `ffill`；成交量缺失常填 0 或删行（需业务规则）。
2. **重复 K 线**：`drop_duplicates(subset=["date","code"], keep="first")`。
3. **涨跌停哨兵**：`replace` 把 `-999`、空白转为 `NaN`。
4. **因子分箱**：`qcut` 做五分位分层回测；`cut` 做固定区间（如市值桶）。
5. **收益异常**：`|ret| > 0.11` 截断或剔除；合并前检查 `describe`。
6. **行业/交易所代码**：`astype("category")` 加速 groupby；`get_dummies` 进回归（注意共线性，可 drop_first）。
7. **股票代码字符串**：`str.replace(".XSHE","")`、`str.zfill(6)` 统一格式。

---

## 五、与 statsmodels 建模的衔接要点

- OLS 前必须 **`dropna(subset=[y, x1, x2, ...])`** 或明确插补策略并记录。
- 分类解释变量：`get_dummies(..., drop_first=True)` 避免完全多重共线性。
- 异常值处理会改变分布与 p 值：清洗规则应 **在训练集上固定**，再应用到测试集。
- 字符串协变量（如 ST 标记）先用 `.str` 清洗再入模。

---

## 本章自检清单

- [ ] 会用 `dropna` / `fillna` / `ffill`  
- [ ] 会按 `(date, code)` 去重  
- [ ] 会用 `map`、`replace`、`rename`  
- [ ] 会用 `cut` 与 `qcut`  
- [ ] 会用布尔索引处理异常收益  
- [ ] 会用 `.str` 与 `get_dummies`  

---

## 后续扩展留白

### 7.1～7.5

（留白）
