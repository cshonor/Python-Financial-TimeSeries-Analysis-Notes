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
| 第 2 章 语法与 Jupyter | [docs/chapter02_python_syntax_ipython_jupyter.md](./docs/chapter02_python_syntax_ipython_jupyter.md) |
| 第 2 章 配套脚本 | [code/chapter02_python_basics_demo.py](./code/chapter02_python_basics_demo.py) |
| 第 3 章 数据结构、函数和文件 | [docs/chapter03_data_structures_functions_files.md](./docs/chapter03_data_structures_functions_files.md) |
| 第 3 章 配套脚本 | [code/chapter03_data_structures_functions_files.py](./code/chapter03_data_structures_functions_files.py) |
| 第 4 章 NumPy 基础 | [docs/chapter04_numpy_basics_arrays_vectorization.md](./docs/chapter04_numpy_basics_arrays_vectorization.md) |
| 第 4 章 综合演示 | [code/chapter04_numpy_basics_demo.py](./code/chapter04_numpy_basics_demo.py) |

## 建议学习顺序

1. 第 1 章：`docs/chapter01_*` + `code/chapter01_environment_setup.py`  
2. 第 2 章：`docs/chapter02_*` + `code/chapter02_python_basics_demo.py`  
3. 第 3 章：`docs/chapter03_*` + `code/chapter03_data_structures_functions_files.py`  
4. 第 4 章：`docs/chapter04_*` + `code/chapter04_numpy_basics_demo.py`，再按 [`code/numpy/README.md`](./code/numpy/README.md) 刷专题  
5. `../Python-Financial-BigData-Analysis/code/pandas/` → 6. `code/matplotlib/`
