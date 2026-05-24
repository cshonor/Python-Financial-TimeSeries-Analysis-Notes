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
| 第 5 章 pandas 入门 | [docs/chapter05_pandas_introduction.md](./docs/chapter05_pandas_introduction.md) |
| 第 5 章 配套脚本 | [code/chapter05_pandas_intro_demo.py](./code/chapter05_pandas_intro_demo.py) |
| 第 6 章 数据 I/O | [docs/chapter06_data_io_file_formats.md](./docs/chapter06_data_io_file_formats.md) |
| 第 6 章 配套脚本 | [code/chapter06_data_io_demo.py](./code/chapter06_data_io_demo.py) |
| 第 7 章 数据清洗 | [docs/chapter07_data_cleaning_preparation.md](./docs/chapter07_data_cleaning_preparation.md) |
| 第 7 章 配套脚本 | [code/chapter07_data_cleaning_demo.py](./code/chapter07_data_cleaning_demo.py) |
| 第 8 章 数据规整 | [docs/chapter08_data_wrangling_join_reshape.md](./docs/chapter08_data_wrangling_join_reshape.md) |
| 第 8 章 配套脚本 | [code/chapter08_data_wrangling_demo.py](./code/chapter08_data_wrangling_demo.py) |
| 第 9 章 绘图和可视化 | [docs/chapter09_plotting_visualization.md](./docs/chapter09_plotting_visualization.md) |
| 第 9 章 配套脚本 | [code/chapter09_plotting_demo.py](./code/chapter09_plotting_demo.py) |
| 第 10 章 数据聚合与分组 | [docs/chapter10_data_aggregation_groupby.md](./docs/chapter10_data_aggregation_groupby.md) |
| 第 10 章 配套脚本 | [code/chapter10_groupby_demo.py](./code/chapter10_groupby_demo.py) |
| 第 11 章 时间序列 | [docs/chapter11_time_series.md](./docs/chapter11_time_series.md) |
| 第 11 章 配套脚本 | [code/chapter11_time_series_demo.py](./code/chapter11_time_series_demo.py) |
| 第 12 章 建模库 | [docs/chapter12_modeling_libraries_patsy_statsmodels.md](./docs/chapter12_modeling_libraries_patsy_statsmodels.md) |
| 第 12 章 配套脚本 | [code/chapter12_statsmodels_demo.py](./code/chapter12_statsmodels_demo.py) |
| 第 13 章 数据分析案例 | [docs/chapter13_data_analysis_case_studies.md](./docs/chapter13_data_analysis_case_studies.md) |
| 第 13 章 配套脚本 | [code/chapter13_case_studies_demo.py](./code/chapter13_case_studies_demo.py) |

## 建议学习顺序

1. 第 1 章：`docs/chapter01_*` + `code/chapter01_environment_setup.py`  
2. 第 2 章：`docs/chapter02_*` + `code/chapter02_python_basics_demo.py`  
3. 第 3 章：`docs/chapter03_*` + `code/chapter03_data_structures_functions_files.py`  
4. 第 4 章：`docs/chapter04_*` + `code/chapter04_numpy_basics_demo.py`，再按 [`code/numpy/README.md`](./code/numpy/README.md) 刷专题  
5. 第 5 章：`docs/chapter05_*` + `code/chapter05_pandas_intro_demo.py`  
6. 第 6 章：`docs/chapter06_*` + `code/chapter06_data_io_demo.py`  
7. 第 7 章：`docs/chapter07_*` + `code/chapter07_data_cleaning_demo.py`  
8. 第 8 章：`docs/chapter08_*` + `code/chapter08_data_wrangling_demo.py`  
9. 第 9 章：`docs/chapter09_*` + `code/chapter09_plotting_demo.py`，再刷 [`code/matplotlib/`](./code/matplotlib/) 专题  
10. 第 10 章：`docs/chapter10_*` + `code/chapter10_groupby_demo.py`  
11. 第 11 章：`docs/chapter11_*` + `code/chapter11_time_series_demo.py`，并联 [`../Python-Time-Series-Forecast/code/time_series_quant/`](../Python-Time-Series-Forecast/code/time_series_quant/)  
12. 第 12 章：`docs/chapter12_*` + `code/chapter12_statsmodels_demo.py`  
13. 第 13 章：`docs/chapter13_*` + `code/chapter13_case_studies_demo.py`（全书正文收官）  
14. 再深入 [`../Python-Financial-BigData-Analysis/code/pandas/`](../Python-Financial-BigData-Analysis/code/pandas/) 与 [`../Python-Time-Series-Forecast/`](../Python-Time-Series-Forecast/)（量化与时序实战）
