# Python-Data-Analysis

对应教材：**《利用 Python 进行数据分析》**（Wes McKinney 体系：NumPy / Pandas 基础 / 可视化 / 科学计算栈）。

## 目录说明

| 子目录 | 用途 |
|--------|------|
| `docs/` | 章节笔记、思维导图（逐步从 `code/` 中拆出 `.md`） |
| `code/` | **当前主力内容**：可运行示例 |
| `dataset/` | 书中或自采样本数据 |
| `exercise/` | 章节习题与变体练习 |
| `assets/` | 配图与截图 |

## `code/` 现状

| 路径 | 说明 |
|------|------|
| `code/numpy/` | ndarray、索引、广播、聚合、缺失值、随机数、线代入门等 |
| `code/matplotlib/` | 绘图基础与常见图表 |
| `code/scipy/` | SciPy 子模块导读（待扩充） |
| `code/statsmodels/` | 统计建模库导读（待扩充） |

## 章节笔记（`docs/`）

| 章节 | 笔记 |
|------|------|
| 第 1 章 准备工作 | [docs/chapter01_getting_started.md](./docs/chapter01_getting_started.md) |
| 第 1 章 环境脚本 | [code/chapter01_environment_setup.py](./code/chapter01_environment_setup.py) |

## 建议学习顺序

1. `docs/chapter01_getting_started.md` + `code/chapter01_environment_setup.py`  
2. `code/numpy/` → 3. `../Python-Financial-BigData-Analysis/code/pandas/` → 4. `code/matplotlib/`
