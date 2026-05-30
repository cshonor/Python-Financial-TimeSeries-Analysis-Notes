# Python-Financial-BigData-Analysis

对应教材：**《Python金融大数据分析（第2版）》**  
英文原名：*Python for Finance: Mastering Data-Driven Finance*（Yves Hilpisch，O'Reilly，2nd ed）

全书 **5 大部分 · 21 章 · 2 附录**，本仓库按章拆分为 `chapter01/`～`chapter21/`，附录见 `appendix_a/`、`appendix_b/`。

## 目录架构

| 子目录 / 文件 | 说明 |
|---------------|------|
| `chapterNN_*.md` | **章总览**（章节总览、小节索引、速查、量化衔接、自检） |
| `sections/` | **小节笔记**（`04_01_*.md`、`15_07_02_*.md` 等） |
| `code/` | 本章配套脚本 |
| [`code/pandas/`](./code/pandas/) | **第 5 章深化专题**（量化向 pandas 笔记，原独立模块） |

## 五大部分与章节索引

### 第1部分 Python与金融

| 章 | 总览 | 代码 |
|----|------|------|
| 第 1 章 为什么将Python用于金融 | [chapter01/](./chapter01/chapter01_why_python_for_finance.md) | [code/](./chapter01/code/) |
| 第 2 章 Python基础架构 | [chapter02/](./chapter02/chapter02_python_infrastructure.md) | [code/](./chapter02/code/) |

### 第2部分 掌握基础知识

| 章 | 总览 | 代码 |
|----|------|------|
| 第 3 章 数据类型与结构 | [chapter03/](./chapter03/chapter03_data_types_and_structures.md) | [code/](./chapter03/code/) |
| 第 4 章 用NumPy进行数值计算 | [chapter04/](./chapter04/chapter04_numpy_numerical_computation.md) | [chapter04/code/](./chapter04/code/) |
| 第 5 章 pandas数据分析 | [chapter05/](./chapter05/chapter05_pandas_data_analysis.md) | [code/](./chapter05/code/) + [`code/pandas/`](./code/pandas/) |
| 第 6 章 面向对象编程 | [chapter06/](./chapter06/chapter06_object_oriented_programming.md) | [code/](./chapter06/code/) |

### 第3部分 金融数据科学

| 章 | 总览 | 代码 |
|----|------|------|
| 第 7 章 数据可视化 | [chapter07/](./chapter07/chapter07_data_visualization.md) | [code/](./chapter07/code/) |
| 第 8 章 金融时间序列 | [chapter08/](./chapter08/chapter08_financial_time_series.md) | [code/](./chapter08/code/) |
| 第 9 章 输入/输出操作 | [chapter09/](./chapter09/chapter09_io_operations.md) | [code/](./chapter09/code/) |
| 第 10 章 高性能的Python | [chapter10/](./chapter10/chapter10_high_performance_python.md) | [code/](./chapter10/code/) |
| 第 11 章 数学工具 | [chapter11/](./chapter11/chapter11_mathematical_tools.md) | [code/](./chapter11/code/) |
| 第 12 章 推断统计学 | [chapter12/](./chapter12/chapter12_inferential_statistics.md) | [code/](./chapter12/code/) |
| 第 13 章 统计学 | [chapter13/](./chapter13/chapter13_statistics.md) | [code/](./chapter13/code/) |

> 第 8 章并行专题：[`../Python-Time-Series-Forecast/code/time_series_quant/`](../Python-Time-Series-Forecast/code/time_series_quant/)

### 第4部分 算法交易

| 章 | 总览 | 代码 |
|----|------|------|
| 第 14 章 FXCM交易平台 | [chapter14/](./chapter14/chapter14_fxcm_trading_platform.md) | [code/](./chapter14/code/) |
| 第 15 章 交易策略 | [chapter15/](./chapter15/chapter15_trading_strategies.md) | [code/](./chapter15/code/) |
| 第 16 章 自动化交易 | [chapter16/](./chapter16/chapter16_automated_trading.md) | [code/](./chapter16/code/) |

### 第5部分 衍生品分析

| 章 | 总览 | 代码 |
|----|------|------|
| 第 17 章 估值框架 | [chapter17/](./chapter17/chapter17_valuation_framework.md) | [code/](./chapter17/code/) |
| 第 18 章 金融模型的模拟 | [chapter18/](./chapter18/chapter18_financial_model_simulation.md) | [code/](./chapter18/code/) |
| 第 19 章 衍生品估值 | [chapter19/](./chapter19/chapter19_derivatives_valuation.md) | [code/](./chapter19/code/) |
| 第 20 章 投资组合估值 | [chapter20/](./chapter20/chapter20_portfolio_valuation.md) | [code/](./chapter20/code/) |
| 第 21 章 基于市场的估值 | [chapter21/](./chapter21/chapter21_market_based_valuation.md) | [code/](./chapter21/code/) |

### 附录

| 附录 | 总览 |
|------|------|
| 附录 A 日期与时间 | [appendix_a/](./appendix_a/appendix_a_日期与时间.md) |
| 附录 B BSM期权类 | [appendix_b/](./appendix_b/appendix_b_BSM期权类.md) |

## 建议学习顺序

1. `chapter01/` → `chapter06/`（Python + NumPy + pandas + OOP 基础）  
2. `chapter07/` → `chapter13/`（可视化、时序、I/O、性能、数学与统计）  
3. `chapter14/` → `chapter16/`（算法交易）  
4. `chapter17/` → `chapter21/`（衍生品定价与组合估值）  
5. 并行精读 [`code/pandas/`](./code/pandas/) 与 [`../Python-Time-Series-Forecast/`](../Python-Time-Series-Forecast/)

**前置**：[`../Python-Data-Analysis/`](../Python-Data-Analysis/) 第 1～5 章（可选，打 pandas/NumPy 基础）

## 运行示例

```bash
python Python-Financial-BigData-Analysis/chapter04/code/chapter04_numpy_demo.py
python Python-Financial-BigData-Analysis/code/pandas/00_core_objects/chapter02_pandas_data_structures_quant.py
```

## 与其他「Python for Finance」书的区分

| 书 | 作者 | 章数 | 本仓库文件夹 |
|----|------|------|--------------|
| *Python for Finance*（Packt） | Yuxing Yan | 17 | （暂未建册） |
| **本册** *Mastering Data-Driven Finance* | Yves Hilpisch | **21** | **`Python-Financial-BigData-Analysis/`** |
| *Python for Data Analysis* | Wes McKinney | 13 | [`Python-Data-Analysis/`](../Python-Data-Analysis/) |
