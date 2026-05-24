# Pandas 数据预处理与量化笔记

本目录是一份**长期可复用**的学习仓库：以《Pandas 数据预处理详解》（增田秀人 著）的章节体系为**结构蓝本**，将书中「数据预处理」主线与**量化金融 + 统计建模前置（statsmodels）**结合，形成**知识点提炼 + 语法速查 + 通用示例 + 量化改造 + 建模衔接**的固定写法。

> **说明**：仓库内容为读书笔记与自写示例代码，用于配合原书学习与本地实验；章节标题与知识结构对齐原书，示例与表述为原创整理，便于你在 GitHub 上长期维护与扩展。

---

## 一、仓库定位

| 维度 | 说明 |
|------|------|
| **核心蓝本** | 《Pandas 数据预处理详解》全书章节顺序 |
| **延伸方向** | 量化：行情 / 因子 / 多标的 / 回测数据准备；统计：回归与时间序列建模前的表格形态 |
| **交付形态** | 各章文件夹内：`*.md`（统一五段模板）+ 可选 `*.py`（可运行示例） |
| **不做的事** | 不把本仓库写成「原书扫描件」；不依赖零散互联网数据集案例作为主线 |

---

## 二、学习前置要求

1. **Python 基础**：变量、函数、列表推导、模块导入。
2. **NumPy 基础**：`ndarray`、形状、`dtype`、向量化思维（建议先完成 `../../Python-Data-Analysis/code/numpy/` 中 01～20 的优先级路线）。
3. **环境**：`Python 3.10+` 推荐；安装 `pandas`、`numpy`；后续章节涉及统计建模时再安装 `statsmodels`：

```bash
pip install pandas numpy
# 建模衔接章节会用到
pip install statsmodels
```

---

## 三、整体学习路线（从入门到「建模可用」）

1. **数据结构**（`00_core_objects`）→ 搞清 Series / DataFrame、索引与 dtype，能规范存放行情与因子表。  
2. **读取、筛选、聚合、排序**（`01_core_data_operations`）→ 能批量读 CSV、按日期筛选、算收益与分层统计。  
3. **变形、缺失、离群、重复**（`02_data_cleaning_preprocessing`）→ 能清洗到可回测、可回归的表格。  
4. **时间序列**（已迁至 [`../../Python-Time-Series-Forecast/code/time_series_quant/`](../../Python-Time-Series-Forecast/code/time_series_quant/)）→ 重采样、rolling、shift 对齐。  
5. **分组与多表、多标的**（`04_multi_asset_data_handling`）→ MultiIndex、长宽表、行业中性等多资产套路。  
6. **综合实战**（[`../../exercise/quant_practice_cases/`](../../exercise/quant_practice_cases/)）→ 从 EDA 到「建模前全流程预处理」模板。

---

## 四、目录与书本章节对应关系

| 仓库目录 | 对应原书主线（便于你对照翻书） | 本仓库中的「量化 + 建模」延伸重点 |
|----------|-------------------------------|-------------------------------------|
| `00_core_objects/` | 第 2 章：pandas 的数据结构 | 金融时间序列索引、`DatetimeIndex`、行情宽表/长表约定、列名与 `dtype` 规范 |
| `01_core_data_operations/` | 第 3 章 数据引用与读取 + 第 4 章 聚合与排序 | 批量读行情 CSV、日期筛选、收益率/分位数、截面 rank、基础因子描述统计 |
| `02_data_cleaning_preprocessing/` | 第 5 章 数据变形 + 第 6 章 缺失/离群/重复 | 停牌类缺失、`ffill` 策略、3σ/Z-score 截断、哑变量（回归必备） |
| `../Python-Time-Series-Forecast/code/time_series_quant/` | 第 8 章 时间序列数据处理 | 交易日对齐、`resample`、rolling/expanding、`shift` 防未来函数 |
| `04_multi_asset_data_handling/` | 第 7 章 分组与高级函数 + 多表合并思路 | `MultiIndex (date, code)`、merge 校验、`pivot`/`stack`、分组行业中性 |
| `../exercise/quant_practice_cases/` | 第 9 章 数据分析基础与实战案例 | 因子 EDA、四类核心操作练习、NumPy+Pandas 入门脚本 |

各子目录下将逐步补齐与上表一致的 **`chapterXX_*.md` + `chapterXX_*.py`**；已有的 `01_series_basics` 等文件保留为**语法速查与短练习**，与章节大笔记并存、互不冲突。

---

## 五、章节笔记统一模板（每个 `.md` 建议结构）

每个章节 Markdown 建议固定为五块（与书中「预处理」主线对齐，并强制加上量化与建模衔接）：

1. **一、书本原文核心知识点提炼**（用自己的话概括，便于复习）  
2. **二、关键语法速查表**（API + 一句话用途）  
3. **三、通用基础示例**（最小可运行片段）  
4. **四、【量化专属改造】金融实战代码**（行情/因子/多标的）  
5. **五、与 statsmodels 建模的衔接要点**（输入是 Series 还是 DataFrame、是否需要 `add_constant`、时间索引等）

**第 2 章的完整示范**见：`00_core_objects/chapter02_pandas_data_structures_quant.md` 与同目录下的 `chapter02_pandas_data_structures_quant.py`。

---

## 六、配套与后续路线

- **statsmodels**：离散因变量（Logit）、线性回归（OLS）、时间序列（ARIMA 等）通常要求「干净二维表 + 正确时间索引 + 无泄漏特征」；本仓库在第 2、5、8 章对应目录中反复强调「shift、合并校验、哑变量」。  
- **与本仓库其他目录**：`Python-Data-Analysis/code/numpy/` 提供向量化底层；`Python-Data-Analysis/code/statsmodels/` 可直接消费本目录输出的建模用表；时序专题见 `Python-Time-Series-Forecast/`。

---

## 七、学习资源

- [Pandas 官方文档](https://pandas.pydata.org/docs/)  
- [Pandas 中文文档](https://www.pypandas.cn/)  
- 原书：《Pandas 数据预处理详解》（增田秀人 著）——章节对照以纸质书/你手中的版本目录为准。

---

## 八、快速入口

| 优先阅读 | 路径 |
|----------|------|
| 第 2 章（数据结构 + 量化约定） | `00_core_objects/chapter02_pandas_data_structures_quant.md` |
| 四类核心操作练习清单 | `../../exercise/quant_practice_cases/00_core_operations_practice_checklist.md` |
| NumPy + Pandas 入门 10 练 | `../../exercise/quant_practice_cases/00_numpy_pandas_beginner_exercises.py` |
| 时间序列专题 | `../../Python-Time-Series-Forecast/code/time_series_quant/` |
