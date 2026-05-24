# 第 13 章 数据分析案例

> 对应教材：《利用 Python 进行数据分析》（原书第 3 版）第 13 章 · **正文最后一章**。  
> 不再引入新 API，而是把第 1～12 章的 **加载、清洗、重塑、groupby、可视化、建模** 串进五个真实风格的数据集，从原始混乱数据提炼业务洞察。

**前置**：[第 12 章 建模库](./chapter12_modeling_libraries_patsy_statsmodels.md)（建议已通读第 6～11 章）。

**演示脚本**（合成小样本，复现各案核心技法）：[`../code/chapter13_case_studies_demo.py`](../code/chapter13_case_studies_demo.py)

**原书数据**：可放入 [`../dataset/chapter13/`](../dataset/chapter13/)（待下载；见脚本内注释链接说明）。

---

## 章节总览

**小节统计**：6 个一级模块（5 个案例 + 总结），约 **12 个逻辑小节**。

| 案例 | 小节 |
|------|------|
| 13.1 Bitly / USA.gov | 13.1.1 纯 Python；13.1.2 pandas |
| 13.2 MovieLens 1M | 多表 merge、争议度、genres explode |
| 13.3 婴儿姓名 | concat、prop、趋势 |
| 13.4 USDA 食品 | JSON 扁平化、idxmax |
| 13.5 FEC 选举捐款 | map、pivot、cut、州占比 |
| 13.6 总结 | — |

---

## 一、书本原文核心知识点提炼

### 13.1 来自 1.USA.gov 的 Bitly 数据

- JSON 按小时日志；嵌套字段（如 `tz` 时区）。
- **13.1.1**：`json` + `Counter` / `defaultdict` 统计 `tz` Top10。
- **13.1.2**：`pd.DataFrame(records)`、`value_counts()`、`fillna`、布尔过滤；`seaborn.barplot`。
- **延伸**：解析 User-Agent → `str.contains` + `groupby` + `unstack` 对比各时区 Windows 占比。

### 13.2 MovieLens 1M

- 三表：`users`、`ratings`、`movies` → **`pd.merge`** 成大表。
- 争议最大电影：`groupby(title).rating.std()` 降序。
- **genres**：`str.split("|")` → **`explode()`** 一行一类，再 `groupby` 统计。

### 13.3 1880—2010 婴儿姓名

- 按年文件 **`pd.concat(..., ignore_index=True)`** + `year` 列。
- 比例列：`groupby(["year","sex"]).apply` 算 `prop`。
- **多样性**：`cumsum` + `searchsorted` 找占 50% 新生儿所需最少名字数。
- 末字母透视、跨性别名字趋势（正则/子串过滤 + 分组）。

### 13.4 USDA 食品数据库

- 嵌套 JSON：info 表 + nutrients 扁平表 → **`merge(on="id")`**，合并前 **`rename`** 防同名列冲突。
- 某营养素含量最高食物：`groupby(nutrient).apply(lambda g: g.loc[g.value.idxmax()])`。

### 13.5 2012 联邦选举委员会（FEC）

- **13.5.1**：职业字段 **`series.map(dict.get)`** 归并变体 → **`pivot_table`** 职业 × 候选人金额。
- **13.5.2**：**`pd.cut`** 出资分桶 + **`unstack`** 看小额捐赠结构。
- **13.5.3**：**`groupby(["cand_nm","contbr_st"]).sum()`** + 列除法算州内占比。

### 13.6 总结

- 正文结束；附录（如高阶 NumPy）供进阶。

---

## 二、关键语法速查表（案例向）

| 案例 | 核心 API |
|------|----------|
| Bitly | `json.loads`, `value_counts`, `fillna` |
| MovieLens | `read_table`, `merge`, `explode` |
| 婴儿名 | `concat`, `groupby().apply`, `cumsum` |
| USDA | 嵌套展平, `rename`, `idxmax` |
| FEC | `map`, `pivot_table`, `cut`, `div` |

---

## 三、通用基础示例

见 [`../code/chapter13_case_studies_demo.py`](../code/chapter13_case_studies_demo.py)（不依赖原书大文件）。

---

## 四、【量化专属改造】金融实战映射

| 原书案例 | 量化类比 |
|----------|----------|
| Bitly JSON 日志 | 行情/逐笔 JSON、API 嵌套字段解析 |
| MovieLens merge | 行情 + 因子 + 行业表 `(date,code)` 合并 |
| genres explode | 概念板块多标签、指数成分 explode |
| 婴儿名 concat | 多年 CSV 拼成面板 `concat` |
| prop / 多样性 | 截面因子分位、持股集中度 |
| USDA 嵌套 JSON | 财报附注、ESG 分项指标扁平化 |
| FEC map / cut | 行业代码归一、成交额分桶、地区出资结构 |
| pivot / unstack | 因子 × 行业矩阵、多空分组收益表 |

**综合演练建议**：用本仓库 [`Python-Financial-BigData-Analysis/exercise/quant_practice_cases/`](../../Python-Financial-BigData-Analysis/exercise/quant_practice_cases/) 做 A 股版“第 13 章”。

---

## 五、与 statsmodels / 全书串联

- **第 6 章**：读 `.dat` / JSON → 案例入口。
- **第 7 章**：`map`、`cut`、`replace` → FEC、日志清洗。
- **第 8 章**：`merge`、`pivot`、`melt` → MovieLens、FEC。
- **第 9 章**：`barplot`、趋势图 → Bitly、婴儿名。
- **第 10 章**：`groupby`、`pivot_table` → 全案例。
- **第 11 章**：婴儿名时间趋势、（可扩展）捐款时间序列。
- **第 12 章**：FEC 出资可对候选人做回归/描述推断（扩展练习）。

---

## 本章自检清单

- [ ] 能从 JSON 列表建 DataFrame 并 `value_counts`  
- [ ] 会三表 `merge` 与 `explode` 多标签字段  
- [ ] 会 `concat` 多文件并 `groupby` 算比例  
- [ ] 会对嵌套表扁平化 + `idxmax` 取极值行  
- [ ] 会 `map` 清洗 + `cut` 分桶 + `pivot_table`  

---

## 后续扩展留白

### 13.1～13.5 完整复现

（留白：下载原书数据放入 `dataset/chapter13/` 后补全 notebook）
