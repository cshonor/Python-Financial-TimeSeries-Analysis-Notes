# Python-Data-Analysis

对应教材：**《利用 Python 进行数据分析》**（Wes McKinney 体系：NumPy / Pandas / 可视化 / 科学计算栈）。

## 目录架构（按章拆分）

全书 **13 章**，每章独立文件夹，内含：

| 子目录 / 文件 | 说明 |
|---------------|------|
| `chapterNN_*.md` | **章总览**（章节总览、速查表、量化衔接、自检、留白索引） |
| `sections/` | **小节笔记**（`01_01_*.md`、`03_02_*.md` 等，对应原书 1.1、3.2…） |
| `code/` | 本章配套可运行脚本 |

书级共享资源（跨章专题）仍放在根目录：

| 路径 | 说明 |
|------|------|
| [`code/numpy/`](./code/numpy/) | NumPy 专题 |
| [`code/matplotlib/`](./code/matplotlib/) | Matplotlib 专题 |
| [`code/scipy/`](./code/scipy/) | SciPy 导读 |
| [`code/statsmodels/`](./code/statsmodels/) | statsmodels 导读 |

## 章节索引

| 章 | 总览 | 配套代码 |
|----|------|----------|
| 第 1 章 准备工作 | [chapter01/chapter01_getting_started.md](./chapter01/chapter01_getting_started.md) | [chapter01/code/](./chapter01/code/) |
| 第 2 章 语法与 Jupyter | [chapter02/chapter02_python_syntax_ipython_jupyter.md](./chapter02/chapter02_python_syntax_ipython_jupyter.md) | [chapter02/code/](./chapter02/code/) |
| 第 3 章 数据结构、函数和文件 | [chapter03/chapter03_data_structures_functions_files.md](./chapter03/chapter03_data_structures_functions_files.md) | [chapter03/code/](./chapter03/code/) |
| 第 4 章 NumPy 基础 | [chapter04/chapter04_numpy_basics_arrays_vectorization.md](./chapter04/chapter04_numpy_basics_arrays_vectorization.md) | [chapter04/code/](./chapter04/code/) |
| 第 5 章 pandas 入门 | [chapter05/chapter05_pandas_introduction.md](./chapter05/chapter05_pandas_introduction.md) | [chapter05/code/](./chapter05/code/) |
| 第 6 章 数据 I/O | [chapter06/chapter06_data_io_file_formats.md](./chapter06/chapter06_data_io_file_formats.md) | [chapter06/code/](./chapter06/code/) |
| 第 7 章 数据清洗 | [chapter07/chapter07_data_cleaning_preparation.md](./chapter07/chapter07_data_cleaning_preparation.md) | [chapter07/code/](./chapter07/code/) |
| 第 8 章 数据规整 | [chapter08/chapter08_data_wrangling_join_reshape.md](./chapter08/chapter08_data_wrangling_join_reshape.md) | [chapter08/code/](./chapter08/code/) |
| 第 9 章 绘图和可视化 | [chapter09/chapter09_plotting_visualization.md](./chapter09/chapter09_plotting_visualization.md) | [chapter09/code/](./chapter09/code/) |
| 第 10 章 数据聚合与分组 | [chapter10/chapter10_data_aggregation_groupby.md](./chapter10/chapter10_data_aggregation_groupby.md) | [chapter10/code/](./chapter10/code/) |
| 第 11 章 时间序列 | [chapter11/chapter11_time_series.md](./chapter11/chapter11_time_series.md) | [chapter11/code/](./chapter11/code/) |
| 第 12 章 建模库 | [chapter12/chapter12_modeling_libraries_patsy_statsmodels.md](./chapter12/chapter12_modeling_libraries_patsy_statsmodels.md) | [chapter12/code/](./chapter12/code/) |
| 第 13 章 数据分析案例 | [chapter13/chapter13_data_analysis_case_studies.md](./chapter13/chapter13_data_analysis_case_studies.md) | [chapter13/code/](./chapter13/code/) |

完整小节列表见各章 `sections/` 目录或章总览中的 **小节笔记索引** 表。

## 建议学习顺序

1. `chapter01/` → `chapter02/` → `chapter03/`  
2. `chapter04/` + [`code/numpy/`](./code/numpy/)  
3. `chapter05/` → `chapter06/` → `chapter07/` → `chapter08/`  
4. `chapter09/` + [`code/matplotlib/`](./code/matplotlib/)  
5. `chapter10/` → `chapter11/`（并联 [`../Python-Time-Series-Forecast/`](../Python-Time-Series-Forecast/)）  
6. `chapter12/` → `chapter13/`  
7. 深入 [`../Python-Financial-BigData-Analysis/code/pandas/`](../Python-Financial-BigData-Analysis/code/pandas/)

## 运行示例

```bash
python Python-Data-Analysis/chapter01/code/chapter01_environment_setup.py
python Python-Data-Analysis/chapter05/code/chapter05_pandas_intro_demo.py
```
